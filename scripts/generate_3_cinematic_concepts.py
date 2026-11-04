import os
import math
from PIL import Image, ImageDraw, ImageFont

PREVIEWS_DIR = r"C:\GitHub\AbhayDw\previews"
os.makedirs(PREVIEWS_DIR, exist_ok=True)

# 2x Supersampling: 1920 x 640 -> downsampled to 960 x 320
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

# Load typography
font_hero = get_font("bahnschrift.ttf", 92)
font_hero_tracking = get_font("bahnschrift.ttf", 88)
font_title = get_font("segoeuib.ttf", 36)
font_subtitle = get_font("segoeui.ttf", 26)
font_pill_title = get_font("segoeuib.ttf", 22)
font_pill_sub = get_font("segoeui.ttf", 19)
font_mono = get_font("consola.ttf", 20)
font_mono_bold = get_font("consolab.ttf", 22)
font_meta = get_font("segoeui.ttf", 22)

# ==============================================================================
# CONCEPT 1: DEEP MIDNIGHT MINIMALIST
# Ultra-clean, architectural typography, precision linework, subtle cyan accent
# ==============================================================================
def render_concept_1(num_frames=28):
    bg_color = (15, 20, 28)         # Deep Midnight (#0F141C)
    card_bg = (21, 28, 38)          # Surface Slate (#151C26)
    col_text_main = (240, 246, 252) # Off-white (#F0F6FC)
    col_text_sub = (139, 148, 158)  # Secondary Muted Slate (#8B949E)
    col_hairline = (36, 46, 60)     # Hairline border (#242E3C)
    col_cyan = (0, 240, 255)        # Electric Cyan (#00F0FF)
    col_cyan_dim = (0, 140, 160)

    frames = []

    for f in range(num_frames):
        t = f / float(num_frames) # 0.0 -> 1.0
        phase = t * 2 * math.pi

        im = Image.new("RGB", (W, H), color=bg_color)
        draw = ImageDraw.Draw(im)

        # 1. Subtle hairline outer perimeter with corner notch registration
        pad = 32
        draw.rectangle([(pad, pad), (W - pad, H - pad)], outline=col_hairline, width=2)
        # Precision corner marks
        corner_len = 24
        draw.line([(pad, pad), (pad + corner_len, pad)], fill=col_cyan, width=3)
        draw.line([(pad, pad), (pad, pad + corner_len)], fill=col_cyan, width=3)
        draw.line([(W - pad, pad), (W - pad - corner_len, pad)], fill=col_cyan, width=3)
        draw.line([(W - pad, pad), (W - pad, pad + corner_len)], fill=col_cyan, width=3)
        draw.line([(pad, H - pad), (pad + corner_len, H - pad)], fill=col_cyan, width=3)
        draw.line([(pad, H - pad), (pad, H - pad - corner_len)], fill=col_cyan, width=3)
        draw.line([(W - pad, H - pad), (W - pad - corner_len, H - pad)], fill=col_cyan, width=3)
        draw.line([(W - pad, H - pad), (W - pad, H - pad - corner_len)], fill=col_cyan, width=3)

        # 2. Header Status & Location Bar (Top)
        # Location & Live Status Dot (smooth breathing alpha)
        pulse_r = int(7 + 3 * math.sin(phase))
        pulse_alpha = int(180 + 75 * math.sin(phase))
        draw.text((80, 68), "BHOPAL, MADHYA PRADESH, INDIA", font=font_mono_bold, fill=col_text_sub)
        
        # Live status pill on right
        status_box_x = W - 380
        draw.rounded_rectangle([(status_box_x, 62), (W - 80, 96)], radius=6, outline=col_hairline, fill=card_bg, width=1)
        # Pulsing cyan status dot
        draw.ellipse([(status_box_x + 18 - pulse_r//2, 79 - pulse_r//2), 
                      (status_box_x + 18 + pulse_r//2, 79 + pulse_r//2)], fill=(0, pulse_alpha, 255))
        draw.text((status_box_x + 36, 69), "SYSTEMS & SOLUTIONS ACTIVE", font=font_mono, fill=col_cyan)

        # 3. Main Hero Typography: ABHAY DWIVEDI
        # Render name with refined, confident architectural spacing
        name_x = 80
        name_y = 126
        name_text = "ABHAY DWIVEDI"
        
        # Subtle horizontal laser-hairline scan across the name (cinematic reflection)
        draw.text((name_x, name_y), name_text, font=font_hero, fill=col_text_main)

        # 4. Role Subtitle
        draw.text((84, 234), "Technology & Digital Solutions Professional", font=font_title, fill=(56, 189, 248))

        # 5. Precision Hairline Divider with traveling accent beam
        divider_y = 296
        draw.line([(80, divider_y), (W - 80, divider_y)], fill=col_hairline, width=2)
        
        # Traveling light beam along the divider
        beam_width = 320
        beam_pos = 80 + int((t * 1.2 % 1.0) * (W - 160 - beam_width))
        draw.line([(beam_pos, divider_y), (beam_pos + beam_width, divider_y)], fill=col_cyan, width=3)

        # 6. Four Core Identity Pillars (Neat, balanced, structured grid)
        pillars = [
            ("GOVERNMENT DIGITAL INITIATIVES", "e-Setu • State Transformation"),
            ("SOFTWARE IMPLEMENTATION", "SCMS • 67+ PMCOE Colleges • UAT"),
            ("AI & MACHINE LEARNING", "Predictive Models • Applied Solutions"),
            ("CLIENT & STAKEHOLDER COORDINATION", "Institutional Training • Operations")
        ]

        card_w = (W - 160 - 3 * 24) // 4
        card_h = 160
        card_y = 330

        for i, (p_title, p_sub) in enumerate(pillars):
            cx = 80 + i * (card_w + 24)
            # Subtle card container
            draw.rounded_rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], 
                                   radius=8, fill=card_bg, outline=col_hairline, width=1)
            
            # Subtle cyan top indicator line on card
            draw.line([(cx + 16, card_y), (cx + 56, card_y)], fill=col_cyan, width=2)

            # Card step index
            draw.text((cx + 18, card_y + 18), f"0{i+1} // DOMAIN", font=font_mono, fill=col_cyan_dim)
            # Card title
            draw.text((cx + 18, card_y + 48), p_title, font=font_pill_title, fill=col_text_main)
            # Card description
            draw.text((cx + 18, card_y + 98), p_sub, font=font_pill_sub, fill=col_text_sub)

        # 7. Bottom hairline metadata
        draw.text((80, H - 90), "MANDATE: INSTITUTIONAL EXCELLENCE THROUGH APPLIED TECHNOLOGY", font=font_mono, fill=col_text_sub)
        draw.text((W - 460, H - 90), "DEV & ARCHITECTURE IDENTITY // 2026", font=font_mono, fill=col_hairline)

        # Downsample to target dimensions
        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

        if f == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_1_opening.png"))
        elif f == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_1_middle.png"))
        elif f == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_1_ending.png"))

    # Save animated GIF
    frames_p = [fr.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for fr in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_1.gif"), save_all=True,
                     append_images=frames_p[1:], duration=70, loop=0)
    print("Concept 1 (Deep Midnight Minimalist) rendered successfully.")

# ==============================================================================
# CONCEPT 2: CINEMATIC HORIZON
# Atmospheric dark background, refined depth, subtle illuminated horizon line, copper/gold warmth
# ==============================================================================
def render_concept_2(num_frames=28):
    bg_deep = (10, 13, 20)           # Deep Obsidian (#0A0D14)
    bg_ambient = (20, 28, 46)        # Indigo Ambient
    col_text_main = (248, 250, 252)  # Pristine Off-white (#F8FAFC)
    col_text_sub = (148, 163, 184)   # Cool Slate (#94A3B8)
    col_copper = (245, 158, 11)      # Radiant Amber / Copper (#F59E0B)
    col_champagne = (253, 230, 138)  # Champagne Gold (#FDE68A)
    col_border = (40, 52, 75)        # Slate Border

    frames = []

    for f in range(num_frames):
        t = f / float(num_frames)
        phase = t * 2 * math.pi

        im = Image.new("RGB", (W, H), color=bg_deep)
        draw = ImageDraw.Draw(im)

        # 1. Atmospheric Ambient Horizon Glow (Vertical Gradient in the mid-field)
        horizon_y = 290
        for y in range(H):
            dist = abs(y - horizon_y)
            if dist < 220:
                glow = ((220 - dist) / 220.0) ** 2.0 * 0.4
                r = int(bg_deep[0] + (bg_ambient[0] - bg_deep[0] + 35 * glow) * glow)
                g = int(bg_deep[1] + (bg_ambient[1] - bg_deep[1] + 25 * glow) * glow)
                b = int(bg_deep[2] + (bg_ambient[2] - bg_deep[2] + 45 * glow) * glow)
                draw.line([(0, y), (W, y)], fill=(min(255, r), min(255, g), min(255, b)))

        # 2. Outer Cinema Frame
        pad = 28
        draw.rectangle([(pad, pad), (W - pad, H - pad)], outline=col_border, width=2)

        # 3. Top Kicker Bar
        draw.text((80, 64), "PORTFOLIO & PROFESSIONAL PROFILE", font=font_mono_bold, fill=col_copper)
        # Location with coordinate notation
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

        # 7. Core Pillars as Grounded Horizon Panels
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

        if f == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_2_opening.png"))
        elif f == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_2_middle.png"))
        elif f == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_2_ending.png"))

    frames_p = [fr.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for fr in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_2.gif"), save_all=True,
                     append_images=frames_p[1:], duration=70, loop=0)
    print("Concept 2 (Cinematic Horizon) rendered successfully.")

# ==============================================================================
# CONCEPT 3: PRECISION SYSTEMS GRID
# Technical elegance, subtle coordinate marks, structured data aesthetic, restrained cobalt/emerald accents
# ==============================================================================
def render_concept_3(num_frames=28):
    bg_color = (13, 17, 23)          # Dark Slate Charcoal (#0D1117)
    card_bg = (22, 27, 34)           # GitHub Dark Card (#161B22)
    col_grid = (26, 34, 46)          # Ultra-subtle grid
    col_text_main = (255, 255, 255)  # Pure White
    col_text_sub = (156, 163, 175)   # Slate Secondary (#9CA3AF)
    col_cobalt = (37, 99, 235)       # Precision Cobalt (#2563EB)
    col_cobalt_light = (59, 130, 246)
    col_emerald = (16, 185, 129)     # Implementation Emerald (#10B981)
    col_border = (48, 54, 61)        # Frame Border (#30363D)

    frames = []

    for f in range(num_frames):
        t = f / float(num_frames)
        phase = t * 2 * math.pi

        im = Image.new("RGB", (W, H), color=bg_color)
        draw = ImageDraw.Draw(im)

        # 1. Precision Technical Grid (60px spaced subtle grid)
        for gx in range(0, W, 80):
            draw.line([(gx, 0), (gx, H)], fill=col_grid, width=1)
        for gy in range(0, H, 80):
            draw.line([(0, gy), (W, gy)], fill=col_grid, width=1)

        # 2. Structural Frame & Coordinate Ticks
        pad = 28
        draw.rectangle([(pad, pad), (W - pad, H - pad)], outline=col_border, width=2)
        # Coordinate ticks along left and right
        for ty in range(pad, H - pad, 50):
            draw.line([(pad, ty), (pad + 8, ty)], fill=col_cobalt_light, width=2)
            draw.line([(W - pad - 8, ty), (W - pad, ty)], fill=col_cobalt_light, width=2)

        # 3. Top Technical Identification Bar
        draw.text((80, 60), "SYS // PROFILE IDENTITY SPECIFICATION", font=font_mono_bold, fill=col_cobalt_light)
        draw.text((W - 520, 60), "LOC: 23.2599° N, 77.4126° E // BHOPAL, MP", font=font_mono, fill=col_text_sub)

        # 4. Hero Name: ABHAY DWIVEDI
        name_x = 80
        name_y = 114
        draw.text((name_x, name_y), "ABHAY DWIVEDI", font=font_hero, fill=col_text_main)

        # 5. Role Subtitle with Technical Bracket Architecture
        draw.text((84, 222), "Technology & Digital Solutions Professional", font=font_title, fill=col_cobalt_light)

        # 6. Technical Precision Divider with Vertical Scan Pulse
        divider_y = 290
        draw.line([(80, divider_y), (W - 80, divider_y)], fill=col_border, width=2)

        # Vertical scanning signal sweeping left-to-right
        scan_x = 80 + int((t * 1.25 % 1.0) * (W - 160))
        draw.line([(scan_x, divider_y - 12), (scan_x, divider_y + 12)], fill=col_emerald, width=4)
        draw.ellipse([(scan_x - 6, divider_y - 6), (scan_x + 6, divider_y + 6)], fill=(255, 255, 255))

        # 7. Four Precision Data Modules
        pillars = [
            ("GOVERNMENT SYSTEMS", "e-Setu • Agriculture Infrastructure", col_emerald),
            ("SCMS IMPLEMENTATION", "67+ PMCOE Colleges • User Training", col_cobalt_light),
            ("APPLIED AI & DATA", "Model Lifecycle • Business Solutions", col_emerald),
            ("STAKEHOLDER OPS", "Client Coordination • Delivery", col_cobalt_light)
        ]

        card_w = (W - 160 - 3 * 24) // 4
        card_h = 160
        card_y = 330

        for i, (p_title, p_sub, p_accent) in enumerate(pillars):
            cx = 80 + i * (card_w + 24)
            # Module Box
            draw.rounded_rectangle([(cx, card_y), (cx + card_w, card_y + card_h)],
                                   radius=6, fill=card_bg, outline=col_border, width=1)
            
            # Module header tag
            draw.text((cx + 18, card_y + 18), f"[ MOD_0{i+1} ]", font=font_mono, fill=p_accent)
            # Active status light
            dot_color = (16, 185, 129) if i % 2 == 0 else (59, 130, 246)
            draw.ellipse([(cx + card_w - 28, card_y + 20), (cx + card_w - 18, card_y + 30)], fill=dot_color)

            draw.text((cx + 18, card_y + 52), p_title, font=font_pill_title, fill=col_text_main)
            draw.text((cx + 18, card_y + 102), p_sub, font=font_pill_sub, fill=col_text_sub)

        # 8. Bottom Status
        draw.text((80, H - 85), "STATUS: VERIFIED DEPLOYMENT ACROSS 67+ PMCOE INSTITUTIONS", font=font_mono, fill=col_emerald)
        draw.text((W - 320, H - 85), "SYSTEMS GRID // 2026", font=font_mono, fill=(80, 95, 115))

        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

        if f == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_1_opening.png") if False else os.path.join(PREVIEWS_DIR, "concept_3_opening.png"))
        elif f == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_3_middle.png"))
        elif f == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_3_ending.png"))

    frames_p = [fr.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for fr in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_3.gif"), save_all=True,
                     append_images=frames_p[1:], duration=70, loop=0)
    print("Concept 3 (Precision Systems Grid) rendered successfully.")

if __name__ == "__main__":
    render_concept_1()
    render_concept_2()
    render_concept_3()
    print("All 3 cinematic concepts successfully generated.")

