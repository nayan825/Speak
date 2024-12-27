
import pyttsx3

text=input("Enter the text to be spoken: ")

speak=pyttsx3.init()
speak.say(text)
speak.runAndWait()


