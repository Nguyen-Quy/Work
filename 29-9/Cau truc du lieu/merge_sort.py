from lib2to3.pytree import Leaf
import random
from turtle import right


def create_random_array(n):
    mang = []
    for i in range(n):
        so = random.randint(-100, 100)
        mang.append(so)
    return mang


def merge_sort(mang):
    if len(mang) > 1:
        middle = len(mang)//2
        left_arr = mang[0:middle]
        right_arr = mang[middle:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                mang[k] = left_arr[i]
                i += 1
            else:
                mang[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            mang[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            mang[k] = right_arr[j]
            j += 1
            k += 1


def main():
    mang = create_random_array(10)
    print('Mang ban dau la:\n', mang)
    merge_sort(mang)
    print('Mang sau sap xep la: \n', mang)


if __name__ == "__main__":
    main()
