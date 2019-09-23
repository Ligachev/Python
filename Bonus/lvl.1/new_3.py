#Pythagorean theorem
cat_a=int(input('add number: '))
cat_b=int(input('add number: '))
def theorem(cat_a, cat_b):
    hypo_c=cat_a**2+cat_b**2
    hypotenuse=round(hypo_c**.5,2)
    return hypotenuse
print('Гипотенуза равна {}'.format(theorem(cat_a, cat_b)))
