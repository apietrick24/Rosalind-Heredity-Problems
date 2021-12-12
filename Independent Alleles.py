import math

given = "2 1"

gen, het = [int(i) for i in given.split(" ")]

# Number of Individuals in the Current Generation (Assuming each Couple has 2 children)
individuals = int(math.pow(2, gen))

pro_het_individuals = 0

for i in range(het, individuals + 1):
    # Note: Regardless of A1 or B1, P(A1 B1 x Dd Pp -> Dd Pp) will be equal to 4/16 or 0.25
    pro_het_individuals += math.comb(individuals, i) * math.pow(.25, i) * math.pow(1 - .25, individuals - i)

print(pro_het_individuals)
