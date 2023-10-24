# O'nlik va yuzlik raqamlarini almashtirish orqali berilgandan olingan butun sonni chiqaring (masalan 123-213 ga o'zgartiriladi)
a=int(input())
def almashtirish_a(a):
    o = a% 10
    y = (a // 10) % 10
    yuzlik = a // 100

    yangi_a = o * 100 + y * 10 + yuzlik
    return yangi_a
natija = almashtirish_a(a)
Z=natija//10
print( natija)
print(Z)