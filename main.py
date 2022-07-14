# задание 1


def f_gen(n):
    fac = 1
    if n == 0:
        yield 0
    for i in range(1, n+1):
        if i == 1:
            fac = 1
        else:
            fac = fac * i
        yield fac


e = f_gen(0)
for i in e:
    print(i)

# задание 2


def gen_range(first, last, step=0):
    sstep = 0
    while True:
        if sstep == 0:
            yield first
            if step == 0:
                first += 1
            sstep = step
            # sstep -= 1
        if sstep != 0:
            first += 1
            sstep -= 1
        if first == last:
            break


ra = gen_range(1, 12)
for i in ra:
    print(i)
print('_____________')
for i in range(1, 12):
    print(i)


