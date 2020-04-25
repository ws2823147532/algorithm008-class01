# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
#  1. 如果 n 是3的倍数，输出“Fizz”；
#
#  2. 如果 n 是5的倍数，输出“Buzz”；
#
#  3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
#
#  示例：
#
#  n = 15,
#
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
#
#


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fizzBuzz1(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res

    ## 使用加减法 优化 % 取余操作
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        f = 0
        for i in range(1, n + 1):
            f += 1
            if f == 15:
                res.append('FizzBuzz')
                f = 0
            elif f == 3 or f == 6 or f == 9 or f == 12:
                res.append('Fizz')
            elif f == 5 or f == 10:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res

# leetcode submit region end(Prohibit modification and deletion)
