
is_male = False
is_tall = False                      # will execute to # you are either not male or not tall or both

if is_male or is_tall:
    print("You are a male or tall both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and (is_tall):
    print("You are a male but are tall")
else:
    print("You are not male and not tall")
