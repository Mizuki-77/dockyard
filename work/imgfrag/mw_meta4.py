import sys, json, time, urllib.request, urllib.parse
import midway_api as m

EXTRA = [
 "File:Mogami & Nichiei Maru after Midway.jpg",
 "File:Japanese cruiser Mikuma burning with DD 1942.jpg",
 "File:Japanese cruiser Mikuma dead in water 1942.jpg",
 "File:USS Hammann alongside USS Yorktown-both torpedoed.jpg",
 "File:USS Hammann DD-412 sunk-depth charges exploding near Yorktown.jpg",
 "File:Japanese B5N2 shot down near USS Yorktown (CV-5) in June 1942.jpg",
 "File:B5Ns attacking USS Yorktown (CV-5) at Midway 1942.jpg",
 "File:Japanese torpedo bombers fly past USS Yorktown (CV-5) on 4 June 1942.jpg",
 "File:Battle of Midway (Japanese air raid).jpg",
 "File:G17056 Oil tanks burn at Midway after japanese attack 4 june 1942.jpg",
 "File:Eastern Island Midway under attack 1942.jpg",
 "File:Memorial service on Midway after battle 1942.jpg",
 "File:PBY sights Japanese minesweepers en route to Midway on 3 June 1942.jpg",
]

r = m.info(EXTRA)
json.dump(r, open("_meta_mid_extra.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(r))
