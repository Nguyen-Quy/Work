import random
import time

st = time.time()


def create_array(n):
    mang = []
    for i in range(n):
        so_ngaunhien = random.randint(-100, 100)
        mang.append(so_ngaunhien)
    return mang


def linear_search(mang, x):
    n = len(mang)
    for i in range(n):
        if mang[i] == x:
            return i
    return -1


def main():
    mang = create_array(20)
    print(mang)
    x = int(input("Nhap gia tri can tim: "))
    vitri = linear_search(mang, x)

    if vitri != -1:
        print(f"Gia tri {x} duoc tim thay tai vi tri {vitri}")
    else:
        print(f"khong tim thay gia tri {x} trong mang")


time.sleep(3)
et = time.time()

if __name__ == "__main__":
    main()
    elapsed_time = et-st
    print('Execution time: ', elapsed_time, 'seconds')
