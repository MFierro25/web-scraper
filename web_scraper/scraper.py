import requests
from bs4 import BeautifulSoup


# topic that will be scraping is Seattle
URL = 'https://en.wikipedia.org/wiki/Seattle'
results = requests.get(URL)

# print(page.content)
soup = BeautifulSoup(results.content, 'html.parser')

# print(soup.prettify())

report = []

citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

def get_citations_needed_count():
    count = 0
    
    for citation in citations_needed:
        count += 1
    print(count)

print('The amount of citations needed is')

get_citations_needed_count()
    
def get_citations_needed_report():    
    for citation in citations_needed:
        parent = citation.find_parent('p')
    
    print(parent.prettify())
    
get_citations_needed_report()    