from random import randint


class RandomGame:

    @staticmethod
    def random_int(last_num: int) -> int:
        return randint(1, last_num)
