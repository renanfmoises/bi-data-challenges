def multiplicator(max_speed, actual_speed):
    """
    Law (2): for every 10 km/h, the tax is doubled
    :param max_speed: int
    :param actual_speed: int
    :return: int
    """
    # Your code
<<<<<<< HEAD
    return 2 ** ((actual_speed - max_speed)//10)
=======
    pass
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35


def basic_tax(max_speed, actual_speed):
    """
    Law (1): 5€ for every km/h above the maximal speed (1), with a minimal tax of 12.5
    :param max_speed: int
    :param actual_speed: int
    :return: float
    """
<<<<<<< HEAD
    min_tax = 12.5
    if multiplicator(max_speed, actual_speed) * 5 < min_tax:
        return min_tax
    return multiplicator(max_speed, actual_speed) * 5
=======
    # Your code
    pass
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35



def total_tax(max_speed, actual_speed):
    """
    Overspeed -> basic fine x multiplicator of the fine
    Not -> return "no infraction committed"
    :param max_speed: int
    :param actual_speed: int
    :return: float or str
    """
    # Your code
    pass
