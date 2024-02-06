import math
import numpy as np


PHI = .5 * (-1 + math.sqrt(5))
PI_BY_4 = math.pi / 4       # θ = ±45°
PI_BY_90 = math.pi / 90     # θ∆ = 2°
# Point Access
X = 0
Y = 1
STROKE = 2

K = [0,0]
SIZE = 25

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
    c = np.array([[X, Y, STROKE]])
    c[X] = np.mean(points, where=[[True], [False], [False]])
    c[Y] = np.mean(points, where=[[False], [True], [False]])
    return c

#TODO Implement bounding_box
def bounding_box(points):
    return [1,2]

class OneDollar():
    # Psuedo code for class found here:
    #
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
        new_points = np.array([[X, Y, STROKE]])
        c = centroid(points)
        q = np.array([[X, Y, STROKE]])
        for p in points:
            q[X] = (p[X] - c[X]) * math.cos(w) - (p[Y] - c[Y]) * math.sin(w) + c[X]
            q[Y] = (p[X] - c[X]) * math.sin(w) - (p[Y] - c[Y]) * math.cos(w) + c[Y]
            new_points = np.concatenate((new_points, q), axis=0)

        return np.delete(new_points, 0)

    def scale_to(self, points):
        box = bounding_box(points)
        new_points = np.array([[X, Y, STROKE]])
        q = np.array([[X, Y, STROKE]])
        for p in points:
            q[X] = p[X] * SIZE / box[X]
            q[Y] = p[Y] * SIZE / box[Y]
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
        b = float('inf')
        for t in templates:
            d = self.distance_at_best_angle(points, t, -PI_BY_4, PI_BY_4, PI_BY_90)
            if d < b:
                b = d
                t1 = t
        score = (1 - b) / (0.5 * math.sqrt(2 * (SIZE ** 2)))
        return [t1, score]

    def distance_at_best_angle(self, points, t, θa, θb, θd):
        x1 = PHI * θa + (1 - PHI) * θb
        f1 = distance
        x2 = (1 - PHI) * θa + PHI * θb
        f2 = self.distance_at_angle(points, t, x2)

        while(abs(θb - θa) > θd):
            if f1 < f2:
                θb = x2
                x2 = x1
                f2 = f1
                x1 = PHI * θa + (1 - PHI) * θb
                f1 = self.distance_at_angle(points, t, x1)

            else:
                θa = x1
                x1 = x2
                f1 = f2
                x2 = (1 - PHI) * θa + PHI * θb
                f2 = self.distance_at_angle(points, t, x2)

        return min(f1, f2)

    def distance_at_angle(self, points, t, θ):
        new_points = self.rotate_by(points, θ)
        return self.path_distance(new_points, t)

    def path_distance(self, a, b):
        d = 0
        for i in range(0, abs(a)):
            d += distance(a[i], b[i])

        return d/abs(a)




