for i in range(1,100):
    if i >=0 and i<10:
        print(f"{i:02}", end=', ')
    else:
        print(i,end=', ')

p = input("Enter a letter to print a pattern")
if p in ['a', 'e','i','o','u']:
    print("Vowels are not allowed in the innput")
elif len(p) > 1:
    print("the length of the character should be one")
else:
    for i in range(1, 5 + 1):
        print(p * i)
word = input("Enter a word to check if it is palendrom")
if p == p[::-1]:
    print("it is a palendrom")
else:
    print("it is not a palendrom")


count = 0
for i in range(1,51):
    if i % 2 == 0:
        if i%3 == 0:
            print("Three")
            count +=1
        elif i%5 ==0:
            print("Five")
            count +=1
        else:
            print(i)
print(f"numbers divided by three and five are {count} ")


    