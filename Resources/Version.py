import Utils
from Resources.Data import AbstractData

class Version(AbstractData):
    ID_TO_NAME_CACHE = {}
    NAME_TO_DATA_CACHE = {}
    ENDPOINT = 'version'

    def __init__(self, data):
        super().__init__(data)

        self.versionGroupID = Utils.GetIDFromURL(data['version_group']['url'])

    def PrintData(self):
        print(self.PrintName)
        print(f"Version Group ID: {self.versionGroupID}")
        pass

    def __str__(self):
        return ''

    def AddToCache(self):
        super().AddToCache()
