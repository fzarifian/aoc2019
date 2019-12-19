from aoc2019.models import Spaceship, SpaceshipModule, round_down


def get_fuel_module_requirement(answer):
    spaceship = Spaceship()
    module = SpaceshipModule(weight=answer)
    spaceship.add_module(module=module)
    return spaceship


def test_day1_round_down():
    """
    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    """
    result = round_down(2.5)
    assert result == 2


def test_day1_step1_test1():
    """
    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    """
    spaceship = get_fuel_module_requirement(12)
    assert spaceship.fuel_modules_requirements == 2


def test_day1_step1_test2():
    """
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    """
    spaceship = get_fuel_module_requirement(14)
    assert spaceship.fuel_modules_requirements == 2


def test_day1_step1_test3():
    """
    For a mass of 1969, the fuel required is 654.
    """
    spaceship = get_fuel_module_requirement(1969)
    assert spaceship.fuel_modules_requirements == 654


def test_day1_step1_test4():
    """
    For a mass of 100756, the fuel required is 33583.
    """
    spaceship = get_fuel_module_requirement(100756)
    assert spaceship.fuel_modules_requirements == 33583


def test_day1_step2_test1():
    """
    A module of mass 14 requires 2 fuel.
    This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel),
    so the total fuel required is still just 2.
    """
    spaceship = get_fuel_module_requirement(14)
    assert spaceship.fuel_requirements == 2


def test_day1_step2_test2():
    """
    At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
    216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
    So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
    """
    spaceship = get_fuel_module_requirement(1969)
    assert spaceship.fuel_modules_requirements == 654
    assert spaceship.fuel_requirements == 966


def test_day1_step2_test3():
    """
    The fuel required by a module of mass 100756 and its fuel is:
    33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
    """
    spaceship = get_fuel_module_requirement(100756)
    assert spaceship.fuel_requirements == 50346
