
friends = ["Kevin", "Karen", "Jim"] # list 3 informations in one value
    #         0        1       2
print(friends[0]) # will print Kevin
print(friends[1]) # will print Karen
print(friends[2]) # will print Jim
print(friends[-1]) # will print value from at the end of the value; Jim
print(friends[-2]) # will print value from at the 2nd end of the value; Karen
print("")

print(friends[1:3]) # specific arrange of value  print("") # although value [3] isnt stored so printed in last value[2]; Karen [1], Jim[2]
friends[1] = "MIKE" # will modify(change) value of its value ex: Karen becomes "MIKE"
print(friends[1])
