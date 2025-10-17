class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ', ' + self.name + '!')

    def display_details(self):
        print('Entry number: ', self.entry)
        print('Name: ', self.name)

        if len(self.types) == 1:
            print('Type: ' + self.types[0])
        else:
            print('Type: ' + self.types[0] + '/' + self.types[1])

        print('Description: ' + self.description)

        if self.is_caught:
            print(self.name + ' has already been caught!')
        else:
            print(self.name + " hasn't been caught yet.")


Pikachu = Pokemon(25, 'Pikachu', ['Eletric'],
                  'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.',
                  True)

Charmander = Pokemon(6, 'Charmander', ['Fire'],
                  "It's a little dragon with fire in the tail",
                  False)

Pikachu.speak()
Pikachu.display_details()

Charmander.speak()
Charmander.display_details()