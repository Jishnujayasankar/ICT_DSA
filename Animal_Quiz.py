def guessAnimal(animal):
    for i in range(3):
        guess=input()
        if(animal==guess.lower()):
            print("Currect Answer")
            return 1
            break
        else:
            if(i==2):
                print("You failed! Correct Answer is:",animal)
                return 0
                break
        print("Wrong Answer,Try Again!",end=" ")
         
score=0
print("Guess the Animals!")
print("Which bear lives at the North Pole?",end=" ")
score+= guessAnimal("polar bear")
print("Which is the fastest land animal?",end=" ")
score+= guessAnimal("cheetah")
print("Which is the largest animal?",end=" ")
score+= guessAnimal("whale")

print("Your Score is:",score)