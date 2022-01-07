def troutspeak(inputstring):
    lis = []
    x=1
    for i in inputstring:
        x^=i.isalpha()
        lis.append((2*i).title()[x])
    return "".join(lis)

text = input("Please enter text:")

text = troutspeak(text)

print(text)
