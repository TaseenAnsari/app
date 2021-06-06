from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
import design
import requests



Window.size = (480, 800)
class LoginPage(Screen):
    pass
class ForgetPassword(Screen):
    pass
class GeneratePassword(Screen):
    pass
class HomePage(Screen):

    pass


class RCU_App(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        helper_string = design.helper_string
        self.help_str = Builder.load_string(helper_string)
        screen.add_widget(self.help_str)
        return screen
    def show_hide_password(self):
        if (self.help_str.get_screen('loginpage').ids.password.password == False):
            self.help_str.get_screen('loginpage').ids.password.password = True
            self.help_str.get_screen('loginpage').ids.passwordicon.icon = "eye-off"
        else:
            self.help_str.get_screen('loginpage').ids.password.password = False
            self.help_str.get_screen('loginpage').ids.passwordicon.icon = "eye"

    def check_auth(self):
        self.url = "https://rcu-app-1a5d2-default-rtdb.firebaseio.com/CSE/.json"
        self.auth = "JQcFTT4qZvFGi8l6Tpfu19l4I9IjdJXPSrhhsYWp"
        coll_id = self.help_str.get_screen('loginpage').ids.college_id.text
        password = self.help_str.get_screen('loginpage').ids.password.text
        print(coll_id,password)
        try:
            request = requests.get(self.url + '?auth=' + self.auth)
            data = request.json()
            col_id_set = set()
            print(data)
            for key,value in data.items():
                col_id_set.add(key)
        except:
            print("connection error")
        if coll_id in col_id_set and password == data[coll_id]['password']:
            self.help_str.get_screen('homepage').manager.current = "homepage"
            self.help_str.get_screen('homepage').ids.stu_name.text = data[coll_id]['name']
            self.help_str.get_screen('homepage').ids.stu_branch.text = data[coll_id]['branch']
            self.help_str.get_screen('homepage').ids.stu_roll_no.text = coll_id
            self.help_str.get_screen('homepage').ids.stu_sess.text = data[coll_id]['Session']
        else:
            print("login failed")
    def logincheck(self):
        coll_id = self.help_str.get_screen('loginpage').ids.college_id.text
        password = self.help_str.get_screen('loginpage').ids.password.text
        data = {"Id":coll_id,"password":password}
        r = requests.get('http://127.0.0.1:8000/get',params=data)
        print(r)









RCU_App().run()
