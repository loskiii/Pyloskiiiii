# game.py

from rooms import Room

class Game:
    def __init__(self):
        self.rooms = {
            'Hall': Room('Hall', 'A dimly lit hall with a wooden floor.'),
            'Kitchen': Room('Kitchen', 'A dank and dirty room buzzing with flies.'),
            'Dining Room': Room('Dining Room', 'A large room with a beautiful dining table.'),
        }
        self.rooms['Hall'].link_room(self.rooms['Kitchen'], 'south')
        self.rooms['Kitchen'].link_room(self.rooms['Hall'], 'north')
        self.rooms['Hall'].link_room(self.rooms['Dining Room'], 'east')
        self.rooms['Dining Room'].link_room(self.rooms['Hall'], 'west')
        self.current_room = self.rooms['Hall']

    def play(self):
        while True:
            self.current_room.get_details()
            command = input("> ")
            if command in ['north', 'south', 'east', 'west']:
                self.current_room = self.current_room.move(command)
            elif command.lower() in ['quit', 'exit']:
                print("Thanks for playing!")
                break
