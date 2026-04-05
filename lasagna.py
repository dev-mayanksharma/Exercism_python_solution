"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Return the bake time remaining in minutes.
    
    :param elapsed_bake_time: int - bake time already elapsed.
    :return: int - remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return preparation time in minutes for given number of layers.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time in minutes.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed bake time in minutes.
    :return: int - total elapsed cooking time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time