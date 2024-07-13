for i in range(10,21):
    print(i, end=' ')

print(" ")
for i in range(10,21,2):
    print(i, end=' ')

gap = int(input("\nenter the gap"))
start = int(input("enter the starting point"))
end = int(input("enter the ending point"))

for i in range(start,end,gap):
    print(i, end=' ')