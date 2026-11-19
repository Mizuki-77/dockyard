import sys, json
import midway_api as m

TITLES = [
 # --- 加贺 ---
 "File:Japanese aircraft carrier kaga.jpg",
 "File:Japanese Navy Aircraft Carrier Kaga.jpg",
 "File:HIJMS Kaga.jpg",
 "File:Japanese.aircraft.carrier.kaga.jpg",
 "File:Kaga Reconstruction overhead.jpg",
 "File:Kaga air operations full deck 1937.jpg",
 "File:Kaga landing operations 1937.jpg",
 "File:Kaga China Incident.jpg",
 "File:Kaga and Zuikaku Pearl Harbor.jpg",
 "File:Kaga Pearl Harbor brief.jpg",
 "File:Kaga B5N Pearl Harbor.jpg",
 "File:Kaga Carrier Zero Fighters.jpg",
 # --- 苍龙 ---
 "File:Japanese aircraft carrier Soryu 1937.jpg",
 "File:Japanese aircraft carrier Soryu 1938.jpg",
 "File:Japanese aircraft carrier Soryu.jpg",
 "File:Japanese aircraft carrier Soryu 02.jpg",
 "File:Soryu 1937.jpg",
 "File:Launching Soryu.jpg",
 "File:Fantail Soryu.jpg",
 "File:Soryu landing test.jpg",
 # --- 飞龙 ---
 "File:Japanese aircraft carrier Hiryu 1939.jpg",
 "File:Japanese aircraft carrier Hiryu.jpg",
 "File:Japanese aircraft carrier hiryu.jpg",
 "File:Hiryu under construction.jpg",
 # --- 约克城 ---
 "File:USS Yorktown (CV-5) underway at Midway 1942.jpg",
 "File:USS Yorktown (CV-5) in a dry dock at the Pearl Harbor Naval Shipyard, 29 May 1942 (80-G-13065).jpg",
 "File:USS Yorktown (CV-5) entering Pearl Harbor May 1942.jpg",
 "File:USS Yorktown (CV-5) anchored in Hampton Roads on 30 October 1937.jpg",
 "File:USS Yorktown (CV-5) during the Battle of the Coral Sea, April 1942.jpg",
 "File:Overhead view of USS Yorktown (CV-5) in the Caribbean Sea on 17 January 1938.jpg",
 "File:80-CF-80301-1 USS Yorktown (CV-5).jpg",
 # --- 大黄蜂 ---
 "File:USS Hornet (CV-8) underway at sea in May 1942.jpg",
 "File:USS Hornet (CV-8) underway in the Southern Pacific on 15 May 1942 (80-G-14866).jpg",
 "File:Hornet (CV8). Aerial, port bow, underway, 10-27-1941 - NARA - 520816.jpg",
 "File:Aft view of USS Hornet (CV-8), circa in late 1941 (NH 81313).jpg",
 "File:USS Hornet (CV-8) steaming in the Coral Sea area on 13 May 1942.jpg",
 "File:USS Hornet (CV-8) entering Pearl Harbor, 26 May 1942.jpg",
]

r = m.info(TITLES)
json.dump(r, open("_meta_mid_ships.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(r))
