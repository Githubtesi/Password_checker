# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/24

import string

password = "helloWorld"


def has_password_filter(pswd: str, pswd_filter: str) -> bool:
    l = []
    for c in pswd:
        result = 1 if c in pswd_filter else 0
        l.append(result)
    return any(l)


upper_case = has_password_filter(password, string.ascii_uppercase)
lower_case = has_password_filter(password, string.ascii_lowercase)
special = has_password_filter(password, string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
digits = has_password_filter(password, string.digits)

characters = [upper_case, lower_case, special, digits]
length = len(password)

score = 0

with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print('password was found in a common list.')
    exit()

