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

def draw_tech_icon(draw, tech_id, cx, cy, r=16):
    """Draws authentic recognizable tech icons with official brand colors."""
    if tech_id == "python":
        draw.ellipse([(cx - r + 3, cy - r + 3), (cx + 1, cy + 1)], fill=(55, 118, 171))
        draw.ellipse([(cx - 1, cy - 1), (cx + r - 3, cy + r - 3)], fill=(255, 212, 59))
        draw.ellipse([(cx - 5, cy - 7), (cx - 1, cy - 3)], fill=(255, 255, 255))
        draw.ellipse([(cx + 1, cy + 3), (cx + 5, cy + 7)], fill=(55, 118, 171))
    elif tech_id == "sql":
        col_sql = (0, 117, 143)
        draw.ellipse([(cx - r + 4, cy - r + 4), (cx + r - 4, cy - r + 10)], fill=(242, 145, 17))
        draw.rectangle([(cx - r + 4, cy - r + 7), (cx + r - 4, cy + r - 6)], fill=col_sql)
        draw.ellipse([(cx - r + 4, cy + r - 10), (cx + r - 4, cy + r - 4)], fill=col_sql)
        draw.ellipse([(cx - r + 4, cy - 2), (cx + r - 4, cy + 4)], fill=(15, 80, 100))
    elif tech_id == "pandas":
        draw.rectangle([(cx - 9, cy - 9), (cx - 4, cy + 9)], fill=(231, 4, 136))
        draw.rectangle([(cx - 2, cy - 5), (cx + 3, cy + 9)], fill=(21, 4, 88))
        draw.rectangle([(cx + 5, cy - 9), (cx + 10, cy + 5)], fill=(255, 165, 0))
    elif tech_id == "numpy":
        draw.polygon([(cx, cy - 10), (cx + 9, cy - 5), (cx, cy), (cx - 9, cy - 5)], fill=(77, 171, 207))
        draw.polygon([(cx - 9, cy - 5), (cx, cy), (cx, cy + 10), (cx - 9, cy + 5)], fill=(1, 50, 67))
        draw.polygon([(cx, cy), (cx + 9, cy - 5), (cx + 9, cy + 5), (cx, cy + 10)], fill=(32, 100, 130))
    elif tech_id == "scikitlearn":
        draw.ellipse([(cx - 10, cy - 10), (cx + 2, cy + 2)], fill=(247, 147, 30))
        draw.ellipse([(cx - 2, cy - 2), (cx + 10, cy + 10)], fill=(52, 153, 205))
        draw.ellipse([(cx - 4, cy - 4), (cx + 4, cy + 4)], fill=(22, 27, 34))
    elif tech_id == "langchain":
        col_lc = (0, 166, 126)
        draw.ellipse([(cx - 9, cy - 6), (cx, cy + 6)], outline=col_lc, width=3)
        draw.ellipse([(cx, cy - 6), (cx + 9, cy + 6)], outline=(40, 200, 160), width=3)
    elif tech_id == "gemini":
        col_gem = (26, 115, 232)
        draw.polygon([(cx, cy - 12), (cx + 3, cy - 3), (cx + 12, cy), (cx + 3, cy + 3),
                      (cx, cy + 12), (cx - 3, cy + 3), (cx - 12, cy), (cx - 3, cy - 3)],
                     fill=col_gem)
        draw.ellipse([(cx - 3, cy - 3), (cx + 3, cy + 3)], fill=(255, 255, 255))
    elif tech_id == "postgresql":
        col_pg = (51, 103, 145)
        draw.ellipse([(cx - 10, cy - 8), (cx + 8, cy + 8)], fill=col_pg)
        draw.ellipse([(cx - 3, cy - 5), (cx + 10, cy + 5)], fill=(65, 130, 180))
        draw.ellipse([(cx + 4, cy - 2), (cx + 8, cy + 2)], fill=(255, 255, 255))
    elif tech_id == "mysql":
        draw.ellipse([(cx - 9, cy - 6), (cx + 7, cy + 6)], fill=(0, 97, 138))
        draw.polygon([(cx + 5, cy - 8), (cx + 10, cy), (cx + 5, cy + 4)], fill=(228, 142, 0))
    elif tech_id == "powerbi":
        draw.rectangle([(cx - 9, cy + 1), (cx - 5, cy + 9)], fill=(242, 200, 17))
        draw.rectangle([(cx - 3, cy - 4), (cx + 1, cy + 9)], fill=(232, 162, 0))
        draw.rectangle([(cx + 3, cy - 9), (cx + 7, cy + 9)], fill=(242, 175, 0))
    elif tech_id == "excel":
        draw.rectangle([(cx - 9, cy - 9), (cx + 9, cy + 9)], fill=(33, 115, 70))
        draw.text((cx - 4, cy - 8), "X", fill=(255, 255, 255), font=get_font("arialbd.ttf", 13))
    elif tech_id == "git":
        col_git = (240, 80, 50)
        draw.polygon([(cx, cy - 10), (cx + 10, cy), (cx, cy + 10), (cx - 10, cy)], fill=col_git)
        draw.line([(cx - 4, cy + 4), (cx + 4, cy - 4)], fill=(255, 255, 255), width=2)
        draw.ellipse([(cx - 6, cy + 2), (cx - 2, cy + 6)], fill=(255, 255, 255))
        draw.ellipse([(cx + 2, cy - 6), (cx + 6, cy - 2)], fill=(255, 255, 255))
    elif tech_id == "github":
        draw.ellipse([(cx - 9, cy - 9), (cx + 9, cy + 9)], fill=(240, 246, 252))
        draw.ellipse([(cx - 6, cy - 4), (cx + 6, cy + 7)], fill=(13, 17, 23))
    elif tech_id == "vscode":
        col_vs = (0, 122, 204)
        draw.polygon([(cx - 8, cy - 4), (cx - 2, cy - 9), (cx + 7, cy - 7), (cx + 2, cy),
                      (cx + 7, cy + 7), (cx - 2, cy + 9), (cx - 8, cy + 4)], fill=col_vs)
        draw.polygon([(cx - 4, cy - 2), (cx + 3, cy), (cx - 4, cy + 2)], fill=(255, 255, 255))
    elif tech_id == "jupyter":
        draw.ellipse([(cx - 9, cy - 6), (cx + 9, cy + 6)], outline=(243, 118, 38), width=3)
        draw.ellipse([(cx - 3, cy - 10), (cx + 3, cy - 4)], fill=(118, 118, 118))
        draw.ellipse([(cx - 3, cy + 4), (cx + 3, cy + 10)], fill=(243, 118, 38))
    else:
        draw.ellipse([(cx - 7, cy - 7), (cx + 7, cy + 7)], fill=(56, 189, 248))

def create_exceptional_header(output_path, num_frames=30):
    w, h = 1920, 600
    target_w, target_h = 960, 300

    font_mono_small = get_font("consola.ttf", 20)
    font_terminal_cmd = get_font("consola.ttf", 22)
    font_name = get_font("bahnschrift.ttf", 68)
    font_title = get_font("segoeuib.ttf", 32)
    font_subtitle = get_font("segoeui.ttf", 22)
    font_status = get_font("segoeui.ttf", 20)
    font_badge = get_font("segoeuib.ttf", 20)
    font_badge_sub = get_font("consola.ttf", 16)

    col_bg = (13, 17, 23)           # GitHub Deep Dark
    col_card_bg = (22, 27, 34)      # GitHub Dark Card
    col_border = (48, 54, 61)       # GitHub Hairline Border
    col_text_white = (240, 246, 252)# Crisp White
    col_text_muted = (139, 148, 158)# Muted Slate
    col_cyan = (56, 189, 248)       # Cyan Accent
    col_amber = (245, 158, 11)      # Amber Accent
    col_emerald = (16, 185, 129)    # Online / Green
    col_rail = (33, 42, 54)         # Rail lines

    track1_items = [
        {"id": "python", "name": "Python", "sub": "Core / AI"},
        {"id": "scikitlearn", "name": "Scikit-Learn", "sub": "ML / Eval"},
        {"id": "pandas", "name": "Pandas", "sub": "Dataframes"},
        {"id": "numpy", "name": "NumPy", "sub": "Vectors"},
        {"id": "langchain", "name": "LangChain", "sub": "Agentic AI"},
        {"id": "gemini", "name": "Gemini", "sub": "GenAI"},
        {"id": "sql", "name": "SQL", "sub": "Querying"}
    ]

    track2_items = [
        {"id": "postgresql", "name": "PostgreSQL", "sub": "Relational"},
        {"id": "mysql", "name": "MySQL", "sub": "Database"},
        {"id": "powerbi", "name": "Power BI", "sub": "Analytics"},
        {"id": "excel", "name": "Excel", "sub": "Modeling"},
        {"id": "git", "name": "Git", "sub": "VCS"},
        {"id": "github", "name": "GitHub", "sub": "Actions / CI"},
        {"id": "vscode", "name": "VS Code", "sub": "Editor"},
        {"id": "jupyter", "name": "Jupyter", "sub": "Notebooks"}
    ]

    card_w = 230
    card_h = 76
    spacing = 20
    unit_w_t1 = (card_w + spacing)
    total_w_t1 = unit_w_t1 * len(track1_items)

    unit_w_t2 = (card_w + spacing)
    total_w_t2 = unit_w_t2 * len(track2_items)

    frames = []

    for frame_idx in range(num_frames):
        t = frame_idx / num_frames
        im = Image.new("RGB", (w, h), color=col_bg)
        draw = ImageDraw.Draw(im)

        # 1. Subtle Engineering Grid
        grid_size = 50
        for gx in range(0, w, grid_size):
            draw.line([(gx, 0), (gx, h)], fill=(18, 24, 33), width=1)
        for gy in range(0, h, grid_size):
            draw.line([(0, gy), (w, gy)], fill=(18, 24, 33), width=1)

        # 2. Terminal Header Bar
        draw.rectangle([(16, 16), (w - 16, h - 16)], outline=col_border, width=2)
        draw.line([(16, 68), (w - 16, 68)], fill=col_border, width=2)

        draw.ellipse([(36, 36), (50, 50)], fill=(239, 68, 68))
        draw.ellipse([(60, 36), (74, 50)], fill=(245, 158, 11))
        draw.ellipse([(84, 36), (98, 50)], fill=(16, 185, 129))

        terminal_title = "abhaydw@workstation: ~/identity/ecosystem — bash"
        draw.text((120, 32), terminal_title, font=font_mono_small, fill=col_text_muted)

        pulse_val = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
        status_color = (int(16 + 10 * pulse_val), int(185 + 40 * pulse_val), 129)
        draw.ellipse([(w - 190, 39), (w - 176, 53)], fill=status_color)
        draw.text((w - 165, 33), "ACTIVE SYSTEM", font=font_mono_small, fill=col_emerald)

        split_x = 930
        draw.line([(split_x, 68), (split_x, h - 16)], fill=(30, 38, 50), width=2)

        draw.line([(16, 68), (16, 92)], fill=col_cyan, width=3)
        draw.line([(w - 16, 68), (w - 16, 92)], fill=col_amber, width=3)
        draw.line([(16, h - 16), (16, h - 40)], fill=col_cyan, width=3)
        draw.line([(w - 16, h - 16), (w - 16, h - 40)], fill=col_amber, width=3)

        # Left Identity Panel
        draw.text((60, 96), "> whoami --profile --detailed", font=font_terminal_cmd, fill=col_cyan)
        draw.text((60, 142), "Abhay Dwivedi", font=font_name, fill=col_text_white)

        # Blinking cursor block
        if (frame_idx % 15) < 9:
            name_bbox = font_name.getbbox("Abhay Dwivedi")
            name_width = name_bbox[2] - name_bbox[0]
            cursor_x = 60 + name_width + 12
            draw.rectangle([(cursor_x, 154), (cursor_x + 18, 206)], fill=col_cyan)

        draw.text((62, 230), "Technology & Digital Solutions Professional", font=font_title, fill=(226, 232, 240))

        draw.line([(62, 284), (880, 284)], fill=(36, 46, 60), width=2)
        draw.line([(62, 284), (200, 284)], fill=col_amber, width=3)
        draw.ellipse([(198, 281), (206, 287)], fill=col_amber)

        focus_text = "Government Digital Initiatives  |  Software Delivery  |  AI & Data  |  Client Coordination"
        draw.text((62, 310), focus_text, font=font_subtitle, fill=(180, 192, 208))

        loc_y = 376
        draw.text((62, loc_y), "LOCATION:", font=font_mono_small, fill=col_amber)
        draw.text((160, loc_y - 2), "Bhopal, Madhya Pradesh, India", font=font_status, fill=col_text_white)

        draw.text((62, loc_y + 44), "STATUS:", font=font_mono_small, fill=col_emerald)
        draw.text((160, loc_y + 42), "Available for Institutional Deployments & Technical Strategy", font=font_status, fill=col_text_muted)

        draw.text((62, loc_y + 98), "// Scope: 67+ PMCOE Colleges • Multi-tier UAT • Applied ML Pipelines", font=font_mono_small, fill=(100, 116, 139))

        # Right Technology Ecosystem Panel
        draw.text((960, 96), "// CONNECTED TECHNOLOGY ECOSYSTEM", font=font_mono_small, fill=col_cyan)
        draw.text((w - 220, 96), "CONTINUOUS FLOW", font=font_mono_small, fill=col_amber)

        rail1_y = 200
        rail2_y = 410

        draw.line([(940, rail1_y), (w - 18, rail1_y)], fill=col_rail, width=3)
        draw.line([(940, rail2_y), (w - 18, rail2_y)], fill=col_rail, width=3)

        for bus_x in [1120, 1380, 1640]:
            draw.line([(bus_x, rail1_y), (bus_x, rail2_y)], fill=(28, 36, 48), width=2)
            bus_pulse_y = rail1_y + ((t * 1.5 + bus_x * 0.001) % 1.0) * (rail2_y - rail1_y)
            draw.ellipse([(bus_x - 3, bus_pulse_y - 3), (bus_x + 3, bus_pulse_y + 3)], fill=col_cyan)

        # TRACK 1: Moves right
        shift_t1 = (t * unit_w_t1) % total_w_t1
        base_x_t1 = 940 + shift_t1 - total_w_t1

        for repeat in range(3):
            for i, item in enumerate(track1_items):
                cx = base_x_t1 + (repeat * total_w_t1) + (i * unit_w_t1)
                cy = rail1_y - card_h // 2
                if -card_w <= cx <= w:
                    draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)],
                                           radius=10, fill=col_card_bg, outline=col_border, width=2)
                    icon_cx = cx + 32
                    icon_cy = cy + card_h // 2
                    draw.rounded_rectangle([(cx + 10, cy + 10), (cx + 54, cy + card_h - 10)],
                                           radius=8, fill=(13, 17, 23), outline=(36, 46, 60), width=1)
                    draw_tech_icon(draw, item["id"], icon_cx, icon_cy, r=14)

                    draw.text((cx + 66, cy + 14), item["name"], font=font_badge, fill=col_text_white)
                    draw.text((cx + 66, cy + 42), item["sub"], font=font_badge_sub, fill=col_cyan)
                    draw.ellipse([(cx + card_w // 2 - 3, rail1_y - 3), (cx + card_w // 2 + 3, rail1_y + 3)], fill=col_cyan)

        # TRACK 2: Moves left
        shift_t2 = (t * unit_w_t2) % total_w_t2
        base_x_t2 = 940 - shift_t2

        for repeat in range(3):
            for i, item in enumerate(track2_items):
                cx = base_x_t2 + (repeat * total_w_t2) + (i * unit_w_t2)
                cy = rail2_y - card_h // 2
                if -card_w <= cx <= w:
                    draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)],
                                           radius=10, fill=col_card_bg, outline=col_border, width=2)
                    icon_cx = cx + 32
                    icon_cy = cy + card_h // 2
                    draw.rounded_rectangle([(cx + 10, cy + 10), (cx + 54, cy + card_h - 10)],
                                           radius=8, fill=(13, 17, 23), outline=(36, 46, 60), width=1)
                    draw_tech_icon(draw, item["id"], icon_cx, icon_cy, r=14)

                    draw.text((cx + 66, cy + 14), item["name"], font=font_badge, fill=col_text_white)
                    draw.text((cx + 66, cy + 42), item["sub"], font=font_badge_sub, fill=col_amber)
                    draw.ellipse([(cx + card_w // 2 - 3, rail2_y - 3), (cx + card_w // 2 + 3, rail2_y + 3)], fill=col_amber)

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
    create_exceptional_header(out)
