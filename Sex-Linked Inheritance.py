given = "0.1 0.5 0.8"

list = ""

for i in [float(i) for i in given.split(" ")]:
    # Since Independent: P(X and Y) = P(X) * P(Y) then P(X | Y) = P(X)
    # 2* P(Y) * P(X)
    list += str(round(2 * i * (1 - i), 3)) + " "

print(list)
