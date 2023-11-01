str_ = "python programming is so cool"

words = str_.split()
js = ""
for word in words:
    js += word[::-1] + " "
print(js)
