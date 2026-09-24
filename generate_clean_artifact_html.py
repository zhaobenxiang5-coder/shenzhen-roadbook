CHECKLIST_CATEGORIES = [{"title": "🏸 户外运动与浪漫互动 (你提到的羽毛球+出片装备)", "items": [{"name": "羽毛球拍2副 + 防风羽毛球1筒 (大万世居外广场/湖畔草坪/海滩随时开打解压)", "note": "重点带上！傍晚微风打球超舒服"}, {"name": "极限飞盘/轻量沙滩球 (草坪和沙滩上两人轻松互动，好玩又吸睛)", "note": "轻量不占地"}, {"name": "赶海小工具组 (折叠小水桶、小耙子、手套，去坝光/百安海滩捡贝壳抓寄居蟹)", "note": "小红书爆款赶海必备"}, {"name": "便携蓝牙复古小音箱 (野餐/湖畔/海风中播放轻柔歌单，氛围感神器)", "note": "Marshall/JBL"}, {"name": "轻便三脚架蓝牙自拍杆 / 拍立得 (情侣两人合影不求路人，分分钟出大片)", "note": "随时捕捉女朋友笑脸"}]}, {"title": "💄 女友专属呵护与随身百宝箱 (极具情商细节)", "items": [{"name": "轻便透气防晒衣 + UPF50+黑胶遮阳伞 + 偏光墨镜 (海边山野双重防晒，不晒黑)", "note": "女孩子最在意"}, {"name": "防蚊喷雾/驱蚊贴 + 泰国青草膏 (广东山野水边小黑飞多，防叮咬止痒神物)", "note": "放随身包里随取随用"}, {"name": "车载便携小毛毯/软披肩 (副驾空调吹久了容易膝盖着凉，贴心指数五星)", "note": "车内必备"}, {"name": "维达便携抽纸 + 75%酒精独立湿巾 + 湿厕纸 (吃完海鲜窑鸡擦手清洁)", "note": "卫生保障"}, {"name": "便携发绳/抓夹 + 小木梳 (海边山风吹乱头发时随手扎起，拍照利落)", "note": "随时整理发型"}, {"name": "大容量保温水杯 (提前装好温热柠檬水或红枣枸杞茶，随时暖胃解腻)", "note": "健康暖心"}, {"name": "备用涉水洞洞鞋/凉鞋 + 换洗干T恤一套 (溯溪或海边踩水湿身可即刻换下)", "note": "干爽舒服回家睡"}]}, {"title": "⛺ 舒适露营与车内后备箱收纳", "items": [{"name": "便携铝合金折叠月亮椅×2 (收纳起来极小，湖边海边一撑就是VIP观景点)", "note": "比硬石凳舒服百倍"}, {"name": "加厚防潮防水铝膜野餐垫 (大草坪铺开，躺着吹风刷剧极度惬意)", "note": "200×200cm大号"}, {"name": "便携车载保温冷藏包 + 冰袋 (放两杯喜茶/霸王茶姬/冰镇气泡水，随时喝冷饮)", "note": "快乐源泉"}, {"name": "车载加厚抽绳垃圾袋一卷 (户外无痕露营，随手打包所有果皮包装纸带走)", "note": "文明自驾"}]}, {"title": "🚗 车辆驾驶与长途安全保障", "items": [{"name": "双口车载快充头 65W + 苹果/Type-C快充线各1根 (两台手机导航拍照全天不断电)", "note": "避免电量焦虑"}, {"name": "出风口防抖重力手机支架 (高德导航视角平视无遮挡)", "note": "驾驶安全第一"}, {"name": "整箱500ml矿泉水一箱放后备箱 (随时补水，踩泥玩沙后也可当流动水源冲洗手脚)", "note": "万能用途"}, {"name": "便携车载充气泵 + 胎压计 (出发前核对冷胎压2.3-2.5bar，高速安心驾驶)", "note": "长途必备"}, {"name": "行车记录仪存储卡清空核查 (确保循环录像正常，沿途记录跨海大桥绝美风景)", "note": "安全兜底"}]}, {"title": "🛡️ 证件与应急药品 (以防万一)", "items": [{"name": "双人身份证原件 (景区购票核验、检查站备用)", "note": "必备"}, {"name": "20000mAh快充移动电源充电宝 (下车游玩全天拍照续航保障)", "note": "随身携带"}, {"name": "便携药盒 (创口贴、布洛芬、晕车贴、健胃消食片、氯雷他定抗过敏)", "note": "吃海鲜防过敏"}, {"name": "大号晴雨两用伞2把 (放在主驾/副驾车门储物格，随手可取)", "note": "遮阳挡雨两不误"}]}]
import json

# Full accurate data matching the user's Claude Artifact reference style
with open("roadbook_enhanced_v6.json", "r", encoding="utf-8") as f:
    mid_days = json.load(f)

with open("national_day_enhanced_v6.json", "r", encoding="utf-8") as f:
    nat_days = json.load(f)

# Combine days and format cleanly
ALL_TRIPS = {
    "mid_autumn": {
        "name": "中秋 3 天假期",
        "dates": "9.24 - 9.26 · 每日日归回丹平大床",
        "summary": "35~55分钟短途微自驾 · 避开东部大梅沙较场尾99%车流 · 溯溪吹海风吃窑鸡",
        "budget": "双人3天总花费约 ¥550 - ¥700 (日均仅约 ¥200，省下¥3000+房费)",
        "days": mid_days
    },
    "national_day": {
        "name": "国庆 5 天黄金周",
        "dates": "10.1 - 10.5 · 高速全免费 · 每日日归",
        "summary": "反向避堵原则 · 10.1不出深 · 10.2客家村 · 10.3深汕果冻海 · 10.4顺德桑拿鸡 · 10.5第一峰",
        "budget": "双人5天总花费约 ¥980 - ¥1300 (高速全免费 + 0房费 + 生猛海鲜)",
        "days": nat_days
    }
}

SHARE_URL = "https://zhaobenxiang5-coder.github.io/shenzhen-roadbook/"

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>深圳龙岗丹平出发 · 自驾路书</title>
  <!-- WeChat & Social Meta -->
  <meta property="og:title" content="深圳自驾反向路书 · 中秋3天+国庆5天">
  <meta property="og:description" content="情侣日归·避堵慢行·每日回丹平睡大床·A/B/C三重平替·地道吃玩全导航">
  <meta property="og:image" content="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="theme-color" content="#faf9f5">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Noto+Serif+SC:wght@500;600;700;900&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #faf9f5;
      --card-bg: #ffffff;
      --card-subtle: #f5f4ef;
      --border-subtle: #eae8e1;
      --border-strong: #d8d5cb;
      --text-main: #1f2328;
      --text-muted: #656d76;
      --text-dim: #8c959f;
      --primary: #c25e00;
      --primary-soft: #fff6ed;
      --primary-border: #fcd9bd;
      --accent-green: #1b7c53;
      --accent-green-soft: #edf8f3;
      --accent-purple: #634099;
      --accent-purple-soft: #f5f0fc;
      --accent-blue: #0969da;
      --accent-blue-soft: #edf5fd;
      --shadow-sm: 0 1px 3px rgba(31,35,40,0.04), 0 8px 24px rgba(31,35,40,0.04);
      --shadow-hover: 0 6px 16px rgba(31,35,40,0.08);
      --font-serif: 'Noto Serif SC', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background-color: var(--bg);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.65;
      min-height: 100vh;
      padding-bottom: 96px;
      -webkit-font-smoothing: antialiased;
    }}

    .container {{
      max-width: 680px;
      margin: 0 auto;
      padding: 24px 16px;
    }}

    /* Editorial Header Block */
    .header {{
      padding: 12px 0 24px;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 20px;
    }}

    .meta-line {{
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-dim);
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}

    .meta-line .dot {{
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #c8c5bc;
    }}

    .page-title {{
      font-family: var(--font-serif);
      font-size: 30px;
      font-weight: 900;
      color: var(--text-main);
      letter-spacing: -0.5px;
      line-height: 1.25;
      margin-bottom: 10px;
    }}

    .intro-paragraph {{
      color: var(--text-muted);
      font-size: 13.5px;
      line-height: 1.6;
    }}

    /* Principle Card (每日回丹平大床) */
    .principle-banner {{
      background: var(--card-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 12px 14px;
      margin-top: 14px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 12.5px;
      color: var(--text-muted);
    }}

    .principle-banner strong {{
      color: var(--primary);
    }}

    /* Main Tab Navigation (中秋 3 天 / 国庆 5 天) */
    .season-nav {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 20px;
    }}

    .season-btn {{
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      padding: 12px 14px;
      border-radius: 12px;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .season-btn.active {{
      border-color: var(--primary);
      background: var(--primary-soft);
      box-shadow: 0 2px 8px rgba(194,94,0,0.08);
    }}

    .season-btn .btn-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }}

    .season-btn.active .btn-title {{
      color: var(--primary);
    }}

    .season-btn .btn-desc {{
      font-size: 11px;
      color: var(--text-dim);
    }}

    .season-btn.active .btn-desc {{
      color: var(--primary);
      opacity: 0.85;
    }}

    /* Day Card Container */
    .day-card {{
      background: var(--card-bg);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 20px 18px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .day-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 6px;
    }}

    .day-num {{
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 900;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .day-date-badge {{
      font-family: var(--font-sans);
      font-size: 11px;
      font-weight: 600;
      color: var(--primary);
      background: var(--primary-soft);
      border: 1px solid var(--primary-border);
      padding: 2px 8px;
      border-radius: 6px;
    }}

    .day-vibe {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}

    /* Minimalist Route Strip (线路节点流) */
    .route-strip {{
      display: flex;
      align-items: center;
      gap: 6px;
      overflow-x: auto;
      padding: 8px 0 12px;
      margin-bottom: 14px;
      border-bottom: 1px dashed var(--border-subtle);
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}
    .route-strip::-webkit-scrollbar {{
      display: none;
    }}

    .route-node {{
      flex-shrink: 0;
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11.5px;
      color: var(--text-muted);
    }}

    .route-node .point {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--primary);
      flex-shrink: 0;
    }}

    .route-node .arrow {{
      color: var(--text-dim);
      font-size: 10px;
    }}

    /* Metrics Grid (里程·耗时·天气·羽毛球) */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: var(--card-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 10px 12px;
      font-size: 11.5px;
      color: var(--text-muted);
      margin-bottom: 16px;
    }}

    .metric-row {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .metric-row strong {{
      color: var(--text-main);
    }}

    /* Triple Plan Switcher (A / B / C 选项卡) */
    .plan-tabs {{
      display: flex;
      gap: 6px;
      background: var(--card-subtle);
      padding: 4px;
      border-radius: 10px;
      margin-bottom: 14px;
    }}

    .plan-tab-btn {{
      flex: 1;
      background: transparent;
      border: none;
      padding: 7px 10px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      border-radius: 7px;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: center;
    }}

    .plan-tab-btn.active.tab-a {{
      background: #ffffff;
      color: var(--primary);
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }}

    .plan-tab-btn.active.tab-b {{
      background: #ffffff;
      color: var(--accent-green);
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }}

    .plan-tab-btn.active.tab-c {{
      background: #ffffff;
      color: var(--accent-purple);
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }}

    .plan-panel {{
      display: none;
    }}
    .plan-panel.active {{
      display: block;
    }}

    /* Photo Dual Grid */
    .photo-dual {{
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 8px;
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 12px;
      height: 145px;
    }}

    .photo-item {{
      position: relative;
      height: 100%;
      background: #eee;
    }}

    .photo-item img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .photo-tag {{
      position: absolute;
      bottom: 6px;
      left: 6px;
      background: rgba(31,35,40,0.7);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      color: #ffffff;
      font-size: 9.5px;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .spot-header-block {{
      margin-bottom: 8px;
    }}

    .spot-title {{
      font-family: var(--font-serif);
      font-size: 16px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.35;
      margin-bottom: 4px;
    }}

    .spot-summary {{
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 10px;
    }}

    .parking-info-row {{
      background: var(--accent-blue-soft);
      border: 1px solid rgba(9,105,218,0.18);
      border-radius: 8px;
      padding: 8px 10px;
      font-size: 11.5px;
      color: var(--accent-blue);
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      gap: 6px;
    }}

    /* Main Navigation Button (高德地图一键直达) */
    .amap-link-button {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--primary);
      color: #ffffff;
      text-decoration: none;
      padding: 10px 14px;
      border-radius: 10px;
      font-size: 12.5px;
      font-weight: 600;
      margin-bottom: 14px;
      box-shadow: 0 2px 6px rgba(194,94,0,0.25);
      transition: opacity 0.15s ease;
    }}
    .amap-link-button:active {{
      opacity: 0.85;
    }}

    /* Detailed Hour-by-Hour Timeline */
    .timeline-wrap {{
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 10px 12px;
      background: #fafaf8;
      margin-bottom: 14px;
    }}

    .timeline-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .timeline-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      border-left: 2px solid var(--border-subtle);
      padding-left: 10px;
      margin-left: 4px;
    }}

    .timeline-step {{
      font-size: 11.5px;
    }}

    .timeline-time {{
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1px;
    }}

    .timeline-text {{
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Cluster Blocks (玩点集群 & 美食集群) */
    .cluster-box {{
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 10px 12px;
      background: #ffffff;
      margin-bottom: 12px;
    }}

    .cluster-box.play-box {{
      border-left: 3px solid var(--sky);
    }}

    .cluster-box.food-box {{
      border-left: 3px solid var(--primary);
    }}

    .cluster-header {{
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .play-box .cluster-header {{ color: var(--accent-blue); }}
    .food-box .cluster-header {{ color: var(--primary); }}

    .item-card {{
      background: var(--card-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 8px 10px;
      margin-bottom: 6px;
      font-size: 11.5px;
    }}
    .item-card:last-child {{
      margin-bottom: 0;
    }}

    .item-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }}

    .item-name {{
      font-weight: 700;
      color: var(--text-main);
    }}

    .item-nav-btn {{
      font-size: 10.5px;
      color: var(--primary);
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      padding: 2px 7px;
      border-radius: 4px;
      text-decoration: none;
      font-weight: 600;
    }}
    .play-box .item-nav-btn {{
      color: var(--accent-blue);
    }}

    .item-desc {{
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .item-price {{
      color: var(--text-dim);
      font-size: 10.5px;
      margin-top: 2px;
    }}

    /* Interactive Checklist Section */
    .checklist-wrap {{
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 18px;
      margin-top: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .checklist-header {{
      font-family: var(--font-serif);
      font-size: 17px;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .check-group {{
      margin-bottom: 14px;
    }}

    .check-group-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 6px;
    }}

    .check-item-row {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      background: var(--card-subtle);
      border: 1px solid var(--border-subtle);
      padding: 7px 10px;
      border-radius: 8px;
      margin-bottom: 5px;
      font-size: 12px;
      cursor: pointer;
    }}

    .check-item-row input[type="checkbox"] {{
      margin-top: 3px;
      accent-color: var(--primary);
      width: 14px;
      height: 14px;
    }}

    .check-item-row span {{
      color: var(--text-main);
      line-height: 1.4;
    }}

    /* Toolbox Section */
    .toolbox-wrap {{
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 16px 18px;
      margin-top: 18px;
      box-shadow: var(--shadow-sm);
    }}

    .toolbox-title {{
      font-family: var(--font-serif);
      font-size: 15px;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 10px;
    }}

    .toolbox-row {{
      padding: 8px 0;
      border-bottom: 1px solid var(--border-subtle);
      font-size: 11.5px;
    }}
    .toolbox-row:last-child {{
      border-bottom: none;
    }}
    .toolbox-row .lbl {{
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 2px;
    }}
    .toolbox-row .cnt {{
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Bottom Floating Action Bar */
    .share-bar {{
      position: fixed;
      bottom: 16px;
      left: 50%;
      transform: translateX(-50%);
      width: calc(100% - 32px);
      max-width: 480px;
      z-index: 100;
    }}

    .share-btn {{
      width: 100%;
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 13px 20px;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 13.5px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(194,94,0,0.3);
      cursor: pointer;
    }}

    .toast {{
      position: fixed;
      top: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(-100px);
      background: #1f2328;
      color: #ffffff;
      font-size: 13px;
      padding: 9px 18px;
      border-radius: 9999px;
      z-index: 999;
      opacity: 0;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    .season-section {{
      display: none;
    }}
    .season-section.active {{
      display: block;
    }}
  </style>
</head>
<body>

  <div class="toast" id="toast">
    <span>✓ 微信分享链接已复制，可直接发给女朋友</span>
  </div>

  <div class="container">
    <!-- Editorial Header Block -->
    <header class="header">
      <div class="meta-line">
        <span>深圳龙岗丹平社区出发</span>
        <span class="dot"></span>
        <span>自驾日归路书</span>
        <span class="dot"></span>
        <span>情侣避堵指南</span>
      </div>
      <h1 class="page-title">深圳反向自驾路书</h1>
      <p class="intro-paragraph">
        专为情侣二人出游定制。拒绝人挤人的大梅沙、较场尾与深圳湾，精选单程 20~80 分钟清凉溪谷、客家围屋、静谧深蓝海滩与顺德市井老味。
      </p>
      <div class="principle-banner">
        <span>🏡</span>
        <div>
          <strong>每日日归法则：</strong>白天自驾尽兴玩，夜晚吃完夜宵回丹平睡舒服大床，0 酒店溢价，轻松省下数千元。
        </div>
      </div>
    </header>

    <!-- Main Navigation: Mid-Autumn vs National Day -->
    <nav class="season-nav">
      <button class="season-btn active" id="btn-mid_autumn" onclick="switchSeason('mid_autumn')">
        <span class="btn-title">🌕 中秋 3 天假期</span>
        <span class="btn-desc">9.24 - 9.26 · 山野清凉与观海</span>
      </button>
      <button class="season-btn" id="btn-national_day" onclick="switchSeason('national_day')">
        <span class="btn-title">🇨🇳 国庆 5 天黄金周</span>
        <span class="btn-desc">10.1 - 10.5 · 逆向反堵与深蓝海</span>
      </button>
    </nav>
"""

# Render both seasons
for season_key, season in ALL_TRIPS.items():
    active_cls = "active" if season_key == "mid_autumn" else ""
    html += f"""
    <section id="section-{season_key}" class="season-section {active_cls}">
    """

    for day in season["days"]:
        day_id = day["id"]
        plans = day["plans"]

        html += f"""
      <article class="day-card" id="{day_id}">
        <div class="day-header">
          <div class="day-num">
            <span>{day['date_str']}</span>
            <span class="day-date-badge">{day['badge'] if 'badge' in day else '当日日归'}</span>
          </div>
        </div>

        <div class="day-vibe">{day['tag_line']}</div>

        <!-- Route strip -->
        <div class="route-strip">
          <div class="route-node"><span class="point"></span><span>丹平出发</span><span class="arrow">→</span></div>
          <div class="route-node"><span class="point"></span><span>主目的地玩水/逛村</span><span class="arrow">→</span></div>
          <div class="route-node"><span class="point"></span><span>特色美食正餐</span><span class="arrow">→</span></div>
          <div class="route-node"><span class="point"></span><span>羽毛球/草坪闲坐</span><span class="arrow">→</span></div>
          <div class="route-node"><span class="point"></span><span>回丹平大床睡好觉</span></div>
        </div>

        <!-- Metrics Grid -->
        <div class="metrics-grid">
          <div class="metric-row"><span>🚗</span><span><strong>路程：</strong>{day['driving_summary']}</span></div>
          <div class="metric-row"><span>⛅</span><span><strong>天气：</strong>{day['weather_info']}</span></div>
          <div class="metric-row"><span>💰</span><span><strong>消费：</strong>{day['budget_dual']}</span></div>
          <div class="metric-row"><span>🏸</span><span><strong>场地：</strong>{day['feather_ball_spot']}</span></div>
        </div>

        <!-- Plan Switcher (A / B / C) -->
        <div class="plan-tabs">
          <button class="plan-tab-btn active tab-a" id="tab-btn-a-{day_id}" onclick="switchSubPlan('{day_id}', 'a')">🌟 主选 A</button>
          <button class="plan-tab-btn tab-b" id="tab-btn-b-{day_id}" onclick="switchSubPlan('{day_id}', 'b')">🌿 平替 B</button>
          <button class="plan-tab-btn tab-c" id="tab-btn-c-{day_id}" onclick="switchSubPlan('{day_id}', 'c')">🍃 备选 C</button>
        </div>
        """

        for plan in plans:
            p_key = plan["key"].lower()
            p_active = "active" if p_key == "a" else ""

            # Timeline steps
            timeline_html = ""
            if plan.get("timeline"):
                steps_html = "".join([f"""
                <div class="timeline-step">
                  <div class="timeline-time">{t['time']}</div>
                  <div class="timeline-text">{t.get('desc', t.get('action', ''))}</div>
                </div>
                """ for t in plan["timeline"]])
                timeline_html = f"""
                <div class="timeline-wrap">
                  <div class="timeline-title">⏰ 当日时间执行节奏 (避开车潮)</div>
                  <div class="timeline-list">{steps_html}</div>
                </div>
                """

            # Play Cluster
            play_html = ""
            if plan.get("play_cluster"):
                items = "".join([f"""
                <div class="item-card">
                  <div class="item-top">
                    <span class="item-name">{s['name']}</span>
                    <a href="{s.get('amap', '#')}" target="_blank" class="item-nav-btn">高德导航</a>
                  </div>
                  <div class="item-desc">{s['desc']}</div>
                </div>
                """ for s in plan["play_cluster"]])
                play_html = f"""
                <div class="cluster-box play-box">
                  <div class="cluster-header"><span>🎡 目的地周边精选玩点 (10分钟车程内)</span></div>
                  {items}
                </div>
                """

            # Food Cluster
            food_html = ""
            if plan.get("food_cluster"):
                items = "".join([f"""
                <div class="item-card">
                  <div class="item-top">
                    <span class="item-name">{f['name']}</span>
                    <a href="{f.get('amap', '#')}" target="_blank" class="item-nav-btn">导航去吃</a>
                  </div>
                  <div class="item-desc">{f.get('spec', f.get('specialty', ''))}</div>
                  <div class="item-price">{f.get('price', '')}</div>
                </div>
                """ for f in plan["food_cluster"]])
                food_html = f"""
                <div class="cluster-box food-box">
                  <div class="cluster-header"><span>🍲 目的地周边地道必吃 (多选不踩雷)</span></div>
                  {items}
                </div>
                """

            html += f"""
          <div class="plan-panel {p_active}" id="plan-panel-{p_key}-{day_id}">
            <!-- Photo Dual -->
            <div class="photo-dual">
              <div class="photo-item">
                <img src="{plan['real_photo']}" alt="实拍风景" loading="lazy">
                <span class="photo-tag">实景风光</span>
              </div>
              <div class="photo-item">
                <img src="{plan['food_photo']}" alt="实拍美食" loading="lazy">
                <span class="photo-tag">特色美味</span>
              </div>
            </div>

            <div class="spot-header-block">
              <h3 class="spot-title">{plan['title']}</h3>
              <p class="spot-summary">{plan.get('spot_desc', plan.get('story', ''))}</p>
            </div>

            <div class="parking-info-row">
              <span>🅿️</span>
              <span>{plan['parking_guide']}</span>
            </div>

            <a href="{plan['main_amap']}" target="_blank" class="amap-link-button">
              高德一键导航主目的地
            </a>

            {timeline_html}
            {play_html}
            {food_html}
          </div>
            """

        html += """
      </article>
        """

    html += """
    </section>
    """

# Add Equipment Checklist Section
html += """
    <!-- Equipment Checklist Section -->
    <section class="checklist-wrap">
      <h3 class="checklist-header">
        <span>🎒</span>
        <span>情侣自驾 · 随车装备核对清单 (可打勾保存)</span>
      </h3>
"""

for cat in CHECKLIST_CATEGORIES:
    html += f"""
      <div class="check-group">
        <div class="check-group-title">{cat['title']}</div>
    """
    for item in cat["items"]:
        html += f"""
        <label class="check-item-row">
          <input type="checkbox" checked onchange="saveCheckState()">
          <span>{item['name']} <small style="color:var(--text-dim);">({item['note']})</small></span>
        </label>
        """
    html += """
      </div>
    """

html += """
    </section>

    <!-- Practical Toolbox Section -->
    <section class="toolbox-wrap">
      <h4 class="toolbox-title">🚦 自驾避堵与安全须知</h4>
      <div class="toolbox-row">
        <div class="lbl">深圳外地车限行政策</div>
        <div class="cnt">中秋与国庆法定假日期间，深圳全市暂停外地车早晚高峰限行，畅行无忧。</div>
      </div>
      <div class="toolbox-row">
        <div class="lbl">大鹏通行预约避坑</div>
        <div class="cnt">节假日大鹏半岛限行需在‘深圳交警’公众号预约。路书特意设置了备选平替（如惠阳澳头小桂村无需任何预约），若未抢到预约号可一键切换平替！</div>
      </div>
      <div class="toolbox-row">
        <div class="lbl">深中通道过桥窗口</div>
        <div class="cnt">早晨08:00前或中午12:30-13:30过桥最畅通；傍晚看落日晚霞，晚饭后20:00返程夜景极美。</div>
      </div>
    </section>
  </div>

  <!-- Bottom Floating Share Bar -->
  <div class="share-bar">
    <button class="share-btn" onclick="copyShareLink()">
      <span>分享给女朋友 / 收藏路书</span>
    </button>
  </div>

  <script>
    function switchSeason(seasonKey) {
      document.querySelectorAll('.season-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.season-section').forEach(s => s.classList.remove('active'));

      document.getElementById('btn-' + seasonKey).classList.add('active');
      document.getElementById('section-' + seasonKey).classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function switchSubPlan(dayId, pKey) {
      const btnA = document.getElementById(`tab-btn-a-${dayId}`);
      const btnB = document.getElementById(`tab-btn-b-${dayId}`);
      const btnC = document.getElementById(`tab-btn-c-${dayId}`);

      const panelA = document.getElementById(`plan-panel-a-${dayId}`);
      const panelB = document.getElementById(`plan-panel-b-${dayId}`);
      const panelC = document.getElementById(`plan-panel-c-${dayId}`);

      [btnA, btnB, btnC].forEach(b => b && b.classList.remove('active'));
      [panelA, panelB, panelC].forEach(p => p && p.classList.remove('active'));

      if (pKey === 'a') {
        btnA.classList.add('active');
        panelA.classList.add('active');
      } else if (pKey === 'b') {
        btnB.classList.add('active');
        panelB.classList.add('active');
      } else {
        btnC.classList.add('active');
        panelC.classList.add('active');
      }
    }

    const SHARE_URL = "https://zhaobenxiang5-coder.github.io/shenzhen-roadbook/";

    function copyShareLink() {
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(SHARE_URL).then(() => {
          showToast();
        }).catch(() => {
          fallbackCopy(SHARE_URL);
        });
      } else {
        fallbackCopy(SHARE_URL);
      }
    }

    function fallbackCopy(text) {
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-999999px";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        showToast();
      } catch (err) {
        alert("长按复制分享链接：" + SHARE_URL);
      }
      document.body.removeChild(textArea);
    }

    function showToast() {
      const toast = document.getElementById('toast');
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    function saveCheckState() {
      try {
        const checkboxes = document.querySelectorAll('.check-item-row input[type="checkbox"]');
        const states = Array.from(checkboxes).map(c => c.checked);
        localStorage.setItem('roadbook_clean_checklist_state', JSON.stringify(states));
      } catch (e) {}
    }

    window.addEventListener('DOMContentLoaded', () => {
      try {
        const saved = JSON.parse(localStorage.getItem('roadbook_clean_checklist_state'));
        if (saved) {
          const checkboxes = document.querySelectorAll('.check-item-row input[type="checkbox"]');
          checkboxes.forEach((c, idx) => {
            if (saved[idx] !== undefined) c.checked = saved[idx];
          });
        }
      } catch (e) {}
    });
  </script>
</body>
</html>
"""

with open("/Users/Zhuanz/Documents/ChatGPT/出/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("/Users/Zhuanz/Desktop/深圳自驾路书.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated clean, refined Claude Artifact editorial styled roadbook HTML!")
