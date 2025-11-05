import os,datetime 
import utils
import affirmation
import time
import sys
import random
from utils import append_journal_entry, blossom_drift

def typeprint(text, speed=0.07): #slow print function
        for char in text:
            print(char, end='', flush=True) #print without newline
            time.sleep(speed) #delay between chars
        print()

def blossom_drift_vertical(): #vertical drift effect
    petals = ["🌸", "  🌸", "    🌸", "      🌸"]
    height = 8
    for _ in range(8):  # only does a small gentle drift
        petal = random.choice(petals)  #randomly choose a petal position
        for i in range(height): #print petal at increasing heights
            print("\n" * i + petal) #print petal with newlines
            time.sleep(0.25)
        print()  #space between drifts

def append_journal_entry(nickname, entry):
    os.makedirs("journals", exist_ok=True) #create a folder if it doesn't exist
    filename = f"journals/{nickname} journal_entries.txt" #file path

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #current time
    with open(filename, "a") as file: #open file in append mode
        file.write(f"{timestamp}\n{entry}\n\n") #write timestamp and entry

def run (nickname ="angel"):
    typeprint(f"\nhi {nickname}! welcome to your care journal. let's take a moment to reflect on your day and jot down some thoughts.\n")
    typeprint("there's no rush lovely, just let your thoughts flow naturally and be kind to yourself.\n")
    typeprint("let's just take a moment and *breathe deeply* together...\n")

    entry = input("whenerver you're ready lovely, what's on your heart today?\n\n")

    entry_line = []
    typeprint("\nyou can continue writing your journal entry. when you're done, just press enter on an empty line to finish:\n")

#allows multi-line input until an empty line is entered
    while True: #looping for multiple lines until tells to stop
        try: 
              line = input() #type a line
        except KeyboardInterrupt: #cntl+c to exit
             print("\ninterrupted. saving your journal entry...\n")
             return
        if line.strip() == "": #check if user pressed enter on empty line
            break
        entry_line += line + "\n" #adding line to entry with newline

    entry = "\n".join(entry_line).strip()
    if entry:
        append_journal_entry(nickname, entry)
        print(f"\nthank you so much for sharing with me {nickname}, i'm so proud of you for taking this time for yourself!\n")
        print("no matter what lovely, you're processing your emotions. you're growing, you're nurturing yourself, you're giving yourself your absolute best!\n")
        print("i'm so so proud of you, soft and truly, my angel <3\n")
    else: #if no entry
        print("\nno worries lovely, journaling is a personal journey and it's okay to take your time. i'm here whenever you're ready <3\n") 
        print("-----------------------------\n")

    blossom_drift_vertical()

    #save entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_journal_entry(nickname, entry)
    print("your journal entry has been saved successfully!\n")
    print("-----------------------------\n")
    
    #gentle reflection    
    typeprint(f"here's a little note for you {nickname}:\n")
    typeprint("remember, journaling is a powerful tool for self-discovery and healing. by taking the time to reflect on your thoughts and feelings, you're nurturing your inner self and fostering personal growth.\n")
    typeprint("be proud of yourself for showing up and being honest with your emotions. you're doing amazing lovely <3\n")
    print("-----------------------------\n")

    message = "see you next time lovely <3"
    for char in message:
        print(char, end='', flush=True) #print without newline
        import time
        time.sleep(0.3)
    print("\n")
    print("────────────────────────────────────────\n")

# optional direct test
if __name__ == "__main__":
    run()