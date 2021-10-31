"""
The included code stub will read an integer, 'n' , from STDIN.

Without using any string methods, try to print the following:
'123...n'

Note that '...' represents the consecutive values in between.

Example
n=5

Print the string 12345.

Input Format

The first line contains an integer n.

Constraints
 1 <= n <= 150

Output Format

Print the list of integers from 1 through n as a string, without spaces.
"""



from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    final_out = 0
    if n not in range(1, 151):
        sys.exit()
    else:
        for i in range(1, int(n)+1):
            if i < 10:
                final_out = final_out + (10**(int(n)-i) * i)
            elif i == 10:
                final_out = (final_out * 10 + (10**(int(n) - i) * i))
            elif i in range(10, 100):
                final_out = final_out * 10 + (10**(int(n)-i)* i)
            elif i in range(100, 151):
                final_out = final_out * 100 + (10**(int(n)-i)* i)
                
                                
    print(final_out)
