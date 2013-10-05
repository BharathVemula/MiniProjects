import sys
"test_cases = open(sys.argv[1], 'r')"
test_cases = open("UniqueElementsTest.txt", 'r')
for test in test_cases:
    if len(test) == 1:
        continue
    numbers = test.strip().split(',')
    results = []
    for num in numbers:
        if num in results:
            continue
        else:
            results.append(num)
    print ','.join(results)

test_cases.close()

        
