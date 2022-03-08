import re

# 方法一：使用字符串的replace方法。


message = 'hello, world!'
print(message.replace('o', 'O').replace('l', 'L').replace('he', 'HE'))

# 方法二：使用正则表达式的sub方法。
message = 'hello, world!'
pattern = re.compile('[aeiou]')
print(pattern.sub('#', message))

filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
letter = re.compile('[a-z]+')
num = re.compile('\d+')
print(sorted(filenames, key=lambda x: (num.sub('',x.split('.')[0]), int(letter.sub('',x.split('.')[0])))))
