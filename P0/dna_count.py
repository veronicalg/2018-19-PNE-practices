sequence = input("Please enter a valid DNA sequence")
A=0
C=0
T=0
G=0
for i in sequence:
    if i == "A":
        A = A+1
    elif i == "C":
        C =C+1
    elif i =="T":
        T =T+1
    elif i == "G":
        G =G+1
    else:
        print("Sorry that is not valid sequence")

print('Total length:', len(sequence))
print('A:', A)
print('C:', C)
print('G:', G)
print('T:', T)
