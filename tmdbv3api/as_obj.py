# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class AsObj:
    def __init__(self, **entries):
        self.entries = entries
        self.__dict__.update(entries)

    def __repr__(self):
        if 'name' in self.entries:
            return self.entries['name'].encode('utf-8')

        elif 'title' in self.entries:
            return self.entries['title'].encode('utf-8')

        return "TMDb Obj"
