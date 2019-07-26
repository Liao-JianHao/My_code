import re
str1 = 'faaasdfaaaaaasdfsdg'

print(re.sub(r'[^a][a]{3}[^a]', 'AAA', str1))
