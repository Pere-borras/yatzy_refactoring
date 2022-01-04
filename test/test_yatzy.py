from src.yatzy import Yatzy
import pytest


@pytest.mark.test_chance
def test_chance():
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


@pytest.mark.test_yatzy
def test_yatzy():
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 2, 1)


@pytest.mark.test_ones
def test_ones():
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)
    assert 2 == Yatzy.ones(1, 5, 3, 2, 1)
    assert 3 == Yatzy.ones(1, 5, 1, 2, 1)


@pytest.mark.test_twoes
def test_twoes():
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
    assert 6 == Yatzy.twos(2, 3, 2, 2, 1)
    assert 2 == Yatzy.twos(2, 3, 1, 5, 1)


@pytest.mark.test_threes
def test_threes():
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)
    assert 12 == Yatzy.threes(3, 3, 3, 3, 5)
    assert 15 == Yatzy.threes(3, 3, 3, 3, 3)
    assert 3 == Yatzy.threes(3, 1, 1, 4, 5)


@pytest.mark.test_fours
def test_fours():
    assert 4 == Yatzy.fours(3, 3, 3, 4, 5)
    assert 8 == Yatzy.fours(4, 3, 3, 4, 5)
    assert 0 == Yatzy.fours(3, 3, 3, 2, 5)
    assert 12 == Yatzy.fours(3, 4, 4, 4, 5)


@pytest.mark.test_fives
def test_fives():
    assert 5 == Yatzy.fives(5, 1, 3, 4, 2)
    assert 20 == Yatzy.fives(5, 1, 5, 5, 5)
    assert 0 == Yatzy.fives(2, 1, 3, 4, 2)
    assert 15 == Yatzy.fives(5, 1, 5, 5, 2)


@pytest.mark.test_sixes
def test_sixes():
    assert 6 == Yatzy.sixes(6, 2, 3, 4, 5)
    assert 12 == Yatzy.sixes(6, 6, 3, 4, 5)
    assert 24 == Yatzy.sixes(6, 6, 3, 6, 6)
    assert 0 == Yatzy.sixes(3, 2, 3, 4, 5)


@pytest.mark.test_pair
def test_pair():
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)


@pytest.mark.test_two_pairs
def test_two_pairs():
    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)


@pytest.mark.test_three_of_a_kind
def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)


@pytest.mark.test_four_of_a_kind
def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)


@pytest.mark.test_small_straight
def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.small_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.small_straight(1, 2, 3, 4, 6)


@pytest.mark.test_large_straight
def test_large_straight():
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.large_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.large_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 6)


@pytest.mark.test_full_house
def test_full_house():
    assert 8 == Yatzy.full_house(1, 1, 2, 2, 2)
    assert 0 == Yatzy.full_house(2, 2, 3, 3, 4)
    assert 0 == Yatzy.full_house(4, 4, 4, 4, 4)
    assert 0 == Yatzy.full_house(4, 4, 4, 3, 4)
    assert 0 == Yatzy.full_house(2, 3, 3, 3, 4)
