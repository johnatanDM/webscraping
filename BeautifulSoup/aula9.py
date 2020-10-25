from bs4.element import NavigableString, Tag
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

#print(soup.div.next_element.next_element)

#print(soup.li.previous_element.previous_element)
'''
for element in soup.ul.next_elements:
    if isinstance(element, Tag):
        print(element)
'''
for e in soup.li.previous_elements:
    print(repr(e))