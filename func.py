def sum(a,b):
    return a + b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def sub(a,b):
    return a - b

def say():
    print(__name__)

def main():

    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(sum(a,b))
    print(mult(a,b))
    print(div(a,b))
    print(sub(a,b))

if __name__ == "__main__":
    main()