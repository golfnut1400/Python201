


def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number: "))
    print("The square of", anum, "is:",squareit(anum))
    print("The cube of", anum, "is:",cubeit(anum))

if __name__ == "__main__":
    main()
