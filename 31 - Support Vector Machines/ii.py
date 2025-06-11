n = int(input("Enter the number of rows: "))
k = n
for i in range(1, n + 1):
    # Print leading spaces
    for s in range(1, k):
        print(" ", end="")
    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")
    # Print increasing numbers
    for j in range(2, i + 1):
        print(j, end="")
    # Move to the next line
    print()
    k=k-1
