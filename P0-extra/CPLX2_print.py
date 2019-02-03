def load_data(filename):
    with open(filename, "r") as f:
        return f

def main():
    filename = input("Please enter the correct filename")
    file = load_data(filename)
    print(file)
