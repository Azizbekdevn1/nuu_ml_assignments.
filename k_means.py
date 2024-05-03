import math


def to_double(lst):
    return [float(x) for x in lst]


def nearly(candidate_center_cord, e):
    min_dist = float('inf')  # tekshirish uchun eng katta son
    result = 0
    for i, center in enumerate(candidate_center_cord):
        dist = sum((x - y) ** 2 for x, y in zip(center, e))
        if math.sqrt(dist) < min_dist:
            min_dist = math.sqrt(dist)
            result = i
    return result


def print_list(lst):
    return "( " + ", ".join(map(str, lst)) + " )"


def new_conditate_center_cord(result, cord_e):
    result_center_cord = []
    for indices in result:
        sum_values = [0] * len(cord_e[0])
        for index in indices:
            for k, value in enumerate(cord_e[index]):
                sum_values[k] += value
        mean_values = [x / len(indices) for x in sum_values]
        result_center_cord.append(mean_values)
    return result_center_cord


def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for l1, l2 in zip(list1, list2):
        if any(x != y for x, y in zip(l1, l2)):
            return False
    return True


def main():
    cord_e = []
    cord_class_center = []
    result = []
    result_test = []

    with open("/home/azizbek/Desktop/data.txt", 'r') as f:
        for line in f:
            if line.strip():
                c = line.strip().split(',')
                cord_e.append(to_double(c))

    count_class = int(input("Nechta klastirga bo'lmoqchisiz : "))

    if count_class <= len(cord_e):
        cord_class_center = cord_e[:count_class]

        while True:
            result = [[] for _ in range(count_class)]

            for i, e in enumerate(cord_e):
                result[nearly(cord_class_center, e)].append(i)

            result = [[x for x in lst if x != []] for lst in result]

            if are_lists_equal(result_test, result):
                for i, lst in enumerate(result):
                    print(f"{i + 1} - class")
                    print(print_list(lst))
                break
            else:
                cord_class_center = new_conditate_center_cord(result, cord_e)
                result_test = result.copy()
                result.clear()
    else:
        print("Bu holatda klastirlarga ajratib bolmaydi! ")


if __name__ == "__main__":
    main()
