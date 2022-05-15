import os

dir(os)

len(dir(os))

for item in dir(os):
    print('os.' + item, eval('os.' + item))
