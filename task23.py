import pyttsx3

engine = pyttsx3.init()
names = ["Abrar", "Yasir", "Ali", "Arslan", "Umair"]
for name in names:
    engine.say(f"Enter {name} ")
    engine.runAndWait()