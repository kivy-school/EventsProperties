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

def custom_on_release_method(*args, **kwargs):
    print("custom on_release method!", *args, **kwargs)
    print("\n")

def custom_on_touch_move_method(*args, **kwargs):
    print("custom on_touch_move method!", *args, **kwargs)
    print("\n")

class LabelB(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(on_press=self.custom_press_method)
        self.bind(on_release=custom_on_release_method)
        #touch events print out a lot, so leave them commented out
        # self.bind(on_touch_down=self.custom_on_touch_down_method)
        # self.bind(on_touch_move=custom_on_touch_move_method)
        # self.bind(on_touch_up=self.custom_on_touch_up_method)

    def on_press(self, *args, **kwargs):
        print("on_press original!", self, *args, **kwargs)

    def custom_press_method(self, *args, **kwargs):
        print("custom press method!", self, *args, **kwargs)
        print("\n")

    def on_touch_down(self, *args, **kwargs):
        print("on_touch_down original!", self, *args, **kwargs, )
        #you need to do super to let touch events propagate: https://kivy.org/doc/stable/api-kivy.uix.widget.html#widget-touch-event-bubbling 
        return super(LabelB, self).on_touch_down(args[0]) 

    def custom_on_touch_down_method(self, *args, **kwargs):
        print("custom on_touch_down method!", self, *args, **kwargs)
        print("\n")

    def on_touch_up(self, *args, **kwargs):
        print("on_touch_up original!", self, *args, **kwargs)

    def custom_on_touch_up_method(self, *args, **kwargs):
        print("custom on_touch_up method!", self, *args, **kwargs)
        print("\n")

class MainApp(App):
    
    def build(self):
        Window.always_on_top = True
        Window.size = (400,500)
        root_widget = Builder.load_string(kv)
        return root_widget

app = MainApp().run()