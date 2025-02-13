# https://www.reddit.com/r/kivy/comments/183go2x/help_needed_with_bindings_setter_not_working/
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ColorProperty
from kivy.uix.button import Button

class NbaProject(BoxLayout):
    text_colour = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.headerLabel = Label(font_size=70, text="Games", size_hint=(1, 0.1))
        self.bind(text_colour=self.headerLabel.setter('color'))
        self.add_widget(self.headerLabel)
        button = Button(text='change colour', on_release=self.change_color)
        self.add_widget(button)

    def change_color(self, obj):
        print('change color')
        self.text_colour = (0, 1, 0, 1)
        print(self.text_colour)


class BindSetterApp(App):
    def build(self):
        return NbaProject()


BindSetterApp().run()