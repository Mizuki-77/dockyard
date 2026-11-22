# 武器图手工挑选（第二版）。
#
# 第一版自动挑（按 PD 优先 + 尺寸降序）挑错了一批：
#   8in 挑到「HMAS Australia 停靠纽约」和「多佛岸炮阵地」
#   6in 挑到「Hobart 号鱼雷损伤」和「伯明翰号儿童派对」
# 这些都在分类里，但拍的不是这型炮。
#
# 教训与 docs/45 §8.2 第 8 条一致：**自动筛选一定混进错图，必须人眼过。**
# 武器图尤其容易错，因为分类里混着「装了这门炮的舰」的其他照片。
#
# 本版逐张指定，并写明为什么选它。
CATS = {
    '8in-50-mk8': {
        'cat': 'BL 8 inch Mk VIII naval gun',
        'picks': [
            ('HMAS Canberra 8-inch gun turrets SLV H98.105 3229.jpeg',
             'turret', 'detail',
             'HMAS 堪培拉号的双联 8 英寸炮塔。郡级装的就是这型炮（Mark VIII），'
             '澳舰与英舰同型。这张能看清炮塔外形与两门炮的间距，是模型制作者要的角度。'),
            ('HMAS Australia 8 inch.JPG',
             'turret', 'detail',
             'HMAS 澳大利亚号的 8 英寸炮塔特写。与上一条是同级舰的另一个角度。'),
        ],
    },
    '6in-50-mk23': {
        'cat': 'BL 6 inch Mk XXIII naval gun',
        'picks': [
            ('HMS Belfast - Gun turret 1.jpg',
             'turret', 'detail',
             '贝尔法斯特号的 6 英寸 Mk XXIII 炮塔内部。该舰作为博物馆舰保存至今，'
             '这是本型炮现存最完整的实物参照。'),
            ('BL 6 inch Mk XXIII gun breech open HMS Belfast.jpg',
             'turret', 'detail',
             '同型炮的炮闩开启状态。城级（含谢菲尔德号）装的就是这型炮。'),
        ],
    },
    '4in-45-mk16': {
        'cat': 'QF 4 inch Mk XVI naval gun',
        'picks': [
            ('Gunners with 4 inch rounds HMS Vivien 1940 IWM A 1770.jpg',
             'turret', 'detail',
             'V 级驱逐舰上的 4 英寸炮组展示炮弹。Mk XVI 是双联高平两用炮座，'
             '城级轻巡的副炮就是它。'),
        ],
    },
    'vickers-50': {
        'cat': 'Vickers .50 machine gun',
        'picks': [
            ('Hr. Ms. Flores. De snelvuurkanonnen pom-poms worden dag en nacht bemand, Bestanddeelnr 934-9988.jpg',
             'turret', 'detail',
             '荷属东印度炮舰 Flores 号上的速射炮组昼夜值守。Vickers .50 四联机枪'
             '在二战初期是英联邦军舰的标准近程防空武器，皇家方舟号装了 32 挺。'),
        ],
    },
    '3pdr-hotchkiss': {
        'cat': 'QF 3 pounder Hotchkiss',
        'picks': [
            ('47 mm Hotchkiss Lennusadam 1.JPG',
             'turret', 'detail',
             '塔林水上飞机港博物馆藏 47 mm 霍奇基斯炮。皇家方舟号上的 3 磅礼炮'
             '属同一型火炮的礼炮版本（礼炮型与作战型结构相同，只是用途不同）。'),
        ],
    },
    'skua': {
        'cat': 'Blackburn Skua',
        'picks': [
            ('Blackburn Skua landing on HMS Ark Royal.jpg',
             'aircraft_handling', 'deck',
             '一架 Skua 正在皇家方舟号上降落。**这张图同时是「武器」与「本舰」的素材**，'
             '因为它拍的就是皇家方舟号的飞行甲板。'),
            ('The Royal Navy during the Second World War A8218.jpg',
             'aircraft_handling', 'deck',
             '四架岸基 Skua 编队。用于看清机型轮廓与涂装。'),
        ],
    },
    'roc': {
        'cat': 'Blackburn Roc',
        'picks': [
            ('15 Blackburn Roc Bristol Perseus Engine (15650907050).jpg',
             'aircraft_handling', 'detail',
             'Roc 战斗机（布里斯托尔 Perseus 发动机）。这型机性能很差，'
             '基本没打过胜仗，但它确实在皇家方舟号的编制里。'),
        ],
    },
    'albacore': {
        'cat': 'Fairey Albacore',
        'picks': [
            ('A Fairey Albacore Mk I of No. 820 Naval Air Squadron operating from HMS FORMIDABLE during the North African landings, November 1942. TR296.jpg',
             'aircraft_handling', 'detail',
             '820 中队的一架 Albacore Mk I，1942-11 北非登陆时从可畏号起飞。'
             '皇家方舟号 1941-10 曾转场搭载该型机 11 架（送马耳他，未作战）。'),
            ('15 Fairey Albacore (15837361162).jpg',
             'aircraft_handling', 'detail',
             'Albacore 的侧面特写，能看清折叠翼与挂架。'),
        ],
    },
}
