from kivy.properties import StringProperty, NumericProperty, DictProperty, ListProperty, ObjectProperty 
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

kv = """

ColoredBox:
    orientation: "vertical"
    bg_color: 1,0,0,0
    LabelB:
        text: root.bat_brick_ref.name
        on_release: 
            print("What is root?", root, root.bat_brick_ref.name)
    LabelB:
        text: "Bat Brick gains health!"
        on_release: 
            print("What is root1?", root,)
            root.bat_brick_ref.name = "testor"
    LabelB:
        text: "bat_brick"
        on_release: 
            print("What is root2?", root, root.bat_brick_ref.name)
   
#<ColoredBox@BoxLayout>:
#	bg_color: 1,1,1,1
#	canvas.before: 
#		Color:
#			rgba: self.bg_color
#		Rectangle:
#			pos: self.pos
#			size: self.size

<LabelB@Button>:
	background_normal: ''
    background_down: ''
    background_disabled_normal: ''
    background_disabled_down: ''
    background_color: 0, 0, 0, 0
"""

from kivy.uix.boxlayout import BoxLayout

class ColoredBox(BoxLayout):
    bat_brick_ref = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bat_brick_ref = bat_brick


class MainApp(App):
    def build(self):
        Window.always_on_top = True
        Window.size = (300,400)
        root = Builder.load_string(kv)
        # root.bat_brick_ref = bat_brick
        return root

app = MainApp().run()