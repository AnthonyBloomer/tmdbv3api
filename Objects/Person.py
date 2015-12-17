import json


class Person:
    persondata = []

    def __init__(self, persondata):
        self.persondata = persondata

    def get_id(self):
        return self.persondata['id']

    def get_name(self):
        return self.persondata['name']

    def get_biography(self):
        return self.persondata['biography']

    def get_birthday(self):
        return self.persondata['birthday']

    def get_deathday(self):
        return self.persondata['deathday']

    def get_profilepath(self):
        return self.persondata['profile_path']

    def get_place_of_birth(self):
        return self.persondata['place_of_birth']

    def get_homepage(self):
        return self.persondata['homepage']

    def get_json(self):
        return json.dumps(self.persondata)
