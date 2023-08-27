# my_map = {
#     3 : 'fizz',
#     5 : 'buzz',
#     7 : 'bazz'
# }

# for i in range(100):
#     text = ''
#     for key in my_map.keys():
#         if i % key == 0:
#             text += my_map[key]
#     if text != '':
#         print(text)
#     else:
#         print(i)
    
# Code Wars Exercises

# Check if number is a perfect square
def is_square(n):
    square = n**(.5)
    return int(square)**2 == n

# Return the 'highest achievable result'
# Note: the explanation on this problem was bad. :(
def expression_matter(a, b, c):
    return max(a*(b+c), a*b*c, a+b*c, (a+b)*c, a+b+c)

# Sort a given string. Each word in the string will contain a single number.
# The number will be the position of the word.
# Example "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
def order(sentence):
    sorted = ''
    if sentence == '':
        return sorted
    words = sentence.split(' ')
    for i in range(10):
        for word in words:
            if str(i) in word:
                sorted += f"{word} "
    return sorted.strip()
# print(order("is2 Thi1s T4est 3a"))

# Given a string, do something that looks like this:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# Note: Capitalize the first letter and repeat in lower case each letter
# until you reach the full length of the original string
def accum(s):
    final = []
    for i in range(len(s)):
        final.append(s[i].upper() + s[i].lower() * i)
    print("-".join(final))
accum('hello')