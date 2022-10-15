print("First task")
a=4-2**3+5*2-3/2
print(a)

print("\nSecond task")
b=int (input("Please enter a number"))
print(bin(b))

print("\nThird task")
c=float (input("Please enter a number of hours worked"))
d=float (input("Please enter salary per hour"))
print(c*d)

print("\nFourth task")
x=(input("Please enter three numbers separated by space").split())
for i in range(len(x)):
    x[i]=int(x[i])
print(sum(x)/len(x))

print("\nFifth task")
y=(input("please enter your name and age separated by space").split())
y[-1]=int(y[-1])
print(100-y[-1])