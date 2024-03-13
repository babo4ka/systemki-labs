import math


def count_n(v_arr):
    temp_n = 0
    for i in range(len(v_arr)):
        temp_n += v_arr[i]

    return temp_n


def count_lam(j_arr, v_arr):
    sum = 0
    for i in range(len(j_arr)):
        sum += j_arr[i] * v_arr[i]

    return sum / n


def count_p(lmbd_v, j_arr):
    p_arr = []
    for i in range(len(j_arr)):
        p_arr.append((math.pow(lmbd_v, j_arr[i]) / math.factorial(j_arr[i])) * math.pow(math.e, (-lmbd_v)))

    return p_arr


def count_Wvib(v_arr, p_arr):
    sum = 0
    for i in range(len(v_arr)):
        sum += (math.pow((v_arr[i] - (n * p_arr[i])), 2)) / (n * p_arr[i])

    return sum


j = [0, 1, 2, 3, 4, 5, 6, 7]
v = [229, 211, 93, 35, 7, 0, 0, 1]

n = count_n(v)

lmbd = count_lam(j, v)

p = count_p(lmbd, j)

W_vib = count_Wvib(v, p)

print(W_vib)


j2 = [0, 1, 2, 3, 4]
v2 = [229, 211, 93, 35, 8]

n2 = count_n(v2)

lmbd2 = count_lam(j2, v2)

p2 = count_p(lmbd2, j2)

W_vib2 = count_Wvib(v2, p2)

print(W_vib2)
