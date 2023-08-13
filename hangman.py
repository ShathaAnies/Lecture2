import random
from re import A
words= ["nawal", "shatha", "raeefah"]
choosenWord = random.choice(words)
choosenWordList=list(choosenWord)
print(choosenWord)

tries = 6

# blanks= len(choosenWord) * "_ "
wordLin= len(choosenWord)
gussed = len(choosenWord)*"_ "
print (gussed)

letter= input("Please enter letter: ")
won =True
while won == True :
    
    if letter in choosenWord :
            
            wordLin-=1
            
            if wordLin>0:
                

                
                print (letter,end="")
                letter= input(" yes , Please enter another letter: ")


            else:
                won =False
                print(f"you Win ,, The word was {choosenWord}" )
    else:
                tries-=1
                
                if tries==0:
                   print("you Lose :( \n    +---+ \n    O   |\n   /|\  |\n   / \  |\n      === ")
                elif tries==5 :
                    letter= input("false  \n    +---+ \n        |\n        |\n        |\n      ===  \n Please enter letter: ")
                elif tries==4 :
                    letter= input("false  \n    +---+ \n    O   |\n    |   |\n        |\n      ===  \n Please enter letter: ")
                elif tries==3 :
                    letter= input("false  \n    +---+ \n    O   |\n   /|   |\n        |\n      ===  \n Please enter letter: ")
                elif tries==2 :
                    letter= input("false  \n    +---+ \n    O   |\n   /|\  |\n        |\n      ===  \n Please enter letter: ")
                elif tries==1 :
                    letter= input("false  \n    +---+ \n    O   |\n   /|\  |\n   /    |\n      ===  \n Please enter letter: ")





# name ="shatha"
# name2=list(name)
# print (name2)

# for Litter in choosenWordList :
#     gussed[Litter]=choosenWordList[Litter]
    

