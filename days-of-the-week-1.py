class WeekDayError(Exception):
    pass

class Weeker:
    day_lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day in self.day_lst:
            self.__day = day
        else:
            raise WeekDayError

    def __str__(self):
        return(self.__day)

    def add_days(self, n):
        self.__day = self.day_lst[(self.day_lst.index(self.__day) + n)%7]
  
    def subtract_days(self, n):
        self.__day = self.day_lst[(self.day_lst.index(self.__day) - n)%7]

try:
    weekday = Weeker('Mon')
    print(weekday)

    weekday.add_days(1)
    print(weekday)
    
    weekday.subtract_days(23)
    print(weekday)
    
    weekday = Weeker('Monday')
    
except WeekDayError:
    print("Sorry, I can't serve your request.")
  
