from aoc2019.models import GravityAssist


def test_day2_step1_t1():
    """
    1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
    """
    ga = GravityAssist(input='1,0,0,0,99')
    assert ga.compute() == '2,0,0,0,99'


def test_day2_step1_t2():
    """
    2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
    """
    ga = GravityAssist('2,3,0,3,99')
    assert ga.compute() == '2,3,0,6,99'


def test_day2_step1_t3():
    """
    2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    """
    ga = GravityAssist('2,4,4,5,99,0')
    assert ga.compute() == '2,4,4,5,99,9801'


def test_day2_step1_t4():
    """
    1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
    """
    ga = GravityAssist('1,1,1,4,99,5,6,0,99')
    assert ga.compute() == '30,1,1,4,2,5,6,0,99'
