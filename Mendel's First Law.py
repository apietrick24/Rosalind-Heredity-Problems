given = "2 2 2"

given = [int(i) for i in given.split(" ")]

# Total Number of Individuals
sample_space_first = sum(given)
sample_space_second = sample_space_first - 1

# Number of Individuals with that Phenotype in the Sample Size
homo_dom = given[0]
hetero = given[1]
homo_rec = given[2]

# Probability of Selecting that Phenotype First
pro_homo_dom_first = homo_dom / sample_space_first
pro_hetero_first = hetero / sample_space_first
pro_homo_rec_first = homo_rec / sample_space_first

# Probability of Selecting that Phenotype Second
pro_homo_dom_second = homo_dom / sample_space_second
pro_hetero_second = hetero / sample_space_second
pro_homo_rec_second = homo_rec / sample_space_second

"""
Key
D - Domain Allele
d - Recessive Allele
a - Either Domain or Recessive Allele

DD - Homozygous Domain
Dd - Heterozygous
dd - Homozygous Recessive
A - Either Homozygous Domain, Heterozygous or Homozygous Recessive
"""

# P(A1 x A2 -> Da | A1 = DD) = P(DD x DD -> Da) + P(DD x Dd -> Da) + P(DD x dd -> Da)
given_homo_dom_first = pro_homo_dom_first * ((homo_dom - 1) / sample_space_second) \
                       + pro_homo_dom_first * pro_hetero_second \
                       + pro_homo_dom_first * pro_homo_rec_second

# P(A1 x A2 -> Da | A1 = Dd) = P(Dd x DD -> Da) + (1 - P(Dd x Dd -> dd)) + P(Dd x dd -> Da)
given_hetero_first = pro_hetero_first * pro_homo_dom_second \
                     + pro_hetero_first * ((hetero - 1) / sample_space_second) - (pro_hetero_first * .5) * (((hetero - 1) / sample_space_second) * .5) \
                     + (pro_hetero_first * .5) * pro_homo_rec_second

# P(A1 x A2 -> Da | A1 = dd) = P(dd x DD -> dD) + P(dd x Dd -> dD)
given_homo_rec_first = pro_homo_rec_first * pro_homo_dom_second \
                       + pro_homo_rec_first * (pro_hetero_second * .5)

# P(A1 x A2 -> Da) = P(A1 x A2 -> Da | A1 = DD) + P(A1 x A2 -> Da | A1 = Dd) + P(A1 x A2 -> Da | A1 = dd)
print("Given:", given)
print("P(A1 x A2 -> Da):", given_homo_dom_first + given_hetero_first + given_homo_rec_first)