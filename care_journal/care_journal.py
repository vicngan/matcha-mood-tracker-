import datetime

print("""
────────────────────────────────────────
      🍵  your care dream journal  ☁️
    soft day for a gentle little heart
────────────────────────────────────────
""")

name = input("your name, lovely:\n> ")

print(f"welcome back {name}! let's get this day started.\n")

today = datetime.date.today()
print(f"\nhi lovely, today is {today}. let's reflect on your day.\n")
print("────────────────────────────────────")           

mood = input("how are you feeling today (1-10)?\n> ")
energy = input("how is your energy level (1-10)?\n> ")
gratitude = input("what is one thing you are grateful for today?\n> ")
self_care = input("what is one self-care activity you did today?\n> ")
water = input("how many glasses of water did you drink today?\n> ")

#dream affirmation section
print("\n taking a moment to affirm your dreams... \n ")

mood = int(mood)
energy = int(energy)    
if mood >= 8 and energy >= 8:
    print("✨ you are radiating positive energy! keep shining bright! ✨\n")        
elif mood >= 5 and energy >= 5:
    print("🌸 you are doing well, keep nurturing your dreams! 🌸\n")
else:
    print("🌙 it's okay to have off days, rest and recharge for your dreams. 🌙\n")

with open("care_journal_log.txt", "a") as log: 
    log.write(f"{today}, name: {name}, mood: {mood}, energy: {energy}, gratitude: {gratitude}, self-care: {self_care}, water: {water}\n")

print("your entry is save with love <3 ")
print("────────────────────────────────────────")
print(f"\nthank you for journaling today, {name}. remember to take care of yourself!\n")
print("\n💗 softly reminding you:\n")
print("you don't have to bloom every day to still be growing 🍃")
print("healing is not linear, and you're allowed to have soft days 🌸")
print("your worth is not measured by productivity, but by your heart 🫶")
print("thank you for showing up for yourself today, even gently.\n")
print("────────────────────────────────────────")

import time
import sys

def blossom_drift():
    message = "🌸 your care journal entry is blossoming into the log... 🌸"
    petals = ["🌸", "🍃", "🌿", "🌸", "🍃"]
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for petals in petals:
        sys.stdout.write(petals)
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

print("\nsoft blossom drift around you...\n")
blossom_drift()
print("your care journal entry has been lovingly recorded. 🌷\n")

