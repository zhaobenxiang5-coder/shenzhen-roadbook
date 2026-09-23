import json

# Comprehensive 3-option itinerary data for each day (Plan A, Plan B, Plan C)
# Tailored from Shenzhen Longgang Danping base, with weather, sunset, costs, parking, food, and multi-layered sports/equipment
DAYS_DATA = [
    # MID-AUTUMN 3 DAYS
    {
        "tab_id": "mid_autumn",
        "day_id": "mid_autumn-d1",
        "date_title": "Day 1 (中秋首日 · 9.24)",
        "theme": "山涧溯溪清凉 · 古堡明月夜 · 避暑漫游",
        "driving": "单程约 35~45km / 40~50分钟 (丹平快速→水官高速→南坪快速)",
        "weather": "⛅ 多云微风 25℃~31℃ | 紫外线: 中等 | 日落 18:18 (18:45月出)",
        "cost": "约 ¥160~220 (双人全天含餐、油电、停车，0门票0住宿)",
        "crowd": "★☆☆☆☆ (纯本地反向小众走法)",
        "sports_gear": "羽毛球拍2副、防风球、溯溪涉水鞋/洞洞鞋、换洗干T恤、小音箱",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "马峦山碧岭瀑布清凉溯溪 + 大万世居月夜灯光秀",
                "spot_desc": "从坪山碧岭步道逆向上山，绿树遮天蔽日，沿路叠水飞瀑声不绝于耳，体感比市区凉快4度！下午出山转场大万世居，全国最大客家围屋之一，外围大广场极平整适合打羽毛球，傍晚青砖灰瓦间看中秋圆月与文艺市集咖啡。",
                "amap_url": "https://uri.amap.com/navigation?to=114.301548,22.653412,马峦山碧岭瀑布&mode=car",
                "parking": "碧岭瀑布停车场（免费/10元/天，早9:30前或午后2点位多）",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 客家窑鸡正餐约 ¥150",
                "food_title": "必吃：坪山柴火客家窑鸡与手打牛肉丸",
                "food_desc": "【客家农家院】现烤出炉土窑走地鸡，金黄爆汁皮脆肉嫩，搭配鲜枸杞叶肉丸汤！",
                "food_amap": "https://uri.amap.com/search?keyword=坪山客家窑鸡",
                "photo_spot": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "横岗园山风景区大康溪谷 + 避暑水潭漫步",
                "spot_desc": "距离丹平仅25分钟车程，完全不走易堵的深盐二通道！园山被称为深圳后花园，大康溪谷山水相依，游人只有梧桐山的十分之一，溪水清澈见底，适合赤足戏水，草坪宽广能尽情挥拍打羽毛球。",
                "amap_url": "https://uri.amap.com/navigation?to=114.249215,22.641235,园山风景区&mode=car",
                "parking": "景区正门地面生态车场（车位充裕，随到随停）",
                "cost_detail": "门票 ¥15/人 | 停车 ¥10 | 潮汕鲜牛肉火锅约 ¥160",
                "food_title": "平替：南湾/丹平社区老字号潮汕鲜牛肉火锅",
                "food_desc": "回丹平家门口吃现切热气吊龙肉、匙柄、手打牛筋丸，配沙茶酱，不用景区排队挨宰！",
                "food_amap": "https://uri.amap.com/search?keyword=龙岗南湾潮汕牛肉火锅",
                "photo_spot": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "大运自然公园大草坪露营 + 神仙湖环湖骑行",
                "spot_desc": "龙岗本地神仙秘境，大片开阔缓坡草坪与环湖水杉步道。带上月亮椅、野餐垫和羽毛球，湖面微波荡漾，黄昏时分夕阳将湖水染成金红，晚上坐在草坪仰望中秋月色极其浪漫。",
                "amap_url": "https://uri.amap.com/navigation?to=114.218412,22.695321,大运自然公园&mode=car",
                "parking": "大运公园东门/地下停车场（车位极多，5元/小时）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 龙城特色乳鸽与糖水双人约 ¥120",
                "food_title": "平替：大运天地小资简餐与深夜甜汤",
                "food_desc": "【大运湖畔餐吧】湖景微风伴着鲜榨果汁或热奶茶，晚上来一碗清心润肺的双皮奶蛋挞！",
                "food_amap": "https://uri.amap.com/search?keyword=深圳大运中心美食",
                "photo_spot": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "避坑提示：千万不要走大梅沙或从小梅沙北入口进，节假日东部沿海必定大排长龙，认准【坪山碧岭入口】高速出口畅通！",
            "羽毛球建议：大万世居围屋门前或大运公园草坪无大阵风，傍晚16:30打球光线温和不刺眼。"
        ]
    },
    {
        "tab_id": "mid_autumn",
        "day_id": "mid_autumn-d2",
        "date_title": "Day 2 (中秋正日 · 9.25)",
        "theme": "古树海岸海风 · 赶海抓螃蟹 · 橘子海日落",
        "driving": "单程约 55~65km / 50~60分钟 (水官高速→惠深沿海高速葵涌/小桂下)",
        "weather": "🌤️ 晴转少云 26℃~32℃ | 紫外线: 较高 (海边备防晒) | 日落 18:17 (海上升明月)",
        "cost": "约 ¥220~280 (双人丰盛海鲜、油电、免门票)",
        "crowd": "★★☆☆☆ (完胜人挤人的较场尾/大梅沙)",
        "sports_gear": "赶海小水桶与小耙子、羽毛球拍、防晒衣、墨镜、折叠月亮椅看日落",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "坝光500年天然古银叶树湿地 + 白沙湾赶海",
                "spot_desc": "避开南澳堵车大军，直奔大鹏最东北端的原生态处女地。500年古银叶树板根硕大，木栈道一路延伸进海湾，退潮时下滩涂抓小寄居蟹和小海螺。傍晚坐在白沙湾看无遮挡橘子海落日与海上升明月！",
                "amap_url": "https://uri.amap.com/navigation?to=114.521820,22.646549,坝光银叶树湿地园&mode=car",
                "parking": "坝光湿地生态停车场（车位充裕，无需大鹏半岛拥堵排队）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 葵涌老街黄椒炒八爪鱼双人约 ¥180",
                "food_title": "必吃：葵涌老街无名海鲜排档",
                "food_desc": "【本地老饕私藏】爆炒野生八爪鱼、黄椒酱生蒸泥鯭鱼、蒜蓉蒸海捕带子，人均80吃得极鲜甜！",
                "food_amap": "https://uri.amap.com/search?keyword=葵涌老街海鲜",
                "photo_spot": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1565680018434-b513d5e5fd47?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "惠阳澳头小桂村沿海绿道骑行 (免大鹏预约)",
                "spot_desc": "从丹平出发走惠深沿海高速在小桂出口下（不进深圳交警大鹏预约圈！）。租一辆双人自行车沿着海天一色的绿道骑行，吹着海风看海鸟低飞，渔排静卧，沿途宽阔驿站还能打羽毛球。",
                "amap_url": "https://uri.amap.com/navigation?to=114.582103,22.709321,小桂村绿道&mode=car",
                "parking": "小桂驿站停车场（停车免费/极便宜）",
                "cost_detail": "门票 ¥0 | 双人单车 ¥30 | 澳头码头现挑海鲜加工约 ¥160",
                "food_title": "平替：澳头海鲜码头现挑现做",
                "food_desc": "直接在码头买刚靠岸的白灼九节虾、椒盐皮皮虾，拿到旁边大排档代加工，性价比极高！",
                "food_amap": "https://uri.amap.com/search?keyword=惠阳澳头海鲜码头",
                "photo_spot": "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "盐田海鲜街后方海滨栈道慢行 + 盐田港夜色",
                "spot_desc": "下午4点后再出发，直奔盐田食街后方的纯观海木栈道。避开大梅沙喧闹，这里沿海临风，听海浪拍打礁石，近距离看货轮往来穿梭，走累了找家老店喝砂锅粥看月亮。",
                "amap_url": "https://uri.amap.com/navigation?to=114.258923,22.583412,盐田海鲜食街&mode=car",
                "parking": "海鲜街公共多层停车场（车位多，傍晚车流渐稀）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 海鲜砂锅粥与炸春卷双人约 ¥140",
                "food_title": "平替：盐田老字号鲜虾蟹肉砂锅粥",
                "food_desc": "【潮味砂锅粥】鲜活膏蟹配基围虾现熬稠粥，撒上香菜冬菜碎，喝上一口暖心熨帖！",
                "food_amap": "https://uri.amap.com/search?keyword=盐田海鲜街砂锅粥",
                "photo_spot": "https://images.unsplash.com/photo-1518495973542-4542c06a5843?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1535473897047-b6745f657a84?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "大鹏预约避坑：若临时没约上深圳交警大鹏自驾号，直接切换平替B（惠阳小桂村）或平替C（盐田），完全不受预约限制！",
            "海边贴心：带上一瓶大矿泉水在后备箱，退潮赶海踩泥后先给女朋友冲洗脚部，换上干爽拖鞋。"
        ]
    },
    {
        "tab_id": "mid_autumn",
        "day_id": "mid_autumn-d3",
        "date_title": "Day 3 (中秋收官 · 9.26)",
        "theme": "万亩森林洗肺 · 湖畔咖啡草坪 · 市井老街寻味",
        "driving": "单程约 30~38km / 30~40分钟 (丹平快速→清平高速/从莞深直达)",
        "weather": "⛅ 阴天间多云 24℃~30℃ | 紫外线: 弱 | 日落 18:16",
        "cost": "约 ¥150~210 (双人正餐瓦煲碌鹅、老字号糖水、免停车)",
        "crowd": "★☆☆☆☆ (纯本地自驾吸氧胜地)",
        "sports_gear": "羽毛球拍、飞盘、手冲咖啡保温壶、防蚊喷雾、蓝牙音箱",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "东莞塘厦大屏嶂森林公园 + 大坪水库草坪放空",
                "spot_desc": "从丹平快速转清平高速仅半小时，万亩荔枝林环抱的超大森林氧吧！沿大坪水库步道绿荫参天，微风习习。在大草坪支起折叠椅喝咖啡、打羽毛球，呼吸纯天然高浓度负氧离子，舒缓身心。",
                "amap_url": "https://uri.amap.com/navigation?to=114.073289,22.782012,大屏嶂森林公园&mode=car",
                "parking": "大屏嶂森林公园南门停车场（完全免费，车位充足）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 农家瓦煲传统碌鹅约 ¥150",
                "food_title": "必吃：塘厦正宗传统瓦煲碌鹅",
                "food_desc": "【客家农家院】酱汁浓郁油亮、鹅肉鲜嫩多汁毫无腥气，汤汁拌米饭能连吃三碗，配柴火豆腐！",
                "food_amap": "https://uri.amap.com/search?keyword=塘厦正宗碌鹅",
                "photo_spot": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "龙岗红花岭生态公园水库步道 + 登顶眺望",
                "spot_desc": "完全在龙岗本地，不跨城。环龙口水库木栈道被茂密树木包围，登顶观景台可360度俯瞰大运中心全景。下山后顺路去平湖守珍街老字号排档喝手工芝麻糊和糖水，充满市井烟火气。",
                "amap_url": "https://uri.amap.com/navigation?to=114.228912,22.716301,红花岭生态公园&mode=car",
                "parking": "公园东侧生态停车场（随到随停，车位多）",
                "cost_detail": "门票 ¥0 | 停车 ¥5 | 平湖守珍街糖水小吃双人约 ¥50",
                "food_title": "平替：平湖守珍街老牌手工糖水铺",
                "food_desc": "【三十年老字号】现磨香滑芝麻糊、姜汁撞奶、炸小油糍，温暖细腻甜入心脾！",
                "food_amap": "https://uri.amap.com/search?keyword=平湖守珍街美食",
                "photo_spot": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "甘坑古镇后山二十四史书院书香夜游",
                "spot_desc": "白天在家睡到自然醒，下午4点悠闲出发去甘坑古镇后山二十四史书院。小桥流水、亭台水榭、万盏明灯初上，宛如千与千寻梦境，适合穿汉服或素裙拍大片，在林下茶社对坐品茗。",
                "amap_url": "https://uri.amap.com/navigation?to=114.129845,22.641290,二十四史书院&mode=car",
                "parking": "甘坑古镇北门多层停车场（车位丰富）",
                "cost_detail": "门票夜场 ¥30/人 | 停车 ¥15 | 围炉煮茶与素面点心双人约 ¥100",
                "food_title": "平替：甘坑客家黄酒酿鸡与纸包豆腐",
                "food_desc": "【古镇客家食坊】醇香温润的客家糯米黄酒煮土鸡，汤汁甘甜暖胃，再来一份手工酿苦瓜！",
                "food_amap": "https://uri.amap.com/search?keyword=甘坑客家菜",
                "photo_spot": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "节奏把控：最后一天以休整为主，下午16:00前返程丹平，完全避开夜间高速大塞车，神清气爽回家洗澡看剧！"
        ]
    },

    # NATIONAL DAY 5 DAYS
    {
        "tab_id": "national_day",
        "day_id": "national_day-d1",
        "date_title": "Day 1 (10.1 首日大堵车 · 逆向静止)",
        "theme": "不上高速不堵车 · 湖畔林盘草坪露营 · 瓦煲黄鳝饭",
        "driving": "单程约 12~18km / 20~25分钟 (丹平快速经地面主干道直达，0高速拥堵)",
        "weather": "🌤️ 秋高气爽 23℃~31℃ | 紫外线: 中等 | 日落 18:10",
        "cost": "约 ¥130~170 (双人吃好玩好，0房费0门票0停车)",
        "crowd": "★☆☆☆☆ (避开全网高速大拥堵的黄金智慧)",
        "sports_gear": "羽毛球拍、飞盘、充气空气沙发、防水野餐垫、保温水杯",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "凤岗官井头水库森林步道 + 龙凤后山大草坪",
                "spot_desc": "10月1日全省高速全面红暴！我们反向走地面辅道20分钟直插凤岗官井头水库与龙凤后山。高大水杉林环抱清澈湖面，开阔草坪随心打羽毛球、扔飞盘，躺在充气沙发上刷朋友圈看别人在高速上堵车！",
                "amap_url": "https://uri.amap.com/navigation?to=114.184321,22.712104,官井头水库&mode=car",
                "parking": "水库外围道旁停车位及后山空旷停车场（免费）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 炭火瓦煲黄鳝饭双人约 ¥130",
                "food_title": "必吃：凤岗客家炭火瓦煲黄鳝饭",
                "food_desc": "【老街瓦煲饭】手撕黄鳝丝拌金黄脆锅巴，葱香四溢焦脆诱人，配爽脆客家酿三宝！",
                "food_amap": "https://uri.amap.com/search?keyword=凤岗客家黄鳝饭",
                "photo_spot": "https://images.unsplash.com/photo-1510312305653-8ed496efae75?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "平湖生态园（平湖水库千亩湿地环湖跑道）",
                "spot_desc": "距离丹平社区仅6公里！数千亩水库湿地与无机动车打扰的环湖绿道，绿树成荫微风阵阵。可以带双人羽毛球拍在林荫开阔处酣畅对拉，漫步看白鹭掠过水面，松弛惬意。",
                "amap_url": "https://uri.amap.com/navigation?to=114.129302,22.684120,平湖生态园&mode=car",
                "parking": "平湖生态园正门生态停车场（车位极多）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 浓香胡椒猪肚鸡约 ¥140",
                "food_title": "平替：南湾/丹竹头老牌胡椒猪肚鸡",
                "food_desc": "回到丹平家门口喝一碗浓白胡椒走地鸡汤，暖胃驱湿，猪肚爽脆弹牙，吃完回家看电视睡觉！",
                "food_amap": "https://uri.amap.com/search?keyword=南湾客家猪肚鸡",
                "photo_spot": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "平湖守珍街老铁路漫步 + 凤凰山矿山公园",
                "spot_desc": "探索平湖鲜为人知的工业遗迹与矿山公园湖泊，深潭如碧玉，老铁路旁林荫安静，几乎没有外地游客，拍照极有胶片复古故事感。",
                "amap_url": "https://uri.amap.com/navigation?to=114.135210,22.693210,凤凰山矿山公园&mode=car",
                "parking": "矿山公园入口停车场（免费停车）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 平湖手磨豆浆炸油条双人约 ¥35",
                "food_title": "平替：老平湖市井宵夜大排档",
                "food_desc": "鲜炸酥脆小肉丸配现滚生滚猪杂枸杞叶汤，地道纯粹的广东老街市井滋味。",
                "food_amap": "https://uri.amap.com/search?keyword=平湖老街大排档",
                "photo_spot": "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "老司机心得：国庆第1天谁上高速谁后悔！留在深莞交界是高级玩家的松弛，花销极小体验极高。"
        ]
    },
    {
        "tab_id": "national_day",
        "day_id": "national_day-d2",
        "date_title": "Day 2 (10.2 · 古村田园漫游)",
        "theme": "避世古围屋 · 梯田樟林古道 · 柴火三杯鸭",
        "driving": "单程约 42~52km / 45~55分钟 (水官高速→深汕西或惠阳内环直达，国庆高速免费)",
        "weather": "⛅ 多云间晴 24℃~30℃ | 紫外线: 中等 | 日落 18:09",
        "cost": "约 ¥180~240 (高速路费¥0全免，正餐柴火三杯鸭，0门票)",
        "crowd": "★★☆☆☆ (文艺幽静，无商业嘈杂)",
        "sports_gear": "羽毛球拍（打古村空坪）、微单/手机云台、防蚊水、遮阳草帽",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "惠阳秋长谷里客家古村落 + 碧溪老围群",
                "spot_desc": "300年历史的大型客家围屋四合院落，背靠梯田和老樟树林。这里改建成了艺术书吧与精品咖啡馆，游人很少，没有商业叫卖。下午在庭院品一杯桂花拿铁，村口开阔处还能打上一场羽毛球。",
                "amap_url": "https://uri.amap.com/navigation?to=114.431204,22.802195,秋长谷里&mode=car",
                "parking": "秋长谷里专属地面生态停车场（完全免费）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 柴火大锅煨三杯鸭双人约 ¥160",
                "food_title": "必吃：秋长客家柴火三杯鸭与艾粄",
                "food_desc": "【古村旁农庄】大铁锅慢煨的三杯鸭，酱汁红润醇厚肉质紧实，配现打客家艾粄糍粑！",
                "food_amap": "https://uri.amap.com/search?keyword=惠阳秋长客家农家乐",
                "photo_spot": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "深圳观澜版画村 + 牛湖老街手作工坊",
                "spot_desc": "若当天去惠州方向车流增加，转走清平快速去观澜。古村依山傍水，排屋古色古香，碉楼矗立，池塘睡莲盛开，版画工坊文艺气息极浓厚，清晨早去毫无喧嚣。",
                "amap_url": "https://uri.amap.com/navigation?to=114.078921,22.723145,观澜版画村&mode=car",
                "parking": "版画基地生态停车场（车位多）",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 观澜老街腌面及第汤双人约 ¥50",
                "food_title": "平替：观澜老街正宗客家腌面与牛肉汤",
                "food_desc": "【老街街坊食堂】蒜油香气扑鼻的梅州客家腌面，搭配一碗热气腾腾的鲜枸杞叶猪杂及第汤！",
                "food_amap": "https://uri.amap.com/search?keyword=观澜老街客家腌面",
                "photo_spot": "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "坪山金龟自然村客家山林漫步",
                "spot_desc": "隐匿在坪山深处的山水画卷，溪流潺潺，两旁全是绿树与文艺小民居，村里有野果树与手作小店，人少空气湿润清爽，完全不收门票。",
                "amap_url": "https://uri.amap.com/navigation?to=114.402134,22.651230,金龟自然村&mode=car",
                "parking": "村口游客生态车位（免费/10元）",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 金龟村手作简餐与农家菜双人约 ¥120",
                "food_title": "平替：金龟农家石磨豆腐与土鸡煲",
                "food_desc": "清甜泉水磨制的嫩豆腐，两面煎至金黄后慢火煲透，外脆里嫩豆香浓郁。",
                "food_amap": "https://uri.amap.com/search?keyword=金龟村农家乐",
                "photo_spot": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "摄影服饰：女生建议穿米白、淡黄色棉麻长裙，与老砖墙、木门及古樟树林极为般配！"
        ]
    },
    {
        "tab_id": "national_day",
        "day_id": "national_day-d3",
        "date_title": "Day 3 (10.3 · 纯净深蓝海滩)",
        "theme": "绝美百安沙滩 · 赶海踩细沙 · 渔港海鲜盛宴",
        "driving": "单程约 105~115km / 1小时20分 (沈海高速深汕段，早8:00前出发畅行无阻，高速免费)",
        "weather": "☀️ 晴朗碧海 25℃~32℃ | 紫外线: 极高 (必涂防晒霜) | 日落 18:08",
        "cost": "约 ¥260~340 (高速路费¥0全免，生猛海鲜大餐吃撑，0海滩门票)",
        "crowd": "★★☆☆☆ (完胜惠州双月湾的人头海)",
        "sports_gear": "沙滩羽毛球拍、赶海小桶与铲子、偏光太阳镜、防晒衣、洗脚备用大矿泉水",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "深汕特别合作区鲘门百安海滩 + 渔港日落",
                "spot_desc": "双月湾国庆会彻底堵瘫！我们反向多开半小时直奔深汕百安海滩。沙质细腻如粉，海水呈渐变青蓝色，关键是没有商业圈地与遮阳伞强制消费！两人可以在海边踩水、打沙滩羽毛球、捡贝壳，黄昏到鲘门渔港看千帆归航。",
                "amap_url": "https://uri.amap.com/navigation?to=115.112930,22.784012,百安海滩&mode=car",
                "parking": "百安村口海滨开敞停车场（免费/15元封顶）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 鲘门渔港海鲜大餐（红鲟饭+马鲛鱼丸）双人约 ¥230",
                "food_title": "必吃：鲘门正宗手打马鲛鱼丸与红鲟饭",
                "food_desc": "【鲘门港口老牌饭店】弹性惊人的手打鲜马鲛鱼丸汤，配满满膏蟹蒸糯米饭（红鲟饭），鲜甜爆表！",
                "food_amap": "https://uri.amap.com/search?keyword=鲘门海鲜饭店",
                "photo_spot": "https://images.unsplash.com/photo-1506929562872-bb421503ef21?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1535473897047-b6745f657a84?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "大鹏杨梅坑鹿嘴山庄清晨追光快线",
                "spot_desc": "如果不愿开到深汕，实行【超早鸟策略】：早晨6:30出发直插大鹏杨梅坑鹿嘴山庄看美人鱼悬崖绝壁，海水蔚蓝壮阔。中午11:30在拥堵大潮到来前打道回府！",
                "amap_url": "https://uri.amap.com/navigation?to=114.593210,22.569431,鹿嘴山庄&mode=car",
                "parking": "杨梅坑主停车场（早到抢占一线海景车位）",
                "cost_detail": "门票 ¥0 | 观光车单程 ¥13.8/人 | 南澳海胆炒饭双人约 ¥150",
                "food_title": "平替：南澳老牌海胆炒饭与窑鸡",
                "food_desc": "金黄诱人的南澳鲜海胆炒饭，海胆香气与米香交织，粒粒分明鲜美满分！",
                "food_amap": "https://uri.amap.com/search?keyword=大鹏海胆炒饭",
                "photo_spot": "https://images.unsplash.com/photo-1518495973542-4542c06a5843?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "惠东范和古村 + 亚婆角滨海公路慢游",
                "spot_desc": "去亚婆角未过度开发的小海湾，水清沙白，顺路探访有数百年历史的范和古村落，罗冈围屋与古戏台宁静祥和，吃一碗范和正宗猪肠粉。",
                "amap_url": "https://uri.amap.com/navigation?to=114.882103,22.812340,范和古村&mode=car",
                "parking": "范和村口文化广场停车场（免费）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 范和手作猪肠粉与海鲜双人约 ¥90",
                "food_title": "平替：范和老街手工葱油石磨猪肠粉",
                "food_desc": "刚出炉米香扑鼻的肠粉卷上秘制肉末香菇酱，淋上头抽与现熬熟葱油，滑嫩爽口！",
                "food_amap": "https://uri.amap.com/search?keyword=惠东范和古村美食",
                "photo_spot": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1565680018434-b513d5e5fd47?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "高速窗口：去深汕务必早晨8:00前上沈海高速，返程建议下午16:00前或晚上20:30后，完美避开潮汐车流！"
        ]
    },
    {
        "tab_id": "national_day",
        "day_id": "national_day-d4",
        "date_title": "Day 4 (10.4 · 跨海工程与世界美食)",
        "theme": "深中通道飞驰 · 顺德容桂老街市井 · 现蒸桑拿鸡",
        "driving": "单程约 90~100km / 1小时15分 (经深中通道直达中山/顺德容桂，高速全免费)",
        "weather": "🌤️ 清爽微风 24℃~31℃ | 紫外线: 中等 | 日落 18:07 (伶仃洋晚霞)",
        "cost": "约 ¥240~320 (深中通道高速费¥0免单！顺德老街私房菜吃饱)",
        "crowd": "★★★☆☆ (避开华侨城，只钻市井老巷)",
        "sports_gear": "羽毛球拍（容桂德胜河滨公园打球超舒服）、大容量保温杯、极舒适健步鞋",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "深中通道跨海体验 + 顺德容桂老街市井寻味",
                "spot_desc": "自驾打卡全球超级工程深中通道与伶仃洋大桥，跨海视野极为震撼！坚决避开顺德大良清晖园的人山人海，直奔容桂渔人码头周边的文创老街与市井小巷，漫步德胜河畔绿道，吃正宗桑拿鸡与双皮奶。",
                "amap_url": "https://uri.amap.com/navigation?to=113.298210,22.774512,容桂渔人码头&mode=car",
                "parking": "德胜河南岸或文创园地下停车场（位多有指引）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 现蒸桑拿鸡与双皮奶双人餐约 ¥190",
                "food_title": "必吃：顺德容桂现蒸桑拿鸡与炸双皮奶",
                "food_desc": "【容桂地道私房菜】桑拿虫草花走地鸡肉（精准蒸3分钟出锅嫩滑到爆汁），配原汁鸡汤煮菜心！",
                "food_amap": "https://uri.amap.com/search?keyword=容桂地道桑拿鸡",
                "photo_spot": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "中山南朗崖口村金色海边稻田与集装箱咖啡",
                "spot_desc": "下深中通道第一站就在中山南朗下高速。崖口村有上千亩临海金色稻田，彩色集装箱咖啡街倚海而建。海风拂面，稻香四溢，点一杯冷萃咖啡看海鸟翻飞，惬意浪漫。",
                "amap_url": "https://uri.amap.com/navigation?to=113.568412,22.482190,崖口村稻田&mode=car",
                "parking": "崖口稻田驿站停车场（停车位丰富）",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 崖口海鲜云吞与脆皮黄鳝煲仔饭约 ¥110",
                "food_title": "平替：中山崖口鲜虾云吞与煲仔饭",
                "food_desc": "【崖口人家】皮薄如蝉翼的现包鲜虾蟹子小云吞，以及炭火现焗的黄鳝煲仔饭，焦香金黄！",
                "food_amap": "https://uri.amap.com/search?keyword=中山崖口云吞",
                "photo_spot": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "中山石岐老街孙文西路 + 岐江夜色",
                "spot_desc": "南洋骑楼风格的百年老街，避开午后大太阳，傍晚漫步在骑楼回廊下，吹着岐江晚风，打卡百年老字号石岐乳鸽，市井氛围浓厚。",
                "amap_url": "https://uri.amap.com/navigation?to=113.374210,22.521098,孙文西路步行街&mode=car",
                "parking": "兴中广场地下停车场（车位海量，直通步行街）",
                "cost_detail": "门票 ¥0 | 停车 ¥12 | 正宗石岐红烧乳鸽双人餐约 ¥130",
                "food_title": "平替：中华老字号石岐脆皮红烧乳鸽",
                "food_desc": "【石岐佬】刚出炉外皮焦脆如玻璃薄纸，撕开时肉汁横流，搭配特色菠萝包与鱼蓉粥！",
                "food_amap": "https://uri.amap.com/search?keyword=石岐红烧乳鸽",
                "photo_spot": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "深中通道过桥时段：早晨08:00前或中午12:30-13:30过桥路况最佳，傍晚返程看伶仃洋跨海大桥落日与亮灯极为壮丽！"
        ]
    },
    {
        "tab_id": "national_day",
        "day_id": "national_day-d5",
        "date_title": "Day 5 (10.5 黄金周收官 · 森林收心)",
        "theme": "东莞第一峰溪谷 · 沿溪洗肺漫步 · 泉水土鸡汤",
        "driving": "单程约 48~56km / 48~55分钟 (从莞深高速→潮莞高速谢岗出口，高速免费)",
        "weather": "⛅ 阴天微凉 22℃~28℃ | 紫外线: 弱 | 日落 18:06",
        "cost": "约 ¥170~220 (高速免费，全免费入园，正宗泉水炖鸡)",
        "crowd": "★☆☆☆☆ (原生态清幽大山，毫无拥挤)",
        "sports_gear": "羽毛球拍（山脚下生态广场打球超赞）、登山杖/健步鞋、保温杯、外带保鲜盒",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "东莞第一峰银瓶山（谢岗入口沿溪谷洗肺）",
                "spot_desc": "拒绝人满为患的梧桐山！自驾至东莞第一峰银瓶山谢岗景区。沿溪流木栈道而上，林荫遮蔽率95%，沿途飞瀑流泉，空气清冽湿润。轻徒步2小时吸氧洗肺，为假期画上清爽健康的句号。",
                "amap_url": "https://uri.amap.com/navigation?to=114.215432,22.923412,银瓶山谢岗景区&mode=car",
                "parking": "银瓶山谢岗第一生态停车场（免费停车，环境整洁）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 山泉水炖走地鸡汤双人约 ¥150",
                "food_title": "必吃：谢岗山泉水煲土鸡与炒山坑螺",
                "food_desc": "【山脚农家食肆】清冽山泉水慢火煲农家走地鸡汤，鲜美甘润回甘，紫苏爆炒野生山坑螺！",
                "food_amap": "https://uri.amap.com/search?keyword=银瓶山谢岗农家乐",
                "photo_spot": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1543353071-873f17a7a088?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "盐田三洲田公路自驾慢游 + 茶溪谷水库晚霞",
                "spot_desc": "深圳最美自驾盘山公路之一！无需买景区门票，顺着盘山绿树公路行驶，观赏三洲田水库碧蓝湖水与山林静谧，在沿途观景平台喝杯露营咖啡看黄昏晚霞。",
                "amap_url": "https://uri.amap.com/navigation?to=114.289123,22.628412,三洲田水库&mode=car",
                "parking": "三洲田水库观景平台及茶溪谷外围停车带",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 盐田老字号脆皮爆汁乳鸽约 ¥130",
                "food_title": "平替：盐田老字号红烧乳鸽与海鲜肠粉",
                "food_desc": "返程下山到盐田海鲜街或沙头角老店吃皮脆肉嫩爆汁的金牌红烧乳鸽，再来一份蒸海鲜肠粉！",
                "food_amap": "https://uri.amap.com/search?keyword=盐田红烧乳鸽",
                "photo_spot": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "惠州罗浮山后山酥醪村古道",
                "spot_desc": "从罗浮山后山进入未商业化的酥醪古村，村落隐匿在深山茶园与溪水竹林间，游客稀少，喝一碗酥醪甘冽山泉水熬制的仙人豆腐，宁静祥和。",
                "amap_url": "https://uri.amap.com/navigation?to=114.052130,23.312040,酥醪村&mode=car",
                "parking": "酥醪观下路边生态车位（免费）",
                "cost_detail": "门票 ¥0 | 停车 ¥0 | 酥醪特色土猪汤与酥醪菜干约 ¥110",
                "food_title": "平替：酥醪村土猪肉汤与客家黄糕",
                "food_desc": "【老村民家宴】山泉水清炖纯正深山土猪肉汤，仅放少许白胡椒，肉甜汤清！",
                "food_amap": "https://uri.amap.com/search?keyword=酥醪村农家菜",
                "photo_spot": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "收官收心：下午15:30前启程返回丹平社区，傍晚回温馨的家整理衣物、洗个热水澡，避开夜间返程大塞车，神清气爽迎接工作！"
        ]
    }
]

# Ultimate packing checklist for couples roadtrip
CHECKLIST_CATEGORIES = [
    {
        "title": "🏸 户外运动与浪漫互动 (你提到的羽毛球+出片装备)",
        "items": [
            {"name": "羽毛球拍2副 + 防风羽毛球1筒 (大万世居外广场/湖畔草坪/海滩随时开打解压)", "note": "重点带上！傍晚微风打球超舒服"},
            {"name": "极限飞盘/轻量沙滩球 (草坪和沙滩上两人轻松互动，好玩又吸睛)", "note": "轻量不占地"},
            {"name": "赶海小工具组 (折叠小水桶、小耙子、手套，去坝光/百安海滩捡贝壳抓寄居蟹)", "note": "小红书爆款赶海必备"},
            {"name": "便携蓝牙复古小音箱 (野餐/湖畔/海风中播放轻柔歌单，氛围感神器)", "note": "Marshall/JBL"},
            {"name": "轻便三脚架蓝牙自拍杆 / 拍立得 (情侣两人合影不求路人，分分钟出大片)", "note": "随时捕捉女朋友笑脸"}
        ]
    },
    {
        "title": "💄 女友专属呵护与随身百宝箱 (极具情商细节)",
        "items": [
            {"name": "轻便透气防晒衣 + UPF50+黑胶遮阳伞 + 偏光墨镜 (海边山野双重防晒，不晒黑)", "note": "女孩子最在意"},
            {"name": "防蚊喷雾/驱蚊贴 + 泰国青草膏 (广东山野水边小黑飞多，防叮咬止痒神物)", "note": "放随身包里随取随用"},
            {"name": "车载便携小毛毯/软披肩 (副驾空调吹久了容易膝盖着凉，贴心指数五星)", "note": "车内必备"},
            {"name": "维达便携抽纸 + 75%酒精独立湿巾 + 湿厕纸 (吃完海鲜窑鸡擦手清洁)", "note": "卫生保障"},
            {"name": "便携发绳/抓夹 + 小木梳 (海边山风吹乱头发时随手扎起，拍照利落)", "note": "随时整理发型"},
            {"name": "大容量保温水杯 (提前装好温热柠檬水或红枣枸杞茶，随时暖胃解腻)", "note": "健康暖心"},
            {"name": "备用涉水洞洞鞋/凉鞋 + 换洗干T恤一套 (溯溪或海边踩水湿身可即刻换下)", "note": "干爽舒服回家睡"}
        ]
    },
    {
        "title": "⛺ 舒适露营与车内后备箱收纳",
        "items": [
            {"name": "便携铝合金折叠月亮椅×2 (收纳起来极小，湖边海边一撑就是VIP观景点)", "note": "比硬石凳舒服百倍"},
            {"name": "加厚防潮防水铝膜野餐垫 (大草坪铺开，躺着吹风刷剧极度惬意)", "note": "200×200cm大号"},
            {"name": "便携车载保温冷藏包 + 冰袋 (放两杯喜茶/霸王茶姬/冰镇气泡水，随时喝冷饮)", "note": "快乐源泉"},
            {"name": "车载加厚抽绳垃圾袋一卷 (户外无痕露营，随手打包所有果皮包装纸带走)", "note": "文明自驾"}
        ]
    },
    {
        "title": "🚗 车辆驾驶与长途安全保障",
        "items": [
            {"name": "双口车载快充头 65W + 苹果/Type-C快充线各1根 (两台手机导航拍照全天不断电)", "note": "避免电量焦虑"},
            {"name": "出风口防抖重力手机支架 (高德导航视角平视无遮挡)", "note": "驾驶安全第一"},
            {"name": "整箱500ml矿泉水一箱放后备箱 (随时补水，踩泥玩沙后也可当流动水源冲洗手脚)", "note": "万能用途"},
            {"name": "便携车载充气泵 + 胎压计 (出发前核对冷胎压2.3-2.5bar，高速安心驾驶)", "note": "长途必备"},
            {"name": "行车记录仪存储卡清空核查 (确保循环录像正常，沿途记录跨海大桥绝美风景)", "note": "安全兜底"}
        ]
    },
    {
        "title": "🛡️ 证件与应急药品 (以防万一)",
        "items": [
            {"name": "双人身份证原件 (景区购票核验、检查站备用)", "note": "必备"},
            {"name": "20000mAh快充移动电源充电宝 (下车游玩全天拍照续航保障)", "note": "随身携带"},
            {"name": "便携药盒 (创口贴、布洛芬、晕车贴、健胃消食片、氯雷他定抗过敏)", "note": "吃海鲜防过敏"},
            {"name": "大号晴雨两用伞2把 (放在主驾/副驾车门储物格，随手可取)", "note": "遮阳挡雨两不误"}
        ]
    }
]

print("Building ultimate HTML...")
