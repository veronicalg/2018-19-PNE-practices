class Seq:
    def __init__(self, strbases):
        """A class for representing sequences"""
        print("New sequence created!")

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

    def get_strbases(self):
        return self.strbases

    def len(self):
        tl = len(self.strbases)
        return "The length of the sequence is :", tl

    def count(self, base):
        return "The number of", base, "that appears in the sequence is :", self.strbases.count(base)

    def perc(self, base):
        if len(self.strbases) < 0:
            return "Sorry that is not a valid sequence"

        elif len(self.strbases) > 0:
            perc= round(100.0 * self.strbases.count(base) / len(self.strbases), 1)
            return "The percentage of the base", base, 'in your DNA sequence is: ', perc


    def complement(self):
        output = []
        for i in self.strbases:
            if i == "A":
                output.append("T")
            elif i == "T":
                output.append("A")
            elif i == "C":
                output.append("G")
            elif i == "G":
                output.append("C")

        str = "".join(output) #Conversion from list to str

        return str

    def reverse(self):
        "This function returns the reverse of your sequence"
        return (self.strbases[::-1])


s1 = Seq("ACTG")

print(s1.perc("A"))
print(s1.count("A"))
print(s1.reverse())
print(s1.complement())

