import json

with open("roadbook_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>{data['meta']['title']}</title>
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#1a202c">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0b0f19;
      --card-bg: rgba(22, 30, 46, 0.75);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover: rgba(30, 41, 65, 0.9);
      --primary: #f97316;
      --primary-light: #fb923c;
      --primary-glow: rgba(249, 115, 22, 0.25);
      --accent: #10b981;
      --accent-glow: rgba(16, 185, 129, 0.2);
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --border: #334155;
      --shadow-sm: 0 2px 8px rgba(0,0,0,0.25);
      --shadow-lg: 0 10px 30px -5px rgba(0,0,0,0.5);
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
        radial-gradient(at 0% 0%, rgba(249, 115, 22, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(30, 41, 65, 0.4) 0px, transparent 100%);
      background-attachment: fixed;
      color: var(--text);
      font-family: 'Plus Jakarta Sans', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      padding-bottom: 90px;
    }}

    /* Container */
    .container {{
      max-width: 680px;
      margin: 0 auto;
      padding: 20px 16px;
    }}

    /* Header */
    .header {{
      padding: 24px 0 16px;
      text-align: left;
      position: relative;
    }}

    .meta-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(249, 115, 22, 0.15);
      border: 1px solid rgba(249, 115, 22, 0.35);
      color: #fdba74;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }}

    .title {{
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.5px;
      line-height: 1.25;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 13px;
      line-height: 1.5;
    }}

    .base-card {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 14px 16px;
      margin-top: 14px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}

    .base-icon {{
      font-size: 22px;
      line-height: 1;
      padding: 6px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 10px;
    }}

    .base-info h4 {{
      font-size: 13px;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 2px;
    }}

    .base-info p {{
      font-size: 12px;
      color: var(--text-dim);
      line-height: 1.4;
    }}

    /* Tab switcher */
    .tab-nav {{
      position: sticky;
      top: 10px;
      z-index: 99;
      background: rgba(11, 15, 25, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 6px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 18px 0;
      box-shadow: var(--shadow-lg);
    }}

    .tab-btn {{
      background: transparent;
      border: none;
      outline: none;
      padding: 10px 14px;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 13px;
      border-radius: 12px;
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
      box-shadow: 0 4px 15px var(--primary-glow);
    }}

    .tab-btn .badge-pill {{
      font-size: 10px;
      opacity: 0.85;
      font-weight: 500;
    }}

    /* Intro box */
    .tab-intro {{
      background: rgba(30, 41, 59, 0.4);
      border-left: 3px solid var(--primary);
      padding: 10px 14px;
      border-radius: 4px 12px 12px 4px;
      font-size: 12px;
      color: #cbd5e1;
      margin-bottom: 20px;
      line-height: 1.5;
    }}

    /* Day Card */
    .day-card {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 20px;
      margin-bottom: 22px;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s ease, border-color 0.2s ease;
      position: relative;
      overflow: hidden;
    }}

    .day-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      padding-bottom: 12px;
    }}

    .day-tag {{
      display: flex;
      align-items: baseline;
      gap: 8px;
    }}

    .day-title {{
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
    }}

    .day-date {{
      font-size: 12px;
      font-weight: 600;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 8px;
      border-radius: 6px;
    }}

    .crowd-pill {{
      font-size: 11px;
      color: #34d399;
      background: rgba(52, 211, 153, 0.12);
      padding: 3px 8px;
      border-radius: 9999px;
      font-weight: 600;
      white-space: nowrap;
    }}

    .day-subtitle {{
      font-size: 15px;
      font-weight: 700;
      color: #e2e8f0;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .day-metrics {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: rgba(15, 23, 42, 0.5);
      padding: 8px 12px;
      border-radius: 10px;
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 16px;
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

    /* Highlights bullets */
    .highlights-box {{
      margin-bottom: 18px;
    }}

    .highlight-item {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 13px;
      color: #cbd5e1;
      margin-bottom: 6px;
      line-height: 1.45;
    }}

    .highlight-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--primary);
      margin-top: 6px;
      flex-shrink: 0;
    }}

    /* Plan Switcher (A / B 平替切换核心) */
    .plan-switch-wrap {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 14px;
      margin-bottom: 16px;
    }}

    .plan-toggle-bar {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      background: rgba(0, 0, 0, 0.35);
      padding: 4px;
      border-radius: 10px;
      margin-bottom: 14px;
    }}

    .plan-toggle-btn {{
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-size: 12px;
      font-weight: 700;
      padding: 8px 10px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    .plan-toggle-btn.active.plan-a-btn {{
      background: #f97316;
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(249, 115, 22, 0.4);
    }}

    .plan-toggle-btn.active.plan-b-btn {{
      background: #10b981;
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(16, 185, 129, 0.4);
    }}

    .plan-content {{
      display: none;
      animation: fadeIn 0.25s ease-out;
    }}

    .plan-content.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .spot-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
      margin-bottom: 8px;
    }}

    .spot-name {{
      font-size: 15px;
      font-weight: 700;
      color: #f8fafc;
      line-height: 1.35;
    }}

    .spot-desc {{
      font-size: 13px;
      color: #94a3b8;
      line-height: 1.5;
      margin-bottom: 12px;
    }}

    .parking-row {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.08);
      padding: 6px 10px;
      border-radius: 8px;
      margin-bottom: 12px;
    }}

    /* Action Nav Buttons (高德一键导航) */
    .nav-btn-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 14px;
    }}

    .amap-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      text-decoration: none;
      padding: 9px 12px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 600;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.3);
      transition: opacity 0.2s;
    }}

    .amap-btn:active {{
      opacity: 0.85;
      transform: scale(0.98);
    }}

    .amap-food-btn {{
      background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
      box-shadow: 0 2px 8px rgba(217, 119, 6, 0.3);
    }}

    /* Food Section */
    .food-card {{
      background: rgba(255, 255, 255, 0.03);
      border-left: 3px solid #f59e0b;
      padding: 10px 12px;
      border-radius: 4px 10px 10px 4px;
      font-size: 12px;
    }}

    .food-title {{
      font-weight: 700;
      color: #fbbf24;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .food-desc {{
      color: #cbd5e1;
      line-height: 1.45;
    }}

    /* Tips Box */
    .tips-card {{
      background: rgba(239, 68, 68, 0.08);
      border: 1px solid rgba(239, 68, 68, 0.2);
      border-radius: 12px;
      padding: 12px;
      font-size: 12px;
      color: #fca5a5;
    }}

    .tips-card strong {{
      color: #f87171;
    }}

    .tips-item {{
      margin-bottom: 4px;
      line-height: 1.4;
    }}

    .tips-item:last-child {{
      margin-bottom: 0;
    }}

    /* Toolbox Section */
    .toolbox {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 20px;
      margin-top: 30px;
    }}

    .toolbox h3 {{
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .toolbox-item {{
      background: rgba(15, 23, 42, 0.6);
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 10px;
      font-size: 12px;
    }}

    .toolbox-item .lbl {{
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 4px;
    }}

    .toolbox-item .cnt {{
      color: #94a3b8;
      line-height: 1.45;
    }}

    /* Floating Share Button */
    .share-bar {{
      position: fixed;
      bottom: 20px;
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
      padding: 14px 20px;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 8px 25px rgba(249, 115, 22, 0.4);
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

    /* Hide unused tab */
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
    <span id="toast-text">路书链接已复制，可直接微信发给女朋友！</span>
  </div>

  <div class="container">
    <!-- Header -->
    <header class="header">
      <div class="meta-tag">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        {data['meta']['base_location']}
      </div>
      <h1 class="title">{data['meta']['title']}</h1>
      <p class="subtitle">{data['meta']['subtitle']}</p>

      <div class="base-card">
        <div class="base-icon">🏡</div>
        <div class="base-info">
          <h4>每日归宿法则：0房费·回丹平睡大床</h4>
          <p>{data['meta']['strategy']}</p>
        </div>
      </div>
    </header>

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
"""

# Render Tabs Content
for tab in data["tabs"]:
    active_cls = "active" if tab["id"] == "mid_autumn" else ""
    html_template += f"""
    <!-- Tab Section: {tab['id']} -->
    <section id="section-{tab['id']}" class="tab-section {active_cls}">
      <div class="tab-intro">
        💡 <strong>本程策略：</strong>{tab['intro']}
      </div>
    """

    for day in tab["days"]:
        day_id = f"{tab['id']}-d{day['day_num']}"
        plan_a = day["plan_a"]
        plan_b = day["plan_b"]

        # Highlights items
        hl_html = "".join([f'<div class="highlight-item"><div class="highlight-dot"></div><div>{hl}</div></div>' for hl in day["highlights"]])
        tips_html = "".join([f'<div class="tips-item">• {t}</div>' for t in day["tips"]])

        html_template += f"""
      <article class="day-card" id="{day_id}">
        <div class="day-header">
          <div class="day-tag">
            <span class="day-title">{day['date']}</span>
          </div>
          <span class="crowd-pill">人流热度：{day['crowd_index']}</span>
        </div>

        <div class="day-subtitle">
          <span>📍</span>
          <span>{day['title']}</span>
        </div>

        <div class="day-metrics">
          <div class="metric-item">
            <svg viewBox="0 0 24 24"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.85 7h10.29l1.08 3.11H5.77L6.85 7zM19 17H5v-5h14v5z"/><circle cx="7.5" cy="14.5" r="1.5"/><circle cx="16.5" cy="14.5" r="1.5"/></svg>
            <span>{day['driving']}</span>
          </div>
          <div class="metric-item">
            <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <span>{day['vibe']}</span>
          </div>
        </div>

        <div class="highlights-box">
          {hl_html}
        </div>

        <!-- Plan Switcher (A / B 平替切换) -->
        <div class="plan-switch-wrap">
          <div class="plan-toggle-bar">
            <button class="plan-toggle-btn plan-a-btn active" id="btn-a-{day_id}" onclick="switchSubPlan('{day_id}', 'a')">
              <span>🌟 主选方案 A</span>
            </button>
            <button class="plan-toggle-btn plan-b-btn" id="btn-b-{day_id}" onclick="switchSubPlan('{day_id}', 'b')">
              <span>🔄 避堵平替 B</span>
            </button>
          </div>

          <!-- Plan A Content -->
          <div class="plan-content active" id="content-a-{day_id}">
            <div class="spot-header">
              <h4 class="spot-name">{plan_a['name']}</h4>
            </div>
            <p class="spot-desc">{plan_a['spot_desc']}</p>
            <div class="parking-row">
              <span>🅿️</span>
              <span><strong>停车攻略：</strong>{plan_a['parking']}</span>
            </div>

            <div class="nav-btn-grid">
              <a href="{plan_a['amap_url']}" target="_blank" class="amap-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71z"/></svg>
                高德一键导航景点
              </a>
              <a href="{plan_a['food']['amap_food']}" target="_blank" class="amap-btn amap-food-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M11 9H9V2H7v7H5V2H3v7c0 2.12 1.66 3.84 3.75 3.97V22h2.5v-9.03C11.34 12.84 13 11.12 13 9V2h-2v7zm5-3v8h2.5v8H21V2c-2.76 0-5 2.24-5 4z"/></svg>
                导航去吃必吃美食
              </a>
            </div>

            <div class="food-card">
              <div class="food-title">
                <span>🍽️</span>
                <span>{plan_a['food']['title']}</span>
              </div>
              <div class="food-desc">{plan_a['food']['recommend']}</div>
            </div>
          </div>

          <!-- Plan B Content -->
          <div class="plan-content" id="content-b-{day_id}">
            <div class="spot-header">
              <h4 class="spot-name">{plan_b['name']}</h4>
            </div>
            <p class="spot-desc">{plan_b['spot_desc']}</p>
            <div class="parking-row">
              <span>🅿️</span>
              <span><strong>停车攻略：</strong>{plan_b['parking']}</span>
            </div>

            <div class="nav-btn-grid">
              <a href="{plan_b['amap_url']}" target="_blank" class="amap-btn" style="background: linear-gradient(135deg, #059669 0%, #047857 100%);">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71z"/></svg>
                高德一键导航平替
              </a>
              <a href="{plan_b['food']['amap_food']}" target="_blank" class="amap-btn amap-food-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M11 9H9V2H7v7H5V2H3v7c0 2.12 1.66 3.84 3.75 3.97V22h2.5v-9.03C11.34 12.84 13 11.12 13 9V2h-2v7zm5-3v8h2.5v8H21V2c-2.76 0-5 2.24-5 4z"/></svg>
                导航去吃平替美食
              </a>
            </div>

            <div class="food-card" style="border-left-color: #10b981;">
              <div class="food-title" style="color: #34d399;">
                <span>🍲</span>
                <span>{plan_b['food']['title']}</span>
              </div>
              <div class="food-desc">{plan_b['food']['recommend']}</div>
            </div>
          </div>
        </div>

        <!-- Tips Card -->
        <div class="tips-card">
          {tips_html}
        </div>
      </article>
        """

    html_template += """
    </section>
    """

# Add practical toolbox
html_template += """
    <!-- Toolbox Section -->
    <section class="toolbox">
      <h3>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#f97316"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg>
        老司机自驾避坑工具箱
      </h3>
"""

for item in data["practical_toolbox"]["emergency_radar"]:
    html_template += f"""
      <div class="toolbox-item">
        <div class="lbl">⚡ {item['label']}</div>
        <div class="cnt">{item['content']}</div>
      </div>
    """

html_template += """
    </section>
  </div>

  <!-- Bottom Floating Share Bar -->
  <div class="share-bar">
    <button class="share-btn" onclick="copyShareLink()">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>
      <span>分享给女朋友 / 收藏路书</span>
    </button>
  </div>

  <script>
    // Tab switching (Mid-autumn vs National Day)
    function switchMainTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-section').forEach(sec => sec.classList.remove('active'));

      if (tabId === 'mid_autumn') {
        document.querySelectorAll('.tab-btn')[0].classList.add('active');
        document.getElementById('section-mid_autumn').classList.add('active');
      } else {
        document.querySelectorAll('.tab-btn')[1].classList.add('active');
        document.getElementById('section-national_day').classList.add('active');
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Sub-plan A/B switcher
    function switchSubPlan(dayId, planType) {
      const btnA = document.getElementById(`btn-a-${dayId}`);
      const btnB = document.getElementById(`btn-b-${dayId}`);
      const contentA = document.getElementById(`content-a-${dayId}`);
      const contentB = document.getElementById(`content-b-${dayId}`);

      if (planType === 'a') {
        btnA.classList.add('active');
        btnB.classList.remove('active');
        contentA.classList.add('active');
        contentB.classList.remove('active');
      } else {
        btnB.classList.add('active');
        btnA.classList.remove('active');
        contentB.classList.add('active');
        contentA.classList.remove('active');
      }
    }

    // Copy and share link
    function copyShareLink() {
      const currentUrl = window.location.href;
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(currentUrl).then(() => {
          showToast();
        }).catch(() => {
          fallbackCopy(currentUrl);
        });
      } else {
        fallbackCopy(currentUrl);
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
        alert("长按网址即可直接复制并分享给好友！");
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
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("index.html created successfully!")
