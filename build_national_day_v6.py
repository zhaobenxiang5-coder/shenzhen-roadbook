import json

NATIONAL_DAY_DB = [
    {
        "id": "national_day_d1",
        "tab": "national_day",
        "day_num": 1,
        "date_str": "10月1日 · 国庆首日 (避大堵)",
        "tag_line": "不上高速避开全网红暴 · 森林湖畔水杉草坪 · 瓦煲黄鳝饭",
        "driving_summary": "单程仅 15km · 20分钟 · 丹平快速地面辅道/平吉大道直达（不走任何收费拥堵高速，0拥堵风险）",
        "weather_info": "🌤️ 秋高气爽 23℃~31℃ · 东北风2级 · 紫外线中等 · 最佳日落 18:10",
        "budget_dual": "双人全天约 ¥130 - ¥170 (瓦煲黄鳝饭+猪肚鸡，0门票0停车0高速)",
        "feather_ball_spot": "🏸 凤岗官井头水库后山草坪 / 平湖新南大草坪（四面环林，地面平缓无风，打羽毛球极舒适）",
        "plans": [
            {
                "key": "A",
                "badge": "老司机首选",
                "title": "凤岗官井头水库森林步道 × 龙凤后山大草坪慢生活",
                "spot_desc": "国庆第1天全省高速必红暴！我们逆向走地面快速20分钟直插凤岗官井头水库与龙凤后山。高大水杉林环抱清澈水库，成片开阔平整大草坪。带上羽毛球拍和充气沙发，吹微风刷朋友圈看别人在高速上堵车，极度松弛。",
                "main_amap": "https://uri.amap.com/search?keyword=官井头水库",
                "parking_guide": "🅿️ 官井头水库外围道旁车位及后山平整开阔场：完全免费，车位充足随停。",
                "real_photo": "https://images.unsplash.com/photo-1510312305653-8ed496efae75?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "10:30 - 10:55", "desc": "丹平社区出发经平湖平吉大道直接开到凤岗官井头水库，全程20分钟无红灯畅行。"},
                    {"time": "11:00 - 13:00", "desc": "避开午间客流，在水库旁老牌私房馆吃炭火现焗台山黄鳝饭，焦脆金黄锅巴喷香扑鼻。"},
                    {"time": "13:30 - 16:30", "desc": "湖畔大草坪支起充气沙发和月亮椅，铺开野餐垫放轻柔音乐，在树荫下打羽毛球。"},
                    {"time": "16:30 - 18:30", "desc": "漫步南门山天鹅湖绿道与风雨桥，看日落余晖将湖面染红。"},
                    {"time": "18:30 - 19:15", "desc": "悠闲开回丹平社区，沿途毫无堵车，回家看国庆晚会大联欢。"}
                ],
                "play_cluster": [
                    {"name": "官井头水库环湖水杉步道", "desc": "水质澄碧，两岸高大水杉随秋意渐泛金黄，水鸟聚集。", "amap": "https://uri.amap.com/search?keyword=官井头水库"},
                    {"name": "南门山森林公园（天鹅湖水上风雨桥）", "desc": "离官井头仅8分钟车程，万亩荔枝林与湖泊环绕，有专门的绿道、风雨桥和大面积野餐草坪。", "amap": "https://uri.amap.com/search?keyword=南门山森林公园"},
                    {"name": "凤岗历史碉楼古村落", "desc": "藏在深林里的西式与客家结合碉楼古建筑，人少安静，青苔爬满老砖墙，复古文艺大片随手拍。", "amap": "https://uri.amap.com/search?keyword=凤岗碉楼"}
                ],
                "food_cluster": [
                    {"name": "凤岗老街正宗炭火瓦煲黄鳝饭", "spec": "现点现焗台山黄鳝饭（手撕黄鳝丝拌金黄香脆锅巴，粒粒泛光）、椒盐九肚鱼、白灼粉肠", "price": "双人约 ¥120", "amap": "https://uri.amap.com/search?keyword=凤岗客家黄鳝饭"},
                    {"name": "龙凤山庄后山客家农家大锅鸭", "spec": "柴火土灶烧鸭、客家酿苦瓜豆腐煲、农家石磨滑豆腐、清炒番薯叶", "price": "双人约 ¥110", "amap": "https://uri.amap.com/search?keyword=凤岗客家农家乐"},
                    {"name": "南门山深林湖畔茶社", "spec": "手冲冷萃陈皮白茶、鲜煮姜汁红薯甜汤、花生芝麻酥饼", "price": "双人约 ¥45", "amap": "https://uri.amap.com/search?keyword=南门山公园咖啡"}
                ]
            },
            {
                "key": "B",
                "badge": "平湖近郊",
                "title": "平湖生态园千亩湿地环湖跑道 × 浓香胡椒猪肚鸡",
                "spot_desc": "距离丹平家门口仅6公里！数千亩水库湿地与无机动车打扰的环湖绿道，绿树成荫微风阵阵。可以带双人羽毛球拍在林荫开阔处酣畅对拉，漫步看白鹭掠过水面，松弛惬意。",
                "main_amap": "https://uri.amap.com/search?keyword=平湖生态园",
                "parking_guide": "🅿️ 平湖生态园正门生态停车场：车位极多，免费停放。",
                "real_photo": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "14:00 - 14:15", "desc": "丹平家门口6公里直达平湖生态园正门，车位宽敞随停。"},
                    {"time": "14:30 - 17:00", "desc": "数千亩环湖湿地漫步，在新南大草坪打羽毛球、扔飞盘。"},
                    {"time": "17:30 - 19:30", "desc": "回南湾/丹竹头老店喝热气腾腾浓白胡椒猪肚鸡汤，暖胃爽脆。"}
                ],
                "play_cluster": [
                    {"name": "平湖生态园环湖骑行漫道", "desc": "数千亩湿地与湖泊环绕，无机动车打扰，绿树成荫。", "amap": "https://uri.amap.com/search?keyword=平湖生态园"},
                    {"name": "平湖新南水杉林大草坪", "desc": "深秋水杉林渐红，湖边有一大片开阔缓坡草坪，打羽毛球避风。", "amap": "https://uri.amap.com/search?keyword=平湖生态园草坪"}
                ],
                "food_cluster": [
                    {"name": "南湾/丹竹头老牌胡椒猪肚鸡总店", "spec": "浓白海南白胡椒煲土鸡汤（第一碗喝汤暖身提神）、爽脆猪肚片、手打香菇肉丸", "price": "双人约 ¥140", "amap": "https://uri.amap.com/search?keyword=南湾客家猪肚鸡"},
                    {"name": "平湖地道潮汕生腌与砂锅粥", "spec": "生腌膏蟹拼皮皮虾、鲜虾生蚝砂锅粥、炸普宁豆干", "price": "双人约 ¥120", "amap": "https://uri.amap.com/search?keyword=平湖生腌海鲜"}
                ]
            },
            {
                "key": "C",
                "badge": "复古工业",
                "title": "平湖凤凰山矿山公园深潭 × 守珍街老铁路漫步",
                "spot_desc": "探索平湖鲜为人知的工业遗迹与矿山公园湖泊，深潭如碧玉，老铁路旁林荫安静，几乎没有外地游客，拍照极有胶片复古故事感。",
                "main_amap": "https://uri.amap.com/search?keyword=凤凰山矿山公园",
                "parking_guide": "🅿️ 矿山公园入口停车场：免费停车。",
                "real_photo": "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "15:00 - 15:30", "desc": "漫步凤凰山矿山公园与老火车站，探访深碧色矿坑湖。"},
                    {"time": "17:30 - 19:30", "desc": "平湖老街吃生滚猪杂及第汤与炒牛河，市井接地气。"}
                ],
                "play_cluster": [
                    {"name": "凤凰山矿坑碧玉湖观景台", "desc": "环绕碧绿矿坑湖建立的悬空木质观景长廊，四周断崖壁立，水色呈现青蓝色。", "amap": "https://uri.amap.com/search?keyword=凤凰山矿山公园"},
                    {"name": "平湖老火车站怀旧铁轨", "desc": "保留完好的工业站台与老铁轨，红砖建筑拍照很有年代感。", "amap": "https://uri.amap.com/search?keyword=平湖火车站"}
                ],
                "food_cluster": [
                    {"name": "平湖老街深夜大排档", "spec": "鲜炸酥脆小肉丸、生滚枸杞叶猪杂及第汤、现炒干炒牛河", "price": "双人约 ¥55", "amap": "https://uri.amap.com/search?keyword=平湖老街大排档"}
                ]
            }
        ]
    },

    {
        "id": "national_day_d2",
        "tab": "national_day",
        "day_num": 2,
        "date_str": "10月2日 · 客家古韵",
        "tag_line": "避世300年客家围屋古村 · 樟林古道 · 柴火大锅煨三杯鸭",
        "driving_summary": "单程约 46km · 48分钟 · 水官高速→深汕西或惠阳内环直达（国庆高速全免费）",
        "weather_info": "⛅ 多云间晴 24℃~30℃ · 东南风微弱 · 紫外线中等 · 最佳日落 18:09",
        "budget_dual": "双人全天约 ¥180 - ¥230 (大铁锅三杯鸭+天街咖啡，0门票0停车)",
        "feather_ball_spot": "🏸 叶挺故里森林大草坪 / 秋长谷里村口禾坪（百年古樟遮阴，平整宽阔）",
        "plans": [
            {
                "key": "A",
                "badge": "田园小资",
                "title": "惠阳秋长谷里客家古村落 × 碧溪老围群",
                "spot_desc": "300年历史的大型客家围屋四合院落，背靠梯田和老樟树林。这里改建成了艺术书吧与精品咖啡馆，游人很少，没有商业叫卖。下午在庭院品一杯桂花拿铁，村口开阔处还能打上一场羽毛球。",
                "main_amap": "https://uri.amap.com/search?keyword=秋长谷里",
                "parking_guide": "🅿️ 秋长谷里专属地面生态停车场：完全免费，车位充足。",
                "real_photo": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:30 - 10:20", "desc": "水官高速转深汕西至惠阳内环路，高速全线免费畅通，直达秋长谷里。"},
                    {"time": "10:30 - 12:30", "desc": "漫步300年客家围屋四合院落与碧溪老围，无商业喧嚣，青砖古朴拍照绝美。"},
                    {"time": "12:30 - 14:00", "desc": "柴火大铁锅慢煨三杯鸭配手打艾粄糍粑，肉质鲜香扎实。"},
                    {"time": "14:30 - 16:30", "desc": "谷里天街古树庭院喝手冲咖啡与桂花冰拿铁，树荫下清风吹拂。"},
                    {"time": "16:30 - 18:00", "desc": "叶挺将军故里森林公园平整草坪打羽毛球，呼吸纯氧。"},
                    {"time": "18:00 - 19:00", "desc": "傍晚顺畅返程丹平，避开夜间车流。"}
                ],
                "play_cluster": [
                    {"name": "秋长谷里客家古宅天街", "desc": "青砖围屋改建的书舍、陶艺与咖啡空间，古树参天环境清幽。", "amap": "https://uri.amap.com/search?keyword=秋长谷里"},
                    {"name": "叶挺将军纪念园（免费国家级生态园）", "desc": "离秋长仅5分钟车程，红花绿树掩映，有清澈人工湖与成片幽静大草坪，打羽毛球绝佳。", "amap": "https://uri.amap.com/search?keyword=叶挺将军故里"},
                    {"name": "碧溪老围客家碉楼群", "desc": "原生态古村落，石板路上有散养土鸡走动，梯田稻谷飘香，拍照具有油画般质感。", "amap": "https://uri.amap.com/search?keyword=惠阳碧溪村"}
                ],
                "food_cluster": [
                    {"name": "秋长古村旁老农庄柴火三杯鸭", "spec": "大铁锅柴火慢煨三杯鸭（色泽红润醇厚、肉质紧实不柴）、现打客家艾粄糍粑、清蒸山坑鱼", "price": "双人约 ¥150", "amap": "https://uri.amap.com/search?keyword=惠阳秋长客家农家乐"},
                    {"name": "谷里天街古树庭院精品咖啡", "spec": "桂花冰摇拿铁、手作陈皮冷萃、手冲巴拿马瑰夏、客家黄酒酿芝士蛋糕", "price": "双人约 ¥60", "amap": "https://uri.amap.com/search?keyword=秋长谷里咖啡"},
                    {"name": "惠阳叶挺故里客家擂茶馆", "spec": "传统现擂山青擂茶（炒米花生芝麻香气四溢）、客家糍粑、艾草青团", "price": "双人约 ¥45", "amap": "https://uri.amap.com/search?keyword=惠阳客家擂茶"}
                ]
            },
            {
                "key": "B",
                "badge": "艺术水塘",
                "title": "深圳观澜版画村 × 牛湖老街手作工坊",
                "spot_desc": "若当天去惠州方向车流增加，转走清平快速去观澜。古村依山傍水，排屋古色古香，碉楼矗立，池塘睡莲盛开，版画工坊文艺气息极浓厚，清晨早去毫无喧嚣。",
                "main_amap": "https://uri.amap.com/search?keyword=观澜版画村",
                "parking_guide": "🅿️ 观澜版画基地生态停车场：车位充足，10元/天。",
                "real_photo": "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:00 - 09:40", "desc": "清平快速直达观澜版画村，清晨人少古朴。"},
                    {"time": "09:45 - 12:00", "desc": "参观古村水塘碉楼与版画工坊，漫步鳌湖艺术村老街。"},
                    {"time": "12:00 - 13:30", "desc": "观澜老街吃猪油蒜香客家腌面配三及第及鲜枸杞叶汤。"}
                ],
                "play_cluster": [
                    {"name": "观澜版画原创产业基地", "desc": "客家老围屋与现代版画工坊融合，池塘倒影碉楼，睡莲盛放。", "amap": "https://uri.amap.com/search?keyword=观澜版画基地"},
                    {"name": "鳌湖艺术村文艺老街", "desc": "独立艺术家入驻的自然村落，古宅壁画与雕塑随处可见。", "amap": "https://uri.amap.com/search?keyword=鳌湖艺术村"}
                ],
                "food_cluster": [
                    {"name": "观澜老街梅州客家腌面总店", "spec": "金牌猪油蒜香客家腌面、鲜枸杞叶三及第猪杂滚汤、手工酿豆腐", "price": "双人约 ¥50", "amap": "https://uri.amap.com/search?keyword=观澜老街客家腌面"},
                    {"name": "牛湖古碉楼下民间柴火煨鸡", "spec": "荷叶清蒸走地土鸡、野生山坑笋炒土花肉、清甜玉米粑粑", "price": "双人约 ¥110", "amap": "https://uri.amap.com/search?keyword=观澜农家乐"}
                ]
            },
            {
                "key": "C",
                "badge": "山野秘境",
                "title": "坪山金龟自然村山谷漫步 × 溪边露营",
                "spot_desc": "隐匿在坪山深处的山水画卷，溪流潺潺，两旁全是绿树与文艺小民居，村里有野果树与手作小店，人少空气湿润清爽，完全不收门票。",
                "main_amap": "https://uri.amap.com/search?keyword=金龟自然村",
                "parking_guide": "🅿️ 金龟村游客服务中心车位：免费停放。",
                "real_photo": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "10:00 - 10:45", "desc": "探访坪山金龟自然村，漫步林下小溪，在无风山谷草坪打羽毛球。"},
                    {"time": "12:00 - 13:30", "desc": "品尝农家手磨山泉豆腐煲与土猪排骨汤。"}
                ],
                "play_cluster": [
                    {"name": "金龟自然村溪谷步道", "desc": "清澈见底的浅溪穿村而过，山花漫野，野趣天然。", "amap": "https://uri.amap.com/search?keyword=金龟自然村"},
                    {"name": "金龟露营小镇缓坡大草坪", "desc": "四面环山的谷底大草坪，两侧溪水清浅，微风和煦，打羽毛球不乱飞。", "amap": "https://uri.amap.com/search?keyword=金龟露营小镇"}
                ],
                "food_cluster": [
                    {"name": "金龟村山泉水石磨豆腐农庄", "spec": "金黄焦香煎酿山泉豆腐、香煎土鸡蛋、苦斋婆土猪排骨汤", "price": "双人约 ¥100", "amap": "https://uri.amap.com/search?keyword=金龟村农家乐"}
                ]
            }
        ]
    },

    {
        "id": "national_day_d3",
        "tab": "national_day",
        "day_num": 3,
        "date_str": "10月3日 · 纯净深蓝海滩",
        "tag_line": "深汕鲘门百安海滩 · 渐变青蓝果冻海 · 渔港生猛海鲜大餐",
        "driving_summary": "单程约 110km · 1小时20分 · 沈海高速深汕段早8:00前出发畅行无阻（国庆高速全免费）",
        "weather_info": "☀️ 晴朗碧海 25℃~32℃ · 海面平缓 · 紫外线极高 (必涂防晒) · 最佳日落 18:08 (渔火落日)",
        "budget_dual": "双人全天约 ¥260 - ¥330 (手打马鲛鱼丸汤+满膏红鲟饭大餐，0海滩门票0高速)",
        "feather_ball_spot": "🏸 鲘门百安沙滩硬质退潮沙坪 / 鲘门港滨海大广场（退潮后沙硬如地毯，打沙滩羽毛球超爽）",
        "plans": [
            {
                "key": "A",
                "badge": "纯蓝沙滩",
                "title": "深汕特别合作区鲘门百安海滩 × 老渔港日落千帆",
                "spot_desc": "双月湾国庆会彻底堵瘫！我们反向多开半小时直奔深汕百安海滩。沙质细腻如粉，海水呈渐变青蓝色，关键是没有商业圈地与遮阳伞强制消费！两人可以在海边踩水、打沙滩羽毛球、捡贝壳，黄昏到鲘门渔港看千帆归航。",
                "main_amap": "https://uri.amap.com/search?keyword=百安海滩",
                "parking_guide": "🅿️ 百安村口海滨开敞停车场：免费/15元封顶，车位宽敞无拥堵。",
                "real_photo": "https://images.unsplash.com/photo-1506929562872-bb421503ef21?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1535473897047-b6745f657a84?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "07:30 - 09:00", "desc": "黄金早鸟窗口！早晨7:30从丹平出发上沈海高速，高速全免费，一路向东90分钟直抵鲘门百安沙滩。"},
                    {"time": "09:15 - 12:30", "desc": "踩在粉白细腻无人的海滩上，清澈渐变青蓝色海水漫过脚踝，打沙滩羽毛球、捡贝壳赶海！"},
                    {"time": "12:30 - 14:30", "desc": "鲘门港口老牌海鲜饭店：现煮手打鲜马鲛鱼丸汤、满膏红鲟海鲜蒸糯米饭，鲜甜冲顶！"},
                    {"time": "15:00 - 16:30", "desc": "驱车沿风车山海滨路漫行，俯瞰半月湾全景，在红泉沙滩吹海风。"},
                    {"time": "16:30 - 18:00", "desc": "鲘门老渔港看夕阳千帆归航，随后早早启程在晚高峰前轻松回到丹平家！"}
                ],
                "play_cluster": [
                    {"name": "深汕百安半月湾沙滩", "desc": "天然纯净细白沙，海水呈渐变青蓝色，无商业圈地收费。", "amap": "https://uri.amap.com/search?keyword=百安海滩"},
                    {"name": "鲘门老渔港码头", "desc": "渔船鸣笛归港，漫天橘红晚霞映照波光粼粼的港湾，渔家风情拉满。", "amap": "https://uri.amap.com/search?keyword=鲘门港"},
                    {"name": "红泉原生态沙滩", "desc": "与百安相邻的海滩，沙滩平缓，几乎没有游客，沙硬平整适合打羽毛球。", "amap": "https://uri.amap.com/search?keyword=红泉沙滩"},
                    {"name": "深汕沿海风车山观景台", "desc": "白色巨大风车在蔚蓝天际下缓缓转动，俯瞰月牙形海湾全景。", "amap": "https://uri.amap.com/search?keyword=深汕风车山"}
                ],
                "food_cluster": [
                    {"name": "鲘门港口老牌海鲜饭店", "spec": "现煮手打鲜马鲛鱼丸汤（汤清肉脆弹性惊人）、满膏红鲟蒸糯米饭、姜葱爆海白虾", "price": "双人约 ¥210", "amap": "https://uri.amap.com/search?keyword=鲘门海鲜饭店"},
                    {"name": "百安海滨渔家乐现捞加工小铺", "spec": "蒜蓉清蒸海捕野生生蚝、椒盐皮皮虾、鲘门特产海马滋补汤", "price": "双人约 ¥180", "amap": "https://uri.amap.com/search?keyword=鲘门百安海鲜"},
                    {"name": "鲘门老街正宗赤石擂茶", "spec": "传统绿茶花生炒米擂茶、手工菜包粿、香煎马鲛鱼排", "price": "双人约 ¥60", "amap": "https://uri.amap.com/search?keyword=鲘门菜包粿"}
                ]
            },
            {
                "key": "B",
                "badge": "早鸟悬崖",
                "title": "大鹏杨梅坑鹿嘴山庄清晨追光快线",
                "spot_desc": "如果不愿开到深汕，实行【超早鸟策略】：早晨6:30出发直插大鹏杨梅坑鹿嘴山庄看美人鱼悬崖绝壁，海水蔚蓝壮阔。中午11:30在拥堵大潮到来前打道回府！",
                "main_amap": "https://uri.amap.com/search?keyword=鹿嘴山庄",
                "parking_guide": "🅿️ 杨梅坑主停车场：早到抢占一线海景车位。",
                "real_photo": "https://images.unsplash.com/photo-1518495973542-4542c06a5843?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "06:30 - 07:30", "desc": "超早鸟特快：早6:30出发直奔杨梅坑鹿嘴山庄，错开所有车流。"},
                    {"time": "07:30 - 10:30", "desc": "悬崖峭壁看美人鱼海蚀洞，海水湛蓝壮美。"},
                    {"time": "11:00 - 12:30", "desc": "吃南澳老牌金黄野生海胆炒饭，中午12点前准时撤离回丹平！"}
                ],
                "play_cluster": [
                    {"name": "鹿嘴山庄海蚀悬崖步道", "desc": "美人鱼拍摄取景地，悬崖立壁千仞，浩瀚太平洋尽收眼底。", "amap": "https://uri.amap.com/search?keyword=鹿嘴山庄"},
                    {"name": "杨梅坑沿海礁石栈道", "desc": "伴随海浪与礁石的慢行道，清晨海风温和舒适。", "amap": "https://uri.amap.com/search?keyword=杨梅坑鹿嘴栈道"}
                ],
                "food_cluster": [
                    {"name": "南澳杨梅坑老字号海胆炒饭", "spec": "金黄诱人本地野生海胆炒饭（米粒金黄颗颗裹海胆）、柴火窑鸡、清蒸野生海石斑", "price": "双人约 ¥150", "amap": "https://uri.amap.com/search?keyword=大鹏海胆炒饭"},
                    {"name": "水头海鲜街名厨加工排档", "spec": "白灼深海大花虾、避风塘炒本地膏蟹、鲜海虾海鲜粥", "price": "双人约 ¥170", "amap": "https://uri.amap.com/search?keyword=水头海鲜街"}
                ]
            },
            {
                "key": "C",
                "badge": "古村古戏台",
                "title": "惠东范和古村落 × 亚婆角滨海公路慢游",
                "spot_desc": "去亚婆角未过度开发的小海湾，水清沙白，顺路探访有数百年历史的范和古村落，罗冈围屋与古戏台宁静祥和，吃一碗范和正宗猪肠粉。",
                "main_amap": "https://uri.amap.com/search?keyword=范和古村",
                "parking_guide": "🅿️ 范和村口文化广场停车场：免费停车。",
                "real_photo": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1565680018434-b513d5e5fd47?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:00 - 10:15", "desc": "漫游惠东范和古村，探访棋盘式水乡围屋。"},
                    {"time": "11:30 - 13:00", "desc": "尝范和老街百年石磨猪肠粉与亚婆角野生海鲜。"}
                ],
                "play_cluster": [
                    {"name": "范和罗冈围古戏台与古庙", "desc": "六百年历史的水乡古村，布局如棋盘，红墙黑瓦古榕树，安宁静谧。", "amap": "https://uri.amap.com/search?keyword=范和古村戏台"}
                ],
                "food_cluster": [
                    {"name": "范和老街百年石磨猪肠粉", "spec": "刚出炉米香扑鼻的肠粉卷秘制肉末香菇酱、葱油干拌石磨粉、炸小油角", "price": "双人约 ¥35", "amap": "https://uri.amap.com/search?keyword=惠东范和古村美食"}
                ]
            }
        ]
    },

    {
        "id": "national_day_d4",
        "tab": "national_day",
        "day_num": 4,
        "date_str": "10月4日 · 跨海工程与世界美食",
        "tag_line": "飞驰深中通道跨海大桥 · 顺德容桂老街市井寻味 · 现蒸桑拿鸡",
        "driving_summary": "单程约 95km · 1小时15分 · 丹平经机荷高速直上深中通道伶仃洋大桥（国庆高速全免费）",
        "weather_info": "🌤️ 清爽微风 24℃~31℃ · 伶仃洋海风徐徐 · 紫外线中等 · 最佳日落 18:07 (跨海大桥晚霞)",
        "budget_dual": "双人全天约 ¥240 - ¥310 (深中通道¥0免费！桑拿鸡+双皮奶大快朵颐)",
        "feather_ball_spot": "🏸 德胜河南岸江滨公园绿道草坪 / 渔人码头滨水长堤（江风拂面，绿草如茵）",
        "plans": [
            {
                "key": "A",
                "badge": "工程与美味",
                "title": "深中通道跨海体验 × 顺德容桂老街市井寻味",
                "spot_desc": "自驾打卡全球超级工程深中通道与伶仃洋大桥，跨海视野极为震撼！坚决避开顺德大良清晖园的人山人海，直奔容桂渔人码头周边的文创老街与市井小巷，漫步德胜河畔绿道，吃正宗桑拿鸡与双皮奶。",
                "main_amap": "https://uri.amap.com/search?keyword=容桂渔人码头",
                "parking_guide": "🅿️ 德胜河南岸地下车库及文创园停车位：车位丰富，有智能引导。",
                "real_photo": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "08:30 - 09:50", "desc": "经机荷高速直上深中通道，跨越伶仃洋大桥，全程免费体验世界级超级工程！"},
                    {"time": "10:00 - 12:30", "desc": "顺德容桂老街市井寻味：漫步柴油机1959红砖文创园，探访300年树生桥古水乡。"},
                    {"time": "12:30 - 14:30", "desc": "阿多私房菜：现点活鸡剔骨桑拿蒸，精准沙漏3分钟出锅嫩滑到爆汁，原汁鸡汤煮菜心！"},
                    {"time": "14:30 - 16:30", "desc": "民信老铺吃原只水牛奶双皮奶，渔人码头河畔喝水牛乳拿铁。"},
                    {"time": "16:30 - 18:00", "desc": "德胜河南岸江滨公园：吹着徐徐江风，在草坪大平台打羽毛球散步消食。"},
                    {"time": "18:30 - 20:00", "desc": "傍晚跨越深中通道返程，看落日余晖洒满伶仃洋海面与大桥华灯初上，壮观无比！"}
                ],
                "play_cluster": [
                    {"name": "德胜河南岸滨江公园（江风草坪）", "desc": "沿顺德母亲河德胜河而建的带状滨江公园，绿草如茵，江风习习，对岸是顺德新城现代天际线，在此打羽毛球神清气爽！", "amap": "https://uri.amap.com/search?keyword=德胜河南岸公园"},
                    {"name": "柴油机1959工业文创园", "desc": "由老工厂改造成的红砖红墙文创区，林荫遮蔽，有许多创意手作工坊、咖啡小馆与老厂房涂鸦，拍照极有复古格调。", "amap": "https://uri.amap.com/search?keyword=柴油机1959"},
                    {"name": "容桂树生桥历史奇观", "desc": "300年榕树气根自然缠绕形成的天然古桥，旁边是宁静的江南水乡河涌，老人们在树下下棋乘凉，毫无商业喧嚣。", "amap": "https://uri.amap.com/search?keyword=树生桥"},
                    {"name": "容桂渔人码头涂鸦街", "desc": "沿江怀旧风情街区，有灯塔、江风步道与巨幅猫咪涂鸦墙，拍照打卡胜地。", "amap": "https://uri.amap.com/search?keyword=容桂渔人码头"}
                ],
                "food_cluster": [
                    {"name": "容桂街坊私藏·阿多地道桑拿菜", "spec": "现点活鸡剔骨桑拿蒸（精准沙漏3分钟揭盖，鸡肉嫩滑多汁毫无纤维感）、原汁鸡骨虫草花粥底、丝瓜蒸脆鲩鱼片", "price": "双人约 ¥180", "amap": "https://uri.amap.com/search?keyword=容桂阿多桑拿鸡"},
                    {"name": "民信老铺容桂分店（免大良排队）", "spec": "热原只水牛奶双皮奶、现炸香脆牛奶块、生滚及第牛肉粥、伦教糕", "price": "双人约 ¥60", "amap": "https://uri.amap.com/search?keyword=容桂民信老铺"},
                    {"name": "德胜河畔·水牛乳咖啡小馆", "spec": "顺德水牛奶拿铁、黑松露巴斯克芝士蛋糕、金凤茶王冷萃", "price": "双人约 ¥60", "amap": "https://uri.amap.com/search?keyword=容桂渔人码头咖啡"},
                    {"name": "红星光发正宗煲仔饭", "spec": "炭火黄鳝窝蛋牛肉煲仔饭（底焦金黄锅巴酥脆起沙）、白灼牛柏叶", "price": "双人约 ¥80", "amap": "https://uri.amap.com/search?keyword=红星光发煲仔饭"}
                ]
            },
            {
                "key": "B",
                "badge": "稻香海风",
                "title": "中山南朗崖口村海边千亩金色稻田",
                "spot_desc": "下深中通道第一站就在中山南朗下高速。崖口村有上千亩临海金色稻田，彩色集装箱咖啡街倚海而建。海风拂面，稻香四溢，点一杯冷萃咖啡看海鸟翻飞，惬意浪漫。",
                "main_amap": "https://uri.amap.com/search?keyword=崖口村稻田",
                "parking_guide": "🅿️ 崖口稻田驿站停车场：停车位丰富。",
                "real_photo": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:00 - 10:00", "desc": "深中通道下桥第一站直达中山南朗崖口村。"},
                    {"time": "10:15 - 12:30", "desc": "漫步海边千亩金色稻田，集装箱咖啡街喝海风生椰拿铁。"},
                    {"time": "12:30 - 14:00", "desc": "崖口人家吃皮薄如纸现包鲜虾蟹子云吞与脆皮黄鳝煲仔饭。"}
                ],
                "play_cluster": [
                    {"name": "崖口千亩临海金色稻田", "desc": "秋收季节金色稻浪起伏，旁边就是蔚蓝海堤，拍照极有宫崎骏漫画感。", "amap": "https://uri.amap.com/search?keyword=崖口村稻田"},
                    {"name": "翠亨村孙中山故里红墙步道", "desc": "离崖口村5分钟，红砖欧式中西合璧建筑，林荫蔽日，草坪修剪平整。", "amap": "https://uri.amap.com/search?keyword=孙中山故居"}
                ],
                "food_cluster": [
                    {"name": "中山崖口人家正宗馄饨铺", "spec": "皮薄如蝉翼现包鲜虾蟹子云吞、炭火生焗脆皮黄鳝煲仔饭（底焦金黄酥脆）", "price": "双人约 ¥95", "amap": "https://uri.amap.com/search?keyword=中山崖口云吞"},
                    {"name": "崖口稻田临海集装箱咖啡", "spec": "海风生椰拿铁、稻香冷萃咖啡、手作柠檬茶", "price": "双人约 ¥50", "amap": "https://uri.amap.com/search?keyword=崖口村集装箱咖啡"}
                ]
            },
            {
                "key": "C",
                "badge": "骑楼老城",
                "title": "中山石岐老街孙文西路 × 岐江夜色",
                "spot_desc": "南洋骑楼风格的百年老街，避开午后大太阳，傍晚漫步在骑楼回廊下，吹着岐江晚风，打卡百年老字号石岐乳鸽，市井氛围浓厚。",
                "main_amap": "https://uri.amap.com/search?keyword=孙文西路步行街",
                "parking_guide": "🅿️ 兴中广场地下停车场：车位海量，直通步行街。",
                "real_photo": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "14:30 - 15:40", "desc": "深中通道直插中山石岐老街孙文西路。"},
                    {"time": "16:00 - 18:30", "desc": "漫步南洋骑楼街与岐江公园，吃石岐佬玻璃脆皮红烧乳鸽。"}
                ],
                "play_cluster": [
                    {"name": "孙文西路南洋骑楼文化街", "desc": "百年粉彩骑楼回廊，欧亚混血建筑风格，夜景灯光温馨迷人。", "amap": "https://uri.amap.com/search?keyword=孙文西路步行街"},
                    {"name": "岐江公园造船厂工业遗址", "desc": "荣获国际景观大奖的公园，铁轨水塔与江畔草坪相映成趣。", "amap": "https://uri.amap.com/search?keyword=岐江公园"}
                ],
                "food_cluster": [
                    {"name": "石岐佬老牌传统中山粤菜", "spec": "百年招牌红烧石岐乳鸽（玻璃脆皮流汁）、香炸大菠萝包、特色菊花炸鱼球", "price": "双人约 ¥150", "amap": "https://uri.amap.com/search?keyword=石岐红烧乳鸽"}
                ]
            }
        ]
    },

    {
        "id": "national_day_d5",
        "tab": "national_day",
        "day_num": 5,
        "date_str": "10月5日 · 黄金周收官收心",
        "tag_line": "东莞第一峰银瓶山溪谷 · 沿溪洗肺慢步 · 山泉水炖走地鸡汤",
        "driving_summary": "单程约 50km · 48分钟 · 从莞深高速→潮莞高速谢岗出口（国庆高速全免费，路况畅顺）",
        "weather_info": "⛅ 阴天微凉 22℃~28℃ · 山谷湿润负离子充盈 · 紫外线弱 · 最佳日落 18:06",
        "budget_dual": "双人全天约 ¥170 - ¥220 (纯正泉水土鸡汤，0门票0停车0高速)",
        "feather_ball_spot": "🏸 银瓶山正门外平整生态大草坪（四面群山环抱阻风，下山打羽毛球超爽快）",
        "plans": [
            {
                "key": "A",
                "badge": "第一峰洗肺",
                "title": "东莞第一峰银瓶山（谢岗入口沿溪谷洗肺）",
                "spot_desc": "拒绝人满为患的梧桐山！自驾至东莞第一峰银瓶山谢岗景区。沿溪流木栈道而上，林荫遮蔽率95%，沿途飞瀑流泉，空气清冽湿润。轻徒步2小时吸氧洗肺，为假期画上清爽健康的句号。",
                "main_amap": "https://uri.amap.com/search?keyword=银瓶山森林公园谢岗景区",
                "parking_guide": "🅿️ 银瓶山谢岗第一生态停车场：完全免费，环境平整整洁。",
                "real_photo": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1543353071-873f17a7a088?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:30 - 10:20", "desc": "从莞深高速转潮莞谢岗出口，高速全线免费畅通，50分钟直抵东莞第一峰银瓶山。"},
                    {"time": "10:30 - 13:00", "desc": "沿溪谷木栈道轻徒步，林荫遮蔽率95%，听飞瀑流泉，呼吸高浓度纯氧洗肺！"},
                    {"time": "13:00 - 14:30", "desc": "山脚农夫饭庄：喝山泉水慢火煲农家走地鸡汤，鲜甜回甘毫无油腻，配紫苏炒山坑螺。"},
                    {"time": "14:30 - 16:00", "desc": "银瓶山正门宽广平整生态草坪：轻挥羽毛球拍运动出身透汗，整个人神清气爽！"},
                    {"time": "16:00 - 17:00", "desc": "错开夜间返程大塞车，下午5点前温馨回到丹平家，洗热水澡收心迎接节后工作。"}
                ],
                "play_cluster": [
                    {"name": "银瓶山谢岗峡谷溪流栈道", "desc": "依溪而建的平缓木栈道，沿途瀑布跌宕，凉意扑面，林荫无暴晒。", "amap": "https://uri.amap.com/search?keyword=银瓶山森林公园"},
                    {"name": "银瓶山正门生态大草坪", "desc": "数千平米平整的草坪广场，四周群山环绕，下山后打羽毛球神清气爽！", "amap": "https://uri.amap.com/search?keyword=银瓶山森林公园草坪"},
                    {"name": "崖山森林水库观景台", "desc": "离谢岗8分钟车程，宁静的冷门小水库，青山倒映在如镜水面。", "amap": "https://uri.amap.com/search?keyword=崖山森林公园"}
                ],
                "food_cluster": [
                    {"name": "银瓶山山脚谢岗生态农夫饭庄", "spec": "清冽山泉水慢火煲农家走地鸡汤（鲜美甘润回甘毫无油腻）、紫苏大火爆炒野生山坑螺、山水客家酿豆腐", "price": "双人约 ¥150", "amap": "https://uri.amap.com/search?keyword=银瓶山谢岗农家乐"},
                    {"name": "谢岗老街传统石磨碌鹅坊", "spec": "柴火秘制碌鹅配鲜蒸粉肠、农家清炒山渡笋、山水石磨嫩豆腐", "price": "双人约 ¥110", "amap": "https://uri.amap.com/search?keyword=谢岗特色美食"}
                ]
            },
            {
                "key": "B",
                "badge": "最美盘山",
                "title": "盐田三洲田公路自驾慢游 × 茶溪谷水库晚霞",
                "spot_desc": "深圳最美自驾盘山公路之一！无需买景区门票，顺着盘山绿树公路行驶，观赏三洲田水库碧蓝湖水与山林静谧，在沿途观景平台喝杯露营咖啡看黄昏晚霞。",
                "main_amap": "https://uri.amap.com/search?keyword=三洲田水库",
                "parking_guide": "🅿️ 三洲田水库观景平台及茶溪谷外围停车带：10元/天。",
                "real_photo": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "14:30 - 15:15", "desc": "沿三洲田盘山最美公路行驶，沿途俯瞰碧蓝水库。"},
                    {"time": "15:30 - 18:00", "desc": "观景平台喝露营咖啡看晚霞，下山到盐田海鲜街吃爆汁乳鸽。"}
                ],
                "play_cluster": [
                    {"name": "三洲田盘山公路景观带", "desc": "九曲十八弯的森林盘山道，两旁竹林密布，俯瞰碧蓝大水库。", "amap": "https://uri.amap.com/search?keyword=三洲田水库"},
                    {"name": "红花沥水库观景悬空步道", "desc": "盘山公路中途隐藏的静谧水库，湖水碧蓝如九寨。", "amap": "https://uri.amap.com/search?keyword=红花沥水库"}
                ],
                "food_cluster": [
                    {"name": "盐田食街金牌红烧乳鸽王", "spec": "金牌红烧脆皮乳鸽（肉汁四溢）、石磨鲜虾红肠粉、海皇豆腐煲", "price": "双人约 ¥140", "amap": "https://uri.amap.com/search?keyword=盐田红烧乳鸽"}
                ]
            },
            {
                "key": "C",
                "badge": "深山仙居",
                "title": "惠州罗浮山后山酥醪村古道",
                "spot_desc": "从罗浮山后山进入未商业化的酥醪古村，村落隐匿在深山茶园与溪水竹林间，游客稀少，喝一碗酥醪甘冽山泉水熬制的仙人豆腐，宁静祥和。",
                "main_amap": "https://uri.amap.com/search?keyword=酥醪村",
                "parking_guide": "🅿️ 酥醪观下路边生态车位：免费停放。",
                "real_photo": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "10:00 - 11:20", "desc": "探访罗浮山后山未开发的酥醪古村，漫步深山茶园竹林。"},
                    {"time": "12:00 - 14:00", "desc": "喝山泉水炖土猪肉汤与山水仙人豆腐脑，静谧养心。"}
                ],
                "play_cluster": [
                    {"name": "酥醪古观与山泉洗心池", "desc": "千年古观依山就势，清泉自岩缝流出甘甜清冽，深山古刹听钟鸣。", "amap": "https://uri.amap.com/search?keyword=酥醪观"}
                ],
                "food_cluster": [
                    {"name": "酥醪村老村民家宴土猪肉汤", "spec": "深山泉水炖土猪肉汤（只放少许白胡椒，肉香汤清极度甘润）、山水仙人豆腐脑", "price": "双人约 ¥100", "amap": "https://uri.amap.com/search?keyword=酥醪村农家菜"}
                ]
            }
        ]
    }
]

with open("national_day_enhanced_v6.json", "w", encoding="utf-8") as f:
    json.dump(NATIONAL_DAY_DB, f, ensure_ascii=False, indent=2)

print("Generated complete National Day 5-day enhanced database with rich cluster spots and authentic food!")
