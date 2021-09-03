EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_time):
    """
    Return remaining bake time

    This function takes actual minutes the lasagna
    has been in the oven as an argument and returns
    how many minutes the lasagna still needs to bake
    """
    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(layers_count):
    """
    Return preparation time

    This function takes the number of layers you want
    to add to the lasagna as an argument and returns
    how many minutes you would spend making them
    """
    return layers_count * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_time):
    """
    Return total number of minutes you spent cooking
    """
    return elapsed_time + number_of_layers * PREPARATION_TIME
