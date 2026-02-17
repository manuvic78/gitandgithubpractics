import random 

question= input("what is your question? :  ")

num = random.randint(1,9)

if num == 1:
  print (f"{question} yes!, absolutly")

elif num == 2:
  print(f"{question} it is decidedly so")

elif num == 3:
  print (f"{question} without a bout")

elif num == 4:
  print (f"{question} Reply hazy, try again.")

elif num == 5:
  print (f"{question} Better not tell you now.")

elif num == 6:
  print (f"{question} My sources say no.")

elif num == 7:
  print (f"{question} Outlook not so good.")

else:
  print(f"{question} very doubtful")