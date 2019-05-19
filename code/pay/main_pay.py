#-*- coding: utf-8 -*-
# from mysyst import reserve_spot
import mysql.connector
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Window.size = (615, 410)


class HomeScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

sm = Builder.load_file("help_pay.kv")

class MainApp(App):

    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()
