import random


def create_random_array(n):
    mang = []
    for i in range(n):
        so = random.randint(0, 100)
        mang.append(so)
    return mang


def insertion_sort(mang):
    n = len(mang)

    for i in range(1, n):
        tam = mang[i]
        j = i
        while j > 0 and mang[j-1] > tam:
            mang[j] = mang[j-1]
            j = j-1
        mang[j] = tam
        print(i, '-', mang)


def main():
    mang = create_random_array(10)
    print('mang ban dau:\n', mang)
    insertion_sort(mang)
    print('mang sau khi sap xep la\n', mang)


if __name__ == "__main__":
    main()
