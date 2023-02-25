# 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 + n
sum = 0
n = int(input("Enter the number of terms: "))

for i in range(1, n+1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i


print(sum)