text = input()  # ввод текста
alf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf1 = 'abcdefghijklmnopqrstuvwxyz'
alf2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
slog = text.split()
for i in range(len(slog)):
    z = slog[i]
    y = 0
    for j in range(len(z)):
        if z[j] in alf:
            y += 1
    step = y

    x = ''
    for i in range(len(z)):
        if z[i] in alf2:
            for j in range(len(alf2)):
                if z[i] == alf2[j]:
                    if j + step < len(alf2):
                        x += alf2[j + step]
                    elif j + step > len(alf2):
                        x += alf2[j + step - len(alf2)]
                    elif j + step == len(alf2):
                        x += alf2[0]
        if z[i] in alf1:
            for j in range(len(alf1)):
                if z[i] == alf1[j]:
                    if j + step < len(alf1):
                        x += alf1[j + step]
                    elif j + step > len(alf1):
                        x += alf1[j + step - len(alf1)]
                    elif j + step == len(alf1):
                        x += alf1[0]

        elif z[i] not in alf1 and z[i] not in alf2:
            x += z[i]
    print(x, end=' ')