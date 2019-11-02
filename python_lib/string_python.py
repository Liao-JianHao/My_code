import string
from string import Formatter

# print(string.ascii_letters)
# # 下文所述 ascii_lowercase 和 ascii_uppercase 常量的拼连
#
# print(string.ascii_lowercase)
# # 小写字母 'abcdefghijklmnopqrstuvwxyz'
#
# print(string.ascii_uppercase)
# # 大写字母 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# print(string.digits)
# # 字符串 '0123456789'
#
# print(string.punctuation)
# # 标点符号的 ASCII 字符所组成的字符串: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
#
# print(string.printable)
# # 由 digits, ascii_letters, punctuation 和 whitespace 的总和

import datetime
d = datetime.datetime(2019, 11, 2, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

points = 19
total = 22
print('Correct answers: {:.2%}'.format(points / total))

coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))

print('{0}, {1}, {2}'.format('a', 'b', 'c'))