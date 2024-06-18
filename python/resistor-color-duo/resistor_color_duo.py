def value(colors):
    color_list = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]

    # Get the values of first two colors
    first_digit = color_list.index(colors[0])
    second_digit = color_list.index(colors[1])

    # Combine the digits
    return first_digit * 10 + second_digit
