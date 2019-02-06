def count_bases(seq):
    """Counting the number of As in the sequence"""

    vars_bases = {}
    bases_list = ["A", "T", "C", "G"]
    for i in bases_list:
        vars_bases[i]= [seq.count(i)]

    # Return the result
    return vars_bases


seq = input("Please enter a valid sequence")
tl = len(seq)
vars_bases = count_bases(seq)

print("This sequence is {} bases in length" .format(tl))


for key in vars_bases:
    print("Base", key)
    print(      "Counter:", vars_bases[key])

    if tl > 0:
        perc = round(100.0 * vars_bases[key]/ tl, 1)
    else:
        perc = 0

    print ("percentage", perc)



#main()


#tl = len(s)

# Calculate the percentage of As in the sequence
#if tl >0:
#    perc = round(100.0 * na/tl, 1)
#else:
#    perc=0

#print("This sequence is  : {}" .format(tl) "in length")
#print("The percentage of As is: {}%" .format(perc))
