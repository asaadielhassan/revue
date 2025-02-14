from schema import Schema, And, Use

import utils
from datetime import datetime, timedelta
from app import app
from flask import jsonify, request
from models import User, Comment, Subvue, Habit
from mongoengine.errors import ValidationError
from authorization import login_required
import ast

@app.route("/api/habits/public")
def habit_index():
    pubs = []
    habits = Habit.objects().order_by("-start_Date")
    for habit in habits:
        if habit.is_public == "true":
            pubs.append(habit.to_public_json())
    
    return jsonify(pubs)


@app.route("/api/habits", methods=["POST"])
@login_required
def habit_create(username: str):
    schema = Schema({
        "name": And(str, len, error="Namr not specified"),
        "description": And(str, len, error="description not specified"),
        "num_Days": And(Use(int), error="Number of Days not specified"),
        "is_public": And(str, len, error="publicity not specified")
    })
    form = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "num_Days": request.form.get("num_Days"),
        "is_public": request.form.get("is_public")
    }
    validated = schema.validate(form)

    temp_data = []
    user = User.objects(username=username).first()
    for i in range(validated["num_Days"]):
        temp_data.append(["false", 0, 0])

    habit = Habit(
        user = user,
        name = validated["name"],
        description=validated["description"],
        num_Days = validated["num_Days"],
        repeat = [],
        start_Date =  datetime.now(),
        string_start = datetime.strftime(datetime.now(), "%B %m, %Y"), #A list with the month in mm format and day in the dd format
        curr_Date = datetime.now(),
        end_Date = datetime.now() + timedelta(days=int(validated["num_Days"])),
        is_public = validated["is_public"],
        habit_data = temp_data
    ).save()
    return jsonify(habit.to_public_json())


@app.route("/api/habits/id/<string:id>")
def habits_item(id: str):
    try:
        habit = Habit.objects(pk=id).first()

        # If habit has alreay been deleted
        if not habit:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "habit not found"}), 404

    return jsonify(habit.to_public_json())


@app.route("/api/habits/user/<string:username>")
def habits_user(username: str):
    try:
        user = User.objects(username=username).first()
    except ValidationError:
        return jsonify({"error": "User not found"}), 404

    habits = Habit.objects(user=user).order_by("-start_Date")

    return jsonify([habit.to_public_json() for habit in habits])


@app.route("/api/habits/id/<string:id>", methods=["DELETE"])
@login_required
def habits_delete(username: str, id: str):
    try:
        habit = Habit.objects(pk=id).first()

        # If habit has alreay been deleted
        if not habit:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Grid not found"}), 404

    # Check whether action was called by creator of the habit
    if username != habit.user.username:
        return jsonify({"error": "You are not the creator of the grid"}), 401

    habit_info = habit.to_public_json()

    habit.delete()

    return jsonify(habit_info)

@app.route("/api/habits/id/<string:id>", methods=["POST"])
@login_required
def habit_update(username: str, id: str):
    x = request.form.get("habit_data")
    y = ""
    habit_data = []
    data = []
    for i in x:
        if i == 't':
            y += 't'
        elif i == 'r':
            y += 'r'
        elif i == 'u':
            y += 'u'
        elif i == 'e':
            y += 'e'
            data.append(y)
            y = ""
        elif i == 'f':
            y += 'f'
        elif i == 'a':
            y += 'a'
        elif i == 'l':
            y += 'l'
        elif i == 's':
            y += 's'
        elif i == "0":
            if len(data) == 2:
                data.append(0)
                habit_data.append(data)
                data = []
            else:
                data.append(0)
    schema = Schema({
        #"habit_data": And(Use(list), error="habit_data not specified")
    })
    form = {
        #"habit_data": request.form.get("habit_data"),
    }
    validated = schema.validate(form)
    try:
        habit = Habit.objects(pk=id).first()
        if not habit:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Grid not found"}), 404

    habit.habit_data = habit_data
    if username != habit.user.username:
        return jsonify({"error": "You are not the creator of the grid"}), 401
    else:
        habit.save()
    return jsonify(habit.to_public_json())
