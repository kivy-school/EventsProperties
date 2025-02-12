from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button

kv = """
ColoredBox:
    orientation: "vertical"
    bg_color: 0,0,0,1
    LabelB:
        text: "Event binding to custom button label"
        on_press: 
            print("on_press kv")
            # print("on_press kv", self, args, type(args), "\\n")
        on_release: 
            print("on_release kv")
            # print("on_release kv", self, args, type(args), "\\n")
        on_touch_down:
            print("on_touch_down kv")
            # print("on_touch_down kv", self, args, type(args), "\\n")
        on_touch_move:
            print("on_touch_move kv")
            # print("on_touch_move kv", self, args, type(args), "\\n")
        on_touch_up:
            print("on_touch_up kv")
            # print("on_touch_up kv", self, args, type(args), "\\n")
   
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

class LabelB(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(on_press=self.custom_press_method)

    def custom_press_method(self, *args, **kwargs):
        print("custom press method!", self, *args, **kwargs)
        print("\n")

class MainApp(App):
    
    def build(self):
        Window.always_on_top = True
        Window.size = (400,500)
        root_widget = Builder.load_string(kv)
        return root_widget

app = MainApp().run()