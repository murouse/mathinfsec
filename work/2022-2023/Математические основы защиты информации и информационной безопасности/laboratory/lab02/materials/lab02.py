
# def mprint(matr):
#     for i in range(len(matr)):
#         for j in range(len(matr[i])):
#             print(f'{matr[i][j]:2}', end='')
#         print()
#     print()

def route_encryption(orig_string, pswd, n):
    string = orig_string.replace(' ','')
    m = len(string)//n+bool(len(string)%n)
    string += 'а'*(m*n-len(string))
    nums = [sorted(pswd).index(c) for c in pswd]
    return ''.join(string[j*n + nums.index(i)] for i in range(n) for j in range(m)).upper()    


def lattice_encryption(orig_string, pswd, k, xys):
    string = orig_string.replace(' ','')
    matr = []
    for i in range(k*2):
        matr.append(['.']*(k*2))

    u = 0
    for i in range(4):
        for x, y in xys:
            matr[x][y] = string[u]
            u+=1
        xys = [(y, 2*k-1-x) for x, y in xys]
        # mprint(matr)

    res = ''.join(''.join(c for c in matr[i]) for i in range(k*2))
    return route_encryption(res, pswd, 2*k)


def vigenere_encryption(orig_string, pswd):
    string = orig_string.replace(' ','')
    pswd = (pswd*(len(string)//len(pswd)+1))[:len(string)]
    alphabet = [chr(c) for c in range(ord('а'), ord('я') + 1)]
    matr = [alphabet[i:] + alphabet[0:i] for i in range(32)]
    # mprint(matr)
    return ''.join(matr[ord(s)-ord('а')][ord(p)-ord('а')] for p, s in zip(pswd, string)).upper()    


print(route_encryption('нельзя недооценивать противника', 'пароль', 6))

print(lattice_encryption('договор подписали', 'шифр', 2, [(0,3), (3,2), (2,3), (2,1)]))
print(lattice_encryption('ТЕКСТ ПОСЛЕ ШИФРОВАНИЯ СТАНЕТ НЕПОНЯТНЫМ', 'абвгде', 3, [(0,5), (4,0), (2,5), (5,1), (4,4), (1,2), (2,0), (3,4), (3,2)]))

print(vigenere_encryption('криптография серьезная наука', 'математика'))











