import random


def create_random_array(n):
    mang = []
    for i in range(n):
        so = random.randint(0, 100)
        mang.append(so)
    return mang


def bubble_sort(mang):
    n = len(mang)
    for i in range(n):
        tt = False
        for j in range(n-2, i-1, -1):
            if mang[j] > mang[j+1]:
                mang[j], mang[j+1] = mang[j+1], mang[j]
                tt = True
        print(i+1, '-', mang)
        if tt == False:
            break


def main():
    mang = create_random_array(20)
    print('mang ban dau\n', mang)
    bubble_sort(mang)
    print('mang sau khi sap xep:\n', mang)


if __name__ == "__main__":
    main()
