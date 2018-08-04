'''
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords
have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random,
generating a new password every time the user asks
for a new password. Include your run-time code in a main method.
'''
import random, io, string

with open("passwords.txt") as file:
    data = file.readlines()

class Password:
    def __init__(self):
        self.strength = input("Would you like a weak, medium, or strong password?\n").lower()
        self.result = ""
        while not (self.strength in ("weak", "medium", "strong")):
            self.strength = input("Please choose from one of the three options:\n weak, medium, strong.\n").lower()

    def randomString(self, size=8, chars=string.ascii_letters + string.punctuation + string.digits):
        '''Thanks to https://stackoverflow.com/a/2257449'''
        return ''.join(random.choice(chars) for _ in range(size))

    def generate(self):
        if(self.strength == "weak"):
            return self.result.join(data[random.randint(0, 2999)]).replace("\n", "") + \
                   self.result.join(data[random.randint(0, 2999)])
        if(self.strength == "medium"):
            self.result = self.randomString()
            return self.result
        if(self.strength == "strong"):
           self.result = self.randomString(30)
           return self.result
        else:
            return "You should not see this message. Something went wrong."



def main():
    password = Password()
    print("Your password strength is {}.".format(password.strength))
    print("Your password is: {}".format(password.generate()))
    return

if __name__ == "__main__": main()
