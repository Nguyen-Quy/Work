import random
import time

st = time.time()


def create_increasing_array(n):
    mang = []
    first_num = random.randint(-100, 100)
    mang.append(first_num)

    for i in range(1, n):
        tang = random.randint(1, 10)
        so = mang[i-1] + tang
        mang.append(so)
    return mang


def binary_search(mang, x):
    trai = 0
    phai = len(mang)-1
    while trai <= phai:
        giua = (trai+phai)//2
        if mang[giua] == x:
            return giua
        if x < mang[giua]:
            phai = giua-1
        else:
            trai = giua+1
    return -1


def main():
    mang = create_increasing_array(20)
    print(mang)
    x = int(input("Nhap gia tri can tim: "))
    vitri = binary_search(mang, x)
    if vitri != -1:
        print(f"Phan tu {x} duoc tim thay tai vi tri {vitri}")
    else:
        print(f"Khong tim thay gia tri {x} trong mang")


time.sleep(3)
et = time.time()

if __name__ == "__main__":
    main()
    elapsed_time = et-st
    print('Execution time: ', elapsed_time, 'seconds')
