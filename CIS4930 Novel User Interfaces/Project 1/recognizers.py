import math

import numpy
import numpy as np
import main as m

PHI = .5 * (-1 + math.sqrt(5))
PI_BY_4 = math.pi / 4  # θ = ±45°
PI_BY_90 = math.pi / 90  # θ∆ = 2°
# Point Access
X = int(0)
Y = int(1)
STROKE = 2

K = [0, 0]
SIZE = 25

# List aspects
FIRST = 0
SECOND = 1
DIMENSIONS = 3

RESAMPLE_N = m.RESAMPLE_N

BBOX_SIZE = m.BBOX_SIZE


def arr_size(points):
    return int((points.size - 1) / 3)


def sanitize(points):
    # Find indices where values are not [-1, -1, -1]
    indices = np.any(points != [-1, -1, -1], axis=1)
    # Filter the array using the indices
    return points[indices]  # .astype(numpy.float32)


# Outputs the euclidean distance between two entries in a numpy array
def distance(p2, p1):
    return math.sqrt((p2[X] - p1[X]) ** 2 + (p2[Y] - p2[Y]) ** 2)


def centroid(points):
    # Uses Numpy mean
    # https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    c = np.array([X, Y, STROKE])
    inc = 0
    # for i in points:
    #    inc += 1
    #    x = i[X]
    #    y = i[Y]
    #
    # x /= inc
    # y /= inc
    c[X] = np.mean(points, where=[True, False, False])
    c[Y] = np.mean(points, where=[False, True, False])
    # return np.array([x,y,0])
    return c


# TODO Implement bounding_box
def bounding_box(points):
    x_coords = points[:, 0]  # Extract x coordinates
    y_coords = points[:, 1]  # Extract y coordinates

    x1 = np.min(x_coords)  # Minimum x coordinate
    x2 = np.max(x_coords)  # Maximum x coordinate

    y1 = np.min(y_coords)  # Minimum y coordinate
    y2 = np.max(y_coords)  # Maximum y coordinate

    width = x2 - x1  # Width of the bounding box
    height = y2 - y1  # Height of the bounding box

    return [width, height]


class RecognitionManager():
    def __init__(self):
        pass


class OneDollar():
    def __init__(self, templates):
        self.templates = []
        for t in templates:
            t = self.resample(t, RESAMPLE_N)
            t = self.rotate_to_zero(t)
            t = self.scale_to_square(t)
            t = self.translate_to_origin(t)
            self.templates.append(t)

    def prepare_templates(self, templates, n):
        temp = []
        for t in templates:
            temp.append(self.resample(t, n))
        return temp

    def resample(self, points, n):
        points = sanitize(points)
        I = self.path_length(points) / (n - 1)
        D = 0

        new_points = np.zeros((n, 3))
        new_points[0] = points[FIRST]

        q = points[FIRST]
        x = 0
        for i in range(1, arr_size(points)):
            pi = points[i]
            p1 = points[i - 1]
            d = distance(p1, pi)
            if D + d >= I:
                eq = (I - D) / d
                q[X] = p1[X] + eq * (pi[X] - p1[X])
                q[Y] = p1[Y] + eq * (pi[Y] - p1[Y])

                new_points[x] = q
                x += 1
                points[i-1] = np.array([q])
                D = 0
            else:
                D = D + d
        print(arr_size(new_points))
        return new_points

    def path_length(self, points):
        d = 0
        for i in range(1, arr_size(points)):
            d += distance(points[i - 1], points[i])
        return d

    def rotate_to_zero(self, points):
        c = centroid(points)
        p = points[FIRST]
        θ = math.atan2(c[Y] - p[Y], c[X] - p[X])
        return self.rotate_by(points, -1 * θ)

    def rotate_by(self, points, w):
        new_points = np.array([[X, Y, STROKE]])
        c = centroid(points)
        q = np.array([[X, Y, STROKE]])
        for p in points:
            q[FIRST][X] = (p[X] - c[X]) * math.cos(w) - (p[Y] - c[Y]) * math.sin(w) + c[X]
            q[FIRST][Y] = (p[X] - c[X]) * math.sin(w) - (p[Y] - c[Y]) * math.cos(w) + c[Y]
            new_points = np.concatenate((new_points, q), axis=0)

        return new_points

    def scale_to_square(self, points):
        box = bounding_box(points)
        new_points = np.array([[X, Y, STROKE]])
        q = np.array([[X, Y, STROKE]])
        for p in points:
            q[FIRST][X] = p[X] * SIZE / box[X]
            q[FIRST][Y] = p[Y] * SIZE / box[Y]
            new_points = np.concatenate((new_points, q), axis=0)

        return new_points

    def translate_to_origin(self, points):
        c = centroid(points)
        new_points = np.array([[-1, -1, -1]])
        q = np.array([X, Y, STROKE])
        for p in points:
            q[X] = p[X] - c[X]
            q[Y] = p[Y] - c[Y]
            new_points = np.concatenate((new_points, np.array([q])), axis=0)

        return sanitize(new_points)

    def sketch(self, points):
        points = self.resample(points, RESAMPLE_N)
        points = self.rotate_to_zero(points)
        points = self.scale_to_square(points)
        points = self.translate_to_origin(points)
        return self.recognize(points)

    def recognize(self, points):
        b = float('inf')
        for t in range(len(self.templates)):
            d = self.distance_at_best_angle(points, self.templates[t], -PI_BY_4, PI_BY_4, PI_BY_90)
            if d < b:
                b = d
                t1 = t
        score = (1 - b) / (0.5 * math.sqrt(2 * (SIZE ** 2)))
        print([t1, score])
        return [t1, score]

    def distance_at_best_angle(self, points, t, θa, θb, θd):
        x1 = PHI * θa + (1 - PHI) * θb
        f1 = self.distance_at_angle(points, t, x1)
        x2 = (1 - PHI) * θa + PHI * θb
        f2 = self.distance_at_angle(points, t, x2)

        while (abs(θb - θa) > θd):
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

    # TODO Work on path distance
    def path_distance(self, a, b):
        d = 0
        for i in range(RESAMPLE_N):
            d += distance(a[i], b[i])
        #
        return d / RESAMPLE_N


class PennyPincher():
    def __init__(self):
        pass

    def resample(self):
        pass
