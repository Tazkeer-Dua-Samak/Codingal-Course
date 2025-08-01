from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def  fact(self):
        pass

class Humming_bird(Bird):
    def  fact(self):
        print("I am the smallest bird in the world!")

class Bald_eagle(Bird):
    def  fact(self):
        print("I am not really bald. Its just a misunderstanding!")

class Crow(Bird):
    def  fact(self):
        print("I love to steal things from your hand and make shrill noises!")

class Parrot(Bird):
    def  fact(self):
        print("People love to keep me as a pet and I repeat what you say to me!")

H = Humming_bird()
H.fact()

B = Bald_eagle()
B.fact()

C = Crow()
C.fact()

P = Parrot()
P.fact()
