import tkinter as tk
Win = tk.Tk()
Win.geometry("1920x1080")
CPower = 1
Clicks = 0
def SecretUpgrade():
    global SecrettUpgrade
    global Clicks
    global CPower
    global Text
    if Clicks > 1000000:
        CPower += 10000
        Clicks -= 1000000
    else:
        Clicks += 0
        CPower += 0
    Text.configure(text=f"You have {Clicks} clicks")
    ClickPower.configure(text=f"Your Click Power is: {CPower}")
SecrettUpgrade = tk.Button(Win, font=("Comic Sans MS", 5), text="+10000 click power|cost 1000000",command=SecretUpgrade)
def ClickAdder():
    global SecrettUpgrade
    global Clicks
    global CPower
    global Text
    Clicks += CPower
    Text.configure(text=Clicks)
    if Clicks > 1000000:
         SecrettUpgrade.place(relx=0.9, rely=0.9)
def Upgradee():
    global Clicks
    global CPower
    global Text
    if Clicks > 250:
        Clicks -= 250
        CPower += 1
    else:
        Clicks += 0
        CPower += 0
    Text.configure(text=f"You have {Clicks} clicks")
    ClickPower.configure(text=f"Your Click Power is: {CPower}")
def Upgradeee():
    global Clicks
    global CPower
    global Text
    if Clicks > 2500:
        CPower += 10
        Clicks -= 2500
    else:
        Clicks += 0
        CPower += 0
    Text.configure(text=f"You have {Clicks} clicks")
    ClickPower.configure(text=f"Your Click Power is: {CPower}")
def Upgradeeee():
    global Clicks
    global CPower
    global Text
    if Clicks > 25000:
        CPower += 100
        Clicks -= 25000
    else:
        Clicks += 0
        CPower += 0
    Text.configure(text=f"You have {Clicks} clicks")
    ClickPower.configure(text=f"Your Click Power is: {CPower}")

button = tk.Button(Win, bg="#1e0040", font=("Comic Sans MS",100),text="Click me",command=ClickAdder)
button.place(relx=0.69,rely=0.35)
Upgrade = tk.Button(Win, bg="#00e1ff", font=("Comic Sans MS",50), text="+1 Click Power|Cost:250",command=Upgradee)
BetterUpgrade = tk.Button(Win, bg="#00ff44", font=("Comic Sans MS",50), text="+10 Click Power|Cost:2500",command=Upgradeee)
MegaUpgrade = tk.Button(Win, bg="#4166F5", font=("Comic Sans MS", 50), text="+100 CLICK POWER|COST 25000", command=Upgradeeee)
MegaUpgrade.place(relx=0.06, rely=0.35)
Upgrade.place(relx=0.06, rely=0.7)
BetterUpgrade.place(relx=0.06, rely=0.53)
Text = tk.Label(Win, font=("Comic Sans MS",50), text=f"You have {Clicks} clicks")
Text.place(relx=0.34, rely=0.13)
ClickPower = tk.Label(Win, font=("Comic Sans MS", 50), text=f"Your Click Power is: {CPower}")
ClickPower.place(relx=0.34, rely=0.05)
Win.mainloop()
