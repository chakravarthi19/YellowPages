# # for i in range(2, 101):
# #     is_prime = True
# #     for j in range(2, i):
# #         if (i % j) == 0:
# #             is_prime = False
# #             break
# #     if is_prime:
# #         print(i, end=" ")
# # print()
# #
# #
# # def is_prime_num(num):
# #     if num<=1:
# #         return False
# #     elif num <=3:
# #         return True
# #     elif num % 2 == 0 or num % 3 == 0:
# #         return False
# #     ii = 5
# #     while ii * ii <= num:
# #         if num % ii == 0 or num % 7 == 0:
# #             return False
# #         ii += 6
# #     return True
# #
# #
# # print(is_prime_num(1))
# # print(is_prime_num(7))
# # print(is_prime_num(9))
# # print(is_prime_num(76))
# # print(is_prime_num(11))
#
#
# for i in range(2, 101):
#     is_prime = True
#     for j in range(2, i):
#         if (i%j) == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i, end=" ")
#
# print()
# # palendrom or not
#
#
# def palendrom_num(n):
#     # print(str(n)[::-1])
#     if str(n) == str(n)[::-1]:
#         return f'{n} , it was palendrom number'
#     else:
#         return f'{n} , it was not a palendrom number'
#
#
# print(palendrom_num(11))
# print(palendrom_num(121))
# print(palendrom_num(12321))
# print(palendrom_num(1011))
#
#
# def fibnokii_num(n):
#     fib_series = [0, 1]
#     while len(fib_series) < n:
#         next_num = fib_series[-1]+fib_series[-2]
#         fib_series.append(next_num)
#     return fib_series
#
#
# print(fibnokii_num(10))
#
# aak = [0, 1]
# for ak in range(10):
#     if len(aak) < 10:
#         ne = aak[-1]+aak[-2]
#         aak.append(ne)
# print(aak)
#
#
#

for ii in str(len(123)):
    print(ii)