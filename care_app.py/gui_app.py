#gui_app.py - GUI journal application
import os #file operations
import datetime
import tkinter as tk #tkinter for GUI
from tkinter import scrolledtext, messagebox #for text area and message boxes
import utils #utility functions
import threading #for autosave thread
import time #for delays
import random #for random choices
from utils import append_journal_entry, blossom_drift
from pathlib import Path

#theme colors
BG = "#F3F8F2"        # soft matcha cream
ACCENT = "#A3C9A8"    # matcha green
CROQUETTE = "#F6E6D6" # warm croquette beige
PINK = "#FFC7D1"      # soft pastry pink
TEXT = "#2E4A3A"      # deep green text

DATA_DIR = Path("journals")
DATA_DIR.mkdir(exist_ok=True)

#----------------UTILIITY-------------------

#autosave journal entry function for GUI
def save_draft(nickname, content):
    draft_path = DATA_DIR / f"{nickname}_draft.txt"
    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(content)

#autosave loop function
def append_journal_entry(nickname, content):
    if not content.strip():
        return  # avoid saving empty entries
    date_str = datetime.datetime.now().strftime("%Y-%m%d_%H%M%S")
    journal_path = DATA_DIR / f"{nickname}_journal.txt"
    with open(journal_path, "a", encoding="utf-8") as f:
        f.write(f"\n\nEntry on {date_str}:\n{content}\n")   

#affirmation message function
def affirmation_message(nickname):
    affirmations = [
        "you are worthy of love and care, just as you are.",
        "every step you take towards self-care is a victory.",
        "be gentle with yourself; you're doing the best you can.",
        "your feelings are valid, and it's okay to take time for yourself.",
        "you deserve kindness and compassion, especially from yourself."
    ]
    affirmation = random.choice(affirmations) #randomly choose an affirmation
    messagebox.showinfo("Affirmation", f"{affirmation}\n\n- from your care journal, {nickname}") #show affirmation message box

#-------------ANIMATION-------------------

#blossom drift effect for GUI
def blossom_thread(canvas, stop_event):
    petals = ["🌸", "💮", "🌺"]
    width = int(canvas['width'])
    height = int(canvas['height'])
    items = []

    while not stop_event.is_set():
        if random.random() < 0.2:  # create petals randomly
            x = random.randint(0, width - 20)
            y = 0
            petal = random.choice(petals)
            item = canvas.create_text(x, y, text=petal, font=("Arial", 20))
            items.append(item)

        for item in items[:]:
            canvas.move(item, 0, 5)
            coords = canvas.coords(item)
            if coords[1] > height:
                canvas.delete(item)
                items.remove(item)

        canvas.update()
        time.sleep(0.05)

    typeprint = lambda text, speed=0.05: [canvas.create_text(200, 20 + i*20, text=char, font=("Arial", 12)) or time.sleep(speed) for i, char in enumerate(text.split('\n'))] #slow print function for GUI
#------------------AUTOSAVE---------------------------

#autosave loop function
def autosave_loop(nickname, text_widget, stop_event):
    last_content = ""
    while not stop_event.is_set():
        try:
            content = text_widget.get("1.0", tk.END)
        except tk.TclError:
            break  # Exit if the text widget is destroyed
        if content != last_content:
            save_draft(nickname, content)
            last_content = content
        time.sleep(3)  #autosave every 3 seconds

#----------------------GUI---------------------------------

#main GUI function
def run_gui(nickname="lovely"):
    root = tk.Tk() #main window
    root.title(f"{nickname} Care Journal 🌸")
    root.geometry("580x760")
    root.configure(bg=BG) #background color
    root.resizable(False, False) #fixed window size 

    canvas = tk.Canvas(root, width=500, height=150, bg="#FFF7F8", highlightthickness=0)
    canvas.pack()

    #top frame
    header_frame = tk.Frame(root, bg=BG) #header frame
    header_frame.pack(fill="x", pady=12) #pack header frame
    tk.Label(header_frame, text=f"{nickname}'s Care Journal 🌸", font=("Helvetica", 24, "bold"), bg=BG, fg=TEXT).pack()
    tk.Label(header_frame, text="A safe space to reflect and nurture yourself.", font=("Helveticaa", 14), bg=BG, fg=TEXT).pack()

    #mood selector
    mood_var = tk.StringVar(value="😊")
    moods = ["😊 Happy", "😢 Sad", "😡 Angry", "😌 Calm", "😰 Anxious"]
    tk.Label(root, text="how are you feeling today lovely:", bg=BG, font=("Helvetica",12)).pack()
    mood_menu = tk.OptionMenu(root, mood_var, *moods)
    mood_menu.pack(pady=5)

    #canvas for blossom drift
    CANVAS_WIDTH = 580
    CANVAS_HEIGHT = 420
    canvas_frame = tk.Frame(root, bg=BG)
    canvas_frame.pack(pady=10)
    canvas.pack()

    # journal entry text area
    entry_text = scrolledtext.ScrolledText(root, 
        wrap=tk.WORD, 
        width=60, 
        height=20, 
        font=("Helvetica", 12), 
        bg=CROQUETTE, 
        fg=TEXT
    )
    entry_text.pack(pady=15)

    def save_entry():
        text = entry_text.get("1.0", "end-1c")
        
        # Save to file / or wherever your code saves currently
        with open("journal.txt", "a") as file:
            file.write(text + "\n\n")

        # CUTE MESSAGE POP UP 💞
        messagebox.showinfo("Saved ✨", "Your entry has been saved, love! 💗🌿🌸")

        # Clear the entry after saving (optional cutie reset moment)
        entry_text.delete("1.0", "end")

    def clear_entry():
        entry_text.delete("1.0", tk.END)
        messagebox.showinfo("Cleared 🌸", "All done! Your journal space is fresh and ready 💗")

    control_frame = tk.Frame(root, bg=BG) #control frame
    control_frame.pack(pady=10)
    save_btn = tk.Button(control_frame, text="Save Entry 💾", command=save_entry, bg=ACCENT, fg=TEXT, font=("Helvetica", 12, "bold")) #save button
    save_btn.pack(side=tk.LEFT, padx=10)
    affirm_btn = tk.Button(control_frame, text="Get Affirmation 🌸", command=lambda 
: affirmation_message(nickname), bg=PINK, fg=TEXT, font=("Helvetica", 12, "bold")) #affirmation button
    affirm_btn.pack(side=tk.LEFT, padx=10)  
    clear_btn = tk.Button(control_frame, text="Clear Entry 🧹", command=clear_entry, bg=PINK, fg=TEXT, font=("Helvetica", 12, "bold")) #clear button
    clear_btn.pack(side=tk.LEFT, padx=10)

    #footer
    footer_frame = tk.Frame(root, bg=BG) #footer frame
    footer_frame.pack(pady=(6,12))
    tk.Label(footer_frame, text="Remember to take care of yourself 💖", font=("Helvetica",14), bg=BG, fg=TEXT).pack()


# Threads
    stop_event = threading.Event()
    threading.Thread(target=blossom_thread, args=(canvas, stop_event), daemon=True).start()
    threading.Thread(target=autosave_loop, args=(nickname, entry_text, stop_event), daemon=True).start()

    # Load draft
    draft_path = DATA_DIR / f"{nickname}_draft.txt"
    if draft_path.exists():
        with draft_path.open("r", encoding="utf-8") as f:
            entry_text.insert("1.0", f.read())

    # Close handler
    def on_closing():
        try:
            save_draft(nickname, entry_text.get("1.0", tk.END))
        except tk.TclError:
            pass
        stop_event.set()
        time.sleep(0.15)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
# ---------------- run
if __name__ == "__main__":
    run_gui()