total_population = (
    6789088686,   
    6872767093,
    6956823603,
    7041194301,
    7125828059,
    7210581976,
    7295290765,
    7379797139,
    7464022049,
    7547858925,
    7631091040,
    7713468100,
    7794798739)

sliced_total_population = total_population[0::3]
print("every 3rd value: " )
print(sliced_total_population)
max_str = str(max(sliced_total_population))
print("the max is: " + max_str)