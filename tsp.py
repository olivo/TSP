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
