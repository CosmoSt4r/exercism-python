def recite(start_verse, end_verse):
    gifts = [
        "Drummers Drumming",
        "Pipers Piping",
        "Lords-a-Leaping",
        "Ladies Dancing",
        "Maids-a-Milking",
        "Swans-a-Swimming",
        "Geese-a-Laying",
        "Gold Rings",
        "Calling Birds",
        "French Hens",
        "Turtle Doves",
        "Partridge in a Pear Tree",
    ]
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
    ]
    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    result = []
    for i in range(start_verse, end_verse + 1):

        string = f"On the {days[i - 1]} day of Christmas my true love gave to me: "

        for j in range(i, 1, -1):
            string += f"{numbers[j - 1]} {gifts[len(gifts) - j]}, "
        if i > 1:
            string += "and "
        string += "a " + gifts[-1] + "."

        result.append(string)

    return result


print(recite(7, 8))
