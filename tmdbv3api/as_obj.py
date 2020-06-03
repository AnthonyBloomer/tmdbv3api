# encoding: utf-8


class AsObj:
    def __init__(self, **entries):
        if 'name' in entries:
            self.obj_name = entries["name"]
        elif 'title' in entries:
            self.obj_name = entries["title"]
        else:
            self.obj_name = "TMDB Obj"
        self.__dict__.update(entries)

    def __repr__(self):
        return self.obj_name
