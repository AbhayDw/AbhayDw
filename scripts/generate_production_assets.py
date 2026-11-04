import os
import math
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"C:\GitHub\AbhayDw\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# 2x supersampling: 1920 x 640 -> 960 x 320
W, H = 1920, 640
TARGET_W, TARGET_H = 960, 320

def get_font(name, size):
    font_path = os.path.join(r"C:\Windows\Fonts", name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    return ImageFont.load_default()

font_hero = get_font("bahnschrift.ttf", 94)
font_title = get_font("segoeuib.ttf", 36)
font_pill_title = get_font("segoeuib.ttf", 22)
font_pill_sub = get_font("segoeui.ttf", 19)
font_mono = get_font("consola.ttf", 20)
font_mono_bold = get_font("consolab.ttf", 22)

def generate_cinematic_horizon_production():
    bg_deep = (10, 13, 20)           # Deep Obsidian (#0A0D14)
    bg_ambient = (20, 28, 46)        # Indigo Ambient (#141C2E)
    col_text_main = (248, 250, 252)  # Pristine Off-white (#F8FAFC)
    col_text_sub = (148, 163, 184)   # Cool Slate (#94A3B8)
    col_copper = (245, 158, 11)      # Radiant Amber / Copper (#F59E0B)
    col_champagne = (253, 230, 138)  # Champagne Gold (#FDE68A)
    col_border = (40, 52, 75)        # Slate Border

    num_frames = 32
    frames = []

    for f in range(num_frames):
        t = f / float(num_frames)
        phase = t * 2 * math.pi

        im = Image.new("RGB", (W, H), color=bg_deep)
        draw = ImageDraw.Draw(im)

        # 1. Atmospheric Ambient Horizon Glow (Vertical Gradient across the mid-field)
        horizon_y = 290
        for y in range(H):
            dist = abs(y - horizon_y)
            if dist < 230:
                glow = ((230 - dist) / 230.0) ** 2.2 * 0.42
                r = int(bg_deep[0] + (bg_ambient[0] - bg_deep[0] + 40 * glow) * glow)
                g = int(bg_deep[1] + (bg_ambient[1] - bg_deep[1] + 28 * glow) * glow)
                b = int(bg_deep[2] + (bg_ambient[2] - bg_deep[2] + 50 * glow) * glow)
                draw.line([(0, y), (W, y)], fill=(min(255, r), min(255, g), min(255, b)))

        # 2. Precision Cinema Perimeter Frame
        pad = 28
        draw.rectangle([(pad, pad), (W - pad, H - pad)], outline=col_border, width=2)
        # Corner gold accent ticks
        tick_len = 20
        draw.line([(pad, pad), (pad + tick_len, pad)], fill=col_copper, width=3)
        draw.line([(pad, pad), (pad, pad + tick_len)], fill=col_copper, width=3)
        draw.line([(W - pad, pad), (W - pad - tick_len, pad)], fill=col_copper, width=3)
        draw.line([(W - pad, pad), (W - pad, pad + tick_len)], fill=col_copper, width=3)
        draw.line([(pad, H - pad), (pad + tick_len, H - pad)], fill=col_copper, width=3)
        draw.line([(pad, H - pad), (pad, H - pad - tick_len)], fill=col_copper, width=3)
        draw.line([(W - pad, H - pad), (W - pad - tick_len, H - pad)], fill=col_copper, width=3)
        draw.line([(W - pad, H - pad), (W - pad, H - pad - tick_len)], fill=col_copper, width=3)

        # 3. Top Kicker Bar
        draw.text((80, 64), "PORTFOLIO & PROFESSIONAL PROFILE", font=font_mono_bold, fill=col_copper)
        draw.text((W - 560, 64), "BHOPAL, MP, INDIA  [23.2599° N, 77.4126° E]", font=font_mono, fill=col_text_sub)

        # 4. Hero Name: ABHAY DWIVEDI
        name_x = 80
        name_y = 118
        draw.text((name_x, name_y), "ABHAY DWIVEDI", font=font_hero, fill=col_text_main)

        # 5. Role Subtitle with Champagne Gold Accent
        draw.text((84, 226), "Technology & Digital Solutions Professional", font=font_title, fill=col_champagne)

        # 6. Horizon Luminous Line with Traveling Radiant Flare
        draw.line([(80, horizon_y), (W - 80, horizon_y)], fill=(50, 65, 90), width=2)

        # Lateral travelling golden horizon sweep
        sweep_x = 80 + int((t * 1.3 % 1.0) * (W - 160))
        # Horizontal flare rays
        draw.line([(max(80, sweep_x - 180), horizon_y), (min(W - 80, sweep_x + 180), horizon_y)], 
                  fill=col_copper, width=4)
        draw.line([(max(80, sweep_x - 70), horizon_y), (min(W - 80, sweep_x + 70), horizon_y)], 
                  fill=col_champagne, width=5)
        # Center flare spark
        draw.ellipse([(sweep_x - 8, horizon_y - 8), (sweep_x + 8, horizon_y + 8)], fill=(255, 255, 255))

        # 7. Four Core Institutional Panels
        pillars = [
            ("GOVERNMENT INITIATIVES", "e-Setu • Agriculture Platforms"),
            ("SOFTWARE IMPLEMENTATION", "SCMS • 67+ PMCOE Colleges • UAT"),
            ("AI & MACHINE LEARNING", "Predictive Analytics • Models"),
            ("STAKEHOLDER LEADERSHIP", "Client Coordination • Training")
        ]

        card_w = (W - 160 - 3 * 24) // 4
        card_h = 160
        card_y = 330

        for i, (p_title, p_sub) in enumerate(pillars):
            cx = 80 + i * (card_w + 24)
            # Horizon panel
            draw.rounded_rectangle([(cx, card_y), (cx + card_w, card_y + card_h)],
                                   radius=8, fill=(16, 22, 34), outline=col_border, width=1)
            # Amber badge accent
            draw.rounded_rectangle([(cx + 18, card_y + 16), (cx + 56, card_y + 36)], radius=4,
                                   fill=(35, 30, 25), outline=col_copper, width=1)
            draw.text((cx + 25, card_y + 18), f"0{i+1}", font=font_mono_bold, fill=col_copper)

            draw.text((cx + 18, card_y + 54), p_title, font=font_pill_title, fill=col_text_main)
            draw.text((cx + 18, card_y + 104), p_sub, font=font_pill_sub, fill=col_text_sub)

        # 8. Footer
        draw.text((80, H - 85), "SCALE: ENTERPRISE & PUBLIC SECTOR DIGITAL TRANSFORMATION", font=font_mono, fill=col_text_sub)
        draw.text((W - 360, H - 85), "CINEMATIC IDENTITY // 2026", font=font_mono, fill=(70, 85, 110))

        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

    # Save animated GIF
    frames_p = [fr.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for fr in frames]
    gif_path = os.path.join(ASSETS_DIR, "profile-header.gif")
    frames_p[0].save(gif_path, save_all=True, append_images=frames_p[1:], duration=65, loop=0)
    print(f"Saved {gif_path}")

    # Save static fallback PNG (using the middle resolved frame)
    png_path = os.path.join(ASSETS_DIR, "profile-header.png")
    frames[len(frames) // 2].save(png_path)
    print(f"Saved {png_path}")

def generate_cinematic_horizon_svg():
    svg_path = os.path.join(ASSETS_DIR, "profile-header.svg")
    svg_content = f'''<svg width="100%" height="320" viewBox="0 0 960 320" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background and Atmospheric Glow -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0A0D14" />
      <stop offset="45%" stop-color="#141C2E" />
      <stop offset="55%" stop-color="#141C2E" />
      <stop offset="100%" stop-color="#0A0D14" />
    </linearGradient>

    <!-- Traveling Horizon Amber Flare -->
    <linearGradient id="horizonFlare" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0" />
      <stop offset="40%" stop-color="#F59E0B" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#FDE68A" stop-opacity="1" />
      <stop offset="60%" stop-color="#F59E0B" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0" />
    </linearGradient>

    <style>
      .hero-title {{
        font-family: Bahnschrift, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 46px;
        font-weight: 700;
        fill: #F8FAFC;
        letter-spacing: 0.5px;
      }}
      .role-sub {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 18px;
        font-weight: 600;
        fill: #FDE68A;
      }}
      .kicker-text {{
        font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 11px;
        font-weight: 700;
        fill: #F59E0B;
        letter-spacing: 1px;
      }}
      .meta-text {{
        font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 10px;
        fill: #94A3B8;
      }}
      .panel-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 11px;
        font-weight: 700;
        fill: #F8FAFC;
      }}
      .panel-sub {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 9.5px;
        fill: #94A3B8;
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="960" height="320" rx="12" fill="url(#bgGrad)" />
  <rect x="14" y="14" width="932" height="292" rx="10" stroke="#28344B" stroke-width="1.5" />

  <!-- Corner Gold Ticks -->
  <path d="M14 24 V14 H24" stroke="#F59E0B" stroke-width="2" />
  <path d="M946 24 V14 H936" stroke="#F59E0B" stroke-width="2" />
  <path d="M14 296 V306 H24" stroke="#F59E0B" stroke-width="2" />
  <path d="M946 296 V306 H936" stroke="#F59E0B" stroke-width="2" />

  <!-- Top Metadata Bar -->
  <text x="40" y="38" class="kicker-text">PORTFOLIO &amp; PROFESSIONAL PROFILE</text>
  <text x="920" y="38" text-anchor="end" class="meta-text">BHOPAL, MP, INDIA [23.2599° N, 77.4126° E]</text>

  <!-- Hero Name -->
  <text x="40" y="86" class="hero-title">ABHAY DWIVEDI</text>
  <text x="42" y="115" class="role-sub">Technology &amp; Digital Solutions Professional</text>

  <!-- Horizon Line -->
  <line x1="40" y1="145" x2="920" y2="145" stroke="#32415A" stroke-width="1.5" />
  <line x1="180" y1="145" x2="480" y2="145" stroke="url(#horizonFlare)" stroke-width="3">
    <animate attributeName="x1" values="40;620;40" dur="8s" repeatCount="indefinite" />
    <animate attributeName="x2" values="340;920;340" dur="8s" repeatCount="indefinite" />
  </line>

  <!-- Four Institutional Panels -->
  <!-- Panel 1 -->
  <rect x="40" y="165" width="205" height="82" rx="6" fill="#101622" stroke="#28344B" stroke-width="1" />
  <rect x="50" y="174" width="22" height="12" rx="2" fill="#231E19" stroke="#F59E0B" stroke-width="0.8" />
  <text x="54" y="183" font-family="monospace" font-size="8" fill="#F59E0B" font-weight="700">01</text>
  <text x="50" y="202" class="panel-title">GOVERNMENT INITIATIVES</text>
  <text x="50" y="222" class="panel-sub">e-Setu • Agriculture Platforms</text>

  <!-- Panel 2 -->
  <rect x="265" y="165" width="205" height="82" rx="6" fill="#101622" stroke="#28344B" stroke-width="1" />
  <rect x="275" y="174" width="22" height="12" rx="2" fill="#231E19" stroke="#F59E0B" stroke-width="0.8" />
  <text x="279" y="183" font-family="monospace" font-size="8" fill="#F59E0B" font-weight="700">02</text>
  <text x="275" y="202" class="panel-title">SOFTWARE IMPLEMENTATION</text>
  <text x="275" y="222" class="panel-sub">SCMS • 67+ PMCOE Colleges • UAT</text>

  <!-- Panel 3 -->
  <rect x="490" y="165" width="205" height="82" rx="6" fill="#101622" stroke="#28344B" stroke-width="1" />
  <rect x="500" y="174" width="22" height="12" rx="2" fill="#231E19" stroke="#F59E0B" stroke-width="0.8" />
  <text x="504" y="183" font-family="monospace" font-size="8" fill="#F59E0B" font-weight="700">03</text>
  <text x="500" y="202" class="panel-title">AI &amp; MACHINE LEARNING</text>
  <text x="500" y="222" class="panel-sub">Predictive Analytics • Models</text>

  <!-- Panel 4 -->
  <rect x="715" y="165" width="205" height="82" rx="6" fill="#101622" stroke="#28344B" stroke-width="1" />
  <rect x="725" y="174" width="22" height="12" rx="2" fill="#231E19" stroke="#F59E0B" stroke-width="0.8" />
  <text x="729" y="183" font-family="monospace" font-size="8" fill="#F59E0B" font-weight="700">04</text>
  <text x="725" y="202" class="panel-title">STAKEHOLDER LEADERSHIP</text>
  <text x="725" y="222" class="panel-sub">Client Coordination • Training</text>

  <!-- Footer -->
  <text x="40" y="282" class="meta-text">SCALE: ENTERPRISE &amp; PUBLIC SECTOR DIGITAL TRANSFORMATION</text>
  <text x="920" y="282" text-anchor="end" class="meta-text">CINEMATIC IDENTITY // 2026</text>
</svg>'''
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Saved {svg_path}")

if __name__ == "__main__":
    generate_cinematic_horizon_production()
    generate_cinematic_horizon_svg()
    print("All production assets generated successfully.")

