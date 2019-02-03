def fibonacci(n):
    a = 0
    b = 1
    count = 0
    for i in range(n+1):
        count = count + a
        a = b
        b = a+b
    return count

def main():
    n = int(input("Please enter a sequence of numbers"))
    sum = fibonacci(n)
    print(sum)
