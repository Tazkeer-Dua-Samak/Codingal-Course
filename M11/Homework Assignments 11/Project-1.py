def circuitOutput(A, B, C):
    First_AND = A & B
    Second_AND = B & C
    First_OR = B | C
    Third_AND = First_OR & Second_AND
    Q = First_AND | Third_AND
    return Q

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(f"For : A = {A}, B = {B}, C = {C}, \n\t\t\t   Q = {circuitOutput(A, B, C)}")