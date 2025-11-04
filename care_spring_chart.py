import matplotlib.pyplot as plt 
import datetime

date = []
moods = []
energies = []

with open("care_journal_log.txt", "r") as log: 
    for line in log:
        parts = line.strip().split(", ")
        entry_date = parts[0]
        mood = int(parts[2].split(": ")[1])
        energy = int(parts[3].split(": ")[1])
        
        date.append(entry_date)
        moods.append(mood)
        energies.append(energy)

plt.figure()

#pink blossome vibes
plt.plot(date, moods, linewidth=2.5, label="Mood", marker='o', linestyle="-", color="#FFB7C5")
plt.plot(date, energies, linewidth=2.5, label="Energy", marker='o', linestyle="-", color="#FFCFE2")        

#spring aesthetics
plt.xlabel("your day", fontsize=12)
plt.ylabel("wellness levels (1-10)", fontsize=12)
plt.title(" your mood and wellness bloom chart ", fontsize=14)

plt.legend()
plt.grid(alpha=0.2)
plt.show()  
