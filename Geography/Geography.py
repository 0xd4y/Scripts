#!/usr/bin/python3

from difflib import SequenceMatcher
import random
import time
import sys

replycon = 0
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
hints = -1
right = 0
close = 0
wrong = 0
helped = 0
hinted = 0
questions = []

right_countries = []
close_countries = []
wrong_countries = []
hint_countries = []

right_capitals = []
close_capitals = []
wrong_capitals = []
hint_capitals = []

print("\nLet's see how well you know your geography!\n")
print("If you would ever like to exit press Ctrl C.\n")
print('Type "score" to see all the questions you got right, close, and wrong')
print("Good luck!\n")
time.sleep(2)

def score():
    print("\n\nThe amount of questions you have done so far:", str(len(set(questions)))+"/196","("+str(((len(set(questions)))/196*100))+"%)")
    print("\n\n----------Questions Right----------\n")
    print("Answers right:", str(right) + "\n\n")
    for country,answer,reply in right_capitals:
        print("What is the capital of " + country + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    print('\n')
    for capital,answer,reply in right_countries:
            print("What is the country with the capital city of " + capital + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    print("\n\n----------Questions Close----------\n")
    print("Answers close:", str(close) +"\n\n")
    for country,answer,reply in close_capitals:
            print("What is the capital of " + country + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    print('\n')
    for capital,answer,reply in close_countries:
            print("What is the country with the capital city of " + capital + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    print("\n\n----------Questions Incorrect----------\n")
    print("Answers wrong:", str(wrong) + "\n\n")
    for country,answer,reply in wrong_capitals:
        print("What is the capital of " + country + "? Correct answer:",answer,"   You replied: "+ reply)
    print('\n')
    for capital,answer,reply in wrong_countries:
            print("What is the country with the capital city of " + capital + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    print("\n\n----------Questions Close or Correct With Hints----------\n")
    print("Answers close or correct with help:", str(helped) + "\n\n")
    for country,answer,reply in hint_capitals:
        print("What is the capital of " + country + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    print('\n')
    for capital,answer,reply in hint_countries:
            print("What is the country with the capital city of " + capital + "? ","Correct answer: ",answer,"   You replied: "+ reply)
    if(len(questions)<196):
        end_review = input("\n\nHit any key if you would like to continue the game.\n")
    elif(len(questions) == 196):
        end_review = input("\n\nHit any key if you would like to exit the game.\n")
        sys.exit()
    if(end_review!=None):
        pass




def main():
    global helped
    global hints
    global replycon
    global replycap 
    global chance
    global randomp
    replycon = 0
    replycap = 0
    hints = -1
    guess = 0
    hint = 0
    if(len(questions)==196):
        print("\nThanks for playing the game! By the way, Beron is my best friend and he is really cool.")
        time.sleep(3)
        score()
    while(True):
        randomp = random.randint(1,196) 
        if(randomp not in questions):
            questions.append(randomp)
            break
    #if equal to or greater than 6 ask for capital given country, otherwise if chance less than or equal to 5 ask for country given capital
    chance = random.randint(1,10)
    
    time.sleep(2)        
    print(chr(27) + "[2J")
    print ('\n      ------------------------')
    print ('          Answers right:', right)
    print ('          Answers close:', close)
    print ('          Answers wrong:', wrong)
    print ('          Answers correct or close with hints:', helped)
    print("          Questions completed:", str(len(set(questions))-1)+"/196","("+str(((len(set(questions))-1)/196*100))+"%)")
    if(wrong!=0):
        print ('          Percent correct:', str(float((right+close)/(wrong+right+close)*100))+"%")
        print ('      ------------------------\n\n')
    elif(wrong+close+right==0): 
        print ('          Percent correct: N/A')
        print ('      ------------------------\n\n')
    else:
        print ('          Percent correct: 100%')
        print ('      ------------------------\n\n')
    con = 1
    with open ('countries.txt', 'r') as countries:
        #scan for all lines up to random integer
        while(True):
            for line in countries: 
                if (con == randomp):
                    country = line.rstrip("\n\r")
                    answercon = country.lower()
                    break
                else:
                    con = con + 1
            break
        
    cap = 1
    with open ('capitals.txt','r') as capitals:
        while(True):
            for line in capitals:

                if (cap == randomp):
                    capital = line.rstrip("\n\r")
                    answercap = capital.lower()
                    break
                else:
                    cap = cap + 1 
            break
        if (chance <= 5):
            replycon = input ("What is the country with the capital city of " + capital + "? ")
            replycon1 = replycon
            replycon = replycon.lower()
            if(replycon == "score"):
                questions.pop()
                score()
                main()
        else:
            
            replycap = input ("What is the capital of " + country + "? ")
            replycap1 = replycap
            replycap = replycap.lower()
            if(replycap == "score"):
                questions.pop()
                score()
                main()

  
    answer = list()
    def hint():

        global hints
        hints = hints + 1
        print(chr(27) + "[2J")
 
        if (chance <=5):
            
            answer.append(country[hints])
            print ("\nThe answer has", len(country), "characters.\n")
            print (''.join(map(str, answer)))
            #p = answercon[hints], "___ "*(len(answercon)-(hints+1))))
            
        else:
            answer.append(capital[hints])
            print ("\nThe answer has", len(capital), "characters.\n")
            print (''.join(map(str, answer)))
             
        
    def countries(guess,replycon,answercon):
        global hinted
        global helped
        if (replycon == answercon):
            global right
            if(hinted==0):
                right = right + 1
                right_countries.append([capital,country,replycon])
                
            elif(hinted ==1):
                helped += 1
                hinted = 0
                hint_countries.append([capital,country,replycon])
            print('\n--------------------------')
            print ('Correct!')
            print ('--------------------------\n')
            main()
        elif (SequenceMatcher(None, replycon, answercon).ratio() >= .75):
            global close
            
            if(hinted==0):
                close_countries.append([capital,country,replycon])
                close = close + 1
            elif(hinted == 1):
                hinted = 0
                helped+=1
                hint_countries.append([capital,country,replycon])
            print ('\n---------------------------\n')
            print('Close enough! The answer is:', country)
            print ('\n---------------------------\n')
            main()
        
        else:
            print(chr(27) + "[2J")
            print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            print('Incorrect!')
            while True:
                if (guess == 1):
                    global wrong
                    wrong = wrong + 1
                    print ("\nThe correct answer is:", country)
                    print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                    time.sleep(1)
                    wrong_countries.append([capital,country,replycon])
                    main()
                
                print ('\nDo you want another chance?')
                ask = input('\nWould you like a hint? Press y and enter if yes.\nIf you would not like a hint press n and enter.\nIf you are ready to guess press g and enter.\n\n')
                ask = ask.lower() 
                
                #If user accidentally types answer before hitting "g"
                if (SequenceMatcher(None, ask, answercon).ratio() >= .75):
                    guess = 1
                    replycon = ask
                    try:
                        wrong_countries.pop()
                    except Exception:
                        pass
                    countries(guess,replycon,answercon)
                if (ask =='y'):
                    hinted = 1
                    hint()
                    if (hints/len(answercon) >= .2):
                        guess = 1
                        replycon = input ('\nYou were given enough hints. What is the answer? ')
                        replycon = replycon.lower()
                        countries(guess,replycon,answercon)
                    #hints = hints + 1
                
                elif (ask =='g'):
                    
                    replycon = input ('\nWhat is the answer? ')
                    replycon = replycon.lower()
                    guess = 1
                    countries(guess,replycon,answercon)
                     
                else:
                    break

            wrong = wrong + 1 
            print ("\nThe correct answer is:", country)
            print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            time.sleep(1)

            wrong_countries.append([capital,country,replycon])
            main()



    
    def capitals(guess,replycap,answercap):
        global hinted
        global helped
        if(replycap == answercap):
            if (hinted==0):
                global right
                right = right + 1
                right_capitals.append([country,capital,replycap])
            elif(hinted==1):
                helped+=1
                hint_capitals.append([country,capital,replycap])
                hinted = 0
            print('\n---------------------------')
            print ('Correct!')
            print ('---------------------------\n')
            main()
        
        elif (SequenceMatcher(None, replycap, answercap).ratio() >= .75):
            if(hinted!=1):
                global close
            
                close = close + 1
            else:
                hinted = 0
                helped+=1
            print ('\n---------------------------\n')
            print('Close enough! The answer is:', capital)
            print ('\n---------------------------\n')
            close_capitals.append([country,capital,replycap])
            main() 
        
        else:
            print(chr(27) + "[2J")
            print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            print('Incorrect!')  
            while True:
                if (guess == 1):
                    
                    global wrong
                    wrong = wrong + 1
                    print ("\nThe correct answer is:", capital)
                    print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                    time.sleep(1)
                    wrong_capitals.append([country,capital,replycap])
                    main()

                print ('\nDo you want another chance?')
                ask = input('\nWould you like a hint? Press y and enter if yes.\nIf you would not like a hint press n and enter.\nIf you are ready to guess press g and enter.\n\n')
                ask = ask.lower() 
                #If user accidentally types answer before hitting "g"
                if (SequenceMatcher(None, ask, answercap).ratio() >= .75):
                    guess = 1
                    replycap = ask
                    try:
                        wrong_capitals.pop()
                    except Exception:
                        pass
                    capitals(guess,replycap,answercap)
                    
                if (ask =='y'): 
                    hinted = 1
                    hint()
                    if (hints/len(answercap) >= .2):
                        guess = 1
                        replycap = input ('\nYou were given enough hints. What is the answer? ')
                        replycap = replycap.lower()
                        capitals(guess,replycap,answercap)
                         
                elif (ask == 'g'):
                    
                    replycap = input ('\nWhat is the answer? ')
                    guess = 1
                    replycap = replycap.lower()
                    capitals(guess,replycap,answercap)
                else:
                    break
            
            wrong = wrong + 1
            print ("\nThe correct answer is:", capital)
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            time.sleep(1)
            wrong_capitals.append([country,capital,replycap])
            main()

    if (chance <=5):
        countries(guess,replycon,answercon)
    else:
        capitals(guess,replycap,answercap)
      

#    if (randomp > 196):
 #       birthday = input ("\nWhose birthday is it today? ")
   #     birthdayboy = ['aba', 'Aba', 'Oren', 'oren']
    #    if (birthday in birthdayboy):
     #       print ("\nHappy 53rd birthday! 07/28/19\n")
      #      time.sleep(3)
       #     main()
       # else:
        #    print ("How do you not know who the birthday boy is?\nHint: He was born on July 28 1966")
         #   time.sleep(3)
          #  main()

main() 

#def remove_duplicates():
#    global wrong_countries
#    global close_countries
#    global right_countries
#    global wrong_capitals
#    global right_capitals
#    global close_capitals
#    res = []
#    for x,y,z in wrong_countries:
#        if(x,y not in res):
#            res.append([x,y,z])
#    wrong_countries = res
#    res = []
#    for x,y,z in wrong_capitals:
#        if(x,y not in res):
#            res.append([x,y,z])
#    wrong_capitals = res
#    res = []
#    for x,y,z in close_countries:
#        if(x,y not in res):
#            res.append([x,y,z])
#    close_countries = res
#    res = []
#    for x,y,z in close_capitals:
#        if(x,y not in res):
#            res.append([x,y,z])
#    close_capitals = res
#    res = []
#    for x,y,z in right_capitals:
#        if(x,y not in res):
#            res.append([x,y,z])
#    right_capitals = res
#    res = []
#    for x,y,z in right_countries:
#        if(x,y not in res):
#            res.append([x,y,z])
#    right_countries = res
#    print(wrong_countries)
