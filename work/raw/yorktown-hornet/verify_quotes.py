import sys, os, re, io, unicodedata
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"D:\deepseek harness\website-warships\work\raw"
YH = os.path.join(BASE, "yorktown-hornet")
EN = os.path.join(BASE, "enterprise")

def load(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

SRC = {}
def add(key, *paths):
    txt = "\n".join(load(p) for p in paths if os.path.exists(p))
    SRC[key] = txt

add("S1", os.path.join(YH, "danfs-yorktown-iii.txt"))
add("S2", os.path.join(YH, "danfs-hornet-vii.txt"))
add("S3", os.path.join(YH, "ibiblio-danfs-cv5.txt"))
add("S4", os.path.join(YH, "ibiblio-danfs-cv8.txt"))
add("S5", os.path.join(YH, "ar-yorktown-midway.txt"))
add("S6", os.path.join(YH, "ar-hornet-midway.txt"))
add("S7", os.path.join(YH, "ar-tf16.txt"))
add("S8", os.path.join(YH, "pdf", "wdr25-yorktown-midway.txt"))
add("S9", os.path.join(EN, "nhhc-composition.txt"))
add("S10", os.path.join(YH, "navsource-cv5.txt"), os.path.join(YH, "navsource-cv8.txt"))
add("S11", os.path.join(YH, "navsource-cv5.txt"), os.path.join(YH, "navsource-cv8.txt"))
add("S12", os.path.join(YH, "arch-ns-cv5.txt"), os.path.join(YH, "arch-ns-cv8.txt"))
add("S13", os.path.join(YH, "wiki-cv5.txt"))
add("S14", os.path.join(YH, "wiki-cv8.txt"))
add("S15", os.path.join(EN, "navypedia-yorktown.txt"))
add("S16", os.path.join(EN, "navweaps-5in38.txt"))
add("S17", os.path.join(EN, "navweaps-40mm.txt"))
add("S18", os.path.join(EN, "navweaps-20mm.txt"))
add("S19", os.path.join(EN, "navweaps-11in75.txt"))
add("S20", os.path.join(EN, "shipcamo-usn_cv.txt"), os.path.join(YH, "ms12.txt"))
add("S21", os.path.join(YH, "nhhc-hornet-cv8.txt"), os.path.join(YH, "nhhc-cv5-aircraft-carriers.txt"))
add("S22", os.path.join(YH, "cf-i168.txt"))
add("S23", os.path.join(YH, "dmn-repair2.txt"))
add("S25", os.path.join(YH, "nhhc-coral-topic.txt"))
add("S26", os.path.join(YH, "wdr-index.txt"), os.path.join(YH, "wdr-index.html"))
add("E-S7", os.path.join(EN, "wiki-yorktown-class.txt"))

def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "--").replace("\u2013", "-")
    s = s.replace("**", "")          # markdown emphasis inside quotes
    s = s.replace("▶", " | ")        # table cell separator convention
    s = re.sub(r"\s+", " ", s)
    return s

def find(quote, key):
    hay = norm(SRC.get(key, ""))
    q = norm(quote)
    return q in hay

# (source_key, quote) pairs harvested from the report
CHECKS = [
 ("S1", "Yorktown III (CV-5)"),
 ("S1", "The third Yorktown (CV-5) was laid down on 21 May 1934 at Newport News, Va., by the Newport News Shipbuilding and Drydock Co.; launched on 4 April 1936; sponsored by Mrs. Franklin D. Roosevelt; and commissioned at the Naval Operating Base (NOB), Norfolk, Va., on 30 September 1937, Capt. Ernest D. McWhorter in command."),
 ("S1", "length 809'6\""),
 ("S1", "beam 83'1\""),
 ("S1", "draft 28'0\""),
 ("S1", "complement 2,919"),
 ("S1", "Yorktown departed Norfolk on 16 December 1941 and sailed for the Pacific, her secondary gun galleries studded with new 20-millimeter Oerlikon machine guns."),
 ("S1", "the carrier dodged eight torpedoes. Attacked then by \"Vals,\" the ship managed to evade all but one bomb. That one, however, penetrated the flight deck and exploded belowdecks, killing or seriously injuring 66 men."),
 ("S1", "at least three months in a yard"),
 ("S1", "Yorktown, too, received orders to return to Hawaii; and she arrived at Pearl Harbor on 27 May."),
 ("S1", "the Japanese submarine I-158 had achieved a favorable firing position"),
 ("S1", "the Japanese submarine I-158 had achieved a favorable firing position"),
 ("S1", "Two torpedoes struck Yorktown just below the turn of the bilge at the after end of the island structure."),
 ("S2", "Hornet VII (CV-8)"),
 ("S2", "length 809'9\""),
 ("S2", "extreme width (flight deck) 114'0\""),
 ("S2", "displacement 19,800"),
 ("S2", "class Yorktown"),
 ("S2", "The seventh Hornet (CV-8) was laid down on 25 September 1939 at Newport News, Va., by Newport News Shipbuilding & Dry Dock Co.; launched on 14 December 1940; sponsored by Mrs. William F. Knox, wife of Secretary of the Navy Frank Knox; and commissioned on 20 October 1941 at the Naval Operating Base (NOB), Norfolk, Va., Capt. Marc A. Mitscher in command."),
 ("S2", "removed her catapults"),
 ("S2", "the SC-1 radar being re-located to the mainmast"),
 ("S2", "where she received a fifth 1.1-inch mount at the bow, replacing the two 20-millimeter mounts"),
 ("S2", "The first squadron to locate the Japanese, Torpedo Eight attacked without hesitation, and one by one, the squadron's Devastators splashed into the unyielding ocean"),
 ("S2", "he was the least seasoned, having had no combat experience whatsoever"),
 ("S2", "his machine guns to rake the after part of Hornet's island, killing five men and wounding 20"),
 ("S2", "Hornet was stricken from the Naval Register on 13 January 1943."),
 ("S2", "Wasp's loss rendered Hornet the only operable U.S. fleet carrier in the theater."),
 ("S2", "Hornet's ship's company had suffered six officers and 70 men killed in action, as well as 15 marines from the ship's Marine Detachment."),
 ("S3", "a. 8 5\", 22 .50-cal mg."),
 ("S4", "The seventh Hornet (CV-8) was launched 14 December 1940"),
 ("S4", "a. 8 5\", 16 1.1 mg., cl. Hornet"),
 ("S4", "ew. 144'"),
 ("S4", "cpl. 1,889"),
 ("S4", "At 0135, 27 October 1942, she finally sank off the Santa Cruz Islands. Her proud name was struck from the Navy List 13 January 1943."),
 ("S4", "She still floated after receiving nine torpedoes and more than 400 rounds of 5-inch shellfire"),
 ("S4", "a gale of more than 40 knots churned the sea with 30-foot crests"),
 ("S4", "The lead plane, commanded by Colonel Doolittle, had but 467 feet of flight deck"),
 ("S4", "she loaded 16 Army B-25 bombers on the flight deck. Under the command of Lieutenant Colonel James H. Doolittle 70 officers and 64 enlisted men reported aboard."),
 ("S4", "By 0920 all 16 of the bombers were airborne"),
 ("S4", "Their sacrifices drew enemy fighters away from dive bombers of Enterprise and Yorktown"),
 ("S5", "The bomb from this plane tumbled in flight and hit just abaft No. 2 elevator on the starboard side"),
 ("S5", "At about 1620 a torpedo hit on the port side at approximately frame 90"),
 ("S5", "At about 1536 a salvo of four torpedoes was seen to be approaching the ship on the starboard beam"),
 ("S5", "the Commanding Officer with 29 selected officers and 141 enlisted men returned aboard Yorktown"),
 ("S5", "About 0530 on the morning of June 7 the list of the Yorktown was noticed to be rapidly increasing to port and, at 0701, Yorktown turned over on her port side and sank in about 3000 fathoms of water with all battle flags flying."),
 ("S5", "This bomb exploded in the stack, and heavy black smoke soon covered the after director, the after starboard automatic gun batteries and Group III 5\" guns."),
 ("S5", "Her position at the time of sinking was Latitude 30°-46' North, Longitude 167°-24' West."),
 ("S5", "(10-20 mm, 4-1.1 mounts, 12-50 caliber, 2-30 caliber)"),
 ("S5", "(e) Replacement of 5\"38 caliber guns, 1.1\" guns and 50 caliber machine guns, by a large number of 40mm automatic guns."),
 ("S5", "This bomb exploded in the stack, and heavy black smoke soon covered the after director, the after starboard automatic gun batteries and Group III 5\" guns."),
 ("S5", "The forward director took control of the starboard 5\" battery and opened fire on these planes."),
 ("S5", "Gun remained out of commission."),
 ("S5", "The repairs made to damage received by the Radar and YE antennas in the battle of the Coral Sea stood up very well during the bombing attack, and both Radar and YE continued to function until the torpedo attack."),
 ("S5", "At about 1359, while fueling the fighters which had turned on board, Radar detected and enemy attack group coming in from a bearing about 250° true, distance 46 miles."),
 ("S5", "low altitude to avoid Radar detection until they were within 40-50 miles"),
 ("S5", "U.S.S. Vireo had a tow line to the ship"),
 ("S6", "the Hornet got underway from Pearl Harbor at 1130, May 28, 1942"),
 ("S6", "all times given hereafter are zone plus 10"),
 ("S6", "None of Scouting 8 or Bombing 8 made contact with the enemy on the above flight."),
 ("S6", "As it turned out, had they turned north, contact would probably have been made."),
 ("S6", "Torpedo 8, led by Lieutenant Commander John C. Waldron, U.S.N., was lost in its entirety."),
 ("S6", "The air Group then consisted of 27 VF, 35 VSB, and 15 VTB"),
 ("S6", "15 TBD on 4 June (1 pilot rescued)."),
 ("S6", "Thirteen planes of Bombing 8 landed at Midway due to lack of gas"),
 ("S7", "Except for the Hornet dive bombers failing to find the target on the forenoon of 4 June, all operations were conducted approximately as intended"),
 ("S7", "Where discrepancies exist between Enterprise and Hornet reports, the Enterprise report should be taken as the more accurate."),
 ("S8", "The port anchor was cast loose and dropped overboard, five port side 20mm gun mounts were dropped overboard"),
 ("S9", "25 Grumman F4F-4 (Wildcat)"),
 ("S9", "17 Douglas SBD-3 (Dauntless)"),
 ("S9", "16 Douglas SBD-3 (Dauntless)"),
 ("S9", "12 Douglas TBD-1 (Devastator)"),
 ("S9", "27 Grumman F4F-4 (Wildcat)"),
 ("S9", "19 Douglas SBD-3 (Dauntless)"),
 ("S9", "15 Douglas SBD-1, SBD-2, and SBD-3 (Dauntless)"),
 ("S9", "15 Douglas TBD-1 (Devastator)"),
 ("S9", "torpedoed by Japanese submarine I-168 on 6 June 1942"),
 ("S10", "Ordered ▶ "),
 ("S10", "Builder: Newport News Shipbuilding & Drydock Co., Newport News, Va."),
 ("S10", "Fate: Disabled by Japanese carrier aircraft bombs and"),
 ("S10", "Displacement: | 19,800 tons standard; 25,500 tons full load"),
 ("S10", "Displacement: | 19,900 tons standard; 25,600 tons full load"),
 ("S10", "Dimensions (wl): | 770' x 83' 3\" x 25' 11"),
 ("S10", "Dimensions (max.): | 824' 9\" x 109' 6"),
 ("S10", "Power plant: | 9 boilers (400 psi); steam turbines; 4 shafts; 120,000 shp"),
 ("S10", "Armament: | 8 single 5\"/38 gun mounts; 4 quad 1.1\"/75 machine gun mounts; 24 .50-cal machine guns"),
 ("S10", "flight deck: 802' x 86' [244.4 x 26.2 m]"),
 ("S10", "flight deck: 814' x 86' [248.1 x 26.2 m]"),
 ("S10", "Crew: | 2,217 (ship's company + air wing) (1941 figure)"),
 ("S10", "Crew: | 2,919 (ship's company + air wing) (wartime figure)"),
 ("S10", "Armor: | 4\"-2.5\" belt; 60 lbs protective deck(s); 4\" bulkheads; 4\" (side)-2\" (top) conning tower; 4\" (side) over steering gear"),
 ("S10", "Aircraft: | 90+"),
 ("S10", "Yorktown (modified) Class Aircraft Carrier"),
 ("S10", "Named to commemorate six American warships which had previously"),
 ("S10", "Authorized under the Naval Expansion Act of 17 May 1938."),
 ("S10", "Named after a town in Virginia, where the climactic battle of the"),
 ("S10", "Authorized under the National Industrial Recovery Act of 16 June 1933."),
 ("S10", "Hit and immobilized by Japanese carrier air"),
 ("S10", "Cruiser USS Northampton"),
 ("S10", "3 elevators (48' x 44' [14.6 x 13.4 m]), 17,000 pounds [7,711.1 kg]"),
 ("S10", "2 flight-deck and 1 hangar-deck hydraulic catapults"),
 ("S10", "One hundred and eleven of her crew were lost with the ship and remain on active duty."),
 ("S10", "The wreckage of Hornet was found in January 2019"),
 ("S11", "Armament and radar had yet"),
 ("S11", "SC radar antenna installed"),
 ("S11", "Mk-4 (FD) radar on forward Mk-37 director"),
 ("S11", "Mk.37 directors on the island differentiated"),
 ("S11", "USS Hornet just after commissioning, 20 October 1941. She was painted in"),
 ("S11", "Measure 12 camouflage. Armament and radar had yet to be fitted."),
 ("S11", "Measure 12 camouflage she brought from the Atlantic is still intact"),
 ("S11", "fake bow wave (Measure 5)"),
 ("S11", "Measure 12 (Modified)"),
 ("S11", "20mm guns were fitted when the ship was at Norfolk Navy Yard in December 1941."),
 ("S11", "The CXAM radar antenna is in the \"down\" position"),
 ("S11", "large \"Y\" painted on her stack"),
 ("S11", "The hull number (5) has not yet been painted on her side"),
 ("S11", "Measure 12, Graded System, camouflage that Yorktown received in late 1941"),
 ("S11", "white stripes"),
 ("S12", "chrome yellow flight deck markings"),
 ("S12", "761' x 83.25'"),
 ("S12", "Dimensions (max.): 824.75' x 114'"),
 ("S13", "Yorktown was found and photographed by oceanographer Dr. Robert Ballard"),
 ("S13", "The wreck of Yorktown, 3 miles (5 km) deep, was sitting upright in excellent condition."),
 ("S13", "24 × 20mm Oerlikon guns"),
 ("S13", "CXAM radar from 1940"),
 ("S14", "the conning tower had splinter protection only, in contrast with her sisters' 4 in (100 mm) armor on the sides with 2 in (51 mm) on top."),
 ("S14", "The steering gear had 4 in (100 mm) protection on the sides with splinter protection on the deck."),
 ("S14", "The flight and hangar decks were unarmored"),
 ("S14", "Hornet had an armor belt that was 2.5"),
 ("S14", "She was designed to host a carrier air group of 18 fighters, 18 bombers, 37 scout planes, 18 torpedo bombers, and six utility aircraft."),
 ("S14", "In June 1942, following the battle of Midway, Hornet had a new CXAM radar installed atop her tripod mast"),
 ("S14", "Unlike her sisters, Hornet's tripod mast and its signal bridge were not enclosed when the CXAM was installed, making her unique among the three ships."),
 ("S14", "She was designed for a ship's crew consisting of 86 officers and 1,280 men and an air complement consisting of 141 officers and 710 men."),
 ("S14", "She was designed to carry 4,280 long tons (4,350 t) of fuel oil and 178,000 US gallons (670,000 L) of aviation fuel (avgas)."),
 ("S14", "During sea trials, she produced 120,500 shp (89,900 kW) and reached 33.85 knots (62.69 km/h; 38.95 mph)."),
 ("S14", "four Parsons Marine geared steam turbines, each driving its own propeller"),
 ("S14", "nine Babcock & Wilcox boilers providing steam at 400 psi (2,800 kPa) and 648"),
 ("S14", "She had two flight-deck and one hangar-deck hydraulic catapults"),
 ("S14", "Her flight deck was 814 ft × 86 ft (248 m × 26 m)"),
 ("S14", "her hangar deck was 546 ft × 63 ft (166 m × 19 m) and 17 ft 3 in (5.26 m) high"),
 ("S14", "three aircraft elevators, each 48 by 44 feet (15 by 13 m) with a lifting capacity of 17,000 lb (7,700 kg)"),
 ("S14", "She had two flight-deck and one hangar-deck hydraulic catapults equipped with the Mark IV Mod 3A arresting gear"),
 ("S14", "20,000 long tons (20,321 t) (standard)"),
 ("S14", "25,500 long tons (25,909 t) (full load)"),
 ("S14", "a beam of 83 ft 3 in (25.37 m) at the waterline"),
 ("S14", "114 ft (35 m) (overall)"),
 ("S14", "770 feet (235 m) at the waterline"),
 ("S14", "Originally, she had 24 M2 Browning"),
 ("S14", "An additional 1.1-inch (28 mm) quad mount was added later at her bow and two more 20 mm AA guns were added for a total of 32 mounts."),
 ("S14", "At 01:35 on 27 October, Hornet finally capsized to starboard and sank, stern first"),
 ("S14", "the loss of 140 of her 2,200 sailors"),
 ("S14", "Her name was revived less than a year later when the newly constructed Essex-class aircraft carrier Kearsarge was commissioned as USS Hornet (CV-12)."),
 ("S2", "bombed targets in Tokyo, Yokosuka, Yokohama, Kobe, and Nagoya"),
 ("S15", "CV5"),
 ("S15", "sunk 7.6.1942"),
 ("S15", "sunk 24.10.1942"),
 ("S15", "Length, m"),
 ("S15", "Breadth, m"),
 ("S15", "Displacement standard, t"),
 ("S15", "Machinery"),
 ("S15", "Power, h. p."),
 ("S15", "Endurance, nm(kts)"),
 ("S15", "Armour, mm"),
 ("S15", "belt: 102 - 64 on 19mm plating, deck 38, bulkheads 102, CT: 102 sides, 51 roof"),
 ("S15", "Complement"),
 ("S15", "3 H II catapults (2 on flight deck and 1 doubled athwartship catapult in the hangar)"),
 ("S15", "Hangar: 166.4 x 19.2 x 5.25 m."),
 ("S15", "Flight deck: 244.6 x 29.9 m"),
 ("S15", "248.3x29.9m on CV8"),
 ("S15", "1940, Yorktown: + CXAM radar"),
 ("S15", "mid-1942, Yorktown, Hornet:"),
 ("S15", "8/1942, Hornet:"),
 ("S15", "180kg TNT warhead"),
 ("S15", "Fuel, t"),
 ("S16", "Yorktown (8) and Enterprise (8): Mark 21 Mod 16"),
 ("S16", "Hornet (8): Mark 24 Mod 2"),
 ("S16", "Yorktown was sunk with these mounts"),
 ("S16", "Sister-ship Hornet"),
 ("S16", "These were altered to Mod 6 sometime prior to September 1942."),
 ("S16", "Yorktown (CV-6) and Essex (CV-9): 450 rounds"),
 ("S16", "USS Yorktown (CV-5) and USS"),
 ("S16", "During construction, it became apparent that there was not enough clearance around the deck edge"),
 ("S16", "then designated as Mark 21 Mod 16"),
 ("S17", "The first USN pilot twin was completed in January 1942 and the first quad in April"),
 ("S17", "The first shipboard quad installation was on the gunnery-training ship (ex-battleship)"),
 ("S18", "Ammunition stowage per gun"),
 ("S20", "5 |"),
 ("S20", "MS 12"),
 ("S20", "On carriers, including Lexington and Saratoga, from"),
 ("S20", "Deck Blue, 20-B"),
 ("S21", "Note Grumman F4F Wildcats and Curtiss SBC Helldivers on deck; 20 mm. and 1.1\" batteries"),
 ("S21", "Camouflage on ship is measure 12 (MOD.)"),
 ("S21", "Radar antennas include those for FD types mounted atop the two Mark 37 gun directors at the island ends"),
 ("S21", "After repairs, she departed on 30 May to take part in the Battle of Midway."),
 ("S22", "At 1331, from 1,900 yards, he fires two torpedoes at the overlapping formation"),
 ("S22", "At 0458, the 19,875-ton YORKTOWN rolls over to port"),
 ("S23", "Yard workers and sailors worked flat out over"),
 ("S23", "We must have this ship back in three days."),
 ("S23", "The next morning"),
 ("S23", "Drydock Number One"),
 ("S23", "Within minutes the first of 1,400 repairmen, who would work around the clock"),
 ("S23", "rolling blackouts"),
 ("S23", "Only the most urgent repairs were made."),
 ("S23", "an enormous steel plate was welded over the damaged section"),
 ("S23", "estimated that repairing the Yorktown would take ninety days"),
 ("S23", "At 11:00 a.m. on May 28"),
 ("S23", "more patched than repaired but fit enough to fight"),
 ("S23", "551-pound armor-piercing bomb"),
 ("S23", "fifty feet"),
 ("S23", "Six compartments"),
 ("S23", "lost her radar and refrigeration system"),
 ("S23", "opened seams in her hull from frames 100 to 130"),
 ("S23", "Dated May 25 and delivered by plane"),
 ("S26", "Yorktown"),
 ("E-S7", "Protection came mainly from a protected box"),
 ("E-S7", "The flight and hangar decks of the ships were unarmored."),
 ("E-S7", "All three ships were equipped with Mark IV Mod 3A arresting gear"),
]

bad = []
for key, q in CHECKS:
    if key not in SRC:
        bad.append((key, "NO_SOURCE_FILE", q[:60]))
        continue
    if not find(q, key):
        bad.append((key, "NOT_FOUND", q[:120]))

print("TOTAL CHECKS:", len(CHECKS))
print("FAILED:", len(bad))
for k, why, q in bad:
    print("  [%s] %s :: %s" % (k, why, q))

# simple missing-marker checks
rep = open(os.path.join(BASE, "yorktown-hornet-tech.md"), encoding="utf-8").read()
print("\nREPORT chars:", len(rep), "lines:", rep.count("\n")+1)
print("未获取 count:", rep.count("未获取"))
print("S-sources cited:", len(set(re.findall(r"\bS(\d{1,2})\b", rep))))
