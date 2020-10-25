from bs4.element import NavigableString, Tag
from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

#print(soup.table.contents)
#print(type(soup.contents))
#print(len(soup.contents))

#print(soup.table.contents[1])

#print(soup.table.contents[1].span)
#print(soup.table.contents[1].span.string)
#print(soup.table.contents[3])
#print(soup.table.contents[3].td)
'''
for child in soup.table.contents:
    #print(child)
    if child.name == 'tr':
        print(child)
'''
#print(type(soup.children))
'''
for child in soup.footer.children:
    print(child)
'''
'''
for child in soup.footer.p.children:
    if child.name == 'a':
        print(child.get('href'))
'''

#print(len(list(soup.children)))
#print(len(list(soup.descendants)))

'''
for tag in soup.descendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else: 
        print(tag.name)
'''
'''
for tag in soup.descendants:
    if isinstance(tag, Tag):
        print(tag)
'''
'''
for string in soup.aside.strings:
    print(repr(string))
'''

for string in soup.aside.stripped_strings:
    print(repr(string))