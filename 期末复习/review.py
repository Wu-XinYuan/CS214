import random


def init(file):
    f = open(file, "r", encoding="utf-8")
    probs = []
    hints = []
    comps = []  # 复杂度
    lines = f.readlines()
    i = 0
    flag = True
    comp = []
    prob = []
    hint = []
    while i < len(lines):
        while not lines[i].startswith('问题：'):
            comp += lines[i]
            i += 1
        if not flag:
            probs.append(prob)
            hints.append(hint)
            comps.append(comp)
        else:
            flag = False
        if i < len(lines):
            prob = lines[i][3:]
            i += 1
        while i < len(lines) and not lines[i].startswith('提示：'):
            prob += lines[i]
            i += 1
        if i < len(lines):
            hint = lines[i][3:]
            i += 1
        while i < len(lines) and not lines[i].startswith('复杂度：'):
            hint += lines[i]
            i += 1
        if i < len(lines):
            comp = lines[i][4:]
            i += 1
    return probs, hints, comps


if __name__ == '__main__':
    p, h, c = init('problems.txt')
    num = list(range(len(p)))
    print(len(p))
    random.shuffle(num)
    for n in num:
        print("问题：")
        input()
        print(p[n])
        print('提示：')
        input()
        print(h[n])
        print('复杂度：')
        input()
        print(c[n])
        input('\n\n')
