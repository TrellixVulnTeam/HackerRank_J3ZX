n = input()
x = input.split(' ')
x = list(map(lambda s: int(s), x))
mean = float(sum(x))/len(x)
print(mean)
x.sort()
if n%2==0:
    pass