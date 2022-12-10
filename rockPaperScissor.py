#rock paper scissor

from random import randint

score = 0


for i in range(1,11):
    your_guess = int(input())
    computer_guess = randint(1,3)

    if your_guess == 1 and computer_guess == 1:
        print("🆕You And Computer Chose Same One!")
    
    elif your_guess == 1 and computer_guess == 2:
        print("Computer Chose Paper🖐️")
        print("You Chose Rock✊")
        print("😵You Lost!😵")    

    elif your_guess == 1 and computer_guess == 3:
        print("Computer Chose Scissor✌️")
        print("You Chose Rock✊")
        print("🏆You Win!🏆")
        score+=1
        
    elif your_guess == 2 and computer_guess == 1:
        print("Computer Chose Rock✊")
        print("You Chose Paper🖐️")
        print("🏆You Win!🏆")
        score+=1
        
    elif your_guess == 2 and computer_guess == 2:
        print("🆕You And Computer Chose Same One!")

    elif your_guess == 2 and computer_guess == 3:
        print("Computer Chose Scissor✌️")
        print("You Chose Paper🖐️")
        print("😵You Lost!😵")    

    elif your_guess == 3 and computer_guess == 1:
        print("Computer Chose Rock✊")
        print("You Chose Scissor✌️")
        print("😵You Lost!😵") 
    
    elif your_guess == 3 and computer_guess == 2:
        print("Computer Chose Paper🖐️")
        print("You Chose Scissor✌️")
        print("🏆You Win!🏆")
        score+=1
        
    elif your_guess == 3 and computer_guess == 3:
        print("🆕You And Computer Chose Same One!")
    
    else:
        print("Error...\nYou Can Just Type- 1,2,3")


    print("Another Try?")


print("Your Score Is",score)

print("Win Rate", (100/10*score),"%")
