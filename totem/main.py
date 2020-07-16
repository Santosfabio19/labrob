from threading import Thread
from kivy.app import App
from kivy.config import Config
from interface import *
from paciente import *

#Código que irá rodar em loop em segundo plano
def runA():
    while(True):
        paciente.getDados()
t1 = Thread(target = runA)
t1.setDaemon(True)
t1.start()

class Totem(App):
    def build(self):
        return Interface()

Config.set('graphics', 'fullscreen', 'auto')
Totem().run()