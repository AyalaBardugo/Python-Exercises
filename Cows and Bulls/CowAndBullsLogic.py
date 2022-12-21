import random
import re


class CowAndBullsLogic:
    def __init__(self):
        self.rand_num = str(self.rand_number())


def rand_number():
    number_range = 4
    rand_num = ""
    temp = ""
    rand_num = str(random.randint(0, 9))
    while len(rand_num) < number_range:
        temp = str(random.randint(0, 9))
        if temp not in rand_num:
            rand_num += temp
    return rand_num


def num_of_cows_and_bulls(self, input):
    cnt_cows = 0
    cnt_bulls = 0
    input_cnt = 0
    for char_self in self:
        input_cnt += 1
        self_cnt = 0
        for char_input in input:
            self_cnt += 1
            if char_self == char_input:
                if input_cnt == self_cnt:
                    cnt_bulls += 1
                else:
                    cnt_cows += 1

    message = "Bulls: " + str(cnt_bulls) + "  Cows: " + str(cnt_cows)
    return message


def checkInput(num):
    number_range = 4

    if num == " " or num is None or len(num) != number_range:
        return False

    if re.search('[a-zA-Z]', num):
        return False

    cnt = 0
    for i in num:
        cnt += 1
        if i in num[cnt:len(num)]:
            return False
    return True
