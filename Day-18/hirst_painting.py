import colorgram

colors = colorgram.extract('image.jpg', 15)
lst_color = []

for i in colors:
    first_color = i.rgb
    red = first_color.r
    green = first_color.g
    blue = first_color.b

    rgb= [red, green, blue]
    lst_color.append(tuple(rgb))

print(lst_color)
