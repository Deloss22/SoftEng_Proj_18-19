#-*- coding: utf-8 -*-
from mysys import *
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

Window.size = (540, 960)


class HomeScreen(Screen):
    def capplate(self, plate):
        gplate = plate
        global gplate
        # print plate

    def capname(self, name):
        gname = name
        global gname
        # print name

class MenuScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class reserv(Popup):
    def printcre(self, restype):
        reserve_spot(gplate, gname, restype)
        print gplate, gname

class cont(Popup): #add telephone to parking
    def palist(self):
        test = request("parking_list", '')
        i = 1
        kati = ''
        for x in test:
            kati += 'Katastima ' + str(i) + ': '
            kati += x[0]
            kati += '\n \n'
            i += 1
        return kati
    # pass
class loginp(Popup):
    # global uname
    # uname = "Babis"
    def chlog(self, nm, pss):
        global uname
        uname = nm
        ret = check_login(nm, pss, "USER")
        if ret:
            print "Login Successful"
        else:
            print "Login Failed"

class hist(Popup):
    # my = loginp()
    def showhi(self):
        test = request("history", uname)
        i = 1
        kati = ''
        for x in test:
            kati += 'Kratisi ' + str(i) + ': '
            kati += ' ' + str(x[0]) + ','
            kati += ' ' + str(x[1]) + ','
            kati += ' ' + str(x[2]) + ','
            kati += ' ' + str(x[3])
            kati += '\n \n'
            i += 1
        return kati

    def cancel(self):
        check_and_cancel(uname)
        print "Done"

sm = Builder.load_file("help_app.kv")

class MainApp(App):

    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()
