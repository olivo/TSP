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

    route.append(route[0])
    return route

def closest_pair(paths):
    best_distance = 0
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
    
    return first_index, second_index
        

# List of points in the plane to be used for testing.
points = list()
points.append(Point(0,0))
points.append(Point(0,1))
points.append(Point(1,2))
points.append(Point(2,2))

tsp_route = compute_nearest_neighbor_tsp_route(points)

print "The TSP route using the nearest neighbor is:"
for point in tsp_route:
    print Point.str(point), " "

cost = 0
for index in range(0, len(tsp_route) - 1):
    cost += Point.distance(tsp_route[index], tsp_route[index + 1])

print "The total cost is:", cost
