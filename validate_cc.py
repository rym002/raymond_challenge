import re
import sys

#Verifies the line matches  a pattern
=
formatted_num = re.compile(r'[4-6]\d{3}-?(\d{4}-?){3}')
has_repeat = re.compile(r"(\d)\1{3,}")
line_num=0
num_lines=0
for line in sys.stdin:
    if num_lines==0:
        num_lines=int(line)
    else:
        matched_format = formatted_num.match(line)
        if (matched_format is not None):
            line = line.replace('-','')
            match_repeat = has_repeat.search(line)
            if (match_repeat==None):
                print('Valid')                
            else:
                print('Invalid')
        else:
            print('Invalid')
        num_lines=num_lines-1
        if num_lines==0:
            break
