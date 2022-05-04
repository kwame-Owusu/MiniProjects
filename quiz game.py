import time
import sys
import os
  
# Function for implementing the loading animation
def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "Preparing the game..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
  
# Driver program
if __name__ == '__main__': 
    load_animation()
  
    # Your desired code continues from here 
    # s = input("Enter your name: ")
    s ="Player"
    sys.stdout.write("Hello "+str(s)+"\n")


print("Welcome to my first computer quiz!")

playing = input("do you want to play?  ")

if playing.lower() == "yes":
	print('Hello there, lets start :')  

else:
    quit()  
score = 0





print ('What is your name ')

answer = input()

print('Nice to meet you ' + answer + '!')

print ('letss goooo ')


answer = input('What is Ghana? ')

if answer.lower() == 'an african country' :
    print('Correct!')
    score += 1
    

else:
      print ('Incorrect!') 
     

print('Next question 😀')
 

answer =  input('1,2,3,4,5.0, 5.001' + ' Which of these numbers is 5 ')

if answer == '5.0':
    print( 'Nice! 👍')
    score += 1

else:
    print('Did you forget your integers and floats!! 😒') 
   


print('Next question(tricky question)🤪🤭')


answer = input('What is it that lives if it is fed, and dies if you give it a drink? ')
 
if answer.lower() == 'fire':
    print('Wow, you tally rascally 🧐')
    score += 1

else:
    print('Nevermind it was a difficult riddle anyway 😌') 
    
    

print('Here is the "Final Boss" Question')
 
answer = input('What is a part of the book 1984, that was turned into a show and movie? ')

if answer.lower() == 'room 101' :
    print('Wow good job 👏👏')
    score += 1

else:
    print('Go get cultured!') 





print("You got " +  str(score)  + " questions correct!")

print("You got " +  str((score / 4) * 100)  + "%")
 



    












