import math

given = "2 1"

given = [int(i) for i in given.split(" ")]

# Note: I'm using the same notation I used in the Mendel's First Law file

# Number of Generation from Tom
num_of_generation = given[0]

# Number of Individuals in the Current Generation (Assuming each Couple has 2 children)
num_of_individuals = int(math.pow(2, num_of_generation))

# Minimum number of Heterozygous individuals in the generation
num_of_hetero = given[1]


# n-choose-k function - Can just use math.comb if using Python 3.10 (I haven't from 3.6 yet)
def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


# https://math.stackexchange.com/questions/439281/probability-of-an-event-happening-n-or-more-times

pro_hetero_in_k = 0

for i in range(num_of_hetero, int(num_of_individuals) + 1):
    # Note: Regardless of A1 or B1, P(A1 B1 x Dd Pp -> Dd Pp) will be equal to 4/16 or 0.25
    pro_hetero_in_k += nCr(num_of_individuals, i) * math.pow(.25, i) * math.pow(1 - .25, num_of_individuals - i)

print("Given:", given)
print("P(At least " + str(num_of_hetero), "Heterozygous individuals in the", str(num_of_generation) + "th generation):",
      pro_hetero_in_k)
