import datetime

class habits:
    timer = datetime.datetime.now()
    name = ""
    days = []
    streak = 0
    start_Day = 0
    curr_Day = 0
    curr_Date = [timer.strftime("%m"), timer.strftime("%d")]
    end_Date = []
    complete = 0

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
            day2 += 30
        if(int(curr_Date[1]) > int(start_Date[1])):
            daycurr += 30
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
