


def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():         # creation of main
    anum = int(input("Please enter a number: "))
    print("The square of", anum, "is:",squareit(anum))  # calls function above
    print("The cube of", anum, "is:",cubeit(anum))

if __name__ == "__main__":
    main()
