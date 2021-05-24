from schema import Schema, And, Use

import utils
from datetime import datetime, timedelta
from app import app
from flask import jsonify, request
from models import User, Comment, Subvue, Habit
from mongoengine.errors import ValidationError
from authorization import login_required

# global counter = 0

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
    # if not request.json:
    #     return jsonify({"error": "Data not specified"}), 409
    # if not request.json.get("name"):
    #     return jsonify({"error": "Name not specified"}), 409
    # if not request.json.get("description"):
    #     return jsonify({"error": "Description not specified"}), 409
    # if not request.json.get("num_Days"):
    #     return jsonify({"error": "numDays not specified"}), 409

    schema = Schema({
        "name": And(str, len, error="Namr not specified"),
        "description": And(str, len, error="description not specified"),
        "num_Days": And(Use(int), error="Number of Days not specified"),
        "is_public": And(str, len, error="publicity not specified"),
        "habit_data": And(list, error="Habit data not specified")
    })
    form = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "num_Days": request.form.get("num_Days"),
        "is_public": request.form.get("is_public"),
        "habit_data": request.form.get("habit_data")
    }
    validated = schema.validate(form)

    #subvue_permalink = validated["habit"]
    #subvue = Subvue.objects(permalink__iexact=subvue_permalink).first()
    #if not subvue:
    #    return jsonify({"error": f"Subvue '{subvue_permalink}' not found"}), 404

    user = User.objects(username=username).first()

    habit = Habit(
        # user=user,
        # id = counter
        # name= validated["title"],
        # description="",
        # days = numDays,
        # repeat = [],
        # self.start_Date = [timer.strftime("%m"), timer.strftime("%d")], #A list with the month in mm format and day in the dd format
        # self.start_Day = int(timer.day()),
        # self.curr_Day = int(timer.day()),
        # endDate = []

        user = user,
        name = validated["name"],
        description=validated["description"],
        num_Days = validated["num_Days"],
        repeat = [],
        start_Date =  datetime.now(),
        string_start = datetime.strftime(datetime.now(), "%B %m, %Y"), #A list with the month in mm format and day in the dd format
        curr_Date = datetime.now(),
        end_Date = datetime.now() + timedelta(days=int(validated["num_Days"])),
        is_public = validated["is_public"]
        habit_data = validated["habit_data"]
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

    habits = Habit.objects(user=user).order_by("-created")

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


#@app.route("/api/habits/<string:id>/comments", methods=["habit"])
#@login_required
#def habits_create_comment(username: str, id: str):
#    schema = Schema({
#        "content": And(str, len, error="No content specified")
#    })
#    validated = schema.validate(request.json)
#
#    try:
#        habit = habit.objects(pk=id).first()
#    except ValidationError:
#        return jsonify({"error": "habit not found"}), 404
#
#    user = User.objects(username=username).first()
#    comments = habit.comments
#    comments.append(Comment(user=user, content=validated["content"]))
#    habit.save()
#
#    return jsonify([comment.to_public_json() for comment in habit.comments][::-1])
