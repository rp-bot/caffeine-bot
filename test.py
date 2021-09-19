import re

str = ["djhfksdjhg = 'dsjhf'\n"]

str[0] = re.sub(r"(?<=\')(.*?)(?=\')", 'name',str[0])
print(str[0])