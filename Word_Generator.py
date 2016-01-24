def main():
    import random
    import time
    import turtle
#
#Todo:Change instructions on line 41

    #=======================================================================================================================
    #Opens file and reads lines into list
    with open("English_words.txt") as f:
        lines=f.read().splitlines()

    x = [[i] for i in (lines)]
    print ("\n\nWelcome to I-CHYPHER,this is an early alpha version. \nThanks for using and have fun.")
    #=======================================================================================================================
    #INSTRUCTIONS:

    instruction=input("Would you like to read the instructions?\nType: Yes/No\n")

    if instruction.lower()=="yes":
        print("\n\n\nThis is a tool for you to practice quick thinking and witty creativity.\nYou will be prompted with a series of words."
              "Get a beat ready or freestyle acapella.\nThe words will continue based on how much time you would like.\n"
              "You should follow the prompts in this screen and when instructed click on the new window that will open."
              "\nThis new window will show you your words. \nHave fun!\n\n")
        time.sleep(8)
    if instruction.lower()=="no":
        print("Okay, follow the prompts. Have fun!")
        time.sleep(2)




    #=======================================================================================================================
    #TIMED RHYME
    #Propmted if you would like to rhyme for a timed amount.
    timed=input("Would you like to rhyme on a timer?\n\n")
    def timed_rhyme(x,timed):
        if timed.lower()=="yes":            #Timed case
            timed=input("How long would you like to go?\nFor example if you want 2 minutes and 30 seconds type:\t2:30\t\n\n")
            minutes,seconds=timed.split(":")
            print ("You have",minutes,"minute and",seconds," seconds on the clock.")
            time.sleep(1)
            delay=input("How many seconds would you like in between each word?\n\n")


            #=======================================================================================================================
            #Turtle Implementation

            rapper=turtle.Turtle()
            wn=turtle.Screen()
            wn.bgcolor("black")
            rapper.color("white")
            rapper.setpos(0,0)
            rapper.shape("blank")
            #=======================================================================================================================

            ready=input("Start your beat and open the new window created. The first word will appear when you press enter.\n\n")
            sec=(int(minutes)*60)+(int(seconds))
            t0=time.time()

            while ready=='' and sec!=0:
                random_word= random.choice(x)
                print ('\n\n\n\n\n',random_word[0])
                #Time for the word to appear.
                rapper.write(random_word[0],False,"center", ("Arial",40,"bold"))
                time.sleep(int(delay))
                print ('\n\n\n')
                rapper.write(random_word[0])
                t1=time.time()
                total_time=int(t1-t0)
                if total_time==int(sec) or total_time>int(sec):
                    time.sleep(int(delay))
                    wn.bye()
                    print ("Good cypher!")
                    return 0
                # elif total_time==10 or total_time<10:
                #     print "10 seconds left"
                rapper.clear()
                #wn.exitonclick()
        elif timed.lower()=="no":
            return 1
        elif timed.lower()!="yes" or timed.lower()!="no":
            return 2
    #======================================================================================================================

    #======================================================================================================================
    #NON TIMED RHYME
    cypher=timed_rhyme(x,timed)
    if cypher==1:           #No time case
        print ("Okay, the words won't stop coming. Have fun!\n\n")

        delay=input("How many seconds would you like in between each word?\n\n")


    #=======================================================================================================================
        #Turtle Implementation

        rapper=turtle.Turtle()
        wn=turtle.Screen()
        wn.bgcolor("black")
        rapper.color("white")
        rapper.setpos(0,0)
        rapper.shape("blank")


    #=======================================================================================================================

        ready=input("Start your beat. The first word will appear when you press enter.")

        while ready=='':
            #Picks a random word

            random_word= random.choice(x)
            print (random_word[0])
            rapper.write(random_word[0],False,"center", ("Arial",40,"bold"))
            time.sleep(int(delay))
            rapper.clear()

    #======================================================================================================================
    #Exception Handler
    if cypher==2:           #If user choses niether yes or no then prompt program to restart.
        print('press shift+F10')
        timed_rhyme(x,timed)
    #======================================================================================================================
main()