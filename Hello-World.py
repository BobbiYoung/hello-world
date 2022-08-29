import random

#Used https://replit.com/languages/python3 to write and test 

#Print out Hello, World!
print("Hello, world! \n")

#Defines several elements
greeting = "Hello, world!"
status = "just getting started here"
who = "I'm"
projects = ["Python coding", "Java coding", "Dog training", "Remodel my basement", "Finish Masters degree", "Binge all of Netflix"]
num = random.randrange(1,260,2)

#Print out greeting and current status
print(greeting, who, status + ". \n")

#Print out a random project from projects array
print("Other projects", who, "working on:", random.choice(projects))
print("And", num, "more... \n")

#Define and call the functions
#Define second function
def favnumber():
  print("49.")

#Define first function
def primary():
  colors = ["~green~", "*purple*", "-blue-", "+red+"]
  print("Let's call a function.\n")
  print("My favorite color right now is", random.choice(colors), "\nAnd my favorite number is", end=' ') 
  #Call second function in the first function
  favnumber()
 
#Call first function
primary()
