import random


def create_random_array(n):
    mang = []
    for i in range(n):
        so = random.randint(0, 100)
        mang.append(so)
    return mang


def selection_sort(mang):
    n = len(mang)

    for i in range(n-1):
        vitri_min = i
        for j in range(i+1, n):
            if mang[vitri_min] > mang[j]:
                vitri_min = j
        mang[i], mang[vitri_min] = mang[vitri_min], mang[i]
        print(i+1, '-', mang)


def main():
    mang = create_random_array(10)
    print('mang ban dau:\n', mang)
    selection_sort(mang)
    print('mang sau khi sap xep la\n', mang)


if __name__ == "__main__":
    main()
