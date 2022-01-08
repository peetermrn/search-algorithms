from queue import Queue, PriorityQueue


class EightPuzzleSolver:

    def __init__(self, start: str, goal: str):
        self.start = start
        self.goal = goal
        self.path = []

    def search(self):
        queue = PriorityQueue()
        queue.put((0, self.start))
        came_from = {self.start: None}
        cost_so_far = {}
        cost_so_far[self.start] = 0
        while not queue.empty():
            _, node = queue.get()
            if node == self.goal:
                step = node
                while step is not None:
                    self.path.append(step)
                    step = came_from[step]
                print("Solution is ", len(self.path), "steps")
                print("Tried: ", len(came_from.keys()))
                return self.path
            for child in self.expand(node):
                new_cost = cost_so_far[node] + 1
                if child not in cost_so_far.keys() or new_cost < cost_so_far[child]:
                    cost_so_far[child] = new_cost
                    came_from[child] = node
                    queue.put((new_cost + self.calc_similarity(child, self.start),
                               child))  # priority is cost so far + child and node's difference.. A better way would be
                    # to use Nilsson's Sequence Score: h(n) = P(n) + 3 S(n), where P(n) is the manhattan distance of
                    # each tile from its proper position. The quantity S(n) is a sequence score obtained by checking
                    # around the noncentral squares in turn, allotting 2 for every tile not followed by its proper
                    # successor and 0 for every other tile, except that a piece in the center scores 1.
        return "Failed"

    @staticmethod
    def calc_similarity(node1: str, node2: str):
        similarity = 0
        for i in range(len(node1)):
            if node1[i] != node2[1]:
                similarity += 1
        return similarity

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
