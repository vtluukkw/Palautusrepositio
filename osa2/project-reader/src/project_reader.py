from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)
        sanaKirjasto = parsed_toml["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(sanaKirjasto["name"], sanaKirjasto["description"], sanaKirjasto["dependencies"], sanaKirjasto["group"]["dev"]["dependencies"])
