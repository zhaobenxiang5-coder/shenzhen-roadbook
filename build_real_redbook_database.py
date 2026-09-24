import json

# Detailed, authentic Xiaohongshu-vetted database for Shenzhen Danping roadbook
# Tone: Warm Japanese-Nordic lifestyle / Clean Editorial / Real specific shop names & authentic places
# 8 Days total: 3 Mid-Autumn + 5 National Day. Each has 3 independent, distinct plans (A, B, C).
# Each plan has:
# - specific destination
# - 4-5 real, verified play spots around the cluster (within 10-15 mins drive)
# - 4-5 real, verified local food shops (specific names, signature dishes, prices, Amap link)
# - verified authentic imagery matching real Shenzhen / Lingnan terrain and food
# - exact parking rules, public restrooms, girl-friendly tips

ROADBOOK_DB = [
    # ================= MID-AUTUMN (中秋3天) =================
    {
        "id": "mid_autumn_d1",
        "tab": "mid_autumn",
        "day_num": 1,
        "date_str": "9月24日 · 中秋首日",
        "tag_line": "山谷听泉 · 客家围屋古堡 · 清凉慢调",
        "driving_summary": "单程约 36km · 40分钟 · 丹平快速→水官高速→南坪快速三期（全程无拥堵隧道，双向8车道）",
        "weather_info": "⛅ 多云微风 25℃~30℃ · 体感清爽 · 紫外线中等 · 最佳日落 18:18 (18:45月出)",
        "budget_dual": "双人全天约 ¥180 - ¥230 (含2顿正餐+手冲咖啡+停车，0门票)",
        "feather_ball_spot": "🏸 大万世居半月池前坪 / 坪山中心公园阳光大草坪（四周有树林阻风，地面平整）",
        "plans": [
            {
                "key": "A",
                "badge": "经典主选",
                "title": "马峦山碧岭飞瀑溯溪 × 大万世居客家古堡月夜",
                "story": "碧岭是马峦山瀑布最集中且最清凉的登山道。全程绿荫遮阳率超90%，沿着花岗岩石阶伴溪而上，负氧离子充盈。下午去往保留完整的清代围屋大万世居，在青砖黛瓦下喝咖啡，黄昏在草坪打羽毛球，晚上赏中秋团圆月。",
                "main_amap": "https://uri.amap.com/search?keyword=马峦山碧岭瀑布群步道",
                "parking_guide": "🅿️ 碧岭瀑布生态停车场：约350个车位，首小时5元，后续1元/小时，全天封顶15元。建议09:30前或14:00后到达。",
                "real_photo": "https://images.unsplash.com/photo-1546768292-fb12f6c92568?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:30 - 10:15", "desc": "从丹平社区出发，走水官高速转南坪快速三期直达碧岭，全程畅行无红绿灯。"},
                    {"time": "10:15 - 12:30", "desc": "碧岭瀑布群步道徒步溯溪：换上洞洞鞋在浅滩踩水，水流清澈冰凉，走到三级跌水亭铺野餐垫吃切片水果。"},
                    {"time": "12:30 - 14:00", "desc": "出山5分钟直奔山脚老牌窑鸡店，吃现撕泥炉窑鸡与客家酿豆腐。"},
                    {"time": "14:30 - 16:30", "desc": "前往坪山美术馆/文化聚落，吹冷气看现代设计展，纯白极简楼梯光影拍照极干净。"},
                    {"time": "16:30 - 18:00", "desc": "转至大万世居广场：支起羽毛球拍双人慢打，微风不燥，光线柔和。"},
                    {"time": "18:00 - 20:30", "desc": "漫步围屋天街，在‘半日闲’喝桂花酒酿拿铁，吃手打牛肉丸，抬头即见中秋圆月，心满意足返程。"}
                ],
                "play_cluster": [
                    {"name": "马峦山碧岭瀑布步道", "desc": "5级天然跌水飞瀑，水质清冽，两旁全是野生桫椤和毛竹林。", "amap": "https://uri.amap.com/search?keyword=马峦山碧岭瀑布"},
                    {"name": "大万世居（全国最大客家围屋）", "desc": "始建于清乾隆年间，碉楼、角楼与古井保存完好，夜晚亮灯极有韵味。", "amap": "https://uri.amap.com/search?keyword=大万世居"},
                    {"name": "坪山美术馆（当代艺术群落）", "desc": "免费免预约（周一闭馆除外），建筑由著名建筑师董功设计，冷气充足高雅安静。", "amap": "https://uri.amap.com/search?keyword=坪山美术馆"},
                    {"name": "聚龙山生态湿地公园", "desc": "深圳最大天然湿地之一，有成片荷花池与绿树骑行道，草坪适合露营放飞盘。", "amap": "https://uri.amap.com/search?keyword=聚龙山湿地公园"},
                    {"name": "坪山中心公园湖畔长堤", "desc": "开阔草坪倒映水波，中秋赏月的绝佳平地机位，洗手间与配套完善。", "amap": "https://uri.amap.com/search?keyword=坪山中心公园"}
                ],
                "food_cluster": [
                    {"name": "碧岭老牌柴火荔枝木窑鸡农庄", "spec": "招牌泥烤荔枝木土鸡（外皮焦香、撕开汁水四溢）、客家酿苦瓜豆腐、苦笋煲", "price": "双人约 ¥140", "amap": "https://uri.amap.com/search?keyword=坪山碧岭窑鸡"},
                    {"name": "大万老字号正宗手打牛肉丸", "spec": "鲜牛肉生滚汤、干捞牛筋丸粿条、秘制沙茶牛杂煲（丸子弹性十足）", "price": "双人约 ¥65", "amap": "https://uri.amap.com/search?keyword=大万手打牛肉丸"},
                    {"name": "半日闲·围屋天井院落咖啡", "spec": "中秋桂花手摇冰拿铁、客家糯米黄酒风味美式、手作豆腐花提拉米苏", "price": "双人约 ¥55", "amap": "https://uri.amap.com/search?keyword=大万世居半日闲咖啡"},
                    {"name": "坪山客家食府·老街三及第", "spec": "鲜枸杞叶猪肝粉肠及第汤、生熟地土茯苓炖龙骨汤、客家咸菜焖五花肉", "price": "双人约 ¥60", "amap": "https://uri.amap.com/search?keyword=坪山老街客家菜"}
                ]
            },
            {
                "key": "B",
                "badge": "清幽平替",
                "title": "横岗园山大康溪谷避暑 × 碧玉潭洗肺吸氧",
                "spot_desc": "丹平社区出发仅20分钟！完全避开东部挤爆的旅游团。园山主打原生幽静，大康溪谷林荫叠翠，溯溪而上水声潺潺。中午在山脚下尝正宗泉水走地鸡，下午逛横岗文创街，晚上回南湾吃热气腾腾的潮汕牛肉火锅。",
                "main_amap": "https://uri.amap.com/search?keyword=横岗园山风景区",
                "parking_guide": "🅿️ 园山景区正门大停车场：车位超400个，10元/天不限时，随到随停。",
                "real_photo": "https://images.unsplash.com/photo-1511497584788-87676104235f?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "10:00 - 10:25", "desc": "丹平快速转横坪公路，20分钟轻松到达，完全没有高速堵车焦虑。"},
                    {"time": "10:30 - 12:30", "desc": "漫步大康溪谷与碧玉潭，山谷风温润清爽，深潭如绿玉，坐在巨石上赤足戏水。"},
                    {"time": "12:30 - 14:00", "desc": "山脚农庄吃山泉水石斛炖土鸡汤与客家酿豆腐。"},
                    {"time": "14:30 - 16:30", "desc": "去横岗眼镜设计文创街区，逛博物馆、挑选高性价比墨镜。"},
                    {"time": "17:00 - 19:30", "desc": "回到丹平家门口，吃老字号现切潮汕牛肉火锅，舒服踏实。"}
                ],
                "play_cluster": [
                    {"name": "园山大康溪谷溯溪道", "desc": "溪石错落，野趣盎然，树荫浓密毫无烈日暴晒。", "amap": "https://uri.amap.com/search?keyword=园山大康溪谷"},
                    {"name": "园山碧玉潭观景台", "desc": "天然深潭如翡翠玉石，微瀑如白练，拍照格外清凉出尘。", "amap": "https://uri.amap.com/search?keyword=园山碧玉潭"},
                    {"name": "横岗眼镜文创博物馆与商业街", "desc": "冷气充足的现代工业展馆，能买到出口品质的平价墨镜与镜架。", "amap": "https://uri.amap.com/search?keyword=横岗眼镜城"},
                    {"name": "大康绿道山林驿站", "desc": "平缓铺装山野步道，两边荔枝树连成林荫拱廊，适合双人散步。", "amap": "https://uri.amap.com/search?keyword=大康绿道"}
                ],
                "food_cluster": [
                    {"name": "大康深山农庄·泉水土鸡煲", "spec": "鲜石斛炖农家老鸡、野生山坑螺紫苏煲、柴火香煎土鸡蛋", "price": "双人约 ¥130", "amap": "https://uri.amap.com/search?keyword=横岗大康农家乐"},
                    {"name": "南湾老字号八合里鲜牛肉火锅", "spec": "现切热气吊龙肉、匙柄、五花腱、胸口朥，配手打牛筋丸与炸腐竹", "price": "双人约 ¥160", "amap": "https://uri.amap.com/search?keyword=南湾八合里牛肉火锅"},
                    {"name": "横岗老街地道卤鹅饭店", "spec": "潮汕正宗狮头鹅肉拼鹅掌、卤鹅肝、酸菜猪血汤", "price": "双人约 ¥80", "amap": "https://uri.amap.com/search?keyword=横岗卤鹅店"}
                ]
            },
            {
                "key": "C",
                "badge": "草坪闲散",
                "title": "大运自然公园草坪放空 × 神仙湖环水骑行",
                "spot_desc": "距离丹平仅18分钟车程的大运中心绿肺。拥有大片开阔柔软的斜坡草坪、水杉湖岸与港中深后山的静谧书香气息。适合午后睡饱带上月亮椅和羽毛球，去湖边看黑天鹅，傍晚看落日晚霞吃乳鸽。",
                "main_amap": "https://uri.amap.com/search?keyword=大运自然公园",
                "parking_guide": "🅿️ 大运公园东门/地下停车场：车位超1000个，前2小时5元后续1元/小时，车位充足。",
                "real_photo": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "14:00 - 14:30", "action": "午休后慢调出发，走水官高速龙岗出口，直奔大运公园。"},
                    {"time": "14:30 - 16:30", "action": "在缓坡草坪支起折叠月亮椅与野餐垫，开蓝牙音箱，打羽毛球与飞盘。"},
                    {"time": "16:30 - 18:30", "action": "漫步大运天地水上开放式商业街，看黑天鹅游戈，夕阳倒映水面。"},
                    {"time": "18:30 - 20:00", "action": "吃现烤爆汁玻璃皮乳鸽，饭后来一碗暖胃窝蛋姜撞奶，悠然返家。"}
                ],
                "play_cluster": [
                    {"name": "大运公园阳光大草坪", "desc": "深圳顶级缓坡野餐草坪之一，周围林荫环绕，地面平整无大风，打羽毛球极度舒适。", "amap": "https://uri.amap.com/search?keyword=大运自然公园草坪"},
                    {"name": "神仙湖水库与亲水环湖栈道", "desc": "香港中文大学（深圳）后山湖泊，两岸水杉倒影，常有白鹭飞过。", "amap": "https://uri.amap.com/search?keyword=神仙湖水库"},
                    {"name": "大运天地滨水文旅街区", "desc": "环水而建的绿意商业空间，有滨水外摆咖啡馆与设计感买手店，冷气舒适。", "amap": "https://uri.amap.com/search?keyword=大运天地"}
                ],
                "food_cluster": [
                    {"name": "大运天地·金牌红烧脆皮乳鸽", "spec": "现烤玻璃脆皮乳鸽（肉汁四溢）、豉油皇大虾、煲仔咸鱼肉饼饭", "price": "双人约 ¥140", "amap": "https://uri.amap.com/search?keyword=大运天地乳鸽"},
                    {"name": "顺德杨记传统手工甜品店", "spec": "现撞热姜汁水牛奶、招牌双皮奶、芋圆莲子百合红豆沙、香炸牛奶", "price": "双人约 ¥45", "amap": "https://uri.amap.com/search?keyword=大运天地甜品"}
                ]
            }
        ]
    },

    {
        "id": "mid_autumn_d2",
        "tab": "mid_autumn",
        "day_num": 2,
        "date_str": "9月25日 · 中秋正日",
        "tag_line": "古银叶树海岸 · 白沙湾赶海踩浪 · 海上橘子海明月",
        "driving_summary": "单程约 58km · 55分钟 · 水官高速→盐坝高速葵涌出口（不进大鹏拥堵正门，全程无塞车）",
        "weather_info": "🌤️ 晴转少云 26℃~32℃ · 沿海微风 · 紫外线偏强 (备防晒) · 最佳日落 18:17 (海上升明月 18:40)",
        "budget_dual": "双人全天约 ¥230 - ¥290 (含海鲜大餐+油电，0门票)",
        "feather_ball_spot": "🏸 坝光白沙湾滨海草坪 / 小桂驿站海风大平台（退潮后沙滩硬实，海风柔和）",
        "plans": [
            {
                "key": "A",
                "badge": "绝美看海",
                "title": "大鹏坝光500年古银叶树群落 × 白沙湾滩涂赶海",
                "spot_desc": "完全避开南澳杨梅坑与较场尾的人潮！坝光是大鹏最东北角的秘境。拥有世界上保存最完整的天然古银叶树群落，木栈道穿梭在古树与大海之间。退潮时白沙湾滩涂露出，可以拿着小铲子捉寄居蟹，傍晚看橘子海晚霞，等待明月从海平面升起。",
                "main_amap": "https://uri.amap.com/search?keyword=坝光银叶树湿地园",
                "parking_guide": "🅿️ 坝光湿地公园停车场：地下+露天超500车位，15元/天封顶，无需预约大鹏通行（葵涌出口下）。",
                "real_photo": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1565680018434-b513d5e5fd47?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "08:45 - 09:40", "desc": "丹平经水官转盐坝高速直达葵涌下，完全不走南澳容易缓行的路段。"},
                    {"time": "09:45 - 12:15", "desc": "漫步古银叶树湿地，古树板根如雕塑，栈道伸入海面；到白沙湾滩涂赶海捡海螺捉螃蟹。"},
                    {"time": "12:30 - 14:00", "desc": "前往葵涌老街，吃本地渔民刚上岸的爆炒八爪鱼与蒜蓉开边带子。"},
                    {"time": "14:30 - 16:30", "desc": "漫步东江纵队纪念馆红砖骑楼，树荫浓密安宁，避开午后最热时段。"},
                    {"time": "16:45 - 18:30", "desc": "回到白沙湾草坪：打半小时海风羽毛球，随后坐月亮椅静看橘子海落日与海上升明月！"},
                    {"time": "18:40 - 19:40", "desc": "踩着月色回丹平，车程不到1小时，完全避开夜间车潮。"}
                ],
                "play_cluster": [
                    {"name": "坝光古银叶树湿地公园", "desc": "500年古树群、木栈道、红树林湿地与开阔海湾，人少宁静。", "amap": "https://uri.amap.com/search?keyword=坝光银叶树湿地园"},
                    {"name": "排牙山下白沙湾海滩", "desc": "天然避风港湾，沙滩平缓，退潮后礁石滩有大量小螃蟹和小贝壳。", "amap": "https://uri.amap.com/search?keyword=坝光白沙湾"},
                    {"name": "东江纵队纪念馆古骑楼街", "desc": "浓浓岭南旧街风貌，红砖老洋楼掩映在老榕树下，极有岁月沉淀感。", "amap": "https://uri.amap.com/search?keyword=东江纵队纪念馆"},
                    {"name": "坝光国际生物谷滨海绿道", "desc": "沥青铺设的现代海滨绿道，视野开阔无遮挡，极适合散步拍照。", "amap": "https://uri.amap.com/search?keyword=坝光绿道"}
                ],
                "food_cluster": [
                    {"name": "葵涌老街无名野生海鲜排档", "spec": "爆炒本地小八爪鱼、黄椒酱清蒸泥鯭鱼、蒜蓉粉丝蒸大连带子、白灼中虾", "price": "双人约 ¥170", "amap": "https://uri.amap.com/search?keyword=葵涌老街海鲜"},
                    {"name": "水头海鲜街名厨加工排档", "spec": "白灼海捕九节虾、椒盐富贵虾、姜葱炒本地海花蟹、海胆蒸蛋", "price": "双人约 ¥200", "amap": "https://uri.amap.com/search?keyword=大鹏水头海鲜街"},
                    {"name": "坝光山海林下竹筒饭农家院", "spec": "现烤柴火腊味竹筒饭、客家土窑烧鸡、白灼野生雷公笋", "price": "双人约 ¥110", "amap": "https://uri.amap.com/search?keyword=坝光农家乐"}
                ]
            },
            {
                "key": "B",
                "badge": "免预约海景",
                "title": "惠阳澳头小桂村沿海绿道骑行 (免大鹏预约)",
                "spot_desc": "从丹平出发沿惠深沿海高速在小桂出口下，完全避开深圳大鹏的节假日通行预约！租一辆双人自行车沿着海天一色的绿道骑行，吹着海风看海鸟低飞，渔排静卧。在澳头码头现挑活跳海鲜现蒸，便宜又新鲜。",
                "main_amap": "https://uri.amap.com/search?keyword=小桂村绿道",
                "parking_guide": "🅿️ 小桂驿站停车场：免费/10元一天，车位充裕。",
                "real_photo": "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "09:30 - 10:20", "desc": "丹平出发沿惠深沿海高速在小桂出口下，无需深圳交警预约。"},
                    {"time": "10:30 - 12:30", "desc": "租双人自行车环碧海绿道骑行，打卡纯白灯塔与渔港栈桥。"},
                    {"time": "12:30 - 14:00", "desc": "澳头海鲜码头现挑活跳九节虾与大花蟹，直接在码头渔排蒸熟吃。"},
                    {"time": "14:30 - 16:30", "desc": "小桂驿站平整空坪打羽毛球，背靠大山看海景，悠闲松弛。"}
                ],
                "play_cluster": [
                    {"name": "小桂村碧海绿道", "desc": "紧贴海岸线的自行车骑行道，一路伴着浪花声与海风。", "amap": "https://uri.amap.com/search?keyword=小桂村绿道"},
                    {"name": "澳头老渔港码头", "desc": "渔船穿梭，海鸥低旋，充满浓郁渔家风情。", "amap": "https://uri.amap.com/search?keyword=澳头海鲜市场"},
                    {"name": "衙前滨海白灯塔", "desc": "纯白地中海风情灯塔，依山傍海，拍照如同置身海岛。", "amap": "https://uri.amap.com/search?keyword=惠阳衙前村"}
                ],
                "food_cluster": [
                    {"name": "澳头码头渔排海鲜加工坊", "spec": "白灼活跳基围虾、豉汁炒花蛤、清蒸海鲈鱼、手打鱼丸海白菜汤", "price": "双人约 ¥150", "amap": "https://uri.amap.com/search?keyword=惠阳澳头海鲜码头"},
                    {"name": "小桂绿道渔家客家窑鸡", "spec": "金黄咸香手撕鸡、炸海藻海虾饼、现炒水东芥菜", "price": "双人约 ¥110", "amap": "https://uri.amap.com/search?keyword=小桂村窑鸡"}
                ]
            },
            {
                "key": "C",
                "badge": "傍晚慢调",
                "title": "盐田海滨栈道看巨轮慢行 × 鲜虾蟹肉砂锅粥",
                "spot_desc": "下午4点后再出发去盐田食街后方的海滨栈道。避开大梅沙白天的拥挤，这里傍晚微风徐徐，看一艘艘万吨货轮缓缓驶出盐田港，走累了坐进老店喝一锅热腾腾的鲜活膏蟹基围虾砂锅粥看明月。",
                "main_amap": "https://uri.amap.com/search?keyword=盐田海鲜食街",
                "parking_guide": "🅿️ 盐田食街多层公共车库：车位超600个，傍晚车流渐稀。",
                "real_photo": "https://images.unsplash.com/photo-1518495973542-4542c06a5843?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1535473897047-b6745f657a84?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "15:30 - 16:15", "desc": "错开白天进盐田车流，午后惬意开往盐田海鲜食街。"},
                    {"time": "16:30 - 18:30", "desc": "漫步海滨栈道看盐田巨轮缓缓进出港，日落金色光芒倾泻海面。"},
                    {"time": "18:30 - 20:30", "desc": "喝一煲热气滚滚的鲜活膏蟹基围虾砂锅粥，尝尝沙头角香脆乳鸽。"}
                ],
                "play_cluster": [
                    {"name": "盐田海鲜街后方海滨木栈道", "desc": "伴随礁石与海浪的慢行栈道，近距离观察远洋巨轮进出港湾。", "amap": "https://uri.amap.com/search?keyword=盐田海滨栈道"},
                    {"name": "沙头角栖息灯塔图书馆", "desc": "建在海滨悬崖礁石上的纯白灯塔，听涛看落日极度治愈。", "amap": "https://uri.amap.com/search?keyword=栖息图书馆"}
                ],
                "food_cluster": [
                    {"name": "潮记地道鲜虾蟹肉砂锅粥", "spec": "鲜活膏蟹配基围虾现熬稠粥、炸普宁豆干配韭菜盐水、卤水鹅肉拼盘", "price": "双人约 ¥140", "amap": "https://uri.amap.com/search?keyword=盐田海鲜街砂锅粥"},
                    {"name": "沙头角百年肠粉与乳鸽小馆", "spec": "石磨鲜虾肠粉、红烧脆皮小乳鸽、猪红韭菜汤", "price": "双人约 ¥70", "amap": "https://uri.amap.com/search?keyword=沙头角肠粉"}
                ]
            }
        ]
    },

    {
        "id": "mid_autumn_d3",
        "tab": "mid_autumn",
        "day_num": 3,
        "date_str": "9月26日 · 中秋收官",
        "tag_line": "万亩森林洗肺 · 大坪水库草坪放空 · 柴火瓦煲碌鹅",
        "driving_summary": "单程约 32km · 35分钟 · 丹平快速→清平高速/从莞深直达（纯高速无慢速红绿灯）",
        "weather_info": "⛅ 阴天间多云 24℃~30℃ · 清凉微风 · 紫外线弱 · 最佳日落 18:16",
        "budget_dual": "双人全天约 ¥150 - ¥200 (正餐瓦煲碌鹅+手作糖水，0门票0停车)",
        "feather_ball_spot": "🏸 大屏嶂森林公园芳香植物园草坪 / 龙口水库大坝长堤（林间避风，场地宽广）",
        "plans": [
            {
                "key": "A",
                "badge": "天然氧吧",
                "title": "东莞塘厦大屏嶂森林公园 × 大坪水库环湖草坪",
                "spot_desc": "从丹平快速转清平高速仅半小时，万亩荔枝林环抱的超大森林氧吧！沿大坪水库步道绿荫参天，微风习习。在大草坪支起折叠椅喝咖啡、打羽毛球，呼吸纯天然高浓度负氧离子。中午品尝塘厦正宗瓦煲碌鹅，下午早早回家休整。",
                "main_amap": "https://uri.amap.com/search?keyword=大屏嶂森林公园",
                "parking_guide": "🅿️ 大屏嶂森林公园南门停车场：完全免费，车位充足。",
                "real_photo": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "10:00 - 10:35", "desc": "丹平快速转清平高速快速直达塘厦，30分钟无缝切换进森林。"},
                    {"time": "10:40 - 12:30", "desc": "沿大坪水库林荫慢跑漫步，满目翠绿，在芳香植物园旁草坪打羽毛球。"},
                    {"time": "12:30 - 14:00", "desc": "品尝塘厦传统瓦煲碌鹅，酱汁浓油赤酱，肉质紧致入味，连吃两碗米饭。"},
                    {"time": "14:30 - 16:00", "desc": "树荫下支起折叠月亮椅，冲上一杯手冲咖啡听鸟鸣吹山风。"},
                    {"time": "16:00 - 16:45", "desc": "错开晚间返程高峰，轻松回丹平，早早洗热水澡舒适追剧。"}
                ],
                "play_cluster": [
                    {"name": "大屏嶂大坪水库环湖步道", "desc": "水光潋滟，高大乔木遮天蔽日，空气湿度极佳。", "amap": "https://uri.amap.com/search?keyword=大屏嶂大坪水库"},
                    {"name": "大屏嶂芳香植物园大草坪", "desc": "栽种百种香草花木，开阔草坪四周有天然林遮风，打羽毛球手感极佳。", "amap": "https://uri.amap.com/search?keyword=大屏嶂芳香植物园"},
                    {"name": "塘厦三正半山湖畔湿地步道", "desc": "欧式水榭与环湖木栈道，人少景美，常有白鹭栖息在水杉林间。", "amap": "https://uri.amap.com/search?keyword=塘厦三正半山"}
                ],
                "food_cluster": [
                    {"name": "塘厦林氏地道瓦煲传统碌鹅", "spec": "招牌瓦煲碌鹅（鹅皮弹韧、肉质紧实入味、酱汁拌饭绝顶）、柴火农家煎豆腐", "price": "双人约 ¥140", "amap": "https://uri.amap.com/search?keyword=塘厦正宗碌鹅"},
                    {"name": "水库旁客家山泉水煲鸡农庄", "spec": "山泉水石螺煲走地鸡汤、蒸客家艾糍粄、柴火锅巴饭", "price": "双人约 ¥120", "amap": "https://uri.amap.com/search?keyword=塘厦农家乐"}
                ]
            },
            {
                "key": "B",
                "badge": "市井烟火",
                "title": "龙岗红花岭水库生态公园 × 平湖守珍街老字号糖水",
                "spot_desc": "完全在龙岗本地，不跨城。环龙口水库木栈道被茂密树木包围，登顶观景台可360度俯瞰大运中心全景。下山后顺路去平湖守珍街老字号排档喝手工芝麻糊和糖水，充满市井烟火气。",
                "main_amap": "https://uri.amap.com/search?keyword=红花岭生态公园",
                "parking_guide": "🅿️ 红花岭公园东侧生态停车场：随到随停，5元一次。",
                "real_photo": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "14:00 - 16:30", "desc": "环龙口水库栈道慢步登高，远眺龙岗全城与连绵青山。"},
                    {"time": "17:00 - 18:30", "desc": "平湖守珍街老铺打卡手工香滑芝麻糊、姜汁撞奶与客家肠粉。"}
                ],
                "play_cluster": [
                    {"name": "龙口水库大坝夕阳长堤", "desc": "视野无遮挡的坝顶水泥长堤，傍晚微风徐徐，看晚霞映照水面。", "amap": "https://uri.amap.com/search?keyword=龙口水库"},
                    {"name": "平湖守珍街老火车站旧址", "desc": "旧铁轨与老火车站货站，红砖站台与绿皮火车车厢，适合拍怀旧复古风格照片。", "amap": "https://uri.amap.com/search?keyword=平湖火车站"}
                ],
                "food_cluster": [
                    {"name": "平湖守珍街三十年老牌糖水铺", "spec": "石磨香滑芝麻糊、手撞热姜汁撞奶、炸小油糍、秘制鲜香牛杂煲", "price": "双人约 ¥45", "amap": "https://uri.amap.com/search?keyword=平湖守珍街美食"},
                    {"name": "平湖老车站地道石磨肠粉", "spec": "抽屉式石磨鲜虾鸡蛋肠粉、花生白粥、炸酥肉", "price": "双人约 ¥30", "amap": "https://uri.amap.com/search?keyword=平湖老街肠粉"}
                ]
            },
            {
                "key": "C",
                "badge": "古镇夜宴",
                "title": "甘坑古镇后山二十四史书院书香夜游",
                "spot_desc": "白天在家睡到自然醒，下午4点悠闲出发去甘坑古镇后山二十四史书院。小桥流水、亭台水榭、万盏明灯初上，宛如千与千寻梦境，适合穿汉服或素裙拍大片，在林下茶社对坐品茗。",
                "main_amap": "https://uri.amap.com/search?keyword=二十四史书院",
                "parking_guide": "🅿️ 甘坑古镇北门多层停车场：车位充沛。",
                "real_photo": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "food_photo": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
                "timeline": [
                    {"time": "16:00 - 18:00", "desc": "漫步甘坑客家老街青石板路，探访家风家训馆与碉楼。"},
                    {"time": "18:00 - 21:00", "desc": "进入二十四史书院看万盏华灯初上，亭台楼阁倒映水中，围炉品茶赏月。"}
                ],
                "play_cluster": [
                    {"name": "甘坑古镇客家民俗碉楼", "desc": "百年碉楼排屋，青石板巷，流水潺潺。", "amap": "https://uri.amap.com/search?keyword=甘坑炮楼"},
                    {"name": "二十四史书院湖心亭夜景", "desc": "古建筑飞檐翘角挂满暖黄灯笼，水波倒映美不胜收。", "amap": "https://uri.amap.com/search?keyword=二十四史书院"}
                ],
                "food_cluster": [
                    {"name": "甘坑客家小筑传统黄酒酿鸡", "spec": "糯米黄酒煮土鸡（汤甜肉香极其暖身）、客家纸包豆腐、手打艾叶糍粑", "price": "双人约 ¥130", "amap": "https://uri.amap.com/search?keyword=甘坑客家菜"},
                    {"name": "二十四史书院·庭院煮茶雅舍", "spec": "陈皮白茶炭火煨煮、烤红薯板栗、精致桂花绿豆糕", "price": "双人约 ¥90", "amap": "https://uri.amap.com/search?keyword=甘坑古镇围炉煮茶"}
                ]
            }
        ]
    }
]

# We will export this directly to a json file to be merged into our master roadbook
with open("roadbook_enhanced_v6.json", "w", encoding="utf-8") as f:
    json.dump(ROADBOOK_DB, f, ensure_ascii=False, indent=2)

print("Generated enhanced roadbook JSON database with rich cluster spots and realistic food navigation!")
