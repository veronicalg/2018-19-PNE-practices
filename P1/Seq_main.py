from Seq import Seq


# Seq()


s1 = Seq("ACGTCA")
s2 = Seq("GGGGGGGA")
s3 = Seq.complement(s1)
s4 = Seq.complement(s1).reverse(s1) #We cannot atribute reverse to a strin object.
list = [s1, s2, s3, s4]
def main():
    """This function organices our program and prints the 4 sequences, its length, number of bases and percentage of bases"""

    cont = 1
    for sequence in list:
        print("The sequence ", cont, "is: ", sequence.get_strbases())
        cont = cont + 1
        print("The total length is: ", sequence.len())
        # dic_bases = count_bases(i)
        # print("Bases count: ", dic_bases)
        for base in sequence:
            dic = {}
            dic[base] = base.count(base)
        print("The number of bases of every type are: ", dic[base])
        for base in sequence:
            dict_perc = {}
            dict_perc[base] = base.perc(base)
        print('The percentage of bases of every type are: ', dict_perc[base])



