from typing import Optional
from random import randint

def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
    while True:
        try:
            num = int(input(input_string))
            if min_num and num <= min_num:
                print(f'Type number bigger than {min_num}!')
                continue
            return num
        except ValueError:
            print(" That's not a natural number.")


def random_list(listlen: int) -> list:
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-10, 10))
    return datalist

