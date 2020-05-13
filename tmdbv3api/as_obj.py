# encoding: utf-8


class AsObj:
    def __init__(self, **entries):
        self.__entries = entries
        self.__dict__.update(entries)

    def __repr__(self):

        if 'name' in self.__entries:
            return self.__entries['name']

        elif 'title' in self.__entries:
            return self.__entries['title']

        return "TMDb Obj"
