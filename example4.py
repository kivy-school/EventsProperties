from kivy.properties import StringProperty, NumericProperty, DictProperty, ListProperty 
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window


def stringerr_handler(*args):
    print(f"string error argument {args} is handled!")
    return str(args[0])

class KivyLegend(EventDispatcher):
    name = StringProperty("Default Name" ,errorhandler = stringerr_handler) # ,errorhandler = stringerr_handler
    health = NumericProperty(100)
    skills = DictProperty({"default_skill": 10})
    alias = ListProperty(["Default Alias"])

bat_brick = KivyLegend(
    name = "Bat Brick", 
    health = 300,
    skills = {"Throwing_stick": 40},
    alias = ["Brutal Wayze"],
    )

brick_frog = KivyLegend(
    name = "Brick Frog",
    health = 400,
    skills = {"Brick_Smash": 50},
    alias = ["Steven Stooge"],
    )

kv = """
Button:
    text: "Hello World"
"""

class MainApp(App):
    def build(self):
        Window.always_on_top = True
        return Builder.load_string(kv)

app = MainApp()
app.run()