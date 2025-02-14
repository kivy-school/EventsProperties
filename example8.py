from kivy.properties import StringProperty, NumericProperty, DictProperty, ListProperty, ObjectProperty, AliasProperty 
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window


class KivyLegend(EventDispatcher):
    name = StringProperty("Default Name")
    health = NumericProperty(100)
    skills = DictProperty({"default_skill": 10})
    alias = ListProperty(["Default Alias"])
    exposed_alias = ListProperty([])

    def legend_vulnerability_getter(self, *args):
        # print("legend_vulnerability getter func!", self, *args)
        solution_string = ""
        if self.health < 300:
            solution_string = solution_string + " " + str(self.health)
        if len(self.exposed_alias) > 0:
            solution_string = solution_string + " " + ', '.join(self.exposed_alias)
        return solution_string
    
    def legend_vulnerability_setter(self, new_identity):
        print("legend_vulnerability setter func arguments:", self, new_identity)
        self.health = new_identity[0]
        self.exposed_alias = [new_identity[1]]
    
    legend_vulnerability = AliasProperty(legend_vulnerability_getter,legend_vulnerability_setter,bind=['health', 'exposed_alias'], cache=True)

    def legend_display_getter(self, *args):
        return f"{self.name} {self.health}"

    legend_display = AliasProperty(legend_display_getter,None,bind=['name', 'health'])

    def custom_method_callback(self, *args):
        print("Using custom method callback to view changes to a Kivy property", self, *args)

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
        text: root.bat_brick_ref.legend_display
        on_release: 
            print("What is root widget and bat brick's legend display?", root, root.bat_brick_ref.legend_display)
    LabelB:
        text: "Legend Vulnerability:\\n" + root.bat_brick_ref.legend_vulnerability
        on_release: 
            print("Legend vulnerability ",root.bat_brick_ref.legend_vulnerability)
    LabelB:
        text: root.bat_brick_ref.name + " increases health: " + str(root.bat_brick_ref.health)
        on_release: 
            root.bat_brick_ref.health = root.bat_brick_ref.health + 10
    LabelB:
        text: root.bat_brick_ref.name + " decreases health: " + str(root.bat_brick_ref.health)
        on_release: 
            root.bat_brick_ref.health = root.bat_brick_ref.health - 10
    
    LabelB:
        text: "Stop observing health by unbinding custom_method_callback!"
        on_release:
            print(self.text)
            root.unbinding_annoying_function()
            # root.bat_brick_ref.unbind(health=KivyLegend.custom_method_callback)

    LabelB:
        text: "What are the health observers?"
        on_release: 
            print("what is observing the health property?", ', '.join([x.__name__ for x in root.bat_brick_ref.get_property_observers('health')]))

   
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

    def unbinding_annoying_function(self, *args):
        self.bat_brick_ref.unbind(health=KivyLegend.custom_method_callback)
    
class MainApp(App):
    bird_brick_ref = bat_brick
    
    def build(self):
        Window.always_on_top = True
        Window.size = (400,500)
        root_widget = Builder.load_string(kv)
        root_widget.bat_brick_ref.bind(health=KivyLegend.custom_method_callback)
        return root_widget

app = MainApp().run()