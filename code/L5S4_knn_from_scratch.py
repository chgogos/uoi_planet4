# https://archive.ics.uci.edu/ml/datasets/iris

from math import sqrt
import csv
import random


def euclidean_distance(v1, v2):
    s = 0
    for x, y in zip(v1, v2):
        s += (x - y) ** 2
    return sqrt(s)


# load data
all_points = []
with open("data/iris/iris.data") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        sepal_length, sepal_width, petal_length, petal_width, iris_class = row
        row = (
            float(sepal_length),
            float(sepal_width),
            float(petal_length),
            float(petal_width),
            iris_class,
        )
        all_points.append(row)

# split data in known points and unknown points
seed = 123456
random.seed(seed)
known_points, unknown_points = [], []
for point in all_points:
    if random.random() < 0.8:
        known_points.append(point)
    else:
        unknown_points.append(point)

print(f"Known points = {len(known_points)}, Unknown points = {len(unknown_points)}")

# classify each unknown point based on the majority class of its k nearest known points
successful_predictions = 0
kappa = 3
for point1 in unknown_points:
    distance_class = []
    for point2 in known_points:
        distance = euclidean_distance(point1[:-1], point2[:-1])
        distance_class.append((distance, point2[-1]))
    distance_class.sort()

    setosa, versicolor, virginica = 0, 0, 0
    for d, c in distance_class[:kappa]:
        if c == "Iris-setosa":
            setosa += 1
        elif c == "Iris-versicolor":
            versicolor += 1
        else:
            virginica += 1

    if setosa >= max(versicolor, virginica):
        predicted_class = "Iris-setosa"
    elif versicolor >= max(setosa, virginica):
        predicted_class = "Iris-versicolor"
    else:
        predicted_class = "Iris-virginica"

    if predicted_class == point1[-1]:
        successful_predictions += 1
    msg = "OK" if point1[-1] == predicted_class else "NOT OK"
    print(f"{point1} prediction = {predicted_class} {msg}")

print(
    f"Successful predictions = {successful_predictions * 100 / len(unknown_points):.2f}%"
)
