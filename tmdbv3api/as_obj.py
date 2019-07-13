# encoding: utf-8


class AsObj:
    def __init__(self, **entries):
        self.entries = entries
        self.__dict__.update(entries)

    def __repr__(self):
        if 'name' in self.entries:
            return self.entries['name']

        elif 'title' in self.entries:
            return self.entries['title']

        return "TMDb Obj"
