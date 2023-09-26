pool = 1000
quantity = int(input("Enter the number of mailings: "))

if quantity == 0:
    print("Divide by zero completed!")
else:
    chunk = pool // quantity
    print("Chunk size:", chunk)