import statistics
from math import sqrt

DATASET = [3, 1, 0, 2, 7, 3, 6, 4, 2, 0, 0, 10, 15, 6]


# def print_output(iqr, lower_bound, upper_bound, threshold):
#     print("\n> IQR: " + str(iqr) + ",    threshold: " + str(threshold))
#     print("> Lower bound: " + str(lower_bound) + "    Upper bound: " + str(upper_bound))

def print_output(lower_bound, upper_bound, threshold):
    print("\n> threshold: " + str(threshold) + ",    Upper bound: " + str(upper_bound) + ",    Lower bound: " + str(
        lower_bound))


def find_outliers(input_set, lower_bound, upper_bound):
    outliers = []
    for item in input_set:
        if item < lower_bound: outliers.append(item)
        if item > upper_bound: outliers.append(item)
    return outliers


# def find_bounds(q1, q3, threshold):
#     iqr = q3 - q1
#     upper_bound = q3 + threshold * iqr
#     lower_bound = q1 - threshold * iqr
#     return iqr, lower_bound, upper_bound

def find_bounds(mean, pstdev, threshold):
    upper_bound = mean + threshold * pstdev
    lower_bound = mean - threshold * pstdev
    return lower_bound, upper_bound


def median(input_set):
    if len(input_set) % 2 == 0:
        return (input_set[int(len(input_set) / 2) - 1] + input_set[int(len(input_set) / 2)]) / 2, int(
            len(input_set) / 2), int(len(input_set) / 2)
    return input_set[int(len(input_set) / 2)], int(len(input_set) / 2), int(len(input_set) / 2) + 1


def mean(input_set):
    sum = 0
    for item in input_set:
        sum += item
    return sum / len(input_set)


def standard_deviation(input_set, mean):
    sum = 0
    for item in input_set:
        sum += (item - mean) ** 2
    return sqrt(sum / len(input_set))


def find_quantiles(input_set):
    q2, m1, m2 = median(input_set)  # or we can use statistics.median()
    q1, m3, m4 = median(input_set[:m1])
    q3, m5, m6 = median(input_set[m2:])
    # print(q1, dataset[:m1], q3, dataset[m2:])
    return q1, q2, q3


if __name__ == '__main__':
    print("> Given Dataset:\n    ", DATASET)

    dataset = sorted(DATASET)
    print("\n> Sorted Dataset:\n    ", dataset)

    # q1, q2, q3 = find_quantiles(dataset)
    # print("\n> Q1: " + str(q1) + ',    Median: ' + str(q2) + ',    Q3: ' + str(q3))
    # iqr, lower_bound, upper_bound = find_bounds(q1, q3, threshold=1.5)
    # print_output(iqr, lower_bound, upper_bound, threshold=1.5)

    mean = mean(dataset)
    pstdev = standard_deviation(dataset, mean)

    lower_bound, upper_bound = find_bounds(mean, pstdev, threshold=3)
    print_output(lower_bound, upper_bound, threshold=3)
    outliers = find_outliers(dataset, lower_bound, upper_bound)
    print("> Outliers: " + str(outliers))

    lower_bound, upper_bound = find_bounds(mean, pstdev, threshold=2.7)
    print_output(lower_bound, upper_bound, threshold=2.7)
    outliers = find_outliers(dataset, lower_bound, upper_bound)
    print("> Outliers: " + str(outliers))

    lower_bound, upper_bound = find_bounds(mean, pstdev, threshold=2)
    print_output(lower_bound, upper_bound, threshold=2)
    outliers = find_outliers(dataset, lower_bound, upper_bound)
    print("> Outliers: " + str(outliers))
