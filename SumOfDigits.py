import sys
"test_cases = open(sys.argv[1], 'r')"
test_cases = open("SumOfDigitsTest.txt", 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    if len(test) == 1:
        continue;
    number = test.strip();
    result = 0;
    for num in number:
        result += int(num);
    print result

test_cases.close()
