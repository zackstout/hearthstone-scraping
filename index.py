
# Notes on https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/:

# re.match() -- only true if match is at beginning
# re.search() -- true no matter where the match is
# re.findall() -- returns array of all matches
# re.split() -- split into array on occurence of a character
# re.sub()
# re.compile()

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print result.group(0)

# To get all words:
result=re.findall(r'\w*','AV is largest Analytics community of India')

# to get rid of spaces from that list:
result=re.findall(r'\w+','AV is largest Analytics community of India')

# last word:
result=re.findall(r'\w+$','AV is largest Analytics community of India')

# FIRST WORD:
result=re.findall(r'^\w+','AV is largest Analytics community of India')

# Good page, has like six more examples.
