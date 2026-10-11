import random
score = 0
while True:
 r = random.randint(0,10)
 play = input("Guess a number between 0 to 10: ")
 if play.isdigit():
     if play == r:
         print(f"You guess:{play}")
         print(f"Computer guess:{r}")
         print("You Win!")
         score+=1
     else:
         print(f"You guess:{play}")
         print(f"Computer guess:{r}")
         print("You Loss!")
         print(f'You correctly guessed {score} numbers')
 else:
    print("Please enter a digit.")