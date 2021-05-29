from schema import Schema, And, Use

import utils
from datetime import datetime, timedelta
from app import app
from flask import jsonify, request
from models import User, Comment, Subvue, Grid
from mongoengine.errors import ValidationError
from authorization import login_required

# global counter = 0

@app.route("/api/grids/public")
def grid_index():
    pubs = []
    grids = Grid.objects().order_by("-start_Date")
    for grid in grids:
        if grid.is_public == "true":
            pubs.append(grid.to_public_json())
    
    return jsonify(pubs)


@app.route("/api/grids", methods=["POST"])
@login_required
def grid_create(username: str):
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
    })
    form = {
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "num_Days": request.form.get("num_Days"),
        "is_public": request.form.get("is_public")
    }
    validated = schema.validate(form)

    #subvue_permalink = validated["grid"]
    #subvue = Subvue.objects(permalink__iexact=subvue_permalink).first()
    #if not subvue:
    #    return jsonify({"error": f"Subvue '{subvue_permalink}' not found"}), 404

    user = User.objects(username=username).first()

    grid = Grid(
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
    ).save()
    return jsonify(grid.to_public_json())


@app.route("/api/grids/id/<string:id>")
def grids_item(id: str):
    try:
        grid = Grid.objects(pk=id).first()

        # If grid has alreay been deleted
        if not grid:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "grid not found"}), 404

    return jsonify(grid.to_public_json())


@app.route("/api/grids/user/<string:username>")
def grids_user(username: str):
    try:
        user = User.objects(username=username).first()
    except ValidationError:
        return jsonify({"error": "User not found"}), 404

    grids = Grid.objects(user=user).order_by("-created")

    return jsonify([grid.to_public_json() for grid in grids])


@app.route("/api/grids/id/<string:id>", methods=["DELETE"])
@login_required
def grids_delete(username: str, id: str):
    try:
        grid = Grid.objects(pk=id).first()

        # If grid has alreay been deleted
        if not grid:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Grid not found"}), 404

    # Check whether action was called by creator of the grid
    if username != grid.user.username:
        return jsonify({"error": "You are not the creator of the grid"}), 401

    grid_info = grid.to_public_json()

    grid.delete()

    return jsonify(grid_info)