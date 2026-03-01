class defend:
    name = "defend"
    def __init__(self, name):
        self._Pivate_name = name

    @property
    def get_name(self):
        return self._Pivate_name

if __name__ == "__main__":
    d = defend("SecureName")
    print(d.get_name)

    

    