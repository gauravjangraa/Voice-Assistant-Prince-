import os 
import webbrowser
import eel
from engine.features import *
from engine.command import *



def start():

    eel.init("frontend")
    playAssistantSound()

    webbrowser.open('http://localhost:8000/model.html')

    eel.start('model.html' ,  mode=None , host='localhost' , block=True)