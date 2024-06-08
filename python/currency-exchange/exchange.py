"""Functions for calculating steps in exchaning currency."""
def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate foreign currency worth of $US on hand.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate currency left after an exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate value of an arbitrary number of bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Caclulate number of bills that will be obtained from an arbitrary amount of money

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount / denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate leftover amount of money after exchanging for whole foreign bills

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: float, denomination: int) -> int:
    """Maximum value of forein bills you can obtain from an exchange taking into
    account exchange rate, denomination of bill requested and exchage fee.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: float - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_rate = exchange_rate + (exchange_rate * (spread / 100))
    num_bills = get_number_of_bills(exchange_money(budget, new_rate), denomination)

    return get_value_of_bills(num_bills, denomination)