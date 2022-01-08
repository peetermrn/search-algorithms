import time
from queue import PriorityQueue


def a_star(map_data, start, goal):
    frontier = PriorityQueue()
    frontier.put((calculate_manhattan_distance(start, goal), start))
    came_from = {start: None}
    diamond_location = ()
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if map_data[current[0]][current[1]] == "D":
            diamond_location = current
            print("FOUND DIAMOND")
            break

        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] + 1, current[1] - 1),
            (current[0], current[1] - 1),
            (current[0] - 1, current[1] - 1),
            (current[0] - 1, current[1]),
            (current[0] - 1, current[1] + 1),
            (current[0], current[1] + 1),
            (current[0] + 1, current[1] + 1),

        ]
        diagonal_neighbors = [
            (current[0] + 1, current[1] - 1),
            (current[0] - 1, current[1] - 1),
            (current[0] - 1, current[1] + 1),
            (current[0] + 1, current[1] + 1),
        ]

        for next_node in neighbors:
            try:
                if map_data[next_node[0]][next_node[1]] != "*":
                    new_cost = cost_so_far[current] + 1
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + calculate_manhattan_distance(next_node, goal)
                        if next_node in diagonal_neighbors:  # to prioritize moving in straight lines
                            priority += 1
                        frontier.put((priority, next_node))
                        came_from[next_node] = current
            except IndexError:  # if edges of the map arent covered with lava
                continue

    loc = came_from[diamond_location]
    path = [diamond_location]
    while loc != start:
        path.append(loc)
        loc = came_from[loc]
    path.append(start)
    path.reverse()
    for pair in came_from.keys():
        if map_data[pair[0]][pair[1]] == " ":
            map_data[pair[0]] = map_data[pair[0]][:pair[1]] + "." + map_data[pair[0]][pair[1] + 1:]
        if pair in path[1:-1]:
            map_data[pair[0]] = map_data[pair[0]][:pair[1]] + "x" + map_data[pair[0]][pair[1] + 1:]

    data_as_string = "\n".join(map_data)
    print(data_as_string)
    print("VISITED ", len(came_from.keys()))
    print(f"Path is {len(path)} steps long.")

    return path


def calculate_manhattan_distance(node, goal):
    return max(abs(node[0] - goal[0]), abs(node[1] - goal[1]))


with open("cave300x300") as f:
    map_data = [l.strip() for l in f.readlines() if len(l) > 1]
    start_time = time.time()
    print(a_star(map_data, (2, 2), (295, 257)))
    print("--- %s seconds ---" % (time.time() - start_time))
