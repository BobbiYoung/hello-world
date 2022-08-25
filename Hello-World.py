import random

#Used https://replit.com/languages/python3 to write and test 

#print out Hello, World!
print("Hello, world! \n")

greeting = "Hello, world!"
status = "just getting started here"
who = "I'm"
projects = ["Python coding", "Java coding", "Dog training", "Remodel my basement", "Finish Masters degree", "Binge all of Netflix"]

#print out greeting and current status
print(greeting, who, status + ". \n")

#print out a random project from projects array
print("Other projects", who, "working on:", random.choice(projects))
