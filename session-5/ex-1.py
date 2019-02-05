def count_a(seq):
    """Counting the number of As in the sequence"""

    result=0
    for i in seq:
        if i == "A":
            result = result +1

    # Return the result
    return result

#Main program
s = "AFTCAGTTGA"
na = count_a(s)
print("The number of As is : {}" .format(na))

# Calculat the total sequence length
tl = len(s)

# Calculate the percentage of As in the sequence
perc = round(100.0 * na/tl, 1)

print("Tge total length is  : {}" .format(tl))
print("The percentage of As is: {}%" .format(perc))
