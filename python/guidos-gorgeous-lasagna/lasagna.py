"""Guido's Gorgeous Lasagna Time Calculator."""

# Define Constants
EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_layers: int) -> int:
    """Calculate the time required to prepare the lasagna for baking.
    
    :param number_layers: int - final number of layers of pasta and fillings desired in lasagna.
    :return: int - time required to prepare lasagna for baking (in minutes) derived from 'num_layers'.

    Function that takes number of layers desired in the lasagna as an argument
    and returns how many minutes are expected to be required to prepare the 
    lasagna for baking based on 'TIME_PER_LAYER'. 
    """
    return num_layers * TIME_PER_LAYER


def elapsed_time_in_minutes(num_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total time elapsed since beginning cooking process.
    
    :param number_layers: int - final number of layers of pasta and fillings desired in lasagna.
    :param elapsed_bake_time: int - time current lasagna has been in the oven.
    :return: int - total time elapsed since beginning of cooking process
    
    Function that takes number of layers of lasagna and time it has been in the oven
    and returns how many minutes have elapsed since start of preparation process.
    calls function preparation_time_in_minutes().
    """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time