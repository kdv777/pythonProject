def lenargs(args):
    length = len(args)
    print("Argument Passed: ")
    for i in args:
        print(i)
    return length


x = lenargs('Rashi')
# x = lenargs('Rashi', 'Shub', 'Chris', 'Maricar')
print('Total NUmber of Args = {}'.format(x))