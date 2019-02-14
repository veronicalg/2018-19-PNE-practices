from Seq import Seq

# Seq()


s1 = Seq("ACGTCA")
s2 = Seq("GGGGGGGA")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())  # We cannot atribute reverse to a string object.
list = [s1, s2, s3, s4]
# """This function organices our program and prints the 4 sequences, its length, number of bases and percentage of bases"""

cont = 1
for sequence in list:
    print("The sequence ", cont, "is: ", sequence.get_strbases())
    cont = cont + 1
    print(sequence.len())
    # dic_bases = count_bases(i)
    # print("Bases count: ", dic_bases)
    for base in sequence.get_strbases():
        dic = {}
        dic[base] = base.count(base)
    print("The number of bases of every type are: ", dic[base])
    for base in sequence.get_strbases():
        dict_perc = {}
        dict_perc[base] = base.perc(base)
    print('The percentage of bases of every type are: ', dict_perc[base])
    # bases = ["A"]
    # for i in bases:
