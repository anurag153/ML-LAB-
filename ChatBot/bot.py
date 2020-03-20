import tkinter as tk
from PIL import ImageTk, Image
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"how are you ?|how are u ?",
        ["I'm doing good \n How about You ?", ]
    ],
    [
        r"i'm (.*) doing (.*)|i am (.*)",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"what is your name ?|what's your name ?",
        ["My name is Neel and I'm a ChatBot, What's yours ?", ]
    ],
    [
        r"(my name is|it's) (.*)",
        ["Hello %2, that's a real good name", ]
    ],
    [
        r"thank you (.*)|thanks",
        ["Welcome" ]
    ],
    [
        r"How old are you?|(.*) age",
        ["I'm a ChatBot! \n Well.. I was created in 2020", ]
    ],
    [
        r"sorry (.*)|sorry",
        ["No worries", "You don't have to say that", ]
    ],
    [
        r"(.*) created ?",
        ["I was created in 2020 by Anurag Mehta ", ]
    ],
    [
        r"how was your day (.*)?",
        ["Tiring", "I remain online 24*7, so you know..", "It was good. How about you?",]
    ],
    [
        r"(.*) good day",
        ["Oh! That's nice to hear ", ]
    ],
    [
        r"quit|good bye|bbye|okay. it was nice talking to you. bye|exit",
        ["See you soon", "Catch you later!","Talk soon"]
    ],
    
]
