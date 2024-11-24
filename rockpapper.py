import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors ]
userchoice = int( input ("select 0,1,2"))
print (game_images[userchoice])
computerchoice = random.randint(0 ,2)
print ("computer chose:")
print (game_images[computerchoice])

if userchoice >=3 or userchoice<0:
    print ("invalid value ")
elif userchoice ==0 and computerchoice == 2:
    print ("you win ")
elif userchoice ==2 and computerchoice ==0:
    print ("you lose")
elif computerchoice > userchoice :
    print ("you lose")
elif computerchoice == userchoice :
    print ("its a draw")
elif userchoice > computerchoice:
    print ("you win")

