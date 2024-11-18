import re

text = 'Hello_There(&V)'
se = 'Hello_There'
se_re = re.search(se + '\(&', text)
if se_re:
    print("Yes")
    print(se_re)
else:
    print("No")
