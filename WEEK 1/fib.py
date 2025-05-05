n = int(input("Enter number of terms: "))

a, b = 0, 1
total = 0  # to store the sum

print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=' ')
    total += a
    a, b = b, a + b

print(f"\nSum of the {n} terms is: {total}")
