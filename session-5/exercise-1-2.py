from Bases import count_bases
#seq = input("Enter the sequence")
#count_bases(seq)
#print(count_bases(seq))

def main():
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

main()
