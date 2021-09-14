from math import ceil
import time

def add_up_version1(list_numbers, number):
    half = ceil(number/2)
    pairs = []

    for item in range(half):
        temp = []
        temp.append(item)
        temp.append(number - item)
        pairs.append(temp)

    for item in pairs:
        if item[0] in list_numbers and item[1] in list_numbers:
            return True

    return False

def add_up_version2(list_numbers, number):

    for item in range(len(list_numbers)):
        temp_list = list_numbers.copy()
        temp_number = temp_list.pop(item)

        for num in temp_list:
            if temp_number + num == number:
                return True

    return False

def main():

    start_time = time.time()
    print(add_up_version1([10, 15, 3, 7], 17))
    print(add_up_version1([1, 2, 3, 4], 3))
    print(add_up_version1([1, 2, 3, 4], 4))
    print(add_up_version1([1, 2, 3, 4], 10))
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()
    print(add_up_version2([10, 15, 3, 7], 17))
    print(add_up_version2([1, 2, 3, 4], 3))
    print(add_up_version2([1, 2, 3, 4], 4))
    print(add_up_version2([1, 2, 3, 4], 10))
    end_time = time.time()
    print(end_time - start_time)

if __name__ == "__main__":
    main()