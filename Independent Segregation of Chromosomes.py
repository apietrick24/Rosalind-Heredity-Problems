import math

given = "5"

n_two = 2 * int(given)

pro = 0
log_pro = []

for k in range(n_two, 0, -1):
    pro += math.comb(n_two, k) * math.pow(0.5, k) * math.pow(0.5, n_two - k)
    log_pro.append(round(math.log(pro, 10), 3))

for i in log_pro[::-1]:
    print(i, end=" ")