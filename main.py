name=input("Enter your name")
time=input("What time do you wake up?")
clothes=input("How long do you take to wear your clothes?")
arrival=input("What time do you reach at school?")
lunch=input("What time do you take your lunch?")
home=input("What time do you go back home?")
extra=input("What do you do for leisure?")
homework=input("How long do you do your homework?")
if clothes<=15 and time<=5:
    print("You can go take breakfast now")
    print("Brush your teeth after breakfast")
else:
    print("You can wake up earlier if your slow")
if arrival<=7:
    print("Get to class and start your day")
else:
    print("Your late you can do better ext time")
if not lunch==12:
    print("It is not lunch stop eating your food")
else:
    print("Enjoy your lunch")
if home>=4 or homework>=1:
    print("Do your homework before playing")
