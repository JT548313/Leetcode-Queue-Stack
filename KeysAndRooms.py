from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        empty = 0
        number_of_rooms = len(rooms)
        visited = {}
        queue = [0]

        while queue:
            cur_room = queue.pop(0)
            num_of_keys = len(rooms[cur_room])
            visited.(cur_room)

            for key in range(num_of_keys):
                if rooms[cur_room][key] not in visited:
                    queue.append(rooms[cur_room][key])

        if len(visited) == number_of_rooms:
            return True

        return False


rooms = [[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]

s = Solution()
s.canVisitAllRooms(rooms)


