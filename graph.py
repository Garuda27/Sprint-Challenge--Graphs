class Graph:
    def __init__(self):
        self.rooms = {}

    
    def build_graph(self, room_graph):
        # add each room to graph
        for room in room_graph:
            if room not in self.rooms:
                self.rooms[room] = set()

        # add direction info to each room
        for room in room_graph:
            for direction in room_graph[room][-1]:
                self.rooms[room] = room_graph[room][-1]
                room_info = self.rooms[room]
                dir_info = self.rooms[room][direction]

                self.rooms[room][direction] = '?'