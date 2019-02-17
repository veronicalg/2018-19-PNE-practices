from Seq import Seq
# We have imported the class Seq.

#Creating 4 objects: s1,s2,s3,s4
s1 = Seq("ACGTCA")
s2 = Seq("GGGGGGGA")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())
list = [s1, s2, s3, s4] #A list is created with the 4 objects.


cont = 1
dic = {} #A dictionary is created to store the number of every base.
dict_perc = {} #A dictionary is created to store the % of every base.
for sequence in list: #For every object in the  list, it is going to be printed: the string sequence, length, a dictionary with the number of bases and a dictionary with the % of bases.
    print("The sequence ", cont, "is: ", sequence.get_strbases()) #Calling the method .get_strbases().
    print("The length of the sequence is: ", sequence.len()) #Calling the method .len().

    bases_list = ["A", "C", "T", "G"]

    for i in bases_list:
        dic[i] = sequence.get_strbases().count(i) #Calling the method .count(base).
        dict_perc[i] = sequence.perc(i) #Calling the method .perc()
    print("The number of bases in the sequence", cont, "is: ", dic)
    print("The percentage of every base in the sequence", cont, "is", dict_perc)
    cont = cont + 1

