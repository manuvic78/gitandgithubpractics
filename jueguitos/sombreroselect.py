Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0 
Gryffindor = 0 
 

Quest_1= int(input( "Q1) Do you like Dawn or Dusk? 1) Dawn  2) Dusk:  "))
if Quest_1==1:
  Gryffindor += 1
  Ravenclaw +=1
elif Quest_1 ==2:
  Slytherin += 1
  Hufflepuff += 1
else:
  print ("Wrong input.")

Quest_2= int(input("Q2) When I’m dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold: "))

if Quest_2 ==1:
  Hufflepuff +=2
elif Quest_2 ==2:
   Slytherin +=2
elif Quest_2 ==3:
   Ravenclaw +=2
elif Quest_2 ==4:
  Gryffindor +=2
else :
   print ("Wrong input.")

Quest_3= int(input("Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum:  "))

if Quest_3 ==1:
   Slytherin +=4
elif Quest_3 ==2:
  Hufflepuff +=4
elif Quest_3 ==3:
   Ravenclaw +4
elif Quest_3 ==4:
  Gryffindor +=4
else :
   print ("Wrong input.")

max_score = max(Gryffindor, Hufflepuff, Ravenclaw, Slytherin)  

if max_score == Gryffindor:  
    house = "Gryffindor"  
elif max_score == Hufflepuff:  
    house = "Hufflepuff"  
elif max_score == Ravenclaw:  
    house = "Ravenclaw"  
else:  
    house = "Slytherin"  

print(f"\nScores:\nGryffindor: {Gryffindor}\nHufflepuff: {Hufflepuff}\nRavenclaw: {Ravenclaw}\nSlytherin: {Slytherin}")  
print(f"\nThe house you belong to is: {house} 🎉")      
