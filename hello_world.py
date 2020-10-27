# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Aisha"
print("Hello" , name )	# with a comma
print("hello" + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 7
print("Hello" , name )	# with a comma
# print("Hello" + name )	# with a +	-- this one should give us an error!
name = 7
print ("Hello " + str(name)) # ninja challenge ??
# # 4. print "I love to eat sushi and pizza." with the foods in variables
food1 = "sushi"
food2 = "pizza"
print("I love to eat {} and {}.".format(food1, food2)) # with .format()
print(f"My favorite food is {food1} and {food2}") # with an f string

count = 0
while count < 5:
    print("looping - ", count)
    count += 1
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
