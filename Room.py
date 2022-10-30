class Room:
    def __init__(self, room_number, room_status):
        self.room_number = room_number
        self.room_status = room_status

    def get_room_no(self):
        return self.room_number

    def get_room_status(self):
        return self.room_status

    def set_room_available(self):
        self.room_status = 1
    
    def set_room_occupied(self):
        self.room_status = 0

room_list = []

def add_room(room):
    room_list.append(room)









    