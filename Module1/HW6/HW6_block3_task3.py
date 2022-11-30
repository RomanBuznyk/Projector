candidat_1 = []
candidat_2 = []

region_1_rating_1 = float(input("Enter rating of the first candidat in first region:"))
region_2_rating_1 = float(input("Enter rating of the first candidat in seconf region:"))

#calculation for region 1
region_1_rating_2 = 100 - region_1_rating_1 
print(f'rating for second candidat is', region_1_rating_2)
people_1 = int((10000 * region_1_rating_1) / 100)
print(f'Number of people voted for candidat 1 in first region - ', people_1)
people_2 = 10000 - people_1
print(f'Number of people voted for candidat 2 in first region - ', people_2)

#calculation for region 2
region_2_rating_2 = 100 - region_2_rating_1 
print(f'Rating for second candidat is', region_2_rating_2)
people_reg2_1 = int((10000 * region_2_rating_1) / 100)
print(f'Number of people voted for candidat 1 in second region - ', people_reg2_1)
people_reg2_2 = 10000 - people_reg2_1
print(f'Number of people voted for candidat 2 in seconf region - ', people_2)

candidat_1.append(people_1)
candidat_2.append(people_2)
print(f' Total votes for candidat 1 - ', *candidat_1, sep = '')
print(f' Total votes for candidat 2 - ', *candidat_2, sep = '')
if candidat_1 > candidat_2:
    print('Candidat 1 win')
else: print('Candidat 2 win')