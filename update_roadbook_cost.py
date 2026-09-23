import json

with open("roadbook_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Update budget and costs for each day and subplan
# Mid-Autumn Day 1
data["tabs"][0]["days"][0]["cost_summary"] = {
    "total_day": "约 ¥170 - ¥220 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "油费/电费约 ¥25 + 高速路费 ¥0 (中秋走水官/南坪免费段或低收费)",
    "tickets": "门票 ¥0 (碧岭瀑布与大万世居均免费免门票)",
    "parking_cost": "约 ¥10 (生态停车场 ¥5-10/天)",
    "food_cost": "正餐窑鸡煲约 ¥140-180 (双人吃饱)"
}
data["tabs"][0]["days"][0]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥10 | 客家窑鸡双人餐约 ¥150"
data["tabs"][0]["days"][0]["plan_b"]["cost_detail"] = "园山门票 ¥15/人 | 停车 ¥10 | 潮汕牛肉火锅双人约 ¥160"

# Mid-Autumn Day 2
data["tabs"][0]["days"][1]["cost_summary"] = {
    "total_day": "约 ¥220 - ¥280 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "油费/电费约 ¥35 + 高速路费约 ¥20",
    "tickets": "门票 ¥0 (坝光古银叶树湿地/白沙湾全部免费开放)",
    "parking_cost": "约 ¥15 (湿地公园地下/露天停车场)",
    "food_cost": "葵涌老街海鲜私房菜/小桂渔排加工约 ¥180-220 (双人3菜1汤)"
}
data["tabs"][0]["days"][1]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥15 | 老街海鲜双人餐约 ¥190"
data["tabs"][0]["days"][1]["plan_b"]["cost_detail"] = "门票 ¥0 | 绿道租双人车 ¥30 | 码头现挑海鲜加工约 ¥160"

# Mid-Autumn Day 3
data["tabs"][0]["days"][2]["cost_summary"] = {
    "total_day": "约 ¥160 - ¥210 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "油费/电费约 ¥20 + 高速路费约 ¥10 (从莞深清平)",
    "tickets": "门票 ¥0 (大屏嶂森林公园纯天然免票)",
    "parking_cost": "¥0 (大屏嶂南门免费停车)",
    "food_cost": "传统瓦煲农家碌鹅双人套餐约 ¥140-160 + 手工糖水小吃 ¥25"
}
data["tabs"][0]["days"][2]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥0 | 农家碌鹅正餐约 ¥150"
data["tabs"][0]["days"][2]["plan_b"]["cost_detail"] = "门票 ¥0 | 停车 ¥5 | 守珍街老铺糖水小吃双人约 ¥45"

# National Day Day 1
data["tabs"][1]["days"][0]["cost_summary"] = {
    "total_day": "约 ¥130 - ¥170 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "电费/油费约 ¥12 + 高速 ¥0 (地面辅道直达，不走收费公路)",
    "tickets": "门票 ¥0 (森林湖畔步道免门票)",
    "parking_cost": "¥0 (湖畔及生态园周边免停车费)",
    "food_cost": "客家瓦煲黄鳝饭 + 猪肚鸡双人约 ¥120-150"
}
data["tabs"][1]["days"][0]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥0 | 瓦煲黄鳝饭双人约 ¥130"
data["tabs"][1]["days"][0]["plan_b"]["cost_detail"] = "门票 ¥0 | 停车 ¥0 | 浓香胡椒猪肚鸡约 ¥140"

# National Day Day 2
data["tabs"][1]["days"][1]["cost_summary"] = {
    "total_day": "约 ¥180 - ¥240 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "国庆高速免费！纯电/油费仅约 ¥28",
    "tickets": "门票 ¥0 (秋长谷里古建筑群免费开放，观澜版画村免预约免费)",
    "parking_cost": "¥0 (秋长谷里专属免费停车场)",
    "food_cost": "农庄大锅三杯鸭 + 现打客家艾粄约 ¥150-180"
}
data["tabs"][1]["days"][1]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥0 | 柴火三杯鸭双人餐约 ¥160"
data["tabs"][1]["days"][1]["plan_b"]["cost_detail"] = "门票 ¥0 | 停车 ¥10 | 观澜老街腌面及第汤双人约 ¥50"

# National Day Day 3
data["tabs"][1]["days"][2]["cost_summary"] = {
    "total_day": "约 ¥260 - ¥340 (双人)",
    "hotel": "¥0 (回丹平睡大床，省下海边酒店千元溢价！)",
    "gas_toll": "国庆高速免费！往返沈海高速电/油费约 ¥65",
    "tickets": "门票 ¥0 (鲘门百安沙滩天然开放，不收门票)",
    "parking_cost": "约 ¥10-20 (村口开敞停车场)",
    "food_cost": "鲘门渔港生猛海鲜大餐（马鲛鱼丸汤+红鲟饭+炒花蟹）约 ¥200-260"
}
data["tabs"][1]["days"][2]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥15 | 渔港生猛海鲜双人约 ¥230"
data["tabs"][1]["days"][2]["plan_b"]["cost_detail"] = "门票 ¥0 | 观光车 ¥20/人 | 南澳海胆炒饭双人约 ¥150"

# National Day Day 4
data["tabs"][1]["days"][3]["cost_summary"] = {
    "total_day": "约 ¥240 - ¥320 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "国庆深中通道与高速全免费！往返纯电/油费约 ¥55",
    "tickets": "门票 ¥0 (容桂文创老街、渔人码头及崖口稻田均无门票)",
    "parking_cost": "约 ¥15 (滨河路及德胜河南岸路边车位)",
    "food_cost": "世界美食之都顺德私房桑拿鸡/双皮奶/生滚粥约 ¥180-230"
}
data["tabs"][1]["days"][3]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥15 | 现蒸桑拿鸡双人餐约 ¥190"
data["tabs"][1]["days"][3]["plan_b"]["cost_detail"] = "门票 ¥0 | 停车 ¥10 | 崖口海鲜云吞煲仔饭约 ¥110"

# National Day Day 5
data["tabs"][1]["days"][4]["cost_summary"] = {
    "total_day": "约 ¥170 - ¥220 (双人)",
    "hotel": "¥0 (回丹平睡大床)",
    "gas_toll": "国庆高速免费！往返电/油费约 ¥32",
    "tickets": "门票 ¥0 (东莞银瓶山森林公园全免票入园)",
    "parking_cost": "约 ¥10 (谢岗景区第一生态停车场)",
    "food_cost": "山泉水慢火炖走地鸡汤 + 紫苏爆炒山坑螺约 ¥140-180"
}
data["tabs"][1]["days"][4]["plan_a"]["cost_detail"] = "门票 ¥0 | 停车 ¥10 | 泉水土鸡农家菜约 ¥150"
data["tabs"][1]["days"][4]["plan_b"]["cost_detail"] = "门票 ¥0 | 停车 ¥10 | 盐田脆皮乳鸽海鲜肠粉约 ¥130"

with open("roadbook_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("roadbook_data.json updated with comprehensive price and cost transparency!")
