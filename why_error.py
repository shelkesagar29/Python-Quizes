# Special methods in python

class methodtest:
    hour=0 # when you define variable here, they are global
    minutes=0
    seconds=0

    def __init__ (self,hour,minutes,seconds):# class constructors
        self.hour=hour
        self.minutes=minutes
        self.seconds=seconds

    def printtime(self):
        print ((self.hour)+":"+(self.minutes)+":"+(self.seconds))
        # because here we are trying to add string with int which is not possible
        # Remember python is strongly typed language
        #solution: try to convert self.hour in string and print

    def __str__ (self): # Method to change object representation
        #keep in mind, for this function return type is always string
        return str(self.hour)+":"+str(self.minutes)+":"+str(self.seconds)

    #printing in two different ways

time=methodtest(7,45,26)
time.printtime()
print (time)