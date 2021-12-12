import math

given = "2 2 2"

hom, het, rec = [int(i) for i in given.split(" ")]

# Total number of different children that can be produced by two organisms
sample_space = 4*math.comb(hom + het + rec, 2)

# Number of possible children which are homozygous recessive
total_pure_rec = 4*math.comb(rec, 2) + 2*rec*het + 1*math.comb(het, 2)

# 1 - P(A x A -> dd)
print(1 - (total_pure_rec/sample_space))
