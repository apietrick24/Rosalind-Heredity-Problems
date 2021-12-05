given = "16593 19963 17524 18545 17147 16316"

given = [int(i) for i in given.split(" ")]

# Note: I'm using the same notation I used in the Mendel's First Law file

"""
Probability of a Couple (A1 x A2) Producing an Individual with a Dominant Genotype

P(DD x DD -> Da) = 1
P(DD x Dd -> Da) = 1
P(DD x dd -> Da) = 1
P(Dd x Dd -> Da) = .75
P(Dd x dd -> Da) = .5
P(dd x dd -> Da) = 0
"""
pro_dominant = [1, 1, 1, .75, .5, 0]

# Summation over all Couples: 2 * P(couple -> Da | couple) * (Number of Couples)
expected = sum([2 * pro_dominant[i] * given[i] for i in range(6)])

print("Given:", given)
print("E[Individuals with a Dominant Genotype]:", expected)
