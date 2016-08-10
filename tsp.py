from point import Point

def compute_nearest_neighbor_index(points, current_point_index):
    min_distance = 0
    min_index = 0
    current_point = points[current_point_index]
    for index in range(0, len(points)):
        if Point.distance(points[index], current_point) < min_distance and current_point_index != index:
            min_distance = Point.distance(points[index], current_point)
            min_index = index
    return min_distance
        

# List of points in the plane to be used for testing.
points = list()
points.append(Point(0,0))
points.append(Point(0,1))
points.append(Point(1,2))
points.append(Point(2,2))

index = compute_nearest_neighbor_index(points, 0)
