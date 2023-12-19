import Utils

ID_TO_NAME_CACHE = {}
NAME_TO_DATA_CACHE = {}
ENDPOINT = 'move'

class Move:
    def __init__(self, data):
        global ID_TO_NAME_CACHE
        self.ID = data.get('id')
        self.name = data.get('name')
        self.accuracy = data.get('accuracy')
        self.effectChance = data.get('effect_chance')
        self.PP = data.get('pp')
        self.priority = data.get('priority')
        self.power = data.get('power')
        self.moveClass = data.get('damage_class').get('name')
        self.type = data.get('type')  # This is a "NamedAPIResource" right now
        ID_TO_NAME_CACHE[self.ID] = self.name

    def __str__(self):
        return f'Move Information:\n - ID: {self.ID}\n - Name: {self.name}\n - Accuracy: {self.accuracy}\n - Effect Chance: {self.effectChance}\n - PP: {self.PP}\n - Priority: {self.priority}\n - Power: {self.power}\n - Class: {self.moveClass}\n - Type: {self.type}\n'


def LoadCache():
    global ID_TO_NAME_CACHE, NAME_TO_DATA_CACHE
    data = Utils.LoadCache(ENDPOINT)
    try:
        ID_TO_NAME_CACHE, NAME_TO_DATA_CACHE = data
    except TypeError:
        print(f"Failed to load {ENDPOINT.upper()} cache")
        pass


def SaveCache():
    global ID_TO_NAME_CACHE, NAME_TO_DATA_CACHE
    if len(NAME_TO_DATA_CACHE) == 0:
        return
    output = (ID_TO_NAME_CACHE, NAME_TO_DATA_CACHE)
    Utils.SaveCache(ENDPOINT, output)


def HandleSearch() -> Move | None:
    global ID_TO_NAME_CACHE, NAME_TO_DATA_CACHE
    query = input(f'{ENDPOINT.title()} Name or ID: ').lower()

    if query.isdigit():
        query = Utils.ProperQueryFromID(int(query), ID_TO_NAME_CACHE)

    if query in NAME_TO_DATA_CACHE:
        return NAME_TO_DATA_CACHE[query]

    data = Utils.GetFromAPI(ENDPOINT, query)
    if data is not None:
        newObject = Move(data)
        NAME_TO_DATA_CACHE[newObject.name] = newObject
        return newObject