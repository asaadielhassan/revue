import pymongo
import habits

def connectDB():
    try:
        conn = MongoClient()
        print("Successfully connected")
    except:
        print("Could not connect")

    db = conn.database

def insertHabit(user, habit):
    entry = {
        "user" = user,
        "name" = habit.getName(),
        "days" = habit.getDays(),
        "start_Day" = habit.getStartDay(),
        "start_Date" = habit.getStartDate(),
        "end_Date" = habit.getEndDate()
    }

    db.habits.insert_one(entry)
