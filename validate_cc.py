# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

validator = re.compile(r'^(?!.*(\d)(-?\1){3})[4-6]\d{3}-?((\d){4}-?){3}$')
num_lines=0
for line in sys.stdin:
    if num_lines==0:
        num_lines=int(line)
    else:
        matched_format = validator.match(line)
        if (matched_format is not None):
            print('Valid')                
        else:
            print('Invalid')
        num_lines=num_lines-1
        if num_lines==0:
            break
