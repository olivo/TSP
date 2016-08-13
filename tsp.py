from point import Point
import sys

def nearest_neighbor(points, current_point):
    return min(points, key = lambda x: Point.distance(x, current_point) if x != current_point else sys.maxint)

def compute_nearest_neighbor_tsp_route(points):
    current_point = points[0]
    route = [current_point]
    points.remove(current_point)

    while points:
        neighbor = nearest_neighbor(points, current_point)
        route.append(neighbor)
        print "Neighbor:", Point.str(neighbor)
        points.remove(neighbor)

    return route

def closest_pair(paths):
    best_distance = sys.maxint
    best_first_index = -1
    best_second_index = -1
    for first_index in range(0, len(paths)):
        for second_index in range(first_index + 1, len(paths)):
            first_to_second_cost = Point.distance(paths[first_index][-1], paths[second_index][0])
            second_to_first_cost = Point.distance(paths[first_index][0], paths[second_index][-1])
            if first_to_second_cost < best_distance or second_to_first_cost < best_distance:
                if first_to_second_cost < second_to_first_cost:
                    best_distance = first_to_second_cost
                    best_first_index = first_index
                    best_second_index = second_index
                else:
                    best_distance = second_to_first_cost
                    best_first_index = second_index
                    best_second_index = first_index
    
    return best_first_index, best_second_index


def merge_pairs(paths, first_index, second_index):
    merged_path = paths[first_index] + paths[second_index]
    first_path = paths[first_index]
    second_path = paths[second_index]
    paths.remove(first_path)
    paths.remove(second_path)
    paths.append(merged_path)
        

def compute_closest_pair_tsp_route(points):
    paths = list()

    for point in points:
        path = [point]
        paths.append(path)

    for index in range(0, len(points) - 1):
        first_index, second_index = closest_pair(paths)
        merge_pairs(paths, first_index, second_index)

    return paths[0]


# List of points in the plane to be used for testing.
points = list()
points.append(Point(0,0))
points.append(Point(0,1))
points.append(Point(0,2))
points.append(Point(0,3))

tsp_route = compute_nearest_neighbor_tsp_route(points)

print "The TSP route using the nearest neighbor is:"
for point in tsp_route:
    print Point.str(point), " "

# Add cost for all edges between the internal nodes.
cost = 0
for index in range(0, len(tsp_route) - 1):
    cost += Point.distance(tsp_route[index], tsp_route[index + 1])

# Add cost for the looping edge
cost += Point.distance(tsp_route[-1], tsp_route[0])

print "The total cost is:", cost
