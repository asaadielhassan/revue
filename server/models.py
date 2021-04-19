import datetime
import hashlib
import os

from mongoengine import (
    connect, Document, EmailField, StringField, ListField, ReferenceField, DateTimeField, EmbeddedDocument,
    EmbeddedDocumentField, CASCADE
)

# GUIDE: Here we are connecting to the mongodb database. os.environ.get is getting environment variables
# if they are not set, the values are None which leads us to login to the default database.
username = os.environ.get('MONGODB_USERNAME')
password = os.environ.get('MONGODB_PASSWORD')
host = os.environ.get('MONGODB_HOSTNAME')
db = os.environ.get('MONGODB_DATABASE', "revue")
connect(username=username, password=password, host=host, db=db)

# GUIDE: These are models for our database entries. They extend mongoengine.Document. 
# This allows us to unwrap database queries directly into objects for convenience
# http://docs.mongoengine.org/apireference.html#documents
class User(Document):
    email = EmailField(required=True, unique=True)
    username = StringField(max_length=50, required=True, unique=True)
    password = StringField(required=True)
    subscribed = ListField(ReferenceField("Subvue"))
    created = DateTimeField(required=True, default=datetime.datetime.now())

    def to_public_json(self):
        hashed_email = hashlib.md5(self.email.encode("utf-8")).hexdigest()

        data = {
            "id": str(self.id),
            "username": self.username,
            "hashedEmail": hashed_email,
            "subscribed": [subvue.to_public_json() for subvue in self.subscribed],
            "created": self.created,
        }

        return data


class Comment(EmbeddedDocument):
    content = StringField(max_length=5000)
    user = ReferenceField(User)
    created = DateTimeField(required=True, default=datetime.datetime.now())

    def to_public_json(self):
        data = {
            "content": self.content,
            "created": self.created,
            "user": {
                "id": str(self.user.id),
                "username": self.user.username
            }
        }

        return data


class Subvue(Document):
    name = StringField(max_length=120, required=True)
    permalink = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=True)
    created = DateTimeField(required=True, default=datetime.datetime.now())
    moderators = ListField(ReferenceField(User))

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "name": self.name,
            "permalink": self.permalink,
            "description": self.description,
            "moderators": [{
                "id": str(moderator.id),
                "username": moderator.username
            } for moderator in self.moderators],
        }

        return data
class Habit(Document):
    timer = datetime.datetime.now()
    name = ""
    days = []
    streak = 0
    start_Day = 0
    curr_Day = 0
    curr_Date = [timer.strftime("%m"), timer.strftime("%d")]
    end_Date = []
    complete = 0
    monthDict = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }

    def habits(self, name, days, end_Date):
        self.name = name
        self.days = days
        self.start_Date = [timer.strftime("%m"), timer.strftime("%d")] #A list with the month in mm format and day in the dd format
        self.start_Day = int(timer.day())
        self.curr_Day = int(timer.day())
        self.end_Date = end_Date

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDays(self, days):
        self.days = days

    def getDays(self):
        return self.days

    def setStreak(self, num):
        self.streak = num

    def getStreak(self):
        return self.streak

    def setStartDay(self, day):
        self.start_Day = day

    def getStartDay(self):
        return self.start_Day

    def setStartDate(self, date):
        self.start_Date = date

    def getStartDate(self):
        return self.start_Date

    def setEndDate(self, date):
        self.end_Date = date
        
    def getEndDate(self):
        return self.end_Date

    def calculate():
        day1 = start_Date[1]
        daycurr = curr_Date[1]
        day2 = end_Date[1]
        if(int(end_Date[1]) > int(start_Date[1])):
            day2 += monthDict[end_Date[1]]
        if(int(curr_Date[1]) > int(start_Date[1])):
            daycurr += monthDict[curr_Date[1]]
        fromStart = daycurr - day1
        totalDays = day2 - day1
        return str(round(fromStart/totalDays, 2))


    def streak():
        if(self.timer.day > self.curr_Date):
            if(self.complete == 1):
                self.streak += 1
                self.curr_Day += 1
                self.complete = 0
                return self.streak
            else:
                return 0
        else:
            return self.streak
            
    def to_public_json(self, user)
        entry = {
            "user":user,
            "name":self.name,
            "description":self.description,
            "days":self.days,
            "start_Day":self.startDay,
            "start_Date":self.startDate,
            "end_Date":self.endDate
        }
        return entry


class Post(Document):
    title = StringField(max_length=120, required=True)
    subvue = ReferenceField(Subvue, required=True, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=5000)
    comments = ListField(EmbeddedDocumentField(Comment))
    created = DateTimeField(required=True, default=datetime.datetime.now())
    image = StringField()
    upvotes = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))
    downvotes = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "title": self.title,
            "subvue": self.subvue.to_public_json(),
            "content": self.content,
            "user": {
                "id": str(self.user.id),
                "username": self.user.username
            },
            "comments": [comment.to_public_json() for comment in self.comments][::-1],
            "created": self.created,
            "image": self.image,
            "upvotes": [{
                "id": str(upvote.id),
                "username": upvote.username
            } for upvote in self.upvotes],
            "downvotes": [{
                "id": str(downvote.id),
                "username": downvote.username
            } for downvote in self.downvotes],
        }

        return data
