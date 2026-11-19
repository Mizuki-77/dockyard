import sys, json, time
import midway_api as m

TITLES = [
 # --- 战役场景 ---
 "File:Air Attack on Japanese Carriers Kagi and Akagi, Midway Battle.jpg",
 "File:Kaga, Akagi and Soryu under attack.jpg",
 "File:Battle of Midway.jpg",
 "File:Japanese aircraft carrier Hiryu burning on 5 June 1942 (NH 73064).jpg",
 "File:Japanese aircraft carrier Hiryu adrift and burning on 5 June 1942 (NH 73065).jpg",
 "File:Japanese aircraft carrier Hiryu dodging bombs on 4 June 1942 (USAF-3725).jpg",
 "File:Japanese aircraft carrier Hiryu maneuvers to avoid bombs on 4 June 1942 (USAF-3725).jpg",
 "File:Aerial view of the Japanese aircraft carrier Sōryū evading an air attack on 4 June 1942 (fsa.8e00397).jpg",
 "File:Japanese aircraft carrier Sōryū underway during Battle of Midway on 4 June 1942.jpg",
 "File:Soryu-Midway.png",
 "File:Japanese cruiser Mikuma burning and sinking on 6 June 1942 (80-G-457861).jpg",
 "File:Japanese heavy cruiser Mikuma sinking on 6 June 1942 (80-G-414422).jpg",
 "File:Battle of Midway- Mikuma capsizing 88-188-ac.jpg",
 "File:88-188-ag.jpg",
 "File:SBD-3 Dauntless bombers of VS-8 over the burning Japanese cruiser Mikuma on 6 June 1942.jpg",
 "File:USS Yorktown (CV-5) burning after the first attack by Japanese dive bombers during the Battle of Midway on 4 June 1942.jpg",
 "File:USS Yorktown (CV-5) burning and listing on 4 June 1942.jpg",
 "File:USS Yorktown (CV-5) being abandonded, 4 June 1942.jpg",
 "File:USS Yorktown (CV-5) listing and abandoned on 4 June 1942.jpg",
 "File:USS Yorktown (CV-5) is hit by a torpedo on 4 June 1942.jpg",
 "File:Sinking of the USS Yorktown (CV-5) 01.jpg",
 "File:Sinking of the USS Yorktown (CV-5) 02.jpg",
 "File:USS Yorktown (CV-5) sinking, 7 June 1942.jpg",
 "File:Damaged USS Yorktown (CV-5) and Astoria (CA-34) at Midway 1942.jpg",
 "File:Flight deck of USS Yorktown (CV-5) after damage at Midway 1942.jpg",
 "File:Island of USS Yorktown (CV-5) after bomb hits during the Battle of Midway, 4 June 1942 (80-G-23978).jpg",
 "File:Survivors of Hiryu USNA 80 G 79974 1.jpg",
 "File:USS Hammann sinking 1942-06-06 seen from USS Yorktown.jpg",
 "File:USS Yorktown (CV-5) survivors aboard USS Benham (DD-397) on 4 June 1942 (80-G-32379).jpg",
 "File:USS Benham (DD-397) on 4 June 1942, with survivors of USS Yorktown (CV-5) on board (80-G-32390).jpg",
]

def run(titles, out):
    r = m.info(titles)
    json.dump(r, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", out, len(r))

run(TITLES, "_meta_mid_battle.json")
