def gamm(text, gamma):
    numbers = lambda text: [ord(i)-ord('А')+1 for i in text.upper().replace(' ','')]
    letters = lambda nums: ''.join(chr(i+ord('А')-1) for i in nums)

    text = numbers(text)
    gamma = numbers(gamma)
    gamma = gamma*(len(text)//len(gamma)+1)

    return letters([(t+g)%33 for t, g in zip(text, gamma)])

print(gamm('ПРИКАЗ', 'ГАММА'))
print(gamm('радиотехника', 'шифр'))