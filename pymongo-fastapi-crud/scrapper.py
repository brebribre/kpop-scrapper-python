from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://kpopping.com/profiles/the-groups/men")


hrefs = r.html.find('div.container > div.row > div.col > div.indexes > div.box > div.index > div.items > div.item > a')


href_attrs = [a.attrs['href'] for a in hrefs]
#   get all group relative links
group_links = []
for a in hrefs:
    href = a.attrs['href']
    group_links.append(href)



