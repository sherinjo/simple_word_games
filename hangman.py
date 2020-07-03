
import random 

def get_word(): 
      
    words = ['imagine', 'welcome', 'science', 'programming', 
             'mathematics', 'bright', 'condition', 'learning', 
             'water', 'board', 'answers']
    
    pick = random.choice(words) 
  
    return pick 
  
   
myword = get_word() 
  

for i in myword: 
      
    print("*", end = " ") 
      

l = len(myword) 
print("\nWord has %d letters" %l) 
  
# Check if entered letter is correct 
def check(myword, your_word, guess1): 
    status = '' 
    matches = 0
      
    for letter in myword: 
        if letter in your_word: 
            status += letter 
        else: 
            status += '*'
        if letter == guess1: 
            matches += 1
              
    if matches > 1: 
        print(matches, guess1) 
          
    elif matches == 1: 
        print(guess1) 
    return status 
  
# Main Game function 
def game(): 
    guess = 0
    guessed = False
    your_word = [] 
    turns = len(myword) + 1
    turns1 = turns 
      
    print("Total turns: ", turns) 
    while guess < turns1: 
        guess1 = input("Enter your guess: ") 
          
        # Decrementing turn 
        # after every guess 
        turns -= 1
          
        # Print turns left 
        print("Turns left", turns) 
          
        # If letter is already guessed 
        if guess1 in your_word: 
            print("You already guessed") 
        elif len(guess1) == 1: 
              
            # Appending the letters 
            # on their place 
            your_word.append(guess1) 
            result = check(myword, your_word, guess1) 
              
            if result == myword: 
                guessed = True 
                print("You won " ) 
                print(myword)
                break
            else: 
                print(result) 
                
        else: 
            print("Invalid entry") 
            guess = int(input("press 1 to continue and 0 to quit :"))
            if guess == 0: 
               print("Word is:") 
               print(myword) 
      
  
# Driver Code 
game() 

