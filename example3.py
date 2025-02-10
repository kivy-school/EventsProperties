from kivy.properties import StringProperty, NumericProperty, DictProperty, ListProperty 

class KivyLegend():
    name = StringProperty("Default Name")
    health = NumericProperty(100)
    skills = DictProperty({"default_skill": 10})
    alias = ListProperty(["Default Alias"])

breakpoint()