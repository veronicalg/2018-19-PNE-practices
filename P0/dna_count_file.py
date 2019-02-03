A= 0
C =0
T=0
G=0
def load_data(filename):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip("\n")
            return line

def count_bases(line):
        for i in line:
            if i == "A":
                A = A+1
            elif i == "C":
                C =C+1
            elif i =="T":
                T =T+1
            elif i == "G":
                G =G+1
        return(len(line), A, C, G, T)

def main():
    filename = input("Please enter a valid filename")
    line = load_data(filename)
    (total, A, C, G, T) = count_bases(line)
    print('Total length:', total)
    print('A: ', A)
    print('C :', C)
    print('G:', G)
    print('T:', T)
