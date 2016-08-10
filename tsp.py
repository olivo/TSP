from point import Point
import sys

def nearest_neighbor(points, current_point):
    return min(points, key = lambda x: Point.distance(x, current_point) if x != current_point else sys.maxint)

# List of points in the plane to be used for testing.
points = list()
points.append(Point(0,0))
points.append(Point(0,1))
points.append(Point(1,2))
points.append(Point(2,2))

start_point = points[0]

nearest_neighbor = nearest_neighbor(points, start_point)

print "The nearest neighbor is:", Point.str(nearest_neighbor)
