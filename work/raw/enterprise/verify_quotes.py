import io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = r"D:\deepseek harness\website-warships\work\raw\enterprise"
checks = [
 ("wiki-yorktown-class.txt", "The flight and hangar decks of the ships were unarmored"),
 ("wiki-yorktown-class.txt", "The ships each had three centerline aircraft elevators"),
 ("wiki-yorktown-class.txt", "Mark IV Mod 3A arresting gear"),
 ("wiki-yorktown-class.txt", "During sea trials, she produced 120,500 shp"),
 ("wiki-yorktown-class.txt", "nine Babcock & Wilcox boilers providing"),
 ("wiki-yorktown-class.txt", "the original design for a flush-deck"),
 ("danfs-nhhc-cv6.txt", "A Board of Inspection and Survey team examined Enterprise"),
 ("danfs-nhhc-cv6.txt", "the breakers cut her up by February 1960"),
 ("danfs-nhhc-cv6.txt", "operated their CXAM-1 radar"),
 ("danfs-nhhc-cv6.txt", "delivered to the fleet and fitted in California, Yorktown"),
 ("danfs-nhhc-cv6.txt", "workers installed four quadruple 40 millimeter mounts"),
 ("danfs-nhhc-cv6.txt", "blisters were fitted between frames 36 and 150"),
 ("navsource-net-cv6-main.txt", "2,217"),
 ("navsource-net-cv6-main.txt", "3 elevators (48' x 44'"),
 ("navsource-net-cv6-main.txt", "Sold for scrapping 1 July 1958"),
 ("navsource-net-cv6-main.txt", "3 Aug 1933"),
 ("navsource-net-cv6.txt", "her old Mk.33 directors"),
 ("navsource-net-cv6.txt", "Measure 21 camouflage"),
 ("navsource-net-cv6.txt", "masthead CXAM-1 radar antenna"),
 ("enterprise-war-history.txt", "blisters were fitted between"),
 ("enterprise-war-history.txt", "the two catapults on the main deck"),
 ("enterprise-war-history.txt", "replacement of four 1.1-inch mounts with four 40mm quadruple mounts"),
 ("enterprise-war-history.txt", "installation of thirty 20mm guns and additional radar units"),
 ("enterprise-war-history.txt", "No. 9 arresting gear"),
 ("enterprise-war-history.txt", "replacement of the two forward flight deck catapults with units of a later design"),
 ("enterprise-war-history.txt", "Construction of ENTERPRISE was ordered 3 August 1933"),
 ("enterprise-war-history.txt", "accumulating 18 out of a possible 22 combat stars"),
 ("cv6-midway-ar.txt", "ten torpedo planes out of fourteen of Torpedo Squadron SIX did not return"),
 ("cv6-midway-ar.txt", "1730 Commenced launching second attack group composed of 24 VSB"),
 ("cv6-midway-ar.txt", "48,000 .50 caliber"),
 ("cv6-midway-ar.txt", "suffered no damage during actions on June 4-5-6"),
 ("nhhc-composition.txt", "27 Grumman F4F-4 (Wildcat)"),
 ("nhhc-composition.txt", "14 Douglas TBD-1 (Devastator)"),
 ("nhhc-radar-ftp.txt", "reliable maximum range on large aircraft is 50 miles"),
 ("nhhc-radar-ftp.txt", "Antenna proper measures 15' x 15'8"),
 ("navweaps-5in38.txt", "Yorktown (8) and Enterprise (8): Mark 21 Mod 16"),
 ("navweaps-5in38.txt", "Ammunition stowage per gun"),
 ("navweaps-5in38.txt", "replaced with Mark 24 Mod 11 mounts during her overhaul at Puget Sound in 1943"),
 ("navypedia-yorktown.txt", "3 H II catapults"),
 ("navypedia-yorktown.txt", "resistance from explosion of torpedo with 180kg TNT warhead"),
 ("navypedia-yorktown.txt", "breadth by wl increased to 29.1m"),
 ("navweaps-11in75.txt", "Ammunition stowage per gun"),
 ("navweaps-11in75.txt", "Weight of Complete Round"),
 ("navweaps-11in75.txt", "HE-T Mark 1 Mods 0 to 28 - 0.917 lbs"),
 ("danfs-nhhc-cv6.txt", "She was stricken from the List of Naval Vessels on 2 October 1956"),
 ("danfs-nhhc-cv6.txt", "Enterprise was sold for $561,333.00 to the Lipsett Corp."),
 ("wikicv6-na", "x"),
]
ok = miss = 0
for f, needle in checks:
    p = os.path.join(d, f)
    if not os.path.exists(p):
        print("MISSINGFILE " + f); continue
    t = io.open(p, encoding="utf-8", errors="replace").read()
    t2 = " ".join(t.split()); n2 = " ".join(needle.split())
    if n2 in t2:
        ok += 1
    else:
        miss += 1
        print("MISS " + f + " :: " + ascii(needle)[:90])
print("OK=%d MISS=%d" % (ok, miss))
