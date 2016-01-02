import json


class Person:
    persondata = []

    def __init__(self, persondata):
        self.persondata = persondata

    def id(self):
        return self.persondata['id']

    def name(self):
        return self.persondata['name']

    def biography(self):
        return self.persondata['biography']

    def birthday(self):
        return self.persondata['birthday']

    def deathday(self):
        return self.persondata['deathday']

    def profilepath(self):
        return self.persondata['profile_path']

    def place_of_birth(self):
        return self.persondata['place_of_birth']

    def homepage(self):
        return self.persondata['homepage']

    def json(self):
        return json.dumps(self.persondata)
