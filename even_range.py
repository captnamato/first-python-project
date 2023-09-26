sum = 0

while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    else:   
        for i in range(num+1):
            if i % 2 == 0:
              sum += i

print("Sum of even numbers:", sum)
