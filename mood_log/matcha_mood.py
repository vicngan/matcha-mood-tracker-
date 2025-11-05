name = input("hi lovelies, what's your name?\n> ")
print(f"\nhi {name}, welcome back to your matcha mood tracker!\n")
print("────────────────────────────────────")

import datetime
#starting a matcha mood tracker 
today = datetime.date.today()
print(f"Welcome to your Matcha Mood Tracker for {today}!")  

sleep = int(input("On a scale of 1-10, how well did you sleep last night? "))
energy = int(input("On a scale of 1-10, how is your energy level? "))
stress = int(input("On a scale of 1-10, how stressed do you feel? "))
mood = int(input("On a scale of 1-10, how is your overall   mood? "))       

average = (sleep + energy + (10 - stress) + mood) / 4

print(f"Your matcha mood score for today is: {average:.2f}/10")
with open("wellness_log.txt", "a") as log: 
    log.write(f"{today}, sleep: {sleep}, energy: {energy}, stress: {stress}, mood: {mood}, avergage:{round(average,1)}\n")


if average >= 8:
    print("you're doing well lovely, keep glowing!!")
    print("i am super proud of you <3")
elif average >= 5:
    print("you're doing okay, take some time for yourself today.")
    print("soft steps are still progress <3")
else:
    print("it's okay to have tough days, grab a matcha and remember to be kind to yourself.") 
    print("you are loved <3")

#end of matcha mood tracker 
#have a lovely day lovelies!