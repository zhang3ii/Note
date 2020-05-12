from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['spam'] = 3
d['grok'] = 4
d['bar'] = 2


for key in d:
    print(key,d[key])