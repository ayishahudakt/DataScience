dict1={}
dict2={}

n1=int(input("enter no.of pairs for 1st dictionary:"))
for i in range(n1):
    key=input("enter key:")
    value=input("enter value:")
    dict1[key]=value
n2=int(input("enter no.of pairs for 2nd dictionary:"))
for i in range(n2):
    key=input("enter key:")
    value=input("enter value:")
    dict2[key]=value

dict1.update(dict2) 
print("merged dictionary using update():",dict1)

merged1={**dict1, **dict2}
print("merged dictionary using **operator",merged1)

#only python 3.9+
#merged2=dict1 | dict2
#print("merged dictionary using | operator",merged2)

