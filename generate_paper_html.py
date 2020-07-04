"""
Download papers, and correctly format them as a table for our website
"""

import requests
import bs4

data = requests.get('https://scholar.google.com/citations?user=LAv0HTEAAAAJ&view_op=list_works&sortby=pubdate&pagesize=20&json')
raw_html = data.json()['B']

soup = bs4.BeautifulSoup(raw_html, 'html.parser')

with open('papers.html', 'w') as out_f:
    for elem in soup.find_all('tr'):

        title = elem.find(class_='gsc_a_at').text
        authors = elem.find(class_='gs_gray').text
        citations = elem.find(class_='gsc_a_ac').text
        year = elem.find(class_='gsc_a_h').text
        paper_id = elem.find(class_='gsc_a_at')['data-href'].split('&')[-1].split('=')[-1].replace(':', '%3A')
        link = 'https://scholar.google.com/citations?user=LAv0HTEAAAAJ#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3DLAv0HTEAAAAJ%26citation_for_view%3D{}%26tzom%3D420'.format(paper_id)

        template = """<li>
    <h4 class="menu-item-name"><a href={}>{}</a></h4>
    <span class="menu-item-price">({}, {})</span>
    <br>
</li>
""".format(link, title, authors, year)

        out_f.write(template)

