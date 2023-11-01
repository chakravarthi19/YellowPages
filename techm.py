str_ = "my name is kalyan"
dict_ = {}
for i in str_:
    if i.isalpha():
        i = i.lower()
    if i != " ":
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1

print(dict_)
print(dict(sorted(dict_.items(), key=lambda item: item[1], reverse=True)))


def card_number(ca):
    if ' ' not in ca and '-' not in ca and len(ca) == 16:
        return f'{ca} "its valid number"'
    elif ' ' in ca:
        ca_ = ca.count(" ")
        if ca_ == 4 and len(ca) == 20:
            return f'{ca} "its valid number"'
        else:
            return f'{ca} "its invalid number"'
    elif "-" in ca and len(ca) == 20:
        ca_ = ca.count("-")
        if ca_ == 4:
            return f'{ca} "its valid number"'
        else:
            return f'{ca} "its invalid number"'
    elif ' ' in ca and '-' in ca:
        return f'{ca} "its invalid number"'
    else:
        return f'{ca} "not valid number"'


print(card_number("4454363614312111"))
# print(len("4454363614312111"))
print(card_number("4454 36361431 2111"))
print(card_number("4454-363614312111"))
print(card_number("4454 363614312111"))
print(card_number("4454 3636 1431 2111"))
print(card_number("4454-3636 1431-2111"))