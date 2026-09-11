test1 = 'PASS'
test2 = 'FAIL'
test3 = 'FAIL'
test4 = 'PASS'
test5 = 'PASS'

total_tests = 5
total_pass = 3
total_fail = 2

print('Total pass is ', total_pass)
print('Total Fail is ', total_fail)
print('Total tests are', total_tests)

pass_percentage = (total_pass/total_tests)* 100
print('Pass Percentage is', pass_percentage)

fail_percentage = (total_fail/total_tests) * 100
print('Fail Percentage is', fail_percentage)

