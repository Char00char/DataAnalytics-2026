#Step 1: Create/open the file in append mode
f = open("about_me.txt", "a")

#Step 2: Add new information to the file
f.write("\nIf I could do anything for my perfect night out, ")
f.write("I would go to a nice restaurant and then watch a movie with friends.\n")

#Step 3: Close the file
f.close()

#Open file in read mode
f = open("about_me.txt", "r")

#Read first 50 characters
first_50 = f.read(50)

#Read the next four lines into a list
next_four_lines = []

for i in range(4):
    next_four_lines.append(f.readline())

#Read the next 100 characters rounded to full lines
next_100 = f.read(100)

#Print the results
print("First 50 characters:")
print(first_50)

print("\nNext four lines, as list by lines:")
print(next_four_lines)

print("\nNext 100 characters, as a list by line, rounded to full lines:")
print(next_100)

#Close the file
f.close()
