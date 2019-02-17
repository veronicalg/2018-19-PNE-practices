# We have imported the class Seq.
from Seq import Seq

#Creating 4 objects: s1,s2,s3,s4
s1 = Seq("ACGTCA")
s2 = Seq("GGGGGGGA")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

#A list is created with the 4 objects.
list = [s1, s2, s3, s4]


cont = 1
#A dictionary is created to store the number of every base.
dic = {}
#A dictionary is created to store the % of every base.
dict_perc = {}

#For every object in the  list, it is going to be printed: the string sequence, length, a dictionary with the number of bases and a dictionary with the % of bases.
for sequence in list:
    print("Sequence ", cont, ":  ", sequence.get_strbases()) #Calling the method .get_strbases().
    print("Length : ", sequence.len()) #Calling the method .len().

    bases_list = ["A", "C", "T", "G"]

    for i in bases_list:
        dic[i] = sequence.get_strbases().count(i) #Calling the method .count(base).
        dict_perc[i] = sequence.perc(i) #Calling the method .perc()
    print("Bases count : ", dic)
    print("Bases percentage :", dict_perc)
    cont = cont + 1

