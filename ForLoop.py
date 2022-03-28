for i in range(1,10,1):#start,stop,step
    print(i)

for i in range(10):#start = 0 and stop = 10 and step as 1 by default
    print(i)

print("---------------------")
for i in range(10,1,-1):#start = 1 and stop = 10 and step as 1 by default
    print(i)

for a in range(0,100,5):
    print(a)
    if a == 50:
        break
else:
    print("No items left")

fruit = ["apple","mango","orange"]
for f in fruit:
    print(f)