from Seq import Seq
Seq()
def main():
    """............"""
    s1= Seq("ACGTCA")
    s2 = Seq("GGGGGGGA")
    s3 = Seq.complement(s1)
    s4 = Seq.reverse(s3)

    list = [s1,s2,s3,s4]

    for i in list:
        return "Sequence", i.get_strbases(), "Length: ", i.len(),  "Bases count: ", i.


