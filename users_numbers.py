from random import choice


class Numbers:

    def __init__(self, len_user: int):
        self.len_user = len_user
        self.numbers_list = self.get_numbers_list()

    def get_numbers_list(self) -> list:
        return [i for i in range(1, self.len_user + 1)]

    def get_number(self) -> int:
        number = choice(self.numbers_list)
        self.numbers_list.remove(number)
        return number
