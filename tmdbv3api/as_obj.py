# encoding: utf-8
from tmdbv3api.exceptions import TMDbException


class AsObj:
    def __init__(self, **entries):
        if "success" in entries and entries["success"] is False:
            raise TMDbException(entries["status_message"])
        if "name" in entries:
            self.obj_name = entries["name"]
        elif "title" in entries:
            self.obj_name = entries["title"]
        else:
            self.obj_name = "TMDB Obj"
        self.__dict__.update(entries)

    def __repr__(self):
        return self.obj_name
