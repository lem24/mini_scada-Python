from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class ThreeWindow(Screen):
    pass

class FourWindow(Screen):
    pass

class FiveWindow(Screen):
    pass

class ScreenManager(ScreenManager):
    pass
class Content(BoxLayout):
    pass

class Myapp(MDApp):
    dialog = None
    dialog2 = None
    data = {
        'Home page': 'home',
        'Login App': 'login',
        'Logout App': 'logout',
    }
    def callback(self, instance):
        if instance.icon == 'home':
            self.root.current = "screen1"
        elif instance.icon == 'login':
            self.show_confirmation_dialog()
        elif instance.icon == 'logout':
            self.show_alert_dialog()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="DO YOU WANT TO LOGOUT!",
                buttons=[
                    MDFlatButton(
                        text="LOGOUT",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,

                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def show_confirmation_dialog(self):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title="Authentication",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="LOGIN",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog2.open()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("this_page.kv")


Myapp().run()


