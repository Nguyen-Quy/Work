import random


def create_random_array(n):
    mang = []
    for i in range(n):
        so = random.randint(0, 100)
        mang.append(so)
    return mang


def divide_arr(mang, duoi, tren):
    i = duoi-1      # index nhỏ hơn mốc
    moc = mang[tren]    # pivot

    for j in range(duoi, tren):
        if mang[j] < moc:
            i += 1
            mang[i], mang[j] = mang[j], mang[i]
    mang[i+1], mang[tren] = mang[tren], mang[i+1]
    return i+1


def quick_sort(mang, duoi, tren):
    if duoi < tren:
        vitri = divide_arr(mang, duoi, tren)
        quick_sort(mang, duoi, vitri-1)
        quick_sort(mang, vitri+1, tren)


def main():
    mang = create_random_array(10)
    print("Mang ban dau la:\n", mang)
    quick_sort(mang, 0, len(mang)-1)
    print("Mang sau khi sap xep la:\n", mang)


if __name__ == "__main__":
    main()
