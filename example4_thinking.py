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
#:import bat_brick example4.bat_brick

ColoredBox:
    bg_color: 0,0,0,0
    orientation: "horizontal"
    ColoredBox:
        orientation: "vertical"
        bg_color: 1,0,0,0
        Button:
            text: "Brick_Frog"
            on_release: 
                print("What is root?", root)
        LabelB:
            text: "Brick_Frog health"
    ColoredBox:
        orientation: "vertical"
        bg_color: 0,1,0,0
        Button:
            text: "Brick_Frog attack"
        Button:
            text: "Bat_Brick attack"
    ColoredBox:
        orientation: "vertical"
        bg_color: 0,0,1,0
        Button:
            text: bat_brick.name
        LabelB:
            text: "Bat_Brick health"


<ColoredBox@BoxLayout>:
	bg_color: 1,1,1,1
	canvas.before: 
		Color:
			rgba: self.bg_color
		Rectangle:
			pos: self.pos
			size: self.size

<LabelB@Button>:
	background_normal: ''
    background_down: ''
    background_disabled_normal: ''
    background_disabled_down: ''
    background_color: 0, 0, 0, 0
"""

class MainApp(App):
    def build(self):
        Window.always_on_top = True
        return Builder.load_string(kv)

app = MainApp()
app.run()