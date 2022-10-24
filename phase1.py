from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import multiprocessing
import tkinter as tk
import sys
import os
import pandas as pd
import time
import datetime
from kivy.metrics import dp

from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
import block

import subprocess

from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, TwoLineListItem, ImageLeftWidget

import block2
import suniteesh

Window.size = (300, 600)
# Builder String
helper_string = '''
ScreenManager:
    Main:
    Hello:
    Helloooo:
    analytics:


<Main>:
    name:'login'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "C:/Users/asgav/Downloads/WhatsApp Image 2022-08-25 at 11.44.52 PM.jpeg"
    MDLabel:
        text: "                       ATTENDANCE        "
        pos_hint:{'center_x':0.5,'center_y':0.8}
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
    MDTextField:
        id:username
        hint_text:"Enter Username"
        line_color_focus:0,0,0.5,1
        helper_text:"Required"
        helper_text_mode:"on_error"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        requires:True
        size_hint:(0.4,0.1)
    MDTextField:
        id:password
        hint_text:"Enter Password"
        line_color_focus:0,0,0.5,1
        helper_text:"Required"
        helper_text_mode:"on_error"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        requires:True
        size_hint:(0.4,0.1)
        password:True
    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_release:root.manager.current='hello'



<Hello>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'

        MDBottomNavigation:
            panel_color: .1,.5,.5,1
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Students'
                icon: 'account-group'
                ScrollView:
                    MDList:
                        TwoLineAvatarListItem:
                            text: "VENKATA SESHA SAI"
                            secondary_text: "IT"
                            on_release: print("venkat")


                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/venkat.jpeg"
                        TwoLineAvatarListItem:
                            text: "KALAM"
                            secondary_text: "ECE"
                            on_release: print("kalam")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/kalam.jpeg"
                        TwoLineAvatarListItem:
                            text: "SRIKANTH"
                            secondary_text: "IT"
                            on_release: print("srikanth")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/srikanth.jpeg"

                        TwoLineAvatarListItem:
                            text: "Anand"
                            secondary_text: "IT"
                            on_release: print("anand")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/anand.jpg"

                        TwoLineAvatarListItem:
                            text: "SARAN"
                            secondary_text: "IT"
                            on_release: print("saranee")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/saran.jpeg"

                        TwoLineAvatarListItem:
                            text: "Hariram"
                            secondary_text: "IT"
                            on_release: print("hariram")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/hariram.jpg"

                        TwoLineAvatarListItem:
                            text: "ragavi"
                            secondary_text: "IT"
                            on_release: print("ragavi")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/ragavi.jpg"
                        TwoLineAvatarListItem:
                            text: "Kavya"
                            secondary_text: "IT"
                            on_release: print("kavya")

                            ImageLeftWidget:
                                source:"C:/Users/asgav/Downloads/face/face/image/kavya.jpg"







                MDFloatingActionButton:
                    icon: "camera"
                    md_bg_color: app.theme_cls.primary_color
                    on_release:app.launchChild()
                    






            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Students Absent'
                icon: 'account-multiple-remove'
                ScrollView:
                    MDList:
                        id:ls
            MDFlatButton:
                text: "             MDRAISEDBUTTON                                                        "
                md_bg_color: .1, .5, .5, 1
                on_release:root.manager.current='analytics'
                        

<Helloooo>:
    name: 'helloooo'
                
<analytics>:
    name:'analytics'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "C:/Users/asgav/Downloads/WhatsApp Image 2022-08-25 at 11.44.52 PM.jpeg"

    MDTextButton:
        text: "           consolidated attendance"
        custom_color: 0, 1, 0, 1
        on_release:app.launchChild3()
        pos_hint: {"center_x": .5, "center_y": .5}
    MDTextButton:
        text: "        gender ratio"
        custom_color: 0, 1, 0, 1
        on_release:app.launchChild4()
        pos_hint: {"center_x": .5, "center_y": .6}
    MDTextButton:
        text: "           daywise attendance"
    
        custom_color: 0, 1, 0, 1
        on_release:app.launchChild5()
        pos_hint: {"center_x": .5, "center_y": .7}
                



'''


class Main(Screen):
    pass


class Hello(Screen):
    pass


class Profile(Screen):
    pass

class Helloooo(Screen):
    pass
class analytics(Screen):
    pass


sm = ScreenManager()

sm.add_widget(Main(name='login'))
sm.add_widget(Hello(name='hello'))
sm.add_widget(Profile(name='profile'))
sm.add_widget(Profile(name='helloooo'))
sm.add_widget(Profile(name='analytics'))


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        df1 = pd.read_excel(
            os.path.join("C:/Users/asgav/PycharmProjects/pythonProject", "file2.xlsx"),
            engine='openpyxl',
        )
        b = df1.values.tolist()
        print(b)
        for i in range(0, len(b)):
            item = OneLineIconListItem(text=b[i][1])
            print((b[i][1]).lower())
            image = ImageLeftWidget(source=f'C:/Users/asgav/Downloads/face/face/image/{(b[i][1]).lower()}.jpeg')
            item.add_widget(image)

            self.help_str.get_screen('hello').ids.ls.add_widget(item)

        return screen

    def launchChild(self):
        z = subprocess.call(['ipython', 'facefile.py'], stdout=True)
    def launchChild2(self):

        subprocess.call(['ipython', 'chelistexe.py'], stdout=True)

    def launchChild3(self):
        z = subprocess.call(['ipython', 'block.py'], stdout=True)
    def launchChild4(self):
        suniteesh.sunitee()
    def launchChild5(self):
        block2.naveeneli()
    def logincheck(self):
        user = self.help_str.get_screen('login').ids.username.text
        password = self.help_str.get_screen('login').ids.password.text


if _name_ == '_main_':
    DemoApp().run()
