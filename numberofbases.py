DNA = input("Please enter a valid DNA sequence")

def count(DNA):

    A = 0
    C = 0
    T = 0
    G = 0



    for i in range((DNA)):
        if i == "A":
            A = +1
        elif i == "C":
            C +=1
        elif i == "G":
            G +=1
        elif i == "T":
            T =+=1
        else:
            stop
            print("Sorry that is not a valid DNA sequence")

    return A,C,G,T

print()
