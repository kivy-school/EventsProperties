class Legend():
    _name = "Default Name" #initial default value
    _health = 100
    skills = {"default_skill": 10}
    alias = ["Default Alias"]

    def _get_name(self):
        print(f"This Legend's name is {self._name}")
        return self._name
    
    def _set_name(self, new_name):
        self._name = new_name
        print(f"This Legend name is now {self._name}")
        return self._name
    
    def _del_name(self):
        print("This Legend will be nameless!")
        del self._name

    name = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="This is the name of the Legend."
    )

    @property
    def health(self):
        "This is the health property of the Legend."
        print("This is the current health")
        return self._health
    
    @health.setter
    def health(self, new_health):
        print(f"This is the new health {new_health}")
        self._health = new_health
        return self._health

    @health.deleter
    def health(self):
        print("Legend health will be set to default!")
        del self._health

print("to get the docstring:", Legend.name.__doc__)

breakpoint()