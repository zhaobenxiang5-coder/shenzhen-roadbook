import json

# Curating ultra-detailed, timetable-rich itineraries for each plan
# Style: Romantic warm cream, sage green, sunset coral, star sparkles (✨ 🌟 💫 ⭐️), glassmorphism, micro-animations
# Details: Hour-by-hour pacing, exact parking fees/entrances, crowd-avoidance hacks, photo spots, girl-friendly restrooms & coffee breaks

ENRICHED_DAYS = [
    # ------------------ MID-AUTUMN 3 DAYS ------------------
    {
        "tab_id": "mid_autumn",
        "day_id": "mid_autumn-d1",
        "date_title": "Day 1 (中秋首日 · 9.24)",
        "theme": "马峦碧岭飞泉 · 围屋明月茶话 · 坪山慢调艺文",
        "driving": "单程约 38km / 45分钟 (丹平快速→水官高速→南坪快速，全程无拥堵隧道)",
        "weather": "⛅ 多云微风 25℃~31℃ | 紫外线: 中等(SPF30即可) | 最佳日落 18:18 (18:45 海上升明月)",
        "cost": "约 ¥160~220 (双人全天含午晚两餐、手冲咖啡、油电停车，0门票0住宿)",
        "crowd": "★☆☆☆☆ (纯本地反向小众走法，避开大梅沙99%拥堵车流)",
        "sports_gear": "🏸 羽毛球拍2副 + 防风羽毛球1筒、涉水洞洞鞋/溯溪鞋、换洗干T恤、防水野餐垫、便携小音箱",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "马峦山碧岭飞瀑溯溪 + 大万世居古堡月夜",
                "spot_desc": "从坪山碧岭步道逆向上山，绿树遮天蔽日，沿路叠水飞瀑声不绝于耳，体感比市区凉快4℃！下午出山转场全国最大客家围屋之一大万世居，外围开阔广场极平整无风，适合舒展打羽毛球；傍晚青砖灰瓦间看中秋圆月高悬，在天井咖啡馆对坐慢聊。",
                "amap_url": "https://uri.amap.com/navigation?to=114.301548,22.653412,马峦山碧岭瀑布&mode=car",
                "parking": "碧岭瀑布步道停车场（停车位约300个，收费首小时5元后续1元/小时，全天封顶15元。建议上午9:30前或下午14:00后到达）",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 客家窑鸡正餐约 ¥150",
                "schedule": [
                    {"time": "09:30 - 10:15", "action": "🚗 丹平社区出发，经丹平快速接入水官高速与南坪快速三期，路况全线飘绿畅行。"},
                    {"time": "10:15 - 12:30", "action": "🌿 碧岭瀑布步道轻溯溪：换上洞洞鞋赤足浸入山泉，沿途5级叠瀑如天然空调房，登至半山亭野餐垫小憩。"},
                    {"time": "12:30 - 14:00", "action": "🍗 驱车5分钟前往碧岭窑鸡老店，吃滚烫金黄爆汁的荔枝木柴火泥烤鸡与客家酿豆腐。"},
                    {"time": "14:30 - 16:30", "action": "🎨 转场坪山美术馆/文化聚落，吹着清凉冷气漫步极简几何建筑群，拍照极有北欧高阶冷调美感。"},
                    {"time": "16:30 - 18:00", "action": "🏸 大万世居前月池草坪：支起羽毛球拍双人欢畅对拉运动，黄昏柔和微光洒在古瓦屋檐。"},
                    {"time": "18:00 - 20:30", "action": "🌕 漫步围屋庭院观赏中秋初升满月，在半日闲咖啡馆喝杯桂花酒酿拿铁，尝老字号手打牛肉丸后舒适返程丹平。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【坪山文化聚落（红立方 / 美术馆）】",
                        "desc": "距离大万世居仅8分钟车程，极具后现代工业风建筑群，冷气充足。有设计感极强的美术馆和万本书城，人少安静，傍晚室外大平台吹风视野极开阔。",
                        "amap": "https://uri.amap.com/search?keyword=坪山美术馆"
                    },
                    {
                        "name": "【聚龙山生态湿地公园（花海木栈道）】",
                        "desc": "驱车12分钟直达，全国最大湿地公园之一。拥有环山自行车道与亲水木栈道，大片开阔平整草坪，极适合铺上野餐垫打羽毛球或放飞盘。",
                        "amap": "https://uri.amap.com/search?keyword=聚龙山公园"
                    },
                    {
                        "name": "【坪山中心公园湖畔（夜景赏月最佳机位）】",
                        "desc": "拥有大片湖面和大草坪，晚上倒映城市灯光与天心明月，情侣散步闲聊首选。",
                        "amap": "https://uri.amap.com/search?keyword=坪山中心公园"
                    }
                ],
                "foods": [
                    {
                        "name": "【老牌山野柴火窑鸡农庄（碧岭总店）】",
                        "specialty": "古法荔枝木瓦窑泥烤走地鸡（外皮焦脆金黄、撕开滚烫爆汁）、客家酿苦瓜豆腐、苦笋五花肉煲",
                        "price": "双人约 ¥140-160",
                        "amap": "https://uri.amap.com/search?keyword=坪山碧岭柴火窑鸡"
                    },
                    {
                        "name": "【大万老字号手打牛肉丸店】",
                        "specialty": "现打鲜牛肉丸生滚苦瓜汤、干捞牛筋丸粿条、秘制沙茶牛杂煲",
                        "price": "双人约 ¥70-80",
                        "amap": "https://uri.amap.com/search?keyword=坪山大万手打牛肉丸"
                    },
                    {
                        "name": "【大万世居古堡·半日闲天街咖啡】",
                        "specialty": "中秋桂花手摇冰拿铁、客家糯米黄酒风味美式、手作豆腐花提拉米苏",
                        "price": "双人约 ¥50-60",
                        "amap": "https://uri.amap.com/search?keyword=大万世居咖啡"
                    }
                ],
                "photo_spot": "https://images.unsplash.com/photo-1546768292-fb12f6c92568?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?auto=format&fit=crop&w=800&q=80"
            },
            "b": {
                "tag": "平替 B",
                "name": "横岗园山风景区大康溪谷 + 避暑水潭漫步",
                "spot_desc": "距离丹平仅25分钟车程，完全不走易堵的深盐二通道！园山被称为深圳后花园，大康溪谷山水相依，游人只有梧桐山的十分之一，溪水清澈见底，适合赤足戏水，草坪宽广能尽情挥拍打羽毛球。",
                "amap_url": "https://uri.amap.com/navigation?to=114.249215,22.641235,园山风景区&mode=car",
                "parking": "景区正门地面生态车场（车位充裕，随到随停，10元/天）",
                "cost_detail": "门票 ¥15/人 | 停车 ¥10 | 潮汕鲜牛肉火锅约 ¥160",
                "schedule": [
                    {"time": "10:00 - 10:25", "action": "🚗 丹平快速转横坪公路直达园山，仅约15公里，极其轻松。"},
                    {"time": "10:30 - 12:30", "action": "🌿 漫步大康溪谷，林木繁盛遮蔽日光，在碧玉潭边坐看微泉飞溅，水温沁凉。"},
                    {"time": "12:30 - 14:00", "action": "🍲 园山脚下品尝石斛炖土鸡汤与客家煎酿豆腐，汤甘味厚。"},
                    {"time": "14:30 - 16:30", "action": "🕶️ 驱车10分钟去横岗眼镜文创街，吹冷气挑选高性价比偏光墨镜与情侣镜框。"},
                    {"time": "17:00 - 19:30", "action": "🍲 顺路返回南湾/丹平社区，吃老字号热气现切潮汕牛肉火锅，鲜美满足。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【横岗眼镜城·文创街区】",
                        "desc": "离园山10分钟车程，全国最大的眼镜产业基地。里面有新潮的眼镜文创博物馆、极低批发价配高品质墨镜和防蓝光镜，顺便逛冷气步行街。",
                        "amap": "https://uri.amap.com/search?keyword=横岗眼镜城"
                    },
                    {
                        "name": "【大康深山绿道与碧玉潭】",
                        "desc": "园山内部纵深步道，沿途茂林修竹，潭水碧绿如玉。潭边有天然大石坪，可坐着听瀑布声或用便携茶具泡冷泡茶。",
                        "amap": "https://uri.amap.com/search?keyword=园山碧玉潭"
                    }
                ],
                "foods": [
                    {
                        "name": "【南湾老字号八合里鲜牛肉火锅】",
                        "specialty": "现切热气吊龙伴、五花趾、匙柄、胸口朥，配牛骨原汤与炸腐竹",
                        "price": "双人约 ¥150-170",
                        "amap": "https://uri.amap.com/search?keyword=南湾八合里牛肉火锅"
                    },
                    {
                        "name": "【园山大康农家柴火走地鸡】",
                        "specialty": "山泉水石斛炖土鸡汤、野生山坑螺煲、客家石磨煎酿豆腐",
                        "price": "双人约 ¥130-150",
                        "amap": "https://uri.amap.com/search?keyword=横岗大康农家乐"
                    }
                ],
                "photo_spot": "https://images.unsplash.com/photo-1511497584788-87676104235f?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80"
            },
            "c": {
                "tag": "平替 C",
                "name": "大运自然公园大草坪露营 + 神仙湖环湖慢行",
                "spot_desc": "龙岗本地神仙秘境，大片开阔缓坡草坪与环湖水杉步道。带上月亮椅、野餐垫和羽毛球，湖面微波荡漾，黄昏时分夕阳将湖水染成金红，晚上坐在草坪仰望中秋月色极其浪漫。",
                "amap_url": "https://uri.amap.com/navigation?to=114.218412,22.695321,大运自然公园&mode=car",
                "parking": "大运公园东门/地下停车场（车位极多，5元/小时）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 龙城特色乳鸽与糖水双人约 ¥120",
                "schedule": [
                    {"time": "14:30 - 15:00", "action": "🚗 午休后从容出发，走水官高速龙岗出口，20分钟直奔大运公园。"},
                    {"time": "15:00 - 17:00", "action": "⛺ 在缓坡大草坪支开双人月亮椅，放音乐、吃水果、打羽毛球与飞盘。"},
                    {"time": "17:00 - 18:30", "action": "🦢 漫步大运天地水上街区，看黑天鹅掠过湖面，拍日落晚霞倒影。"},
                    {"time": "18:30 - 20:30", "action": "🕊️ 吃现炸爆汁金牌乳鸽，饭后来一碗热气窝蛋姜撞奶，悠闲回家。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【深圳大运天地·滨湖商业街区】",
                        "desc": "环水系而建的全新开放式街区，小桥流水、黑天鹅游戈，汇聚了各种潮流咖啡馆、甜品屋与买手店，冷气十足且极其出片。",
                        "amap": "https://uri.amap.com/search?keyword=大运天地"
                    },
                    {
                        "name": "【香港中文大学（深圳）后山神仙湖步道】",
                        "desc": "依山傍湖的栈道，学术人文气息与清幽山林交织，常有白鹭掠过水面，极少游客打扰。",
                        "amap": "https://uri.amap.com/search?keyword=神仙湖水库"
                    }
                ],
                "foods": [
                    {
                        "name": "【大运天地·金牌红烧脆皮乳鸽】",
                        "specialty": "现炸玻璃皮乳鸽（咬开滚烫爆汁）、豉油皇大虾、煲仔咸鱼肉饼饭",
                        "price": "双人约 ¥130-150",
                        "amap": "https://uri.amap.com/search?keyword=大运天地乳鸽"
                    },
                    {
                        "name": "【顺德杨记传统手作甜汤】",
                        "specialty": "传统窝蛋姜撞奶、招牌双皮奶、芋圆莲子百合红豆沙、炸牛奶",
                        "price": "双人约 ¥45-55",
                        "amap": "https://uri.amap.com/search?keyword=大运甜品"
                    }
                ],
                "photo_spot": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80"
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
        "theme": "大鹏坝光古银叶树海岸 · 白沙湾赶海拾贝 · 橘子海日落",
        "driving": "单程约 55~65km / 50~60分钟 (水官高速→惠深沿海高速葵涌/小桂下，避开较场尾)",
        "weather": "🌤️ 晴转少云 26℃~32℃ | 紫外线: 较高 (海边备防晒) | 最佳日落 18:17 (海上升明月)",
        "cost": "约 ¥220~280 (双人丰盛海鲜大餐、油电、免门票)",
        "crowd": "★★☆☆☆ (完胜人挤人的较场尾/大梅沙)",
        "sports_gear": "赶海小水桶与小耙子、羽毛球拍、防晒衣、墨镜、折叠月亮椅看日落",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "坝光500年天然古银叶树湿地 + 白沙湾赶海",
                "spot_desc": "避开南澳堵车大军，直奔大鹏最东北端的原生态处女地。500年古银叶树板根硕大，木栈道一路延伸进海湾，退潮时下滩涂抓小寄居蟹和小海螺。傍晚坐在白沙湾看无遮挡橘子海落日与海上升明月！",
                "amap_url": "https://uri.amap.com/navigation?to=114.521820,22.646549,坝光银叶树湿地园&mode=car",
                "parking": "坝光湿地生态停车场（车位充裕，无需大鹏半岛拥堵排队，15元/天封顶）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 葵涌老街黄椒炒八爪鱼双人约 ¥180",
                "schedule": [
                    {"time": "08:30 - 09:30", "action": "🚗 避开车流高峰，从丹平经水官转惠深沿海高速直抵葵涌，顺畅进坝光。"},
                    {"time": "09:30 - 12:00", "action": "🦀 漫步500年古银叶树林海栈道，趁低潮在白沙湾滩涂赶海，拾贝壳捉寄居蟹。"},
                    {"time": "12:00 - 13:30", "action": "🐙 葵涌老街吃刚靠岸海鲜，脆嫩爆炒野生小八爪鱼与蒜蓉蒸带子。"},
                    {"time": "14:00 - 16:00", "action": "🏛️ 漫步东江纵队纪念馆与老街红砖骑楼，树荫浓密闲适。"},
                    {"time": "16:30 - 18:30", "action": "🏸 白沙湾滨海草坪：支起羽毛球拍运动对打，随后并肩坐看橘子海晚霞与海上升明月！"},
                    {"time": "18:40 - 20:00", "action": "🚗 吃饱海风后踏着月色轻松返程丹平，不塞车舒服归巢。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【葵涌东江纵队纪念馆与老街骑楼】",
                        "desc": "离坝光12分钟车程，浓郁的岭南历史风貌街区，老街古朴安宁，红砖骑楼适合漫步，没有喧闹的商业小吃街。",
                        "amap": "https://uri.amap.com/search?keyword=东江纵队纪念馆"
                    },
                    {
                        "name": "【排牙山麓脚下茶园与水库观景台】",
                        "desc": "沿排牙山盘山道行驶5分钟，俯瞰整个大亚湾海平面的观景平台，海风呼啸吹拂，云雾缭绕如同仙境。",
                        "amap": "https://uri.amap.com/search?keyword=排牙山观景台"
                    },
                    {
                        "name": "【白沙湾红树林露营草坪（打羽毛球绝佳地）】",
                        "desc": "湿地公园旁平坦的滨海海风草坪，背靠大山面朝大海，傍晚风势缓和，打羽毛球和散步非常舒适。",
                        "amap": "https://uri.amap.com/search?keyword=坝光白沙湾"
                    }
                ],
                "foods": [
                    {
                        "name": "【葵涌老街无名野生海鲜排档】",
                        "specialty": "爆炒本地小八爪鱼、黄椒酱生蒸泥鯭鱼、蒜蓉粉丝蒸本地鲜开边带子",
                        "price": "双人约 ¥170-190",
                        "amap": "https://uri.amap.com/search?keyword=葵涌老街海鲜"
                    },
                    {
                        "name": "【水头海鲜街自选代加工小馆】",
                        "specialty": "白灼九节虾、椒盐富贵虾（皮皮虾）、姜葱炒本地海花蟹",
                        "price": "双人约 ¥190-220",
                        "amap": "https://uri.amap.com/search?keyword=大鹏水头海鲜街"
                    },
                    {
                        "name": "【坝光山海林下竹筒饭农家院】",
                        "specialty": "现烤腊味竹筒饭、柴火土窑走地鸡、白灼本地野生雷公笋",
                        "price": "双人约 ¥110-130",
                        "amap": "https://uri.amap.com/search?keyword=坝光农家乐"
                    }
                ],
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
                "schedule": [
                    {"time": "09:30 - 10:20", "action": "🚗 丹平出发走惠深沿海在小桂下，完全不进大鹏预约管制区。"},
                    {"time": "10:30 - 12:30", "action": "🚲 租双人自行车环碧海绿道骑行，沿途海风习习，打卡白塔与渔港。"},
                    {"time": "12:30 - 14:00", "action": "🦐 澳头海鲜码头现挑活跳九节虾与大花蟹，直接在码头渔排蒸熟吃。"},
                    {"time": "14:30 - 16:30", "action": "🏸 小桂驿站平整空坪打羽毛球，背靠大山看海景，悠闲松弛。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【澳头海鲜市场与老渔港码头】",
                        "desc": "渔船归港直接售卖，可以和渔民砍价挑选刚出海的活蟹大虾，充满人间烟火气。",
                        "amap": "https://uri.amap.com/search?keyword=澳头海鲜市场"
                    },
                    {
                        "name": "【衙前滨海绿道灯塔（小圣托里尼风机位）】",
                        "desc": "离小桂村10分钟，纯白灯塔与蔚蓝海岸，拍照极为吸睛出片。",
                        "amap": "https://uri.amap.com/search?keyword=惠阳衙前村"
                    }
                ],
                "foods": [
                    {
                        "name": "【澳头海鲜码头第一线渔排加工】",
                        "specialty": "现靠岸基围虾白灼、豉汁炒海瓜子、海胆蒸水蛋、本地杂鱼汤",
                        "price": "双人约 ¥150-170",
                        "amap": "https://uri.amap.com/search?keyword=惠阳澳头海鲜码头"
                    },
                    {
                        "name": "【小桂绿道渔家客家窑鸡】",
                        "specialty": "咸香手撕鸡、炸海藻鲜虾饼、农家现炒番薯叶",
                        "price": "双人约 ¥110-120",
                        "amap": "https://uri.amap.com/search?keyword=小桂村窑鸡"
                    }
                ],
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
                "schedule": [
                    {"time": "15:30 - 16:15", "action": "🚗 错开白天车流，午后惬意开往盐田海鲜食街。"},
                    {"time": "16:30 - 18:30", "action": "🌊 漫步海景栈道看盐田巨轮缓缓进出港，日落金色光芒倾泻海面。"},
                    {"time": "18:30 - 20:30", "action": "🍲 喝一煲热气滚滚的鲜活膏蟹基围虾砂锅粥，尝尝沙头角香脆乳鸽。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【中英街历史博物馆与海景栈道】",
                        "desc": "提前在公众号预约免门票，感受一街两制的独特风情，傍晚在沙头角海滨栈道看夕阳。",
                        "amap": "https://uri.amap.com/search?keyword=中英街历史博物馆"
                    },
                    {
                        "name": "【大梅沙灯塔图书馆（外围海滨草坪）】",
                        "desc": "白色独栋灯塔造型，坐落在礁石海岸边，听着涛声看落日极度治愈。",
                        "amap": "https://uri.amap.com/search?keyword=栖息图书馆"
                    }
                ],
                "foods": [
                    {
                        "name": "【潮记地道鲜虾蟹肉砂锅粥】",
                        "specialty": "鲜活膏蟹配基围虾现熬稠粥、炸普宁豆干配韭菜盐水、卤水鹅肉拼盘",
                        "price": "双人约 ¥140-160",
                        "amap": "https://uri.amap.com/search?keyword=盐田海鲜街砂锅粥"
                    },
                    {
                        "name": "【沙头角百年肠粉与乳鸽小馆】",
                        "specialty": "石磨鲜虾肠粉、红烧脆皮小乳鸽、猪红韭菜汤",
                        "price": "双人约 ¥70-80",
                        "amap": "https://uri.amap.com/search?keyword=沙头角肠粉"
                    }
                ],
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
        "theme": "东莞大屏嶂万亩森林氧吧 · 大坪水库漫步 · 正宗农家瓦煲碌鹅",
        "driving": "单程约 30~38km / 30~40分钟 (丹平快速→清平高速/从莞深直达)",
        "weather": "⛅ 阴天间多云 24℃~30℃ | 紫外线: 弱 | 最佳日落 18:16",
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
                "schedule": [
                    {"time": "10:00 - 10:35", "action": "🚗 丹平快速转清平高速快速直达塘厦，30分钟无缝切换进森林。"},
                    {"time": "10:40 - 12:30", "action": "🌲 沿大坪水库林荫慢跑漫步，满目翠绿，在芳香植物园旁草坪打羽毛球。"},
                    {"time": "12:30 - 14:00", "action": "🍲 品尝塘厦传统瓦煲碌鹅，酱汁浓油赤酱，肉质紧致入味，连吃两碗米饭。"},
                    {"time": "14:30 - 16:30", "action": "☕ 树荫下支起折叠月亮椅，冲上一杯手冲咖啡听鸟鸣吹山风。"},
                    {"time": "16:30 - 17:15", "action": "🚗 错开晚间返程高峰，轻松回丹平，早早洗热水澡休息。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【塘厦三正半山湖畔湿地步道】",
                        "desc": "环绕天然湖泊而建的隐秘步道，欧式建筑倒映湖中，人迹罕至，两旁有白鹭聚集与水杉倒影，极其静谧浪漫。",
                        "amap": "https://uri.amap.com/search?keyword=塘厦三正半山"
                    },
                    {
                        "name": "【大屏嶂芳香植物园（羽毛球草坪胜地）】",
                        "desc": "公园内部种植上百种芳香花木，开阔平整的林间草坪四周有天然林木挡风，打羽毛球手感极佳。",
                        "amap": "https://uri.amap.com/search?keyword=大屏嶂芳香植物园"
                    }
                ],
                "foods": [
                    {
                        "name": "【塘厦林氏地道瓦煲传统碌鹅】",
                        "specialty": "金牌瓦煲碌鹅（鹅皮弹韧酱汁浓厚，鹅肉软烂入味拌饭绝顶）、柴火农家豆腐",
                        "price": "双人约 ¥140-160",
                        "amap": "https://uri.amap.com/search?keyword=塘厦正宗碌鹅"
                    },
                    {
                        "name": "【水库旁客家山泉水煲鸡农庄】",
                        "specialty": "山泉水石螺煲走地鸡、蒸客家艾糍粄、柴火锅巴饭",
                        "price": "双人约 ¥120-140",
                        "amap": "https://uri.amap.com/search?keyword=塘厦农家乐"
                    }
                ],
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
                "schedule": [
                    {"time": "14:00 - 16:30", "action": "🌲 环龙口水库栈道慢步登高，远眺龙岗全城与连绵青山。"},
                    {"time": "17:00 - 18:30", "action": "🥣 平湖守珍街老铺打卡手工香滑芝麻糊、姜汁撞奶与客家肠粉。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【平湖守珍街老火车站旧址】",
                        "desc": "旧铁轨与老火车站货站，红砖站台与绿皮火车车厢，适合拍怀旧复古风格照片。",
                        "amap": "https://uri.amap.com/search?keyword=平湖火车站"
                    },
                    {
                        "name": "【龙口水库大坝夕阳长堤】",
                        "desc": "视野无遮挡的坝顶水泥长堤，傍晚微风徐徐，看晚霞映照水面，极少人打扰。",
                        "amap": "https://uri.amap.com/search?keyword=龙口水库"
                    }
                ],
                "foods": [
                    {
                        "name": "【平湖守珍街三十年老牌糖水铺】",
                        "specialty": "石磨香滑芝麻糊、手撞热姜汁撞奶、炸小油糍、秘制鲜香牛杂煲",
                        "price": "双人约 ¥45-55",
                        "amap": "https://uri.amap.com/search?keyword=平湖守珍街美食"
                    },
                    {
                        "name": "【平湖老车站地道石磨肠粉】",
                        "specialty": "抽屉式石磨鲜虾鸡蛋肠粉、花生白粥、炸酥肉",
                        "price": "双人约 ¥30-40",
                        "amap": "https://uri.amap.com/search?keyword=平湖老街肠粉"
                    }
                ],
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
                "schedule": [
                    {"time": "16:00 - 18:00", "action": "🏮 漫步甘坑客家老街青石板路，探访家风家训馆与碉楼。"},
                    {"time": "18:00 - 21:00", "action": "✨ 进入二十四史书院看万盏华灯初上，亭台楼阁倒映水中，围炉品茶赏月。"}
                ],
                "nearby_spots": [
                    {
                        "name": "【甘坑客家小镇·家风家训馆与炮楼】",
                        "desc": "穿梭在百年碉楼与青石板巷弄间，古朴民居里有皮影戏展馆和非遗民俗展示。",
                        "amap": "https://uri.amap.com/search?keyword=甘坑炮楼"
                    },
                    {
                        "name": "【甘坑后山绿道（生态观鸟台）】",
                        "desc": "书院后方的纯原生态登山绿道，树影摇曳，林荫避暑。",
                        "amap": "https://uri.amap.com/search?keyword=甘坑公园"
                    }
                ],
                "foods": [
                    {
                        "name": "【甘坑客家小筑传统黄酒酿鸡】",
                        "specialty": "糯米黄酒煮土鸡（汤甜肉香极其暖身）、客家纸包豆腐、手打艾叶糍粑",
                        "price": "双人约 ¥130-150",
                        "amap": "https://uri.amap.com/search?keyword=甘坑客家菜"
                    },
                    {
                        "name": "【二十四史书院·庭院煮茶雅舍】",
                        "specialty": "陈皮白茶炭火煨煮、烤红薯板栗、精致桂花绿豆糕",
                        "price": "双人约 ¥90-110",
                        "amap": "https://uri.amap.com/search?keyword=甘坑古镇围炉煮茶"
                    }
                ],
                "photo_spot": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "节奏把控：最后一天以休整为主，下午16:00前返程丹平，完全避开夜间高速大塞车，神清气爽回家洗澡看剧！"
        ]
    }
]

print("Script template ready.")
