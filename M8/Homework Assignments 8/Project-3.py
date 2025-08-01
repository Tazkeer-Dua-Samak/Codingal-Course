class tom():
    name = "Tom"
    working = "I often chase Jerry."

    def introduction(self):
        print("Hi! My name is", self.name)

    def details(self):
        print("I am a Robot! My main objective is to Capture unauthorized rodent activity "
        "and looking good while doing it is my secondary objective")
        print(self.working)

ob = tom()
ob.introduction()
ob.details()

class jerry():
    name = "Jerry"
    working = "I love to tease Tom."

    def introduction(self):
        print("Hi! My name is", self.name)

    def details(self):
        print("I am a Robot as well! But I am based off of a Stealth Operative Model. " \
        "I am small, I am fast, and I always win no matter what Tom does to defeat me.")
        print(self.working)

ob = jerry()
ob.introduction()
ob.details()