class Timer:
    def __init__(self, h, m, s):
        self.__h = int(h)
        self.__m = int(m)
        self.__s = int(s)

    def __str__(self):
        return(str(self.__h).zfill(2)+':'+str(self.__m).zfill(2)+':'+str(self.__s).zfill(2))

    def next_second(self):
        self.__s += 1
        if self.__s == 60:
            self.__s = 0
            self.__m += 1
            if self.__m == 60:
                self.__m = 0
                self.__h += 1
                if self.__h == 24:
                    self.__h = 0
                
    def prev_second(self):
        self.__s -= 1
        if self.__s == -1:
            self.__s = 59
            self.__m -= 1
            if self.__m == -1:
                self.__m = 59
                self.__h -= 1
                if self.__h == -1:
                    self.__h = 23

timer = Timer(23, 59, 59)
print(timer)

timer.next_second()
print(timer)

timer.prev_second()
print(timer)
