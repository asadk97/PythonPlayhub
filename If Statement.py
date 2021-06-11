is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short man")
elif not is_male and is_tall:
    print("You are a tall woman")
else:
    print("You are a female and short")
