def main():
    import random
    import time
    #=======================================================================================================================
    #Opens file and reads lines into list
    with open("English_words.txt") as f:
        lines=f.read().splitlines()

    x = [[i] for i in (lines)]
    print "\n\nWelcome to I-CHYPHER,this is an early alpha version. \nThanks for using and have fun."
    #=======================================================================================================================

    #=======================================================================================================================
    #TIMED RHYME
    #Propmted if you would like to rhyme for a timed amount.
    timed=raw_input("Would you like to rhyme on a timer?")
    def timed_rhyme(x,timed):
        if timed.lower()=="yes":
            timed=raw_input("How long would you like to go?\nType in your time like this:   minutes:seconds\t")
            #Todo: Change the wording for this prompt. Needs to be more clear about syntax for input.
            minutes,seconds=timed.split(":")
            print "You have",minutes,"minute and",seconds," seconds on the clock."
            time.sleep(1)
            delay=raw_input("How many seconds would you like in between each word?")
            ready=raw_input("Start your beat. The first word will appear when you press enter.")
            sec=(int(minutes)*60)+(int(seconds))
            t0=time.time()
            while ready=='' and sec!=0:
                random_word= random.choice(x)
                print '\n\n\n\n\n'*5,random_word[0]
                #Time for the word to appear.
                time.sleep(int(delay))
                print '\n\n\n'

                t1=time.time()
                total_time=int(t1-t0)
                if total_time==int(sec) or total_time>int(sec):
                    print "Good cypher!"
                    return 0
                # elif total_time==10 or total_time<10:
                #     print "10 seconds left"
        elif timed.lower()=="no":
            return 1
        elif timed.lower()!="yes" or timed.lower()!="no":
            return 2
    #======================================================================================================================

    #======================================================================================================================
    #NON TIMED RHYME
    cypher=timed_rhyme(x,timed)
    if cypher==1:
        print "Okay, the words won't stop coming. Have fun!\n\n"

        ready=raw_input("Start your beat. The first word will appear when you press enter.")
        while ready=='':
            #Picks a random word
            random_word= random.choice(x)
            print random_word[0]
    if cypher==2:
        print'press shift+F10'
        timed_rhyme(x,timed)
#======================================================================================================================
main()