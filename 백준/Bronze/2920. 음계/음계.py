import sys

dict = {
    '12345678': 'ascending',
    '87654321': 'descending'
}

scale = ''.join(sys.stdin.readline().split())

if scale in dict.keys():
    print(dict[scale])
else:
    print('mixed')
