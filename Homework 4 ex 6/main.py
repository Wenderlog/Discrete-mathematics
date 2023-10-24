def encode(s):
    buffer = ""
    d = {}
    res = []
    for i in s:
        if buffer + i in d:
            buffer += i
        else:
            res.append((d[buffer] if buffer in d else 0, i))
            d[buffer + i] = len(d) + 1
            buffer = ""
    if buffer != "":
        last = buffer[-1]
        buffer = buffer[:-1]
        res.append((d[buffer], last))
    return res

def decode(a):
    d = [""]
    res = ""
    for n in a:
        word = d[n[0]] + n[1]
        res += word
        d.append(word)
    return res

print(encode("Грибанов Кирилл Владимирович"))
