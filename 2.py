from sys import stdin, stdout

def CountPhonetics(s, l):
    rl = []
    for x in l:
        temp = x
        t = s
        c = 0
        for v in temp:
            if v in t:
                c += 1
                t = t.replace(v, "")
        if c > len(s) // 2:
            rl.append(temp)
    return rl

s = 'murthy'
lst = ['murthi', 'moorthy', 'moorthi', 'murti', 'murthee', 'martii', 'murthay']
print(CountPhonetics(s, lst))

