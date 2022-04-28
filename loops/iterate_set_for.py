print('Set Iteration')
set={1,2,3,4,5,6}
for i in set:
    print(i)

print('\nString Iteration')
a='Subhash'
for i in a:
    print(i)

print('\nList Iteration\n')
b=["Coding","is","my","Passion"]     # 'is'  is a keyword so we can't use it directly 
for i in b:
    print(i)

print("\nTuple Iteration\n")
c=("python", "is", "life")
for i in c:
    print(i)
print()

for i in range(10):
    print(i, end=" ")
print()


d=["programming","is","my","passion"]
print()
for i in range(len(d)  ):
    print(d[i])
else:
    print("inside the else block")

print("Continue Statement: It returns the control to the beginning of the loop.")
word="geeksforgeeks"
for letter in word:
    if letter=='e' or letter =='s':
        continue
    print('Current letter:' ,letter)  
    # var=2
print()

# word1="geeksforgeeks"
# for i in word1:
print("Break Statement: It brings control out of the loop")
for i in 'geeksforgeeks':
    if i=="k" or i == "s":
        break
    print("iterated elements:",i)
print("current letter:" ,i)
print()



# word2="geeksforgeeks"
# for i in word2:
#     if i=="k" or i=="o":
#         pass
#     print(i)

# Pass Statement: We use pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.
print("We use pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.")
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)


fruits = ["apple", "orange", "kiwi"]
 
# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)
 
# Infinite while loop
while True:
  try:
    # getting the next item
    fruit = next(iter_obj)
    print(fruit)
  except StopIteration:
 
    # if StopIteration is raised,
    # break from loop
    break

