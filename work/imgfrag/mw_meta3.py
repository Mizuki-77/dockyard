import sys, json
import midway_api as m

TITLES = [
 # --- 日军舰载机 ---
 "File:Kaga B5N Pearl Harbor departure.jpg",
 "File:Kaga B5N aircrew Pearl Harbor.jpg",
 "File:Kaga Type 3 fighter pilots.jpg",
 "File:96siki-kankou.jpg",
 "File:Japanese planes preparing-Pearl Harbor.jpg",
 "File:Soryu B5N1 1939.png",
 "File:Aichi D3A Replica Airshow.jpg",
 "File:GF in Indian Ocean, 1942.jpg",
 "File:Akagi Pearl Harbor Second Wave.jpg",
 "File:Zuikaku and Kaga and Akagi.jpg",
 "File:Zuikaku November 1941.jpg",
 # --- 美军舰载机 ---
 "File:TBD VT-8 taking off from USS Hornet (CV-8) May 1942.jpg",
 "File:TBD VT-8 taking off from USS Hornet (CV-8).jpg",
 "File:TBD on Enterprise elevator 1942.jpg",
 "File:TBDs on USS Enterprise (CV-6) during Battle of Midway.jpg",
 "File:Douglas TBD-1 Devastators of VT-6 are spotted for launch aboard USS Enterprise (CV-6) on 4 June 1942 (80-G-41686).jpg",
 "File:TBD T-5 VT-8 CV-8 15May42.jpg",
 "File:SBD 8-B-11 on USS Hornet Midway.jpg",
 "File:USS Hornet island SBD Midway.jpg",
 "File:SBD VB-8 over LSO USS Hornet 1942.jpg",
 "File:USS Hornet Air Group on deck May 1942.jpg",
 "File:Hornet Air Group morning take off 1942-06-04.jpg",
 "File:Douglas SBD-3 take off USS Hornet CV-8.jpg",
 "File:SBD-3 VS-5 on USS Yorktown Midway.jpg",
 "File:TBD sinking astern of USS Enterprise (CV-6) in May 1942.jpg",
 "File:F4F-4 wings folded.jpg",
 "File:Damaged Grumman F4F-3 Wildcat of VMF-221 on Midway, 24 June 1942 (80-G-11636).jpg",
 "File:F2As VMF-221 over Midway.jpg",
 "File:Brewster F2A-3 VMF-221 in flight 1941.jpg",
 # --- 人物 ---
 "File:Chuichi Nagumo.jpg",
 "File:Chuichi Nagumo in the bridge of Akagi heading to attack Pearl Harbor.jpg",
 "File:Chuichi Nagumo with the staff of the 1st Air Fleet.jpg",
 "File:NagumoSaipan.jpg",
 "File:Admiral Isoroku Yamamoto.jpg",
 "File:Isoroku Yamamoto on deck photo 1942.jpg",
 "File:Portrait of Yamamoto Isoroku.jpg",
 "File:Ray Spruance.jpg",
 "File:80-G-495845 Admiral Raymond A. Spruance.jpg",
 "File:Admiral Frank Jack Fletcher.jpg",
 "File:Adm Jack Fletcher.jpg",
 "File:TamonYamaguchi.jpg",
 "File:Last Moments of Admiral Yamaguchi.jpg",
 "File:Joichi Tomonaga.jpg",
 "File:Kaku Tomeo.jpg",
]

r = m.info(TITLES)
json.dump(r, open("_meta_mid_air.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(r))
