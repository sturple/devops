import feedparser
import urllib.parse
import urllib.request
import time
import json
import xmljson
import xml.etree.ElementTree as ET
import re


# finds what geo location it is in, and determines if meets criteria
def meets_geo_requirements(geoxml, locations):
    for g in geoxml:
        if 'location' in g.find('./valueName').text.lower():
            v = g.find('./value').text[0:1]
            if v != 'n' and v in locations:
                return True
    return False


# 4 - alberta, 5 - BC, 6 is terito
location = ['4', '5']

start = time.time()

# get main feed
output = feedparser.parse("http://rss.naad-adna.pelmorex.com")
json_list = []
count = 0
count_geo = 0
# get all the alerts from main feed.
for post in output.entries:
    alert = feedparser.parse(post.link)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
        'method': 'GET'
    }
    ++count
    try:
        # getting feed from url
        xml = urllib.request.Request(post.link, None, headers)
        with urllib.request.urlopen(xml) as response:
            raw_xml = re.sub(b' xmlns="[^"]+"', b'', response.read(), count=1)
            root = ET.fromstring(raw_xml)

            # this will be list to add to the final output if meets requirements.
            alertd = xmljson.yahoo.data(root)

            # pics out location
            if meets_geo_requirements(root.findall('.//geocode'), location):
                ++count_geo
                print(post.link)
                json_list.append(alertd)

    except urllib.error.HTTPError:
        print('Error')


end = time.time()
print("Process time for %s items, of which %s was added is %s seconds " % (count, count_geo, (end - start)))
json_list = {
    'status': 200,
    'date': end,
    'process_time': (end-start),
    'location': location,
    'data': json_list
}

# outputs the json in a data.json file
with open('/app/data/data.json', 'w') as outfile:
    json.dump(json_list, outfile)


