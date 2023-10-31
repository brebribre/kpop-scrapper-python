from requests_html import HTMLSession
import requests
import re


#   get all group relative links
def get_group_links():
    session = HTMLSession()
    response = session.get("https://kpopping.com/profiles/the-groups/men")

    hrefs = response.html.find(
        'div.container > div.row > div.col > div.indexes > div.box > div.index > div.items > div.item > a')

    group_links = []
    for a in hrefs:
        href = a.attrs['href']
        group_links.append(href)

    #   Girl Groups
    response = session.get("https://kpopping.com/profiles/the-groups/women")
    hrefs = response.html.find(
        'div.container > div.row > div.col > div.indexes > div.box > div.index > div.items > div.item > a')
    for a in hrefs:
        href = a.attrs['href']
        group_links.append(href)

    return group_links


def get_data_from_page(url):
    s = HTMLSession()
    site = "https://kpopping.com" + url
    r = s.get(site)

    #   get the image
    images = r.html.find(
        'body > div.container > div > div.col.overflow-hidden > div:nth-child(1) > figure > div'
    )
    image_url = images[0].attrs['data-bg']
    print(image_url)

    #   get group name
    group_name = r.html.find(
        'body > div.container > div > div.col.overflow-hidden > div:nth-child(1) > figure > figcaption > h1'
    )
    print(group_name[0].text)
    print("---------")

    #   get the members div block
    members = r.html.find(
        'body > div.container > div > div.col.overflow-hidden > div:nth-child(5) > div > div.summary.summary-only-one'
    )

    members_for_db = []
    for member in members:
        #   get the member data
        img = member.find('figure > a')
        name = member.find('section > h3 > a:nth-child(1)')
        native_name = member.find('section > h4 > p:nth-child(1)')
        birthday = member.find('section > div > div:nth-child(2) > a')
        position = member.find('section > div > div:nth-child(10)')
        #   birthplace
        birthplace = member.find('section > div > div:nth-child(6)')

        if bool(img):
            img = img[0].attrs['data-bg']

        if bool(name):
            name = name[0].text

        if bool(native_name):
            native_name = native_name[0].text

        if bool(name) & bool(native_name):
            trimmed_native_name = native_name.split(': ', 1)[1]
            complete_name = name + " " + trimmed_native_name
            name = complete_name

        if bool(birthday):
            birthday = birthday[0].text

        if bool(birthplace):
            birthplace_trimmed = re.sub(r'\s+', ' ', birthplace[0].text)
            birthplace = birthplace_trimmed

        if bool(position):
            position = position[0].text

        members_for_db.append({
            "name": name,
            "member_img_url": img,
            "birthday": birthday,
            "birthplace": birthplace,
            "positions": position
        })

    # create group object

def insert_group_in_db(data):
    base_url = "http://localhost:8000"
    # Send a POST request to the /group route with the data
    response = requests.post(f"{base_url}/group", json=data)

    # Check the response status code and handle it as needed
    if response.status_code == 201:
        print(f"Object sent successfully: {data}")
    else:
        print(f"Failed to send object: {data}")


group_links = get_group_links()
get_data_from_page(group_links[0])