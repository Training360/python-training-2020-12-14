from random import Random

from random_seed_demo import random_string


def test_random_string():
    assert random_string("xyz", 10, 20, Random(10)) == "xyyzxxyyyzxxzyyxxzy"