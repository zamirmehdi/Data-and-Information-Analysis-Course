from math import sqrt

DATASET = [-5.0, 23.0, 17.6, 7.23, 1.11]
J = 2

NEW_MIN = 0
NEW_MAX = 1


def mean(input_set):
    sum = 0
    for item in input_set:
        sum += item
    return sum / len(input_set)


def standard_deviation(input_set):
    mean_val = mean(input_set)
    sum = 0
    for item in input_set:
        sum += (item - mean_val) ** 2
    return sqrt(sum / len(input_set))


def standard_deviation_normalization(input_set):
    output_set = []
    for item in input_set:
        new_item = (item - mean(input_set)) / standard_deviation(
            input_set)  # or we can use statistics.mean() and statistics.pstdev functions instead
        new_item = float("{:.4f}".format(new_item))
        output_set.append(new_item)

    # print(mean(output_set))
    # print(standard_deviation(output_set))
    return output_set


def min_max_normalization(input_set):
    output_set = []
    for item in input_set:
        new_item = (item - min(input_set)) / (max(input_set) - min(input_set)) * (NEW_MAX - NEW_MIN) + NEW_MIN
        new_item = float("{:.4f}".format(new_item))
        output_set.append(new_item)
    return output_set


def decimal_scaling_normalization(input_set):
    output_set = []
    for item in input_set:
        new_item = item / 10 ** J
        new_item = float("{:.4f}".format(new_item))
        output_set.append(new_item)
    return output_set


if __name__ == '__main__':
    print("\n> Given Dataset:\n    ",
          DATASET)
    print("\n> Decimal scaling normalization on interval [-1, 1]:\n    ",
          decimal_scaling_normalization(input_set=DATASET))
    print("\n> Min-Max normalization on interval [0, 1]:\n    ",
          min_max_normalization(input_set=DATASET))
    print("\n> Standard Deviation normalization:\n    ",
          standard_deviation_normalization(input_set=DATASET))
