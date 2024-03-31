# rooms.py

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = {}
    
    def describe(self):
        print(self.description)
    
    def link_room(self, room, direction):
        self.linked_rooms[direction] = room
    
    def get_details(self):
        print(self.name)
        print("--------------------")
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
