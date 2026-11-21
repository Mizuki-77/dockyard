import io
import json
import urllib.parse
import urllib.request

UA = 'DockyardArchive/1.0 (historical research)'
title = 'File:"Tirpitz" i Fættenfjorden (17301883111).jpg'
u = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode({
    'action': 'query', 'titles': title, 'prop': 'imageinfo',
    'iiprop': 'url|size', 'iiurlwidth': '1280', 'format': 'json'})
d = json.loads(urllib.request.urlopen(
    urllib.request.Request(u, headers={'User-Agent': UA}), timeout=30
).read().decode('utf-8'))
for p in d['query']['pages'].values():
    ii = (p.get('imageinfo') or [{}])[0]
    print('thumb:', ii.get('thumburl'))
    print('size :', ii.get('width'), 'x', ii.get('height'))
