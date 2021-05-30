import datetime

class habits:
    timer = datetime.datetime.now()
    name = ""
    days = []
    streak = 0
    start_Date = timer.day()
    curr_Date = timer.day()
    end_Date = ""
    complete = 0

    def habits(self, name, days, start_Date, end_Date):
        self.name = name
        self.days = days
        self.start_Date = start_Date
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
    def setStartDate(self, date):
        self.start_Date = date
    def getStartDate(self):
        return self.start_Date
    def setEndDate(self, date):
        self.end_Date = date
    def getEndDate(self):
        return self.end_Date

    def calculate():

    def streak():
        if(self.timer.day > self.curr_Date):
            if(self.complete = 1):
                self.streak += 1
                self.curr_Date += 1
                self.complete = 0
                return self.streak
            else:
                return 0
        else:
            return self.streak
