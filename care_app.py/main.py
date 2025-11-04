print("˗ˏˋ 💗 𝒞𝒶𝓇𝑒 𝒞𝑜𝓃𝓈𝑜𝓁𝑒 💗 ˎˊ˗\n")
      
nickname ="angel"

#homescreen
print(f"hi {nickname}! i'm glad you're here. let's build something great together!\n")
print("what would you like to work on today?\n")

print("1)my mood check-in <3")
print("2)my care journal")
print("3)my self-care toolkit") 

choice = input("\nchoose 1, 2, or 3: ")

if choice == "1":
    import check_in
elif choice == "2":
    import journal
elif choice == "3":
    import toolkit
else:
    print("\nthat's ok, we can try agin later! get some reast lovely :)")
