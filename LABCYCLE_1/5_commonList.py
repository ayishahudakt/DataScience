l1=input("Enter elements of first list  separated by space:").split()
l2=input("Enter elements of second list  separated by space:").split()

common=False
for i in l1:
    if i in l2:
        common = True
        break

print("Do the lists have at least one common member?", common)

