import json

with open("roadbook_enhanced_v6.json", "r", encoding="utf-8") as f:
    mid_autumn_days = json.load(f)

with open("national_day_enhanced_v6.json", "r", encoding="utf-8") as f:
    national_days = json.load(f)

ALL_DAYS = mid_autumn_days + national_days

from generate_super_app import CHECKLIST_CATEGORIES

SHARE_URL = "https://zhaobenxiang5-coder.github.io/shenzhen-roadbook/"

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>✨ 深圳龙岗丹平出发 · 避坑反向自驾路书 (中秋3天+国庆5天) 🌟</title>
  <!-- WeChat & Social Meta -->
  <meta property="og:title" content="🌟 深圳自驾反向路书 · 中秋3天+国庆5天">
  <meta property="og:description" content="情侣专属·小清新慢调·每日回丹平睡大床·A/B/C三重平替·地道吃玩全导航 ✨">
  <meta property="og:image" content="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#0e1726">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090e1a;
      --card-bg: rgba(20, 29, 48, 0.85);
      --card-border: rgba(255, 255, 255, 0.12);
      --card-inner: rgba(13, 20, 36, 0.65);
      --primary: #fb923c;
      --primary-light: #fdba74;
      --primary-glow: rgba(251, 146, 60, 0.35);
      --star-gold: #fde047;
      --star-glow: rgba(253, 224, 71, 0.45);
      --accent: #34d399;
      --accent-glow: rgba(52, 211, 153, 0.3);
      --sky: #38bdf8;
      --purple: #a78bfa;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --border: #334155;
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
        radial-gradient(at 10% 10%, rgba(251, 146, 60, 0.14) 0px, transparent 45%),
        radial-gradient(at 90% 25%, rgba(56, 189, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 30% 75%, rgba(167, 139, 250, 0.1) 0px, transparent 50%),
        radial-gradient(at 80% 90%, rgba(52, 211, 153, 0.1) 0px, transparent 50%);
      background-attachment: fixed;
      color: var(--text);
      font-family: 'Plus Jakarta Sans', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      padding-bottom: 96px;
      position: relative;
    }}

    /* Floating Little Stars Background Animations */
    .star-sparkle {{
      position: fixed;
      pointer-events: none;
      color: var(--star-gold);
      font-size: 14px;
      opacity: 0.6;
      animation: twinkle 3.2s infinite ease-in-out alternate;
      z-index: 1;
    }}
    .star-1 {{ top: 8%; left: 8%; animation-delay: 0.2s; }}
    .star-2 {{ top: 18%; right: 10%; animation-delay: 0.8s; }}
    .star-3 {{ top: 45%; left: 4%; animation-delay: 1.4s; }}
    .star-4 {{ top: 65%; right: 6%; animation-delay: 0.5s; }}
    .star-5 {{ top: 85%; left: 12%; animation-delay: 1.9s; }}

    @keyframes twinkle {{
      0% {{ opacity: 0.2; transform: scale(0.8) rotate(0deg); }}
      50% {{ opacity: 0.9; transform: scale(1.15) rotate(45deg); }}
      100% {{ opacity: 0.3; transform: scale(0.9) rotate(90deg); }}
    }}

    .container {{
      max-width: 680px;
      margin: 0 auto;
      padding: 14px;
      position: relative;
      z-index: 2;
    }}

    /* Cover Hero Banner with warm fresh tones */
    .hero-banner {{
      position: relative;
      border-radius: 26px;
      overflow: hidden;
      margin-bottom: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
      border: 1px solid rgba(255,255,255,0.14);
    }}

    .hero-bg {{
      width: 100%;
      height: 230px;
      object-fit: cover;
      display: block;
      filter: brightness(0.68) saturate(1.2);
    }}

    .hero-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(9, 14, 26, 0.1) 0%, rgba(9, 14, 26, 0.95) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 18px;
    }}

    .meta-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(251, 146, 60, 0.25);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(251, 146, 60, 0.5);
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

    .title span.star-icon {{
      color: var(--star-gold);
      font-size: 20px;
      filter: drop-shadow(0 0 8px var(--star-gold));
    }}

    .subtitle {{
      color: #cbd5e1;
      font-size: 12px;
      line-height: 1.5;
    }}

    /* Global Cost Summary Widget */
    .cost-overview-card {{
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.15) 0%, rgba(245, 158, 11, 0.05) 100%);
      border: 1px solid rgba(251, 191, 36, 0.35);
      border-radius: 20px;
      padding: 14px 16px;
      margin-bottom: 14px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }}

    .cost-stat {{
      display: flex;
      flex-direction: column;
    }}

    .cost-stat .label {{
      font-size: 11px;
      color: #fef08a;
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
      background: rgba(13, 20, 36, 0.94);
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
      background: linear-gradient(135deg, #fb923c 0%, #ea580c 100%);
      color: #ffffff;
      box-shadow: 0 4px 18px var(--primary-glow);
    }}

    .tab-btn .badge-pill {{
      font-size: 10px;
      opacity: 0.9;
      font-weight: 500;
    }}

    .tab-intro {{
      background: rgba(30, 41, 59, 0.55);
      border-left: 3px solid var(--primary);
      padding: 10px 14px;
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
      border-radius: 24px;
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
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding-bottom: 8px;
    }}

    .day-title {{
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .day-title .sparkle {{
      color: var(--star-gold);
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
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.2);
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
      background: rgba(167, 139, 250, 0.08);
      border: 1px solid rgba(167, 139, 250, 0.25);
      border-radius: 12px;
      padding: 8px 12px;
      margin-bottom: 12px;
      font-size: 11px;
      color: #ddd6fe;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Day Cost Box */
    .day-cost-bar {{
      background: rgba(251, 191, 36, 0.08);
      border: 1px solid rgba(251, 191, 36, 0.25);
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
      background: linear-gradient(135deg, #fb923c 0%, #ea580c 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(251, 146, 60, 0.4);
    }}

    .plan-toggle-btn.active.btn-plan-b {{
      background: linear-gradient(135deg, #34d399 0%, #059669 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(52, 211, 153, 0.4);
    }}

    .plan-toggle-btn.active.btn-plan-c {{
      background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(167, 139, 250, 0.4);
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

    /* Day Timetable / Flow (超详细节奏时间线) */
    .schedule-cluster-wrap {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(253, 224, 71, 0.2);
      border-radius: 14px;
      padding: 10px 12px;
      margin-bottom: 12px;
    }}

    .schedule-title {{
      font-size: 12px;
      font-weight: 700;
      color: #fde047;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .schedule-timeline {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      position: relative;
      padding-left: 12px;
      border-left: 2px dashed rgba(253, 224, 71, 0.3);
      margin-left: 6px;
    }}

    .schedule-step {{
      position: relative;
      font-size: 11px;
    }}

    .schedule-step::before {{
      content: '✨';
      position: absolute;
      left: -20px;
      top: -2px;
      font-size: 10px;
    }}

    .schedule-time {{
      font-weight: 700;
      color: #fdba74;
      margin-bottom: 1px;
    }}

    .schedule-act {{
      color: #cbd5e1;
      line-height: 1.45;
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
      accent-color: #fb923c;
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
      background: linear-gradient(135deg, #fb923c 0%, #ea580c 100%);
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
      box-shadow: 0 10px 25px rgba(251, 146, 60, 0.45);
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

  <!-- Floating Star Sparkles -->
  <div class="star-sparkle star-1">✨</div>
  <div class="star-sparkle star-2">🌟</div>
  <div class="star-sparkle star-3">💫</div>
  <div class="star-sparkle star-4">⭐️</div>
  <div class="star-sparkle star-5">✨</div>

  <div class="toast" id="toast">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toast-text">✨ 微信分享链接已复制！快发给女朋友吧 🌟</span>
  </div>

  <div class="container">
    <!-- Hero Cover Banner -->
    <header class="hero-banner">
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80" alt="Cover" class="hero-bg">
      <div class="hero-overlay">
        <div class="meta-tag">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
          深圳龙岗丹平社区出发 · 基地化漫游
        </div>
        <h1 class="title">
          <span class="star-icon">✨</span> 深圳周边小清新自驾避坑路书 <span class="star-icon">🌟</span>
        </h1>
        <p class="subtitle">中秋3天 + 国庆5天 · 每日日归0房费 · A/B/C三重平替 · 小清新慢调吃玩全收录</p>
      </div>
    </header>

    <!-- Global Cost Overview Card -->
    <section class="cost-overview-card">
      <div class="cost-stat">
        <span class="label">🌕 中秋3天总预算 (双人)</span>
        <span class="val">¥550 - ¥700 ✨</span>
        <span class="sub">日均仅约 ¥200 (回丹平睡大床，省下¥3000+房费)</span>
      </div>
      <div class="cost-stat">
        <span class="label">🇨🇳 国庆5天总预算 (双人)</span>
        <span class="val">¥980 - ¥1300 🌟</span>
        <span class="sub">高速全免费 + 0房费 + 生猛海鲜吃到饱</span>
      </div>
    </section>

    <!-- Top Tab Navigation -->
    <nav class="tab-nav">
      <button class="tab-btn active" onclick="switchMainTab('mid_autumn')">
        <span>🌕 中秋 3 天假期</span>
        <span class="badge-pill">山野清凉 · 观海赏月 ✨</span>
      </button>
      <button class="tab-btn" onclick="switchMainTab('national_day')">
        <span>🇨🇳 国庆 5 天黄金周</span>
        <span class="badge-pill">避堵反向 · 纯净海滩 🌟</span>
      </button>
    </nav>

    <!-- Section: Mid Autumn -->
    <section id="section-mid_autumn" class="tab-section active">
      <div class="tab-intro">
        💡 <strong>中秋避堵锦囊 ✨：</strong>假期间高速不免费，东部沿海（大梅沙/较场尾）车流易集中。本路书单程严控在 35~55 分钟内，全部采用<strong>【逆向清凉 + 每日 A/B/C 三选一 + 极细致小时时间轴 + 目的地周边吃玩集群】</strong>，傍晚赏月打羽毛球，吃完夜宵回丹平安心睡好觉。
      </div>
"""

# Render Mid-Autumn and National Day days
for day in ALL_DAYS:
    day_id = day["id"]

    if day["tab"] == "national_day" and 'id="section-national_day"' not in html:
        html += """
    </section>
    <!-- Section: National Day -->
    <section id="section-national_day" class="tab-section">
      <div class="tab-intro">
        💡 <strong>国庆反向自驾法则 🌟：</strong>国庆高速全免费、全网出行井喷！本路线严格践行<strong>【10.1留在深莞边界避堵，10.2深入客家古村，10.3直奔冷门深汕海滩，10.4走顺德老街寻味，10.5登第一峰吸氧】</strong>，天天回家睡大床，省下天价酒店！
      </div>
        """

    html += f"""
      <article class="day-card" id="{day_id}">
        <div class="day-header">
          <span class="day-title"><span class="sparkle">✨</span> {day['date_str']}</span>
          <span class="crowd-pill">热度指数：★☆☆☆☆</span>
        </div>

        <div class="day-subtitle">
          <span>📍</span>
          <span>{day['tag_line']}</span>
        </div>

        <!-- Weather Box -->
        <div class="weather-box">
          <span>{day['weather_info']}</span>
          <span><strong>适宜：</strong>户外/慢调</span>
        </div>

        <!-- Gear Mini Bar -->
        <div class="gear-mini-bar">
          <span>🏸 <strong>当日随车适玩装备：</strong></span>
          <span>{day['feather_ball_spot']}</span>
        </div>

        <!-- Cost Bar -->
        <div class="day-cost-bar">
          <span class="tit">💰 当日双人预计花费</span>
          <span class="val">{day['budget_dual']}</span>
        </div>

        <div class="day-metrics">
          <div class="metric-item">
            <svg viewBox="0 0 24 24"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.85 7h10.29l1.08 3.11H5.77L6.85 7zM19 17H5v-5h14v5z"/><circle cx="7.5" cy="14.5" r="1.5"/><circle cx="16.5" cy="14.5" r="1.5"/></svg>
            <span>{day['driving_summary']}</span>
          </div>
        </div>

        <!-- Plan Switcher A / B / C -->
        <div class="plan-switch-wrap">
          <div class="plan-toggle-bar">
            <button class="plan-toggle-btn btn-plan-a active" id="btn-a-{day_id}" onclick="switchTriplePlan('{day_id}', 'a')">
              <span>🌟 主选 A</span>
            </button>
            <button class="plan-toggle-btn btn-plan-b" id="btn-b-{day_id}" onclick="switchTriplePlan('{day_id}', 'b')">
              <span>🌿 平替 B</span>
            </button>
            <button class="plan-toggle-btn btn-plan-c" id="btn-c-{day_id}" onclick="switchTriplePlan('{day_id}', 'c')">
              <span>🍃 备选 C</span>
            </button>
          </div>
    """

    for plan in day["plans"]:
        p_key = plan["key"].lower()
        active_cls = "active" if p_key == "a" else ""
        p_color = "#fb923c" if p_key == "a" else ("#34d399" if p_key == "b" else "#a78bfa")
        badge_style = "" if p_key == "a" else f"style=\"background: {p_color};\""

        # Detailed schedule timeline HTML
        schedule_html = ""
        if plan.get("timeline"):
            step_items = ""
            for step in plan["timeline"]:
                step_items += f"""
                <div class="schedule-step">
                  <div class="schedule-time">{step['time']}</div>
                  <div class="schedule-act">{step.get('desc', step.get('action', ''))}</div>
                </div>
                """
            schedule_html = f"""
            <div class="schedule-cluster-wrap">
              <div class="schedule-title">⏰ <strong>从早到晚·极细致小时时间线 (避堵节奏)：</strong></div>
              <div class="schedule-timeline">
                {step_items}
              </div>
            </div>
            """

        # Nearby spots HTML
        nearby_spots_html = ""
        if plan.get("play_cluster"):
            items_html = ""
            for s in plan["play_cluster"]:
                items_html += f"""
                <div class="cluster-item">
                  <div class="cluster-item-head">
                    <span class="cluster-item-name">{s['name']}</span>
                    <a href="{s.get('amap', '#')}" target="_blank" class="cluster-item-amap">高德导航 ✨</a>
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
        if plan.get("food_cluster"):
            food_items_html = ""
            for f in plan["food_cluster"]:
                food_items_html += f"""
                <div class="food-item-card">
                  <div class="food-item-head">
                    <span class="food-item-name">{f['name']}</span>
                    <a href="{f['amap']}" target="_blank" class="food-item-amap">导航去吃 🍲</a>
                  </div>
                  <div class="food-item-spec">🥢 {f['spec']}</div>
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
                <img src="{plan['real_photo']}" alt="景致实拍" loading="lazy">
                <span class="photo-badge" {badge_style}>📷 秘境风光</span>
              </div>
              <div class="photo-card">
                <img src="{plan['food_photo']}" alt="美食实拍" loading="lazy">
                <span class="photo-badge" {badge_style}>🍲 地道风味</span>
              </div>
            </div>
            <h4 class="spot-name">{plan['title']}</h4>
            <div class="plan-cost-tag">🏷️ {plan.get('cost_detail', '免门票高性价比')}</div>
            <p class="spot-desc">{plan.get('spot_desc', plan.get('story', ''))}</p>
            <div class="parking-row">
              <span>{plan['parking_guide']}</span>
            </div>

            <a href="{plan['main_amap']}" target="_blank" class="amap-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71z"/></svg>
              高德一键导航主目的地 🚀
            </a>

            <!-- Detailed Schedule Timeline -->
            {schedule_html}

            <!-- Nearby Play Cluster -->
            {nearby_spots_html}

            <!-- Foods Cluster -->
            {foods_html}
          </div>
        """

    html += f"""
        </div>

        <div class="tips-card">
          <div class="tips-item">• 贴心避坑提示：避开人挤人热门干道，多选择备用平替走法。</div>
          <div class="tips-item">• 穿搭建议：带好舒适运动鞋、洞洞鞋与换洗衣物，随时享受大自然。</div>
        </div>
      </article>
    """

# Close national day section
html += """
    </section>

    <!-- Couple Roadtrip Packing Checklist (全维度装备清单) -->
    <section class="checklist-section">
      <h3>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#fb923c"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 14l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
        情侣自驾 · 极细致出行准备与后备箱清单 (支持实时勾选保存) ✨
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
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#fb923c"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg>
        自驾避堵与安全应急雷达 🌟
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
      <span>✨ 一键复制微信链接 / 发给女朋友 🌟</span>
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
        localStorage.setItem('roadbook_checklist_starry_master_v6', JSON.stringify(states));
      }} catch (e) {{}}
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      try {{
        const saved = JSON.parse(localStorage.getItem('roadbook_checklist_starry_master_v6'));
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

print("Masterpiece HTML generated successfully!")
