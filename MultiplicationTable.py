
def multiplicationTable():
    for row in range(1,13):
        s = '';
        for col in range(1,13):
            num = row*col;
            s = s + '{:>4}'.format(num);
        print s.lstrip();

multiplicationTable();
