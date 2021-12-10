COLOR_TO_CODE = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                 "ALIZARIN CRIMSON": "#e32636", "AMARATH": "#e52b50",
                 "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7", "AQUA": "#00ffff",
                 "BLACK": "#000000"}

print(COLOR_TO_CODE)

color_name = input("Enter color name: ").upper()
while color_name != "":
    if color_name in COLOR_TO_CODE:
        print(color_name, "is", COLOR_TO_CODE[color_name])
        color_name = input("Enter color name: ").upper()
    else:
        print("Invalid color name!")
        color_name = input("Enter color name: ").upper()


