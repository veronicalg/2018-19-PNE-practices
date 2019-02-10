#from (exercise-1) import count_bases(seq)
#count_bases(seq)


def count_bases(seq):
    """Counting the number of As in the sequence"""

    dic_bases = {}
    bases_list = ["A", "T", "C", "G"]
    for i in bases_list:
        dic_bases[i]= seq.count(i)

    # Return the result
    return dic_bases


seq1 = input("Please enter a valid sequence")
seq2 = input("Please enter a second valid sequence")
seq = [seq1, seq2]
cont = 1
for i in seq:
    tl = len(i)
    print("Sequence", cont, "is {} bases in length" .format(tl))
    cont = cont +1
    dic_bases = count_bases(i)

    for key in dic_bases:
        print("Base", key)
        print(      "Counter:", dic_bases[key])

        if tl > 0:
            perc = round(100.0 * dic_bases[key]/ tl, 1)
            print ("Percentage: ", perc)
        else:
            perc = 0

