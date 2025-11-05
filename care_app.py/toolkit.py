import time
nickname ="angel"

print(f"\nhi {nickname}! welcome to your self-care toolkit. i'm here to support you in taking care of yourself.\n")
print("remember lovely, self-care is a journey and it's okay to take it one step at a time. be gentle with yourself!\n") 
print("-------------------------------\n")  
print("let's breathe together for a minute... nice and slow.\n")

for i in range(3): #3 breaths
    print("breathe in... ")
    time.sleep(3)
    print("breathe out...\n")
    time.sleep(3)

print("great job lovely! i'm so proud of you <3\n")
print("you're safe now bestie, and i'm here to help you take care of yourself.\n")

print("here are some self-care activities you can try today:\n")
print("1) take a short walk outside and enjoy nature\n")
print("2) listen to your favorite music and dance around\n")
print("3) write down three things you're grateful for\n")
print("4) treat yourself to a healthy snack or drink\n")        

activity = input("which activity would you like to try today lovely (choose 1, 2, 3, or 4)? ")  
print("\n") 

if activity == "1":
    print("that's a wonderful choice lovely! taking a walk outside can help clear your mind and boost your mood. enjoy the fresh air and the beauty of nature <3\n")
elif activity == "2":       
    print("yay lovely! dancing to your favorite music is a great way to lift your spirits and have fun. let loose and enjoy yourself <3\n")
elif activity == "3":
    print("such a beautiful choice lovely! practicing gratitude can help shift your focus to the positive aspects of your life. take your time and really think about what you're grateful for <3\n")
elif activity == "4":
    print("treating yourself to a healthy snack or drink is a great way to nourish your body and show yourself some love. enjoy every bite and sip lovely <3\n")
else:
    print("that's okay lovely, sometimes it's hard to choose. remember, self-care is about doing what feels right for you in the moment. be kind to yourself <3\n")
print("i'm so proud of you for taking this time for yourself today lovely. remember, self-care is a journey and every step you take is a step towards nurturing yourself <3\n") 

from affirmation import affirmations #importing affirmations list
import random
affirmation = random.choice(affirmations)  #randomly choose an affirmation 

print("here's a gentle affirmation for you lovely:\n")
print(f"✨ {affirmation} ✨\n") 
print("keep this affirmation close to your heart throughout the day, and remember that you are worthy of love and care just as you are <3\n")   

message = "see you next time lovely <3"
for char in message:
    print(char, end='', flush=True) 
    time.sleep(0.3)
print("\n")

import time
import sys
def blossom_drift():
    petals = ["🌸", "🍃", "🌿", "🌸", "🍃"]
    for petals in petals: #drift effect
        sys.stdout.write(petals) #print without newline
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

print("\nsoftly, the cherry blossoms begin to drift down around you...\n")
blossom_drift()

print("────────────────────────────────────────\n")
#back to homescreen
