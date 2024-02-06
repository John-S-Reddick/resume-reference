import math
import numpy as np

# Point Access
X = 0
Y = 1
STROKE = 2

<<<<<<< Updated upstream
=======
K = [0,0]

>>>>>>> Stashed changes
# List aspects
FIRST = 0
DIMENSIONS = 3


# Outputs the euclidean distance between two entries in a numpy array
def distance(p2, p1):
    # sqrt((x2 - x1)^2 + (y2 - y1)^2))
    return math.sqrt((p2[X] - p1[X]) ** 2 + (p2[Y] - p2[Y]) ** 2)

def centroid(points):
    # Uses Numpy mean
    # https://numpy.org/doc/stable/reference/generated/numpy.mean.html
<<<<<<< Updated upstream
    c = np.array([X, Y, STROKE])
=======
    c = np.array([[X, Y, STROKE]])
>>>>>>> Stashed changes
    c[X] = np.mean(points, where=[[True], [False], [False]])
    c[Y] = np.mean(points, where=[[False], [True], [False]])
    return c

<<<<<<< Updated upstream
class OneDollar():
    # Psuedo code for class found here:
    # https://github.com/John-S-Reddick/resume-reference/blob/ea908d0069c7ea63b2ef6da9cfee86df927a580d/CIS4930%20Novel%20User%20Interfaces/Project%201/Papers%20Cited/$1%20Recognizer.pdf
=======
#TODO Implement bounding_box
def bounding_box(points):
    return [1,2]

class OneDollar():
    # Psuedo code for class found here:
    # 
>>>>>>> Stashed changes
    def resample(self, points, n):
        I = self.path_length(points) / (n - 1)
        D = 0

        p1 = points[FIRST]
        new_points = np.array([points[FIRST]])

        for p2 in points:
            if p2 == p1:
                continue

            d = distance(p1, p2)
            if D + d >= I:
                c = (I - D) / d
                p1x = p1[X] + c * (p2[X] - p1[X])
                p1y = p1[Y] + c * (p2[Y] - p1[Y])
                p1 = np.array([[p1x, p1y, 0]])

                new_points = np.concatenate((new_points, p1), axis=0)

                D = 0

            else:
                D = D + d

        return new_points
    def path_length(self, points):
        d = 0
        p1 = points[FIRST]
        for p2 in points:
            if p1 == p2:
                continue
            d += distance(p2, p1)
            p1 = p2

        return d

    def indicative_angle(self, points):
        c = centroid(points)
        p = points[FIRST]
        return math.atan2(c[Y] - p[Y], c[X] - p[X])

    def rotate_by(self, points, w):
<<<<<<< Updated upstream
        new_points = np.array([X, Y, STROKE])
        c = centroid(points)
        q = np.array([X, Y, STROKE])
=======
        new_points = np.array([[X, Y, STROKE]])
        c = centroid(points)
        q = np.array([[X, Y, STROKE]])
>>>>>>> Stashed changes
        for p in points:
            q[X] = (p[X] - c[X]) * math.cos(w) - (p[Y] - c[Y]) * math.sin(w) + c[X]
            q[Y] = (p[X] - c[X]) * math.sin(w) - (p[Y] - c[Y]) * math.cos(w) + c[Y]
            new_points = np.concatenate((new_points, q), axis=0)

        return np.delete(new_points, 0)

<<<<<<< Updated upstream
=======
    def scale_to(self, points, size):
        box = bounding_box(points)
        new_points = np.array([[X, Y, STROKE]])
        q = np.array([[X, Y, STROKE]])
        for p in points:
            q[X] = p[X] * size / box[X]
            q[Y] = p[Y] * size / box[Y]
            new_points = np.concatenate((new_points, q), axis=0)

        return np.delete(new_points, 0)

    def translate_to(self, points, k):
        c = centroid(points)
        new_points = np.array([[X, Y, STROKE]])
        q = np.array([[X, Y, STROKE]])
        for p in points:
            q[X] = p[X] + K[X] - c[X]
            q[Y] = p[Y] + K[Y] - c[Y]
            new_points = np.concatenate((new_points, q), axis=0)

        return np.delete(new_points, 0)

    def recognize(self, points, templates):
        b =
>>>>>>> Stashed changes
