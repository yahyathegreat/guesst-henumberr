import random
import time
number=random.randint(1, 300)
def intro():
    print("may i ask you for your name")
    global name
    name = input()
    print(name + ", we are going to play a game, i am thinking of a number between 1 and 100")
    if(number%2==0):
            x= 'even'
    else:
            x= 'odd'
   print("\nthis id an {} number". format(x))
    time.sleep(.5)
    print("go ahead. Guess!")
def pick():
       guessestaken = 0
       while guessestaken < 6:
             time.sleep(.25)
             enter=input("Guess: ")
             try:
                   guess = int(enter)
                   if guess<=100 and and guess>=1:
                         guessestaken=guessestaken+1
                         if guesstaken<6:
                          if guess<number:
                            print("the guess of the number you have entered is too low")
                          if guess>number:
                                print("the guess of the number you have entered is too high")
                          if guess != number:
                                     time.sleep(.5)
                                     print("try again!")