# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/24

import string

password = "ADTAjfldsajkf$jklfsdalk13"


# password = "123456"


def has_password_filter(pswd: str, pswd_filter: str) -> bool:
    l = []
    for c in pswd:
        result = 1 if c in pswd_filter else 0
        l.append(result)
    return any(l)


# 大文字、小文字、特殊文字、数字
upper_case = has_password_filter(password, string.ascii_uppercase)
lower_case = has_password_filter(password, string.ascii_lowercase)
special = has_password_filter(password, string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
digits = has_password_filter(password, string.digits)

characters = [upper_case, lower_case, special, digits]
length = len(password)

# パスワード強度
score = 0

# 脆弱性のあるパスワード
with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print('password was found in a common list.')
    exit()

# パスワードの長さ
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Password has is {str(sum(characters))} different character types, adding {str(sum(characters)-1)} points!")

if score < 4:
    print(f"The password is quite weak! Score: {str(score)} / 7")
if score == 4:
    print(f"The password is ok! Score: {str(score)} / 7")
if 4 < score and score < 6:
    print(f"The password is pretty good! Score: {str(score)} / 7")
if 6 <= score:
    print(f"The password is strong! Score: {str(score)} / 7")
