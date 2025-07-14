n=int(input("enter no.of pairs:"))
pair = []
for i in range(n):
    key=input(f"enter the key for pair {i+1}:")
    value=input(f"enter the value for pair {i+1}:")
    pair.append((key,value))

print(pair)
result=dict(pair)
print("\n after conversion", result)

