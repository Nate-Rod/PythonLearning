'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
#from datetime import date

class User:
    def __init__(self):
        self.name = input("What is your name, user?\n").capitalize()
        self.age = int(input("And how old are you, {}?\n".format(self.name)))
        self.turnsAHundred = (2018 - self.age) + 100
    def hundredYears(self):
        if(self.turnsAHundred > 2017):
            print("{}, you will turn 100 years old in the year {}.\n"
              .format(self.name, self.turnsAHundred))
        else:
            print("{}, you turned 100 years old in the year {}.\n"
              .format(self.name, self.turnsAHundred))

user = User()
user.hundredYears()


