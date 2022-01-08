from queue import Queue


class EightPuzzleSolver:

    def __init__(self, start: str, goal: str):
        self.start = start
        self.goal = goal
        self.path = []

    def search(self):
        queue = Queue()
        queue.put(self.start)
        came_from = {self.start: None}
        while not queue.empty():
            node = queue.get()
            if node == self.goal:
                step = node
                while step is not None:
                    self.path.append(step)
                    step = came_from[step]
                print("Solution is ", len(self.path), "steps")
                print("Tried: ",len(came_from.keys()))
                return self.path
            for child in self.expand(node):
                if child not in came_from.keys():
                    came_from[child] = node
                    queue.put(child)
        return "Failed"


    @staticmethod
    def expand(node_: str):
        result = []
        zero_index = node_.index("0")
        try:
            new_list = list(node_)
            new_list[zero_index] = node_[zero_index - 3]
            new_list[zero_index - 3] = "0"
            if zero_index - 3 >= 0:
                result.append("".join(new_list))
        except IndexError:
            pass
        try:
            new_list = list(node_)
            new_list[zero_index] = node_[zero_index + 3]
            new_list[zero_index + 3] = "0"
            result.append("".join(new_list))
        except IndexError:
            pass
        try:
            new_list = list(node_)
            new_list[zero_index] = node_[zero_index + 1]
            new_list[zero_index + 1] = "0"
            if zero_index not in [2, 5, 8]:
                result.append("".join(new_list))
        except IndexError:
            pass
        try:
            new_list = list(node_)
            new_list[zero_index] = node_[zero_index - 1]
            new_list[zero_index - 1] = "0"
            if zero_index not in [0, 3, 6]:
                result.append("".join(new_list))
        except IndexError:
            pass
        return result


solver = EightPuzzleSolver("123456780", "087654321")
for list_ in solver.search():
    print(list_[:3] + "\n" + list_[3:6] + "\n" + list_[6:] + "\n\n")
