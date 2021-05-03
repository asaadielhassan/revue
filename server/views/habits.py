from schema import Schema, And

import utils
from app import app
from flask import jsonify, request
from models import Post, User, Comment, Subvue, Habit
from mongoengine.errors import ValidationError
from authorization import login_required

# global counter = 0

@app.route("/api/habits")
def habit_index():
    habit = Habit.objects().order_by("-created")
    return jsonify([habit.to_public_json() for hab in habit])


@app.route("/api/habits", methods=["HABIT"])
@login_required
def habit_create(username: str):
    if not request.json:
        return jsonify({"error": "Data not specified"}), 409
    if not request.json.get("title"):
        return jsonify({"error": "Name not specified"}), 409
    if not request.json.get("description"):
        return jsonify({"error": "Description not specified"}), 409
    if not request.json.get("num_Days"):
        return jsonify({"error": "numDays not specified"}), 409

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
        name = request.json.get("name"),
        description=request.json.get("description"),
        num_Days = request.json.get("num_Days"),
        repeat = [],
        start_Date =  datetime.now(), #A list with the month in mm format and day in the dd format
        curr_Date = datetime.now(),
        end_Date = datetime.now() + timedelta(days=int(request.json.get("numDays"))),
        is_public = request.json.get("is_public")
    ).save()
    return jsonify(habit.to_public_json())


@app.route("/api/habits/id/<string:id>")
def habits_item(id: str):
    try:
        habit = Habit.objects(pk=id).first()

        # If post has alreay been deleted
        if not post:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post.to_public_json())


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

        # If post has alreay been deleted
        if not habit:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Grid not found"}), 404

    # Check whether action was called by creator of the post
    if username != habit.user.username:
        return jsonify({"error": "You are not the creator of the grid"}), 401

    habit_info = habit.to_public_json()

    habit.delete()

    return jsonify(habit_info)


#@app.route("/api/posts/<string:id>/comments", methods=["POST"])
#@login_required
#def posts_create_comment(username: str, id: str):
#    schema = Schema({
#        "content": And(str, len, error="No content specified")
#    })
#    validated = schema.validate(request.json)
#
#    try:
#        post = Post.objects(pk=id).first()
#    except ValidationError:
#        return jsonify({"error": "Post not found"}), 404
#
#    user = User.objects(username=username).first()
#    comments = post.comments
#    comments.append(Comment(user=user, content=validated["content"]))
#    post.save()
#
#    return jsonify([comment.to_public_json() for comment in post.comments][::-1])
