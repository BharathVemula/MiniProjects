limit = 0

def square_digits(number):
    result = 0
    for num in number:
        result += int(num)*int(num)
    return str(result)

def happy_number(number):
    global limit
    if number == "1":
        return 1
    if limit == 100:
        return 0
    limit+=1
    return happy_number(square_digits(number))

def main():
    import sys
    "test_cases = open(sys.argv[1], 'r')"
    test_cases = open("HappyNumberTest.txt", 'r')
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        if len(test) == 1:
            continue;
        number = test.strip();
        global limit
        limit = 0
        print happy_number(number)

    test_cases.close()

main()
