def count_bases(seq):
    """Counting the number of As in the sequence"""

    dic_bases = {}
    bases_list = ["A", "T", "C", "G"]
    for i in bases_list:
        dic_bases[i]= seq.count(i)

    # Return the result
    return dic_bases


seq = input("Please enter a valid sequence")
tl = len(seq)
print("This sequence is {} bases in length" .format(tl))
dic_bases = count_bases(seq)

for key in dic_bases:
    print("Base", key)
    print(      "Counter:", dic_bases[key])

    if tl > 0:
        perc = round(100.0 * dic_bases[key]/ tl, 1)
        print ("Percentage: ", perc)
    else:
        perc = 0
