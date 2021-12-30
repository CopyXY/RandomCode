
conversions = [
    [1, 1000, 2.205, 35.274],  # kg to 
    [1 / 1000, 1, 1 / 454, 1 / 28.35],  # g to
    [1 / 2.205, 1.454, 1, 16],  # lb to
    [1 / 35.274, 28.35, 1 / 16, 1],  # oz to
]

input_1 = int(input("")) 
weight = int(input("Weight :"))
input_2 = int(input(""))

print(weight * conversions[1 - 1][input_2 - 1])




