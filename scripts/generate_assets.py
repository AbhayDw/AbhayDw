import math
import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    font_path = os.path.join(r"C:\Windows\Fonts", name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def create_rich_artistic_header(output_path, num_frames=32):
    # Render at 2x supersampling for razor-sharp retina quality (1920x620 -> 960x310)
    w, h = 1920, 620
    target_w, target_h = 960, 310

    # Typography
    font_kicker = get_font("consola.ttf", 20)
    font_name = get_font("bahnschrift.ttf", 74)
    font_title = get_font("segoeuib.ttf", 34)
    font_sub = get_font("segoeui.ttf", 22)
    font_pill = get_font("segoeuib.ttf", 19)
    font_meta = get_font("segoeui.ttf", 21)
    font_tech_name = get_font("segoeuib.ttf", 18)

    # Rich, Prestigious Luxury Color Palette
    col_bg_top = (10, 14, 23)        # Deep obsidian night
    col_bg_bot = (7, 10, 18)         # Deepest black-slate
    col_border = (30, 42, 60)        # Refined indigo border
    
    col_gold = (245, 175, 45)        # Topaz Warm Gold
    col_gold_light = (254, 215, 120) # Champagne Highlight
    col_amber = (225, 115, 30)       # Molten Amber Copper
    col_ultramarine = (59, 130, 246) # Vivid Ultramarine Blue
    col_cyan_glow = (56, 189, 248)   # Electric Cyan
    col_emerald = (16, 185, 129)     # Jade Green
    col_white = (255, 255, 255)      # Crisp Pearl White
    col_ivory = (241, 245, 249)      # Soft Ivory
    col_slate = (148, 163, 184)      # Refined Slate

    tech_nodes = [
        {"name": "Python", "angle_deg": 0, "radius": 240, "color": (59, 130, 246), "accent": (245, 175, 45)},
        {"name": "Scikit-Learn", "angle_deg": 48, "radius": 175, "color": (225, 115, 30), "accent": (56, 189, 248)},
        {"name": "Pandas", "angle_deg": 96, "radius": 260, "color": (236, 72, 153), "accent": (147, 51, 234)},
        {"name": "SQL / DB", "angle_deg": 144, "radius": 190, "color": (0, 180, 216), "accent": (245, 175, 45)},
        {"name": "LangChain", "angle_deg": 192, "radius": 250, "color": (16, 185, 129), "accent": (52, 211, 153)},
        {"name": "PostgreSQL", "angle_deg": 240, "radius": 180, "color": (67, 97, 238), "accent": (96, 165, 250)},
        {"name": "Power BI", "angle_deg": 288, "radius": 235, "color": (245, 175, 45), "accent": (225, 115, 30)},
        {"name": "Git / CI", "angle_deg": 330, "radius": 160, "color": (239, 68, 68), "accent": (245, 175, 45)},
    ]

    orb_cx = 1450
    orb_cy = 310

    frames = []

    for frame_idx in range(num_frames):
        t = frame_idx / num_frames
        phase = t * 2 * math.pi

        im = Image.new("RGB", (w, h), color=col_bg_top)
        draw = ImageDraw.Draw(im)

        # 1. Subtle luxury vertical gradient background
        for y in range(0, h, 4):
            ratio = y / h
            r = int(col_bg_top[0] * (1 - ratio) + col_bg_bot[0] * ratio)
            g = int(col_bg_top[1] * (1 - ratio) + col_bg_bot[1] * ratio)
            b = int(col_bg_top[2] * (1 - ratio) + col_bg_bot[2] * ratio)
            draw.rectangle([(0, y), (w, y + 4)], fill=(r, g, b))

        # Ambient deep sapphire radial glow in the right quadrant
        glow_rad = 340
        for gr in range(glow_rad, 60, -35):
            g_alpha = (1 - gr / glow_rad) * 0.15
            gr_col = (int(10 + 35 * g_alpha), int(16 + 55 * g_alpha), int(30 + 110 * g_alpha))
            draw.ellipse([(orb_cx - gr, orb_cy - gr), (orb_cx + gr, orb_cy + gr)], outline=gr_col, width=2)

        # 2. Refined Architectural Frame & Precision Registration Corner Brackets
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=col_border, width=2)
        
        c_len = 32
        draw.line([(20, 20), (20 + c_len, 20)], fill=col_gold, width=4)
        draw.line([(20, 20), (20, 20 + c_len)], fill=col_gold, width=4)

        draw.line([(w - 20 - c_len, 20), (w - 20, 20)], fill=col_ultramarine, width=4)
        draw.line([(w - 20, 20), (w - 20, 20 + c_len)], fill=col_ultramarine, width=4)

        draw.line([(20, h - 20 - c_len), (20, h - 20)], fill=col_cyan_glow, width=4)
        draw.line([(20, h - 20), (20 + c_len, h - 20)], fill=col_cyan_glow, width=4)

        draw.line([(w - 20 - c_len, h - 20), (w - 20, h - 20)], fill=col_amber, width=4)
        draw.line([(w - 20, h - 20 - c_len), (w - 20, h - 20)], fill=col_amber, width=4)

        # Center separator
        sep_x = 960
        draw.line([(sep_x, 40), (sep_x, h - 40)], fill=(25, 35, 52), width=2)
        pulse_y = 60 + ((t * 1.3) % 1.0) * (h - 120)
        draw.line([(sep_x, max(40, pulse_y - 40)), (sep_x, pulse_y)], fill=col_gold, width=3)
        draw.ellipse([(sep_x - 4, pulse_y - 4), (sep_x + 4, pulse_y + 4)], fill=col_gold_light)

        # ----------------- LEFT PANEL: BESPOKE TYPOGRAPHIC IDENTITY -----------------
        kicker_x, kicker_y = 80, 60
        draw.rounded_rectangle([(kicker_x, kicker_y), (kicker_x + 460, kicker_y + 36)],
                               radius=6, fill=(16, 24, 38), outline=(38, 54, 78), width=1)
        draw.ellipse([(kicker_x + 14, kicker_y + 13), (kicker_x + 24, kicker_y + 23)], fill=col_gold)
        draw.text((kicker_x + 34, kicker_y + 8), "DIGITAL SOLUTIONS & TECHNOLOGY LEADERSHIP",
                  font=font_kicker, fill=col_gold_light)

        name_x, name_y = 80, 118
        draw.text((name_x, name_y), "Abhay Dwivedi", font=font_name, fill=col_white)

        line_y = name_y + 92
        draw.line([(name_x, line_y), (name_x + 220, line_y)], fill=col_gold, width=4)
        draw.line([(name_x + 220, line_y), (name_x + 580, line_y)], fill=col_ultramarine, width=2)
        draw.line([(name_x + 580, line_y), (880, line_y)], fill=(30, 42, 60), width=1)

        draw.text((82, line_y + 22), "Technology & Digital Solutions Professional", font=font_title, fill=col_ivory)

        pillars = [
            ("GOVERNMENT INITIATIVES", col_gold),
            ("SOFTWARE DELIVERY", col_ultramarine),
            ("APPLIED AI & DATA", col_cyan_glow),
            ("CLIENT COORDINATION", col_emerald),
        ]
        pill_x = 82
        pill_y = line_y + 78
        for p_label, p_col in pillars:
            bbox = font_pill.getbbox(p_label)
            pw = bbox[2] - bbox[0] + 34
            ph = 38
            draw.rounded_rectangle([(pill_x, pill_y), (pill_x + pw, pill_y + ph)],
                                   radius=8, fill=(18, 25, 38), outline=(40, 56, 80), width=1)
            draw.ellipse([(pill_x + 12, pill_y + 14), (pill_x + 20, pill_y + 22)], fill=p_col)
            draw.text((pill_x + 28, pill_y + 9), p_label, font=font_pill, fill=col_ivory)
            pill_x += pw + 14

        meta_y = pill_y + 60
        draw.text((82, meta_y), "LOC", font=font_kicker, fill=col_gold)
        draw.text((135, meta_y - 2), "Bhopal, Madhya Pradesh, India", font=font_meta, fill=col_ivory)

        draw.text((490, meta_y), "STATUS", font=font_kicker, fill=col_emerald)
        draw.text((570, meta_y - 2), "Available for Institutional Deployments & Advisory", font=font_meta, fill=col_slate)

        draw.text((82, meta_y + 46), "// Production Scope: 67+ PMCOE Colleges • Multi-tier UAT • Applied ML Pipelines",
                  font=font_kicker, fill=(100, 116, 139))

        # ----------------- RIGHT PANEL: HARMONIC KINETIC NEXUS & ORBITAL CONSTELLATION -----------------
        draw.text((1020, 58), "TECHNOLOGY RESONANCE & SYSTEM ECOSYSTEM", font=font_kicker, fill=col_cyan_glow)
        draw.text((w - 200, 58), "HARMONIC FLOW", font=font_kicker, fill=col_gold)

        orbital_radii = [100, 165, 235]
        for idx, rad in enumerate(orbital_radii):
            ring_col = (26, 38, 56) if idx % 2 == 0 else (34, 48, 70)
            draw.ellipse([(orb_cx - rad, orb_cy - rad), (orb_cx + rad, orb_cy + rad)],
                         outline=ring_col, width=1)

        sweep_angle = phase
        sweep_len = 260
        sweep_x = orb_cx + sweep_len * math.cos(sweep_angle)
        sweep_y = orb_cy + sweep_len * math.sin(sweep_angle)
        draw.line([(orb_cx, orb_cy), (sweep_x, sweep_y)], fill=(38, 80, 140), width=2)

        beam_dot_r = 180
        bx = orb_cx + beam_dot_r * math.cos(sweep_angle)
        by = orb_cy + beam_dot_r * math.sin(sweep_angle)
        draw.ellipse([(bx - 4, by - 4), (bx + 4, by + 4)], fill=col_gold_light)

        wave_pts = []
        for step in range(60):
            w_prog = step / 59.0
            wx = (orb_cx - 280) + w_prog * 560
            wy = orb_cy + 45 * math.sin(w_prog * 3 * math.pi + phase) + 25 * math.cos(w_prog * 2 * math.pi - phase)
            wave_pts.append((wx, wy))

        for pt_i in range(len(wave_pts) - 1):
            draw.line([wave_pts[pt_i], wave_pts[pt_i + 1]], fill=(32, 65, 115), width=2)

        pulse_idx = int((t * len(wave_pts)) % len(wave_pts))
        pw_x, pw_y = wave_pts[pulse_idx]
        draw.ellipse([(pw_x - 6, pw_y - 6), (pw_x + 6, pw_y + 6)], fill=col_gold)
        draw.ellipse([(pw_x - 2, pw_y - 2), (pw_x + 2, pw_y + 2)], fill=col_white)

        core_r = int(24 + 6 * math.sin(phase))
        draw.ellipse([(orb_cx - core_r - 8, orb_cy - core_r - 8), (orb_cx + core_r + 8, orb_cy + core_r + 8)],
                     outline=(40, 90, 160), width=2)
        draw.ellipse([(orb_cx - core_r, orb_cy - core_r), (orb_cx + core_r, orb_cy + core_r)],
                     fill=(20, 32, 52), outline=col_gold, width=3)
        draw.ellipse([(orb_cx - 8, orb_cy - 8), (orb_cx + 8, orb_cy + 8)], fill=col_gold_light)
        draw.ellipse([(orb_cx - 3, orb_cy - 3), (orb_cx + 3, orb_cy + 3)], fill=col_white)

        for node in tech_nodes:
            curr_angle = math.radians(node["angle_deg"]) + (phase * 0.5)
            nx = orb_cx + node["radius"] * math.cos(curr_angle)
            ny = orb_cy + node["radius"] * 0.75 * math.sin(curr_angle)

            draw.line([(orb_cx, orb_cy), (nx, ny)], fill=(22, 34, 50), width=1)

            bbox = font_tech_name.getbbox(node["name"])
            nw = bbox[2] - bbox[0] + 46
            nh = 42
            x0 = nx - nw // 2
            y0 = ny - nh // 2
            x1 = x0 + nw
            y1 = y0 + nh

            angle_diff = abs((curr_angle - sweep_angle + math.pi) % (2 * math.pi) - math.pi)
            is_illuminated = angle_diff < 0.45

            node_border = col_gold if is_illuminated else (45, 62, 88)
            node_fill = (22, 32, 48) if is_illuminated else (14, 20, 30)

            draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=10, fill=node_fill, outline=node_border,
                                   width=2 if is_illuminated else 1)

            jewel_x = x0 + 16
            jewel_y = y0 + nh // 2
            draw.ellipse([(jewel_x - 6, jewel_y - 6), (jewel_x + 6, jewel_y + 6)], fill=node["color"])
            draw.ellipse([(jewel_x - 2, jewel_y - 2), (jewel_x + 2, jewel_y + 2)], fill=node["accent"])

            label_col = col_white if is_illuminated else col_ivory
            draw.text((x0 + 30, y0 + 10), node["name"], font=font_tech_name, fill=label_col)

        im_down = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im_palette = im_down.convert("P", palette=Image.Palette.ADAPTIVE, colors=96)
        frames.append(im_palette)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=70,  # ~14 fps
        loop=0,
        optimize=True
    )
    print(f"Generated {output_path}: {os.path.getsize(output_path)} bytes with {len(frames)} frames.")

if __name__ == "__main__":
    out = r"C:\GitHub\AbhayDw\assets\profile-header.gif"
    create_rich_artistic_header(out)
