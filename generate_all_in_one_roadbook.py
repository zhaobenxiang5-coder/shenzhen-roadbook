import json

# Complete, enriched, full-day itinerary data
# Each day, each plan has:
# - specific destination main spot
# - 2-3 nearby complementary play spots (cluster travel within 10-15 mins drive, full afternoon & evening options)
# - 2-3 authentic specific restaurants with specialties, prices, and Amap search links
# - weather, UV, sunset time, driving distance/route
# - cost breakdown (fuel, toll, tickets, parking, meals)
# - specific gear recommendations (badminton, stream wading, beach crab hunting, camp chairs, etc.)
# - realistic authentic photography

FULL_ROADBOOK = [
    # ================= MID-AUTUMN 3 DAYS =================
    {
        "tab_id": "mid_autumn",
        "day_id": "mid_autumn-d1",
        "date_title": "Day 1 (中秋首日 · 9.24)",
        "theme": "马峦山碧岭飞瀑溯溪 · 大万世居客家围屋月夜 · 坪山文化聚落",
        "driving": "单程约 38km / 45分钟 (丹平快速→水官高速→南坪快速直达，避开东部沿海二通道大堵车)",
        "weather": "⛅ 多云微风 25℃~31℃ | 紫外线: 中等 | 最佳日落 18:18 (18:45 海上升明月)",
        "cost": "约 ¥160~220 (双人全天含餐、油电、停车，0门票0住宿)",
        "crowd": "★☆☆☆☆ (纯本地反向小众走法)",
        "sports_gear": "羽毛球拍2副、防风羽毛球1筒、溯溪涉水鞋/洞洞鞋、换洗干T恤、野餐垫、小音箱",
        "plans": {
            "a": {
                "tag": "主选 A",
                "name": "马峦山碧岭瀑布群溯溪 + 大万世居月夜围屋",
                "spot_desc": "从坪山碧岭步道逆向上山，绿树遮天蔽日，沿路叠水飞瀑声不绝于耳，体感比市区凉快4度！下午出山转场大万世居，全国最大客家围屋之一，外围大广场极平整适合打羽毛球，傍晚青砖灰瓦间看中秋圆月与文艺市集咖啡。",
                "amap_url": "https://uri.amap.com/navigation?to=114.301548,22.653412,马峦山碧岭瀑布&mode=car",
                "parking": "碧岭瀑布步道停车场（停车费 ¥10/天，早9:30前或午后2点位多）",
                "cost_detail": "门票 ¥0 | 停车 ¥10 | 客家窑鸡正餐约 ¥150",
                "nearby_spots": [
                    {
                        "name": "【坪山文化聚落（红立方 / 美术馆）】",
                        "desc": "距离大万世居仅8分钟车程，极具后现代工业风建筑群，冷气充足。有设计感极强的美术馆和万本书城，人少安静，傍晚室外大平台吹风视野极开阔。",
                        "amap": "https://uri.amap.com/search?keyword=坪山美术馆"
                    },
                    {
                        "name": "【聚龙山生态湿地公园（花海木栈道）】",
                        "desc": "驱车12分钟直达，全国最大湿地公园之一。拥有环山自行车道与亲水木栈道，大片开阔平整草坪，极适合铺上野餐垫打羽毛球或放飞盘。",
                        "amap_url": "https://uri.amap.com/search?keyword=聚龙山公园"
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
                "parking": "坝光湿地生态停车场（车位充裕，无需大鹏半岛拥堵排队）",
                "cost_detail": "门票 ¥0 | 停车 ¥15 | 葵涌老街黄椒炒八爪鱼双人约 ¥180",
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
    },

    # ================= NATIONAL DAY 5 DAYS =================
    {
        "tab_id": "national_day",
        "day_id": "national_day-d1",
        "date_title": "Day 1 (10.1 首日大堵车 · 逆向静止)",
        "theme": "不上高速不堵车 · 湖畔林盘草坪露营 · 瓦煲黄鳝饭",
        "driving": "单程约 12~18km / 20~25分钟 (丹平快速经地面主干道直达，0高速拥堵)",
        "weather": "🌤️ 秋高气爽 23℃~31℃ | 紫外线: 中等 | 最佳日落 18:10",
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
                "nearby_spots": [
                    {
                        "name": "【南门山森林公园（天鹅湖水上绿道）】",
                        "desc": "离官井头水库仅8分钟车程，万亩荔枝林与湖泊环绕，有专门的绿道、风雨桥和大面积野餐草坪，极适合打羽毛球与徒步。",
                        "amap": "https://uri.amap.com/search?keyword=南门山森林公园"
                    },
                    {
                        "name": "【凤岗历史碉楼老围村】",
                        "desc": "藏在深林里的西式与客家结合碉楼古建筑，人少安静，青苔爬满老砖墙，复古文艺大片随手拍。",
                        "amap": "https://uri.amap.com/search?keyword=凤岗碉楼"
                    }
                ],
                "foods": [
                    {
                        "name": "【凤岗老街正宗炭火瓦煲黄鳝饭】",
                        "specialty": "现点现焗台山黄鳝饭（手撕黄鳝丝拌金黄香脆锅巴，粒粒泛光）、椒盐九肚鱼",
                        "price": "双人约 ¥120-140",
                        "amap": "https://uri.amap.com/search?keyword=凤岗客家黄鳝饭"
                    },
                    {
                        "name": "【龙凤山庄后山客家农家大锅鸭】",
                        "specialty": "柴火土灶烧鸭、客家酿苦瓜煲、农家石磨滑豆腐",
                        "price": "双人约 ¥110-130",
                        "amap": "https://uri.amap.com/search?keyword=凤岗客家农家乐"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【平湖新南水杉林草坪】",
                        "desc": "深秋水杉林渐红，湖边有一大片开阔缓坡草坪，背风遮阳，带折叠椅和咖啡发呆极佳。",
                        "amap": "https://uri.amap.com/search?keyword=平湖生态园草坪"
                    }
                ],
                "foods": [
                    {
                        "name": "【南湾/丹竹头老牌胡椒猪肚鸡总店】",
                        "specialty": "浓白海南白胡椒煲土鸡汤（第一碗喝汤暖身提神）、爽脆猪肚片、手打香菇肉丸",
                        "price": "双人约 ¥130-150",
                        "amap": "https://uri.amap.com/search?keyword=南湾客家猪肚鸡"
                    },
                    {
                        "name": "【平湖地道潮汕生腌与砂锅粥】",
                        "specialty": "生腌膏蟹拼皮皮虾、鲜虾生蚝砂锅粥、炸普宁豆干",
                        "price": "双人约 ¥120-140",
                        "amap": "https://uri.amap.com/search?keyword=平湖生腌海鲜"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【凤凰山国家矿山公园观景长廊】",
                        "desc": "环绕碧绿矿坑湖建立的悬空木质观景长廊，四周断崖壁立，水色呈现青蓝色，视觉冲击强烈。",
                        "amap": "https://uri.amap.com/search?keyword=凤凰山矿山公园"
                    }
                ],
                "foods": [
                    {
                        "name": "【平湖老街深夜大排档】",
                        "specialty": "鲜炸酥脆小肉丸、生滚枸杞叶猪杂及第汤、现炒干炒牛河",
                        "price": "双人约 ¥50-70",
                        "amap": "https://uri.amap.com/search?keyword=平湖老街大排档"
                    }
                ],
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
        "date_title": "Day 2 (10.2 · 避世古围屋田园漫步)",
        "theme": "避世古围屋 · 梯田樟林古道 · 柴火大锅三杯鸭",
        "driving": "单程约 42~52km / 45~55分钟 (水官高速→深汕西或惠阳内环直达，国庆高速免费)",
        "weather": "⛅ 多云间晴 24℃~30℃ | 紫外线: 中等 | 最佳日落 18:09",
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
                "nearby_spots": [
                    {
                        "name": "【叶挺将军纪念园（免费国家级森林人文园）】",
                        "desc": "离秋长谷里仅5分钟车程，红花绿树掩映，有清澈的人工湖和成片幽静的大草坪，游人极少，适合散步和铺野餐垫打羽毛球。",
                        "amap": "https://uri.amap.com/search?keyword=叶挺将军故里"
                    },
                    {
                        "name": "【碧溪古村碉楼群与古梯田】",
                        "desc": "保持原汁原味的古村落，石板路上有散养土鸡走动，梯田稻谷飘香，拍照具有油画般质感。",
                        "amap": "https://uri.amap.com/search?keyword=惠阳碧溪村"
                    }
                ],
                "foods": [
                    {
                        "name": "【秋长古村旁老农庄柴火三杯鸭】",
                        "specialty": "大铁锅柴火慢煨三杯鸭（色泽红润醇厚、肉质紧实不柴）、现打客家艾粄糍粑",
                        "price": "双人约 ¥150-170",
                        "amap": "https://uri.amap.com/search?keyword=惠阳秋长客家农家乐"
                    },
                    {
                        "name": "【谷里天街古树庭院精品咖啡】",
                        "specialty": "桂花冰摇拿铁、手作陈皮冷萃、手冲巴拿马瑰夏、客家黄酒酿芝士蛋糕",
                        "price": "双人约 ¥60-70",
                        "amap": "https://uri.amap.com/search?keyword=秋长谷里咖啡"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【鳌湖艺术村（牛湖老街文艺小店）】",
                        "desc": "艺术创作者聚集的隐秘社区，各种手作陶艺、涂鸦老墙与静谧咖啡馆，漫步非常松弛。",
                        "amap": "https://uri.amap.com/search?keyword=鳌湖艺术村"
                    }
                ],
                "foods": [
                    {
                        "name": "【观澜老街老字号梅州客家腌面】",
                        "specialty": "金牌猪油蒜香客家腌面、鲜枸杞叶三及第猪杂滚汤、手工酿豆腐",
                        "price": "双人约 ¥50-60",
                        "amap": "https://uri.amap.com/search?keyword=观澜老街客家腌面"
                    },
                    {
                        "name": "【牛湖古碉楼下民间柴火煨鸡】",
                        "specialty": "荷叶清蒸走地土鸡、野生山坑笋炒土花肉、清甜玉米粑粑",
                        "price": "双人约 ¥100-120",
                        "amap": "https://uri.amap.com/search?keyword=观澜农家乐"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【金龟露营小镇草坪（无风打球地）】",
                        "desc": "四面环山的谷底大草坪，两侧溪水清浅，微风和煦，打羽毛球不乱飞。",
                        "amap": "https://uri.amap.com/search?keyword=金龟露营小镇"
                    }
                ],
                "foods": [
                    {
                        "name": "【金龟村山泉水石磨豆腐农庄】",
                        "specialty": "金黄焦香煎酿山泉豆腐、香煎土鸡蛋、苦斋婆土猪排骨汤",
                        "price": "双人约 ¥100-120",
                        "amap": "https://uri.amap.com/search?keyword=金龟村农家乐"
                    }
                ],
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
        "theme": "深汕鲘门百安海滩 · 赶海踩细白沙 · 渔港生猛海鲜盛宴",
        "driving": "单程约 105~115km / 1小时20分 (沈海高速深汕段，早8:00前出发畅行无阻，国庆高速全免费)",
        "weather": "☀️ 晴朗碧海 25℃~32℃ | 紫外线: 极高 (必涂防晒霜) | 最佳日落 18:08",
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
                "nearby_spots": [
                    {
                        "name": "【鲘门渔港老码头（千帆归航日落）】",
                        "desc": "距离百安海滩仅7分钟车程，傍晚17:30渔船鸣笛归港，漫天橘红晚霞映照波光粼粼的港湾，海鲜大排档灯火初上，渔家风情拉满。",
                        "amap": "https://uri.amap.com/search?keyword=鲘门港"
                    },
                    {
                        "name": "【芒屿岛远眺观景平台与沿海风车山】",
                        "desc": "沿海滨公路行驶，白色巨大风车在蔚蓝天际下缓缓转动，俯瞰月牙形海湾全景，视野震撼无遮挡。",
                        "amap": "https://uri.amap.com/search?keyword=深汕风车山"
                    },
                    {
                        "name": "【红泉沙滩（更加清幽的原生态野海）】",
                        "desc": "与百安相邻的海滩，沙滩平缓，几乎没有游客，只有几只归海小渔船，在硬沙滩上打羽毛球球感极佳！",
                        "amap": "https://uri.amap.com/search?keyword=红泉沙滩"
                    }
                ],
                "foods": [
                    {
                        "name": "【鲘门港口老牌海鲜饭店】",
                        "specialty": "现煮手打鲜马鲛鱼丸汤（汤清肉脆弹性惊人）、满膏红鲟蒸糯米饭、姜葱爆海白虾",
                        "price": "双人约 ¥200-240",
                        "amap": "https://uri.amap.com/search?keyword=鲘门海鲜饭店"
                    },
                    {
                        "name": "【百安海滨渔家乐现捞加工小铺】",
                        "specialty": "蒜蓉清蒸海捕野生生蚝、椒盐皮皮虾、鲘门特产海马滋补汤",
                        "price": "双人约 ¥170-200",
                        "amap": "https://uri.amap.com/search?keyword=鲘门百安海鲜"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【杨梅坑天然礁石海谷栈道】",
                        "desc": "沿悬崖步道一路走向海蚀洞，海水碧绿如宝石，浪花拍岸卷起千堆雪。",
                        "amap": "https://uri.amap.com/search?keyword=杨梅坑鹿嘴栈道"
                    }
                ],
                "foods": [
                    {
                        "name": "【南澳杨梅坑老字号海胆炒饭】",
                        "specialty": "金黄诱人本地野生海胆炒饭（米粒金黄颗颗裹海胆）、柴火窑鸡、清蒸野生海石斑",
                        "price": "双人约 ¥150-170",
                        "amap": "https://uri.amap.com/search?keyword=大鹏海胆炒饭"
                    },
                    {
                        "name": "【水头海鲜街名厨加工排档】",
                        "specialty": "白灼深海大花虾、避风塘炒本地膏蟹、鲜海虾海鲜粥",
                        "price": "双人约 ¥160-190",
                        "amap": "https://uri.amap.com/search?keyword=水头海鲜街"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【范和罗冈围古戏台与古庙】",
                        "desc": "六百年历史的水乡古村，布局如棋盘，红墙黑瓦古榕树，安宁静谧。",
                        "amap": "https://uri.amap.com/search?keyword=范和古村戏台"
                    }
                ],
                "foods": [
                    {
                        "name": "【范和老街百年石磨猪肠粉】",
                        "specialty": "刚出炉米香扑鼻的肠粉卷秘制肉末香菇酱、葱油干拌石磨粉、炸小油角",
                        "price": "双人约 ¥35-45",
                        "amap": "https://uri.amap.com/search?keyword=惠东范和古村美食"
                    }
                ],
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
        "driving": "单程约 90~100km / 1小时15分 (经深中通道直达中山/顺德容桂，国庆高速全免费)",
        "weather": "🌤️ 清爽微风 24℃~31℃ | 紫外线: 中等 | 最佳日落 18:07 (伶仃洋晚霞)",
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
                "nearby_spots": [
                    {
                        "name": "【德胜河南岸滨江公园（江风羽毛球草坪）】",
                        "desc": "沿顺德母亲河德胜河而建的带状滨江公园，绿草如茵，江风习习，对岸是顺德新城现代天际线，在此打羽毛球神清气爽！",
                        "amap": "https://uri.amap.com/search?keyword=德胜河南岸公园"
                    },
                    {
                        "name": "【柴油机1959文创园区（复古工业胶片风）】",
                        "desc": "由老工厂改造成的红砖红墙文创区，林荫遮蔽，有许多创意手作工坊、咖啡小馆与老厂房涂鸦，拍照极有复古格调。",
                        "amap": "https://uri.amap.com/search?keyword=柴油机1959"
                    },
                    {
                        "name": "【容桂树生桥历史奇观】",
                        "desc": "300年榕树气根自然缠绕形成的天然古桥，旁边是宁静的江南水乡河涌，老人们在树下下棋乘凉，毫无商业喧嚣。",
                        "amap": "https://uri.amap.com/search?keyword=树生桥"
                    }
                ],
                "foods": [
                    {
                        "name": "【容桂街坊私藏·阿多地道桑拿菜】",
                        "specialty": "现点活鸡剔骨桑拿蒸（精准沙漏3分钟揭盖，鸡肉嫩滑多汁毫无纤维感）、原汁鸡骨虫草花粥底",
                        "price": "双人约 ¥170-190",
                        "amap": "https://uri.amap.com/search?keyword=容桂阿多桑拿鸡"
                    },
                    {
                        "name": "【民信老铺容桂分店（免排队）】",
                        "specialty": "热原只水牛奶双皮奶、炸香脆牛奶块、现滚生滚及第牛肉粥",
                        "price": "双人约 ¥50-70",
                        "amap": "https://uri.amap.com/search?keyword=容桂民信老铺"
                    },
                    {
                        "name": "【德胜河畔·水牛乳咖啡小馆】",
                        "specialty": "顺德水牛奶拿铁、黑松露巴斯克芝士蛋糕",
                        "price": "双人约 ¥55-65",
                        "amap": "https://uri.amap.com/search?keyword=容桂渔人码头咖啡"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【翠亨村孙中山故里红墙步道】",
                        "desc": "离崖口村5分钟，红砖欧式中西合璧建筑，林荫蔽日，草坪修剪平整，历史人文与自然风光融合。",
                        "amap": "https://uri.amap.com/search?keyword=孙中山故居"
                    },
                    {
                        "name": "【崖口红树林海堤（看日落伶仃洋）】",
                        "desc": "漫步海堤看退潮滩涂与海鸥掠水，落日余晖洒在海面上极其出片。",
                        "amap": "https://uri.amap.com/search?keyword=崖口海堤"
                    }
                ],
                "foods": [
                    {
                        "name": "【中山崖口人家正宗馄饨铺】",
                        "specialty": "皮薄如蝉翼现包鲜虾蟹子云吞、炭火生焗脆皮黄鳝煲仔饭（底焦金黄酥脆）",
                        "price": "双人约 ¥90-110",
                        "amap": "https://uri.amap.com/search?keyword=中山崖口云吞"
                    },
                    {
                        "name": "【崖口稻田临海集装箱咖啡】",
                        "specialty": "海风生椰拿铁、稻香冷萃咖啡、手作柠檬茶",
                        "price": "双人约 ¥45-55",
                        "amap": "https://uri.amap.com/search?keyword=崖口村集装箱咖啡"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【岐江公园（工业造船厂旧址改建）】",
                        "desc": "荣获国际景观设计大奖的公园，铁轨、红砖水塔与江畔草坪相映成趣，打羽毛球或漫步非常舒适。",
                        "amap": "https://uri.amap.com/search?keyword=岐江公园"
                    }
                ],
                "foods": [
                    {
                        "name": "【石岐佬老牌传统中山粤菜】",
                        "specialty": "百年招牌红烧石岐乳鸽（玻璃脆皮流汁）、香炸大菠萝包、特色菊花炸鱼球",
                        "price": "双人约 ¥140-160",
                        "amap": "https://uri.amap.com/search?keyword=石岐红烧乳鸽"
                    }
                ],
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
        "theme": "东莞第一峰银瓶山溪谷 · 沿溪洗肺慢步 · 山泉水炖走地鸡汤",
        "driving": "单程约 48~56km / 48~55分钟 (从莞深高速→潮莞高速谢岗出口，国庆高速全免费)",
        "weather": "⛅ 阴天微凉 22℃~28℃ | 紫外线: 弱 | 最佳日落 18:06",
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
                "nearby_spots": [
                    {
                        "name": "【谢岗银瓶山生态下山大草坪（羽毛球胜地）】",
                        "desc": "景区正门外有数千平米平整的草坪广场，四周群山环绕，下山后打上半小时羽毛球出身透汗极度爽快！",
                        "amap": "https://uri.amap.com/search?keyword=银瓶山森林公园"
                    },
                    {
                        "name": "【崖山森林公园水库观景道】",
                        "desc": "离谢岗8分钟车程，宁静的冷门小水库，青山倒映在如镜水面，带月亮椅喝杯茶极舒服。",
                        "amap": "https://uri.amap.com/search?keyword=崖山森林公园"
                    }
                ],
                "foods": [
                    {
                        "name": "【银瓶山山脚谢岗生态农夫饭庄】",
                        "specialty": "清冽山泉水慢火煲农家走地鸡汤（鲜美甘润回甘毫无油腻）、紫苏大火爆炒野生山坑螺",
                        "price": "双人约 ¥140-160",
                        "amap": "https://uri.amap.com/search?keyword=银瓶山谢岗农家乐"
                    },
                    {
                        "name": "【谢岗老街传统石磨碌鹅坊】",
                        "specialty": "柴火秘制碌鹅配鲜蒸粉肠、农家清炒山渡笋、山水石磨嫩豆腐",
                        "price": "双人约 ¥100-120",
                        "amap": "https://uri.amap.com/search?keyword=谢岗特色美食"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【红花沥水库观景悬空步道】",
                        "desc": "盘山公路中途隐藏的静谧水库，湖水碧蓝如九寨，沿途有木栈道可坐着吹风。",
                        "amap": "https://uri.amap.com/search?keyword=红花沥水库"
                    }
                ],
                "foods": [
                    {
                        "name": "【盐田食街金牌红烧乳鸽王】",
                        "specialty": "金牌红烧脆皮乳鸽（肉汁四溢）、石磨鲜虾红肠粉、海皇豆腐煲",
                        "price": "双人约 ¥130-150",
                        "amap": "https://uri.amap.com/search?keyword=盐田红烧乳鸽"
                    }
                ],
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
                "nearby_spots": [
                    {
                        "name": "【酥醪古观与山泉洗心池】",
                        "desc": "千年古观依山就势，清泉自岩缝流出甘甜清冽，深山古刹听钟鸣。",
                        "amap": "https://uri.amap.com/search?keyword=酥醪观"
                    }
                ],
                "foods": [
                    {
                        "name": "【酥醪村老村民家宴土猪肉汤】",
                        "specialty": "深山泉水炖土猪肉汤（只放少许白胡椒，肉香汤清极度甘润）、山水仙人豆腐脑",
                        "price": "双人约 ¥90-110",
                        "amap": "https://uri.amap.com/search?keyword=酥醪村农家菜"
                    }
                ],
                "photo_spot": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1000&q=80",
                "photo_food": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80"
            }
        },
        "tips": [
            "收官收心：下午15:30前启程返回丹平社区，傍晚回温馨的家整理衣物、洗个热水澡，避开夜间返程大塞车，神清气爽迎接工作！"
        ]
    }
]

from generate_super_app import CHECKLIST_CATEGORIES
SHARE_URL = "https://zhaobenxiang5-coder.github.io/shenzhen-roadbook/"

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>深圳龙岗丹平出发 · 避坑反向自驾路书 (中秋3天+国庆5天)</title>
  <!-- WeChat & Social Meta -->
  <meta property="og:title" content="深圳自驾反向路书 · 中秋3天+国庆5天">
  <meta property="og:description" content="情侣专属·厌人避堵·每日回丹平睡大床·A/B/C三重平替·吃玩集群深度清单">
  <meta property="og:image" content="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#090d16">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: rgba(18, 24, 38, 0.9);
      --card-border: rgba(255, 255, 255, 0.09);
      --primary: #f97316;
      --primary-light: #fb923c;
      --primary-glow: rgba(249, 115, 22, 0.35);
      --accent: #10b981;
      --accent-glow: rgba(16, 185, 129, 0.3);
      --purple: #8b5cf6;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --border: #334155;
      --gold: #fbbf24;
      --shadow-lg: 0 16px 36px -8px rgba(0,0,0,0.65);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background-color: var(--bg);
      background-image: 
        radial-gradient(at 0% 0%, rgba(249, 115, 22, 0.16) 0px, transparent 50%),
        radial-gradient(at 100% 30%, rgba(14, 165, 233, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(16, 185, 129, 0.1) 0px, transparent 60%);
      background-attachment: fixed;
      color: var(--text);
      font-family: 'Plus Jakarta Sans', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      padding-bottom: 96px;
    }}

    .container {{
      max-width: 680px;
      margin: 0 auto;
      padding: 14px;
    }}

    /* Cover Hero Header */
    .hero-banner {{
      position: relative;
      border-radius: 24px;
      overflow: hidden;
      margin-bottom: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
      border: 1px solid rgba(255,255,255,0.12);
    }}

    .hero-bg {{
      width: 100%;
      height: 220px;
      object-fit: cover;
      display: block;
      filter: brightness(0.65) saturate(1.2);
    }}

    .hero-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(9, 13, 22, 0.15) 0%, rgba(9, 13, 22, 0.95) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 18px;
    }}

    .meta-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(249, 115, 22, 0.25);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(249, 115, 22, 0.5);
      color: #ffedd5;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      width: fit-content;
    }}

    .title {{
      font-family: 'Noto Serif SC', serif;
      font-size: 23px;
      font-weight: 900;
      letter-spacing: 0.2px;
      line-height: 1.25;
      color: #ffffff;
      text-shadow: 0 2px 10px rgba(0,0,0,0.6);
      margin-bottom: 4px;
    }}

    .subtitle {{
      color: #cbd5e1;
      font-size: 12px;
      line-height: 1.45;
    }}

    /* Global Cost Summary Widget */
    .cost-overview-card {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(217, 119, 6, 0.05) 100%);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 18px;
      padding: 12px 14px;
      margin-bottom: 14px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }}

    .cost-stat {{
      display: flex;
      flex-direction: column;
    }}

    .cost-stat .label {{
      font-size: 11px;
      color: #fde68a;
      font-weight: 600;
      margin-bottom: 2px;
    }}

    .cost-stat .val {{
      font-size: 18px;
      font-weight: 800;
      color: #ffffff;
    }}

    .cost-stat .sub {{
      font-size: 10px;
      color: #cbd5e1;
    }}

    /* Tab switcher */
    .tab-nav {{
      position: sticky;
      top: 10px;
      z-index: 99;
      background: rgba(13, 17, 28, 0.92);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 18px;
      padding: 5px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-lg);
    }}

    .tab-btn {{
      background: transparent;
      border: none;
      outline: none;
      padding: 9px 10px;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 13px;
      border-radius: 14px;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
    }}

    .tab-btn.active {{
      background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
      color: #ffffff;
      box-shadow: 0 4px 18px var(--primary-glow);
    }}

    .tab-btn .badge-pill {{
      font-size: 10px;
      opacity: 0.9;
      font-weight: 500;
    }}

    .tab-intro {{
      background: rgba(30, 41, 59, 0.5);
      border-left: 3px solid var(--primary);
      padding: 10px 12px;
      border-radius: 4px 14px 14px 4px;
      font-size: 12px;
      color: #e2e8f0;
      margin-bottom: 18px;
      line-height: 1.5;
    }}

    /* Day Card */
    .day-card {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 16px;
      margin-bottom: 22px;
      box-shadow: var(--shadow-lg);
      position: relative;
    }}

    .day-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      padding-bottom: 8px;
    }}

    .day-title {{
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.3px;
    }}

    .crowd-pill {{
      font-size: 11px;
      color: #34d399;
      background: rgba(52, 211, 153, 0.12);
      border: 1px solid rgba(52, 211, 153, 0.3);
      padding: 2px 8px;
      border-radius: 9999px;
      font-weight: 600;
    }}

    .day-subtitle {{
      font-size: 14px;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    /* Weather & Sunset Bar */
    .weather-box {{
      background: rgba(14, 165, 233, 0.08);
      border: 1px solid rgba(14, 165, 233, 0.2);
      border-radius: 12px;
      padding: 8px 12px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: #7dd3fc;
    }}

    .weather-box strong {{
      color: #bae6fd;
    }}

    /* Sports & Gear Widget */
    .gear-mini-bar {{
      background: rgba(139, 92, 246, 0.08);
      border: 1px solid rgba(139, 92, 246, 0.2);
      border-radius: 12px;
      padding: 8px 12px;
      margin-bottom: 12px;
      font-size: 11px;
      color: #c4b5fd;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Day Cost Box */
    .day-cost-bar {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.2);
      border-radius: 12px;
      padding: 8px 12px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
    }}

    .day-cost-bar .tit {{
      font-weight: 700;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .day-cost-bar .val {{
      font-weight: 800;
      color: #ffffff;
    }}

    .day-metrics {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: rgba(15, 23, 42, 0.6);
      padding: 8px 12px;
      border-radius: 12px;
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }}

    .metric-item {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .metric-item svg {{
      width: 14px;
      height: 14px;
      fill: currentColor;
      color: var(--primary-light);
    }}

    /* Plan Switcher (A / B / C 3选项平替切换) */
    .plan-switch-wrap {{
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 18px;
      padding: 14px;
      margin-bottom: 14px;
    }}

    .plan-toggle-bar {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 6px;
      background: rgba(0, 0, 0, 0.4);
      padding: 4px;
      border-radius: 12px;
      margin-bottom: 12px;
    }}

    .plan-toggle-btn {{
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-size: 11px;
      font-weight: 700;
      padding: 8px 6px;
      border-radius: 10px;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      white-space: nowrap;
    }}

    .plan-toggle-btn.active.btn-plan-a {{
      background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(249, 115, 22, 0.4);
    }}

    .plan-toggle-btn.active.btn-plan-b {{
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
    }}

    .plan-toggle-btn.active.btn-plan-c {{
      background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(139, 92, 246, 0.4);
    }}

    .plan-content {{
      display: none;
      animation: fadeIn 0.25s ease-out;
    }}

    .plan-content.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Photo Grid */
    .photo-grid {{
      display: grid;
      grid-template-columns: 1.5fr 1fr;
      gap: 8px;
      margin-bottom: 12px;
      border-radius: 14px;
      overflow: hidden;
      height: 140px;
    }}

    .photo-card {{
      position: relative;
      height: 100%;
      overflow: hidden;
    }}

    .photo-card img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }}

    .photo-card:hover img {{
      transform: scale(1.05);
    }}

    .photo-badge {{
      position: absolute;
      bottom: 8px;
      left: 8px;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      color: #ffffff;
      font-size: 10px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .spot-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
      margin-bottom: 4px;
    }}

    .spot-name {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
    }}

    .plan-cost-tag {{
      display: inline-block;
      font-size: 11px;
      font-weight: 600;
      color: #fbbf24;
      background: rgba(251, 191, 36, 0.12);
      padding: 3px 8px;
      border-radius: 6px;
      margin-bottom: 8px;
    }}

    .spot-desc {{
      font-size: 12px;
      color: #94a3b8;
      line-height: 1.5;
      margin-bottom: 10px;
    }}

    .parking-row {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.2);
      padding: 6px 10px;
      border-radius: 10px;
      margin-bottom: 12px;
    }}

    /* Action Nav Buttons (高德一键导航) */
    .amap-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      text-decoration: none;
      padding: 10px 12px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
      transition: all 0.2s;
      width: 100%;
      margin-bottom: 12px;
    }}

    .amap-btn:active {{
      opacity: 0.85;
      transform: scale(0.98);
    }}

    /* Nearby Spots Cluster (目的地周边玩点集群) */
    .nearby-cluster-wrap {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(56, 189, 248, 0.18);
      border-radius: 12px;
      padding: 10px 12px;
      margin-bottom: 12px;
    }}

    .cluster-title {{
      font-size: 12px;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .cluster-item {{
      background: rgba(15, 23, 42, 0.6);
      padding: 8px 10px;
      border-radius: 8px;
      margin-bottom: 6px;
      font-size: 11px;
    }}

    .cluster-item:last-child {{
      margin-bottom: 0;
    }}

    .cluster-item-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }}

    .cluster-item-name {{
      font-weight: 700;
      color: #e2e8f0;
    }}

    .cluster-item-amap {{
      color: #38bdf8;
      text-decoration: none;
      font-size: 10px;
      background: rgba(56, 189, 248, 0.15);
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .cluster-item-desc {{
      color: #94a3b8;
      line-height: 1.4;
    }}

    /* Food Cluster (目的地特色美食精选) */
    .food-cluster-wrap {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 12px;
      padding: 10px 12px;
      margin-bottom: 10px;
    }}

    .food-cluster-title {{
      font-size: 12px;
      font-weight: 700;
      color: #fbbf24;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .food-item-card {{
      background: rgba(15, 23, 42, 0.6);
      padding: 8px 10px;
      border-radius: 8px;
      margin-bottom: 6px;
      font-size: 11px;
    }}

    .food-item-card:last-child {{
      margin-bottom: 0;
    }}

    .food-item-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }}

    .food-item-name {{
      font-weight: 700;
      color: #fde68a;
    }}

    .food-item-amap {{
      color: #fbbf24;
      text-decoration: none;
      font-size: 10px;
      background: rgba(245, 158, 11, 0.15);
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .food-item-spec {{
      color: #cbd5e1;
      line-height: 1.4;
      margin-bottom: 2px;
    }}

    .food-item-price {{
      color: #94a3b8;
      font-size: 10px;
    }}

    /* Tips Box */
    .tips-card {{
      background: rgba(239, 68, 68, 0.08);
      border: 1px solid rgba(239, 68, 68, 0.2);
      border-radius: 14px;
      padding: 10px 12px;
      font-size: 11px;
      color: #fca5a5;
    }}

    .tips-item {{
      margin-bottom: 3px;
      line-height: 1.45;
    }}

    .tips-item:last-child {{
      margin-bottom: 0;
    }}

    /* Interactive Checklist Section */
    .checklist-section {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 18px;
      margin-top: 24px;
      box-shadow: var(--shadow-lg);
    }}

    .checklist-section h3 {{
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .check-category {{
      margin-bottom: 14px;
    }}

    .check-cat-title {{
      font-size: 13px;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .check-item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      background: rgba(15, 23, 42, 0.6);
      padding: 8px 12px;
      border-radius: 10px;
      margin-bottom: 6px;
      font-size: 12px;
      color: #cbd5e1;
      cursor: pointer;
      user-select: none;
      transition: background 0.2s;
    }}

    .check-item input[type="checkbox"] {{
      margin-top: 3px;
      accent-color: #f97316;
      width: 15px;
      height: 15px;
    }}

    .check-item-info {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .check-item-note {{
      font-size: 10px;
      color: #94a3b8;
    }}

    /* Toolbox Section */
    .toolbox {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 18px;
      margin-top: 20px;
      box-shadow: var(--shadow-lg);
    }}

    .toolbox h3 {{
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .toolbox-item {{
      background: rgba(15, 23, 42, 0.6);
      border-radius: 12px;
      padding: 10px 12px;
      margin-bottom: 8px;
      font-size: 11px;
    }}

    .toolbox-item .lbl {{
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 3px;
    }}

    .toolbox-item .cnt {{
      color: #94a3b8;
      line-height: 1.45;
    }}

    /* Floating Share Button */
    .share-bar {{
      position: fixed;
      bottom: 16px;
      left: 50%;
      transform: translateX(-50%);
      width: calc(100% - 32px);
      max-width: 480px;
      z-index: 100;
      display: flex;
      gap: 10px;
    }}

    .share-btn {{
      flex: 1;
      background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
      color: #ffffff;
      border: none;
      outline: none;
      padding: 13px 20px;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 10px 25px rgba(249, 115, 22, 0.45);
      cursor: pointer;
    }}

    .toast {{
      position: fixed;
      top: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(-100px);
      background: #10b981;
      color: white;
      font-weight: 600;
      font-size: 13px;
      padding: 10px 22px;
      border-radius: 9999px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      z-index: 999;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    .tab-section {{
      display: none;
    }}

    .tab-section.active {{
      display: block;
    }}

    svg {{
      vertical-align: middle;
    }}
  </style>
</head>
<body>

  <div class="toast" id="toast">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toast-text">微信分享链接已复制！</span>
  </div>

  <div class="container">
    <!-- Hero Cover Banner -->
    <header class="hero-banner">
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80" alt="Cover" class="hero-bg">
      <div class="hero-overlay">
        <div class="meta-tag">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
          深圳龙岗丹平社区出发
        </div>
        <h1 class="title">深圳周边避坑反向自驾路书</h1>
        <p class="subtitle">中秋3天 + 国庆5天 · 每日日归回家睡 · A/B/C三重平替 · 吃玩集群全清单</p>
      </div>
    </header>

    <!-- Global Cost Overview Card -->
    <section class="cost-overview-card">
      <div class="cost-stat">
        <span class="label">🌕 中秋3天总预算 (双人)</span>
        <span class="val">¥550 - ¥700</span>
        <span class="sub">日均仅约 ¥200 (省下¥3000+房费)</span>
      </div>
      <div class="cost-stat">
        <span class="label">🇨🇳 国庆5天总预算 (双人)</span>
        <span class="val">¥980 - ¥1300</span>
        <span class="sub">高速全免费 + 0房费 + 生猛海鲜</span>
      </div>
    </section>

    <!-- Top Tab Navigation -->
    <nav class="tab-nav">
      <button class="tab-btn active" onclick="switchMainTab('mid_autumn')">
        <span>🌕 中秋 3 天假期</span>
        <span class="badge-pill">山野清凉 · 观海赏月</span>
      </button>
      <button class="tab-btn" onclick="switchMainTab('national_day')">
        <span>🇨🇳 国庆 5 天黄金周</span>
        <span class="badge-pill">避堵反向 · 纯净海滩</span>
      </button>
    </nav>

    <!-- Section: Mid Autumn -->
    <section id="section-mid_autumn" class="tab-section active">
      <div class="tab-intro">
        💡 <strong>中秋避堵锦囊：</strong>假期间高速不免费，东部沿海（大梅沙/较场尾）车流易集中。本路书单程严控在 35~55 分钟内，全部采用<strong>【逆向清凉 + 每日 A/B/C 三选一 + 目的地周边吃玩集群】</strong>，傍晚赏月吃夜宵后回丹平安心睡好觉。
      </div>
"""

# Render Mid-Autumn and National Day days
for day in FULL_ROADBOOK:
    day_id = day["day_id"]
    tips_html = "".join([f'<div class="tips-item">• {t}</div>' for t in day["tips"]])

    if day["tab_id"] == "national_day" and 'id="section-national_day"' not in html:
        html += """
    </section>
    <!-- Section: National Day -->
    <section id="section-national_day" class="tab-section">
      <div class="tab-intro">
        💡 <strong>国庆反向自驾法则：</strong>国庆高速全免费、全网出行井喷！本路线严格践行<strong>【10.1留在深莞边界避堵，10.2深入客家古村，10.3直奔冷门深汕海滩，10.4走顺德老街寻味，10.5登第一峰吸氧】</strong>，天天回家睡大床，省下天价酒店！
      </div>
        """

    html += f"""
      <article class="day-card" id="{day_id}">
        <div class="day-header">
          <span class="day-title">{day['date_title']}</span>
          <span class="crowd-pill">热度指数：{day['crowd']}</span>
        </div>

        <div class="day-subtitle">
          <span>📍</span>
          <span>{day['theme']}</span>
        </div>

        <!-- Weather Box -->
        <div class="weather-box">
          <span>{day['weather']}</span>
          <span><strong>适宜：</strong>户外/运动</span>
        </div>

        <!-- Gear Mini Bar -->
        <div class="gear-mini-bar">
          <span>🏸 <strong>当日随车适玩装备：</strong></span>
          <span>{day['sports_gear']}</span>
        </div>

        <!-- Cost Bar -->
        <div class="day-cost-bar">
          <span class="tit">💰 当日双人预计花费</span>
          <span class="val">{day['cost']}</span>
        </div>

        <div class="day-metrics">
          <div class="metric-item">
            <svg viewBox="0 0 24 24"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.85 7h10.29l1.08 3.11H5.77L6.85 7zM19 17H5v-5h14v5z"/><circle cx="7.5" cy="14.5" r="1.5"/><circle cx="16.5" cy="14.5" r="1.5"/></svg>
            <span>{day['driving']}</span>
          </div>
        </div>

        <!-- Plan Switcher A / B / C -->
        <div class="plan-switch-wrap">
          <div class="plan-toggle-bar">
            <button class="plan-toggle-btn btn-plan-a active" id="btn-a-{day_id}" onclick="switchTriplePlan('{day_id}', 'a')">
              <span>🌟 主选 A</span>
            </button>
            <button class="plan-toggle-btn btn-plan-b" id="btn-b-{day_id}" onclick="switchTriplePlan('{day_id}', 'b')">
              <span>🔄 平替 B</span>
            </button>
            <button class="plan-toggle-btn btn-plan-c" id="btn-c-{day_id}" onclick="switchTriplePlan('{day_id}', 'c')">
              <span>🍃 备选 C</span>
            </button>
          </div>
    """

    for p_key, p_color in [("a", "#f97316"), ("b", "#10b981"), ("c", "#8b5cf6")]:
        plan = day["plans"][p_key]
        active_cls = "active" if p_key == "a" else ""
        badge_style = "" if p_key == "a" else f"style=\"background: {p_color};\""

        # Nearby spots HTML
        nearby_spots_html = ""
        if plan.get("nearby_spots"):
            items_html = ""
            for s in plan["nearby_spots"]:
                items_html += f"""
                <div class="cluster-item">
                  <div class="cluster-item-head">
                    <span class="cluster-item-name">{s['name']}</span>
                    <a href="{s.get('amap', s.get('amap_url', '#'))}" target="_blank" class="cluster-item-amap">高德导航</a>
                  </div>
                  <div class="cluster-item-desc">{s['desc']}</div>
                </div>
                """
            nearby_spots_html = f"""
            <div class="nearby-cluster-wrap">
              <div class="cluster-title">🎡 <strong>目的地周边集群好玩推荐 (10分钟内多选)：</strong></div>
              {items_html}
            </div>
            """

        # Foods HTML
        foods_html = ""
        if plan.get("foods"):
            food_items_html = ""
            for f in plan["foods"]:
                food_items_html += f"""
                <div class="food-item-card">
                  <div class="food-item-head">
                    <span class="food-item-name">{f['name']}</span>
                    <a href="{f['amap']}" target="_blank" class="food-item-amap">导航去吃</a>
                  </div>
                  <div class="food-item-spec">🥢 {f['specialty']}</div>
                  <div class="food-item-price">💰 消费预算：{f['price']}</div>
                </div>
                """
            foods_html = f"""
            <div class="food-cluster-wrap">
              <div class="food-cluster-title">🍲 <strong>目的地周边地道必吃集群 (多选不踩雷)：</strong></div>
              {food_items_html}
            </div>
            """

        html += f"""
          <!-- Content {p_key.upper()} -->
          <div class="plan-content {active_cls}" id="content-{p_key}-{day_id}">
            <div class="photo-grid">
              <div class="photo-card">
                <img src="{plan['photo_spot']}" alt="景致实拍" loading="lazy">
                <span class="photo-badge" {badge_style}>📷 秘境风光</span>
              </div>
              <div class="photo-card">
                <img src="{plan['photo_food']}" alt="美食实拍" loading="lazy">
                <span class="photo-badge" {badge_style}>🍲 地道风味</span>
              </div>
            </div>
            <h4 class="spot-name">{plan['name']}</h4>
            <div class="plan-cost-tag">🏷️ {plan['cost_detail']}</div>
            <p class="spot-desc">{plan['spot_desc']}</p>
            <div class="parking-row">
              <span>🅿️ <strong>停车指引：</strong>{plan['parking']}</span>
            </div>

            <a href="{plan['amap_url']}" target="_blank" class="amap-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71z"/></svg>
              高德一键导航主目的地
            </a>

            <!-- Nearby Play Cluster -->
            {nearby_spots_html}

            <!-- Foods Cluster -->
            {foods_html}
          </div>
        """

    html += f"""
        </div>

        <div class="tips-card">
          {tips_html}
        </div>
      </article>
    """

# Close national day section
html += """
    </section>

    <!-- Couple Roadtrip Packing Checklist (全维度装备清单) -->
    <section class="checklist-section">
      <h3>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#f97316"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 14l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
        情侣自驾 · 极细致出行准备与后备箱清单 (支持实时勾选保存)
      </h3>
"""

for cat in CHECKLIST_CATEGORIES:
    html += f"""
      <div class="check-category">
        <div class="check-cat-title">{cat['title']}</div>
    """
    for item in cat["items"]:
        html += f"""
        <label class="check-item">
          <input type="checkbox" checked onchange="saveCheckState()">
          <div class="check-item-info">
            <span>{item['name']}</span>
            <span class="check-item-note">💡 {item['note']}</span>
          </div>
        </label>
        """
    html += """
      </div>
    """

html += f"""
    </section>

    <!-- Toolbox Section -->
    <section class="toolbox">
      <h3>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#f97316"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg>
        自驾避堵与安全应急雷达
      </h3>
      <div class="toolbox-item">
        <div class="lbl">⚡ 深圳外地车限行政策</div>
        <div class="cnt">中秋与国庆法定假期期间，深圳全市暂停外地车早晚高峰限行，外地车牌自驾畅行无忧。</div>
      </div>
      <div class="toolbox-item">
        <div class="lbl">⚡ 大鹏半岛通行预约</div>
        <div class="cnt">节假日自驾进大鹏需在“深圳交警”公众号预约。本路书专门配置了平替B（惠阳澳头小桂村免预约）与平替C（盐田免预约），即使未抢到预约也能一键切换！</div>
      </div>
      <div class="toolbox-item">
        <div class="lbl">⚡ 深中通道错峰指南</div>
        <div class="cnt">深中通道早晨08:00前或中午12:30-13:30过桥最畅通；傍晚17:30-19:30车流较密，可在中山/顺德吃完晚饭后20:00返程，夜风微凉看桥面霓虹灯光秀。</div>
      </div>
      <div class="toolbox-item">
        <div class="lbl">⚡ 赶海与潮汐安全常识</div>
        <div class="cnt">去坝光或百安海滩赶海前，可用手机查‘潮汐表’，退潮时（落潮前后2小时）海螺寄居蟹最多。务必穿涉水鞋防礁石划伤。</div>
      </div>
    </section>
  </div>

  <!-- Bottom Floating Share Bar -->
  <div class="share-bar">
    <button class="share-btn" onclick="copyShareLink()">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>
      <span>一键复制微信链接 / 发给女朋友</span>
    </button>
  </div>

  <script>
    function switchMainTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-section').forEach(sec => sec.classList.remove('active'));

      if (tabId === 'mid_autumn') {{
        document.querySelectorAll('.tab-btn')[0].classList.add('active');
        document.getElementById('section-mid_autumn').classList.add('active');
      }} else {{
        document.querySelectorAll('.tab-btn')[1].classList.add('active');
        document.getElementById('section-national_day').classList.add('active');
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function switchTriplePlan(dayId, planType) {{
      const btnA = document.getElementById(`btn-a-${{dayId}}`);
      const btnB = document.getElementById(`btn-b-${{dayId}}`);
      const btnC = document.getElementById(`btn-c-${{dayId}}`);
      const contentA = document.getElementById(`content-a-${{dayId}}`);
      const contentB = document.getElementById(`content-b-${{dayId}}`);
      const contentC = document.getElementById(`content-c-${{dayId}}`);

      // Reset
      [btnA, btnB, btnC].forEach(b => {{ if (b) b.classList.remove('active'); }});
      [contentA, contentB, contentC].forEach(c => {{ if (c) c.classList.remove('active'); }});

      if (planType === 'a') {{
        btnA.classList.add('active');
        contentA.classList.add('active');
      }} else if (planType === 'b') {{
        btnB.classList.add('active');
        contentB.classList.add('active');
      }} else {{
        btnC.classList.add('active');
        contentC.classList.add('active');
      }}
    }}

    const SHARE_URL = "{SHARE_URL}";

    function copyShareLink() {{
      if (navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(SHARE_URL).then(() => {{
          showToast();
        }}).catch(() => {{
          fallbackCopy(SHARE_URL);
        }});
      }} else {{
        fallbackCopy(SHARE_URL);
      }}
    }}

    function fallbackCopy(text) {{
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-999999px";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {{
        document.execCommand('copy');
        showToast();
      }} catch (err) {{
        alert("长按复制分享链接：" + SHARE_URL);
      }}
      document.body.removeChild(textArea);
    }}

    function showToast() {{
      const toast = document.getElementById('toast');
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2500);
    }}

    function saveCheckState() {{
      try {{
        const checkboxes = document.querySelectorAll('.check-item input[type="checkbox"]');
        const states = Array.from(checkboxes).map(c => c.checked);
        localStorage.setItem('roadbook_checklist_v4', JSON.stringify(states));
      }} catch (e) {{}}
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      try {{
        const saved = JSON.parse(localStorage.getItem('roadbook_checklist_v4'));
        if (saved) {{
          const checkboxes = document.querySelectorAll('.check-item input[type="checkbox"]');
          checkboxes.forEach((c, idx) => {{
            if (saved[idx] !== undefined) c.checked = saved[idx];
          }});
        }}
      }} catch (e) {{}}
    }});
  </script>
</body>
</html>
"""

with open("/Users/Zhuanz/Documents/ChatGPT/出/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("/Users/Zhuanz/Desktop/深圳自驾路书.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated all-in-one comprehensive roadbook HTML!")
