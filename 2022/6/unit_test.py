import pytest
import solution1

def  test_repeats():
    assert not solution1.has_repeats("abcd")
    assert solution1.has_repeats("aabc")
    assert solution1.has_repeats("abcc")
    assert solution1.has_repeats("abca")

def test_find_first():
    assert solution1.find_first_no_repeats("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert solution1.find_first_no_repeats("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert solution1.find_first_no_repeats("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert solution1.find_first_no_repeats("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    assert solution1.find_first_no_repeats("mjqjpqmgbljsphdztnvjfqwrcgsmlb", length=14) == 19
    assert solution1.find_first_no_repeats("bvwbjplbgvbhsrlpgdmjqwftvncz", length=14) == 23
    assert solution1.find_first_no_repeats("nppdvjthqldpwncqszvftbrmjlhg", length=14) == 23
    assert solution1.find_first_no_repeats("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", length=14) == 29
    assert solution1.find_first_no_repeats("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", length=14) == 26
