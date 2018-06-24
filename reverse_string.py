# -*- encoding: utf-8 -*-
import string
import random


# Python version:2.7.14
# 思路：用循环做，构建一个新的字符串，从末尾向头取字符串，每次取一个然后添加到后面。
def reverse_string_1(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result


# 思路：也是用循环，不能构造新的字符串，通过交换实现。(先把字符串转换成list，然后交换实现，最后再转换成字符串)
def reverse_string_2(s):
    list_data = list(s)
    len_string = len(s)

    for i in range(0, len(s)/2):
        # 为什么是len_string - 1 - i呢？左边是i，要保证两者之和是len_string-1。
        list_data[i], list_data[len_string - 1 - i] = list_data[len_string - 1 - i], list_data[i]

    new_string = "".join(list_data)

    return new_string


# 用来测试的已知函数
def reverse_str(s):
    return s[::-1]


# 产生随机字符串
def produce_random_string(min_len=1, max_len=100):
    random_string = ""

    letters = string.letters
    len_letters = len(letters)
    len_string = random.randint(min_len, max_len)

    for i in range(len_string):
        pos = random.randint(0, len_letters - 1)
        random_string += letters[pos]

    return random_string


def test_reverse_string(f, times=1000):
    for i in range(times):
        random_string = produce_random_string()
        assert(f(random_string) == reverse_str(random_string))

    print str(f.func_name) + " finished"


if __name__ == "__main__":
    test_reverse_string(reverse_string_1, 1000)
    test_reverse_string(reverse_string_2, 1000)
