"""
A script to find out if there is numerical values in a list. Its a fcked up way to do it.
"""

def maybe_float(num):
    try:
        return int(num)
    except (ValueError, TypeError):
        try:
            return float(num)
        except (ValueError, TypeError):
            return num

lis = ['cat' ,'s-3-f','7390.19','12']
num_list = [maybe_float(v) for v in vals_]        
# print(lis,the_list)
if any( isinstance(x, int) or isinstance(x, float) for x in num_list):
    print('There are numerical vlaues in the list')
