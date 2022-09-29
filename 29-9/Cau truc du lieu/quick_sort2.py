import random


def create_random_array(n):
    mang = []
    for i in range(n):
        so = random.randint(0, 100)
        mang.append(so)
    return mang


def quick_sort(mang):
    if len(mang) > 1:
        nho_hon = []
        bang = []
        lon_hon = []

        p = mang[0]
        for x in mang:
            if x < p:
                nho_hon.append(x)
            elif x == p:
                bang.append(x)

            else:
                lon_hon.append(x)
        return quick_sort(nho_hon)+bang+quick_sort(lon_hon)
    else:
        return mang


def main():
    mang = create_random_array(10)
    print("Mang ban dau la:\n", mang)
    mang = quick_sort(mang)
    print("Mang sau khi sap xep la:\n", mang)


if __name__ == "__main__":
    main()
