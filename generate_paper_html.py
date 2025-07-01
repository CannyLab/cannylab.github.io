"""
Download papers, and correctly format them as a table for our website
"""
from scholarly import scholarly
from tqdm import tqdm
import html

# Step 1: Search for the author by ID
author = scholarly.search_author_id('LAv0HTEAAAAJ')
author = scholarly.fill(author, sections=['publications'])

# Step 2: Sort publications by year (descending)
publications = sorted(author['publications'], key=lambda p: p.get('bib', {}).get('pub_year', '0'), reverse=True)

# Step 3: Write to HTML file
with open('papers_new.html', 'w', encoding='utf-8') as out_f:
    for pub in tqdm(publications[:20], desc="Processing papers"):  # Limit to most recent 20
        pub = scholarly.fill(pub)
        bib = pub.get('bib', {})
        title = html.escape(bib.get('title', ''))
        authors = html.escape(bib.get('author', ''))
        authors = authors.replace(' and ', ', ')
        year = bib.get('pub_year', '')
        citations = pub.get('num_citations', 0)
        paper_id = pub.get('pub_url', '')  # might be None
        link = pub.get('pub_url', '#')
        # import pdb; pdb.set_trace()
        # Use scholar link if available
        # if 'citation_id' in pub:
        #     citation_id = pub['citation_id']
        #     link = f"https://scholar.google.com/citations?view_op=view_citation&hl=en&user=LAv0HTEAAAAJ&citation_for_view={citation_id}"
        # else:
        #     link = bib.get('pub_url', '#')

        template = f"""<li>
    <h4 class="menu-item-name"><a href="{link}">{title}</a></h4>
    <span class="menu-item-price">({authors}, {year})</span>
    <br>
</li>
"""
        out_f.write(template)
