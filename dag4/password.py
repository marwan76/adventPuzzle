passPhrase = 0
for pwd in range(402328, 864247+1):
    digits = [int(x) for x in str(pwd)]
    pair = any([digits[i] == digits[i+1] for i in range(len(digits)-1)])
    dec = any([digits[i] > digits[i+1] for i in range(len(digits)-1)])

    if pair and not dec:
        passPhrase += 1
print(passPhrase)
