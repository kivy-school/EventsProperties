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

    def on_health(self, *args):
        print("Kivy legend health changed tracked by on_health!", self, *args)
    
    def custom_method_callback(self, *args):
        print("Using custom method callback to view changes to a Kivy property", self, *args)

    def on_alias(self, *args):
        print("Kivy legend alias tracked by on_alias!", self, *args)
    
    def on_skills(self, *args):
        print("Kivy legend skills tracked by on_skills!", self, *args)
    
    def skills_checking(self, *args):
        print("Kivy legend skill observed by skills_checking!", self, *args)

def custom_global_callback(*args):
    print("Using custom global callback to view changes to a Kivy property", *args)

bat_brick = KivyLegend(
    name = "Bat Brick", 
    health = 300,
    skills = {"Throwing_stick": 40},
    alias = ["Brutal Wayze"],
    )

kv = """
#:import time time
ColoredBox:
    orientation: "vertical"
    bg_color: 0,0,0,1
    LabelB:
        text: "Legend: \\n" + root.bat_brick_ref.name
        on_release: 
            print("What is root widget and bat brick's name?", root, root.bat_brick_ref.name)
    LabelB:
        text: root.bat_brick_ref.name + " health: " + str(root.bat_brick_ref.health)
        on_release: 
            print("What is bat_brick's health?", root, root.bat_brick_ref.health)
    LabelB:
        text: "Bat Brick gains health!"
        on_release: 
            root.bat_brick_ref.health = root.bat_brick_ref.health + 10
            #root.bat_brick_ref.health = root.bat_brick_ref.health
    LabelB:
        text: "Bat Brick changes name!"
        on_release: 
            root.bat_brick_ref.name = "Funny Man that Laughs"
    LabelB:
        text: root.bat_brick_ref.name + " finds a new life!"
        on_release: 
            root.bat_brick_ref.alias.append("Hairy Pottery")
    LabelB:
        text: root.bat_brick_ref.name + " gets new skill!"
        on_release: 
            root.bat_brick_ref.skills["Unicycle_smash"] = [40, 60 , 80]
    LabelB:
        text: root.bat_brick_ref.name + " upgrades Unicycle_smash (need Unicycle_smash skill or else this will crash)!"
        text_size: self.size
        on_release: 
            root.bat_brick_ref.skills["Unicycle_smash"][0] = 45
    LabelB:
        text: root.bat_brick_ref.name + " check skills!"
        on_release: 
            print(root.bat_brick_ref.skills)
    LabelB:
        text: root.bat_brick_ref.name + " stops time!"
        on_release: 
            time.sleep(10000)
    LabelB:
        text: "breakpoint"
        on_release: 
            breakpoint()
   
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

#imports should be at the top but there are here for explanations
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ColoredBox(BoxLayout):
    bat_brick_ref = ObjectProperty(bat_brick) #initialize here, not on init!
    
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.bat_brick_ref = bat_brick

class MainApp(App):
    bird_brick_ref = bat_brick
    
    def build(self):
        Window.always_on_top = True
        Window.size = (400,500)
        root_widget = Builder.load_string(kv)
        root_widget.bat_brick_ref.bind(health=custom_global_callback)
        root_widget.bat_brick_ref.bind(health=KivyLegend.custom_method_callback)
        # KivyLegend.health = "3.14"
        root_widget.bat_brick_ref.bind(skills=KivyLegend.skills_checking)
        return root_widget

app = MainApp().run()