
def isPrime(n):

    for i in range(2, n):
        if n % i == 0:
            return ("Not prime")
    return "Prime"


n = int(input("Enter the number: "))

j = 2
l1 = []
count = 0

while count < n:
    if isPrime(j) == "Prime":
        l1.append(j)
        count += 1
    j += 1

print(l1)