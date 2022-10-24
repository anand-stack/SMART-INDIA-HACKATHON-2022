from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import smtplib
import pandas as pd
import os
import suniteesh

# Builder String
helper_string = '''
ScreenManager:
    Hello:
    Bye:
<Hello>:
    name: 'hello'
   
<Bye>:
    name: 'bye'
    MDLabel:
        id : tex
        text: "Username"
'''


class Hello(Screen):
    pass


class Bye(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Hello(name='hello'))
sm.add_widget(Bye(name='bye'))





class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        df1 = pd.read_excel(
            os.path.join("C:/Users/asgav/Desktop/code1.xlsx"),
            engine='openpyxl'
        )
        b = df1.values.tolist()

        print(b)



        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.9, 0.6),rows_num=30,
                            column_data=[
                                ("slno", dp(30)),
                                ('reg no', dp(30)),
                                ('name', dp(30)),
                                ('attendance percentage', dp(30))],
                            row_data=[
                                (b[i]) for i in range(len(b))
                            ],)


        self.help_str.get_screen('hello').add_widget(table)
        return screen




if _name_ == '_main_':
        DemoApp().run()
