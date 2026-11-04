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

def draw_glowing_orb(draw, cx, cy, r, base_col, highlight_col):
    """Draws a 3D luminous glass-like technology orb."""
    # Outer ambient glow
    for gr in range(r + 8, r, -2):
        alpha = (r + 8 - gr) / 8.0
        glow_c = (int(base_col[0] * alpha * 0.4), int(base_col[1] * alpha * 0.4), int(base_col[2] * alpha * 0.4))
        draw.ellipse([(cx - gr, cy - gr), (cx + gr, cy + gr)], outline=glow_c, width=1)
    
    # Base sphere fill
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=base_col)
    
    # Specular 3D highlight (top-left)
    hl_r = int(r * 0.45)
    hl_x = cx - int(r * 0.35)
    hl_y = cy - int(r * 0.35)
    draw.ellipse([(hl_x - hl_r, hl_y - hl_r), (hl_x + hl_r, hl_y + hl_r)], fill=highlight_col)
    draw.ellipse([(hl_x - int(hl_r * 0.4), hl_y - int(hl_r * 0.4)),
                  (hl_x + int(hl_r * 0.4), hl_y + int(hl_r * 0.4))], fill=(255, 255, 255))

def create_cinematic_motion_header(output_path, num_frames=32):
    # 2x supersampling: 1920 x 640 -> downsampled to 960 x 320 for retina sharpness
    w, h = 1920, 640
    target_w, target_h = 960, 320

    # Fonts
    font_kicker = get_font("consola.ttf", 21)
    font_name = get_font("bahnschrift.ttf", 76)
    font_title = get_font("segoeuib.ttf", 34)
    font_pill = get_font("segoeuib.ttf", 19)
    font_meta = get_font("segoeui.ttf", 22)
    font_tech = get_font("segoeuib.ttf", 19)
    font_sub_label = get_font("consola.ttf", 15)

    # Rich, Vibrant Cinematic Palette
    col_bg_top = (11, 15, 26)       # Midnight deep sapphire
    col_bg_mid = (16, 23, 40)       # Rich twilight indigo
    col_bg_bot = (9, 13, 22)        # Deep obsidian base
    col_border = (42, 58, 88)       # Luminous frame border

    # Vibrant Accent Colors
    col_cyan = (0, 240, 255)        # Electric Neon Cyan (#00F0FF)
    col_amber = (255, 138, 0)       # Sunset Saffron Gold (#FF8A00)
    col_magenta = (236, 72, 153)    # Hyper Violet Magenta (#EC4899)
    col_blue = (59, 130, 246)       # Royal Electric Blue (#3B82F6)
    col_emerald = (16, 185, 129)    # Emerald Jade (#10B981)
    col_purple = (168, 85, 247)     # Royal Amethyst (#A855F7)
    col_white = (255, 255, 255)
    col_ivory = (241, 245, 249)

    # Technology Orbs with authentic vibrant signatures
    nodes = [
        {"name": "Python", "base": (55, 118, 171), "accent": (255, 212, 59), "orbit_r": 230, "speed": 1.0, "offset": 0},
        {"name": "SQL", "base": (0, 168, 204), "accent": (255, 186, 8), "orbit_r": 160, "speed": 1.2, "offset": 45},
        {"name": "Scikit-Learn", "base": (247, 147, 30), "accent": (52, 153, 205), "orbit_r": 250, "speed": 0.8, "offset": 90},
        {"name": "Pandas", "base": (231, 4, 136), "accent": (147, 51, 234), "orbit_r": 175, "speed": 1.1, "offset": 135},
        {"name": "LangChain", "base": (16, 185, 129), "accent": (52, 211, 153), "orbit_r": 240, "speed": 0.9, "offset": 180},
        {"name": "PostgreSQL", "base": (67, 97, 238), "accent": (144, 224, 239), "orbit_r": 190, "speed": 1.3, "offset": 225},
        {"name": "Power BI", "base": (242, 200, 17), "accent": (232, 162, 0), "orbit_r": 225, "speed": 1.0, "offset": 270},
        {"name": "Git / CI", "base": (240, 80, 50), "accent": (255, 170, 140), "orbit_r": 150, "speed": 1.4, "offset": 315},
    ]

    orb_cx = 1440
    orb_cy = 320

    frames = []

    for frame_idx in range(num_frames):
        t = frame_idx / num_frames
        phase = t * 2 * math.pi

        im = Image.new("RGB", (w, h), color=col_bg_top)
        draw = ImageDraw.Draw(im)

        # 1. Radiant Ambient Gradient Canvas
        for y in range(h):
            prog = y / float(h)
            if prog < 0.5:
                r1, g1, b1 = col_bg_top
                r2, g2, b2 = col_bg_mid
                sub_p = prog * 2
            else:
                r1, g1, b1 = col_bg_mid
                r2, g2, b2 = col_bg_bot
                sub_p = (prog - 0.5) * 2
            
            r = int(r1 * (1 - sub_p) + r2 * sub_p)
            g = int(g1 * (1 - sub_p) + g2 * sub_p)
            b = int(b1 * (1 - sub_p) + b2 * sub_p)
            draw.line([(0, y), (w, y)], fill=(r, g, b))

        # Ambient radiant glow bloom around right nexus
        bloom_r = 380
        for br in range(bloom_r, 40, -40):
            b_alpha = (1 - br / bloom_r) * 0.18
            bloom_col = (int(25 + 60 * b_alpha), int(35 + 90 * b_alpha), int(75 + 180 * b_alpha))
            draw.ellipse([(orb_cx - br, orb_cy - br), (orb_cx + br, orb_cy + br)], outline=bloom_col, width=2)

        # 2. Precision Outer Frame & Glowing Cyan-Amber Corner Brackets
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=col_border, width=2)

        c_len = 36
        draw.line([(20, 20), (20 + c_len, 20)], fill=col_cyan, width=4)
        draw.line([(20, 20), (20, 20 + c_len)], fill=col_cyan, width=4)
        draw.line([(w - 20 - c_len, 20), (w - 20, 20)], fill=col_amber, width=4)
        draw.line([(w - 20, 20), (w - 20, 20 + c_len)], fill=col_amber, width=4)
        draw.line([(20, h - 20 - c_len), (20, h - 20)], fill=col_magenta, width=4)
        draw.line([(20, h - 20), (20 + c_len, h - 20)], fill=col_magenta, width=4)
        draw.line([(w - 20 - c_len, h - 20), (w - 20, h - 20)], fill=col_cyan, width=4)
        draw.line([(w - 20, h - 20 - c_len), (w - 20, h - 20)], fill=col_cyan, width=4)

        # Luminous Vertical Divider
        sep_x = 940
        draw.line([(sep_x, 40), (sep_x, h - 40)], fill=(32, 46, 70), width=2)
        # Laser pulse along divider
        div_pulse_y = 50 + ((t * 1.4) % 1.0) * (h - 100)
        draw.line([(sep_x, max(40, div_pulse_y - 45)), (sep_x, div_pulse_y)], fill=col_cyan, width=4)
        draw.ellipse([(sep_x - 5, div_pulse_y - 5), (sep_x + 5, div_pulse_y + 5)], fill=col_white)

        # ----------------- LEFT PANEL: VIBRANT TYPOGRAPHIC MASTHEAD -----------------
        # Dynamic Command Kicker Pill
        kx, ky = 76, 56
        draw.rounded_rectangle([(kx, ky), (kx + 470, ky + 38)], radius=8,
                               fill=(18, 28, 48), outline=(48, 72, 112), width=1)
        draw.ellipse([(kx + 14, ky + 14), (kx + 24, ky + 24)], fill=col_cyan)
        draw.text((kx + 36, ky + 8), "DIGITAL SOLUTIONS & TECHNOLOGY LEADERSHIP", font=font_kicker, fill=col_cyan)

        # Main Name with Neon-Lit Presence
        name_x, name_y = 76, 116
        draw.text((name_x, name_y), "Abhay Dwivedi", font=font_name, fill=col_white)

        # Glowing dynamic laser rule underneath
        ry = name_y + 96
        draw.line([(name_x, ry), (name_x + 280, ry)], fill=col_cyan, width=4)
        draw.line([(name_x + 280, ry), (name_x + 580, ry)], fill=col_amber, width=3)
        draw.line([(name_x + 580, ry), (880, ry)], fill=(40, 58, 88), width=2)
        draw.ellipse([(name_x + 277, ry - 3), (name_x + 283, ry + 3)], fill=col_white)

        # Title / Role
        draw.text((78, ry + 22), "Technology & Digital Solutions Professional", font=font_title, fill=col_ivory)

        # Category Pill Cards with rich glowing jewels
        pillars = [
            ("GOVERNMENT DIGITAL INITIATIVES", col_cyan),
            ("SOFTWARE IMPLEMENTATION", col_amber),
            ("APPLIED AI & DATA SCIENCE", col_magenta),
            ("CLIENT & STAKEHOLDER COORDINATION", col_emerald),
        ]
        px = 78
        py = ry + 82
        for i, (p_text, p_color) in enumerate(pillars):
            if i == 2:
                px = 78
                py += 52
            bbox = font_pill.getbbox(p_text)
            pw = bbox[2] - bbox[0] + 38
            ph = 42
            draw.rounded_rectangle([(px, py), (px + pw, py + ph)], radius=8,
                                   fill=(20, 30, 50), outline=(50, 72, 110), width=1)
            draw.ellipse([(px + 14, py + 16), (px + 24, py + 26)], fill=p_color)
            draw.text((px + 32, py + 10), p_text, font=font_pill, fill=col_white)
            px += pw + 16

        # Location & Availability Bar
        loc_y = py + 64
        draw.text((78, loc_y), "LOCATION", font=font_kicker, fill=col_amber)
        draw.text((170, loc_y - 2), "Bhopal, Madhya Pradesh, India", font=font_meta, fill=col_ivory)

        pulse_green = 0.5 + 0.5 * math.sin(phase * 2)
        beacon_r = int(5 + 3 * pulse_green)
        beacon_x, beacon_y = 530, loc_y + 11
        draw.ellipse([(beacon_x - beacon_r, beacon_y - beacon_r),
                      (beacon_x + beacon_r, beacon_y + beacon_r)], fill=(int(16 + 30 * pulse_green), int(185 + 40 * pulse_green), 129))
        draw.ellipse([(beacon_x - 3, beacon_y - 3), (beacon_x + 3, beacon_y + 3)], fill=col_white)
        draw.text((550, loc_y - 2), "Available for Institutional Deployments & Technical Leadership", font=font_meta, fill=(180, 205, 230))

        # ----------------- RIGHT PANEL: 3D HOLOGRAPHIC CONSTELLATION & KINETIC WAVES -----------------
        draw.text((1000, 56), "TECHNOLOGY RESONANCE & SYSTEM ECOSYSTEM", font=font_kicker, fill=col_cyan)
        draw.text((w - 220, 56), "CONTINUOUS HARMONY", font=font_kicker, fill=col_amber)

        # Concentric Luminous Orbital Rings with dual-tone depth
        for r_i, rad in enumerate([100, 170, 245]):
            ring_col = (45, 68, 105) if r_i % 2 == 0 else (35, 52, 82)
            draw.ellipse([(orb_cx - rad, orb_cy - rad), (orb_cx + rad, orb_cy + rad)], outline=ring_col, width=1)

        # Multi-Wave Kinetic Ribbon (Lissajous Fluid Spectrum)
        for wave_idx, (w_col, w_speed, w_amp) in enumerate([(col_cyan, 1.0, 38), (col_magenta, 1.3, 48), (col_amber, 0.8, 30)]):
            wave_pts = []
            for step in range(50):
                prog = step / 49.0
                wx = (orb_cx - 280) + prog * 560
                wy = orb_cy + w_amp * math.sin(prog * 2.5 * math.pi + phase * w_speed + wave_idx)
                wave_pts.append((wx, wy))
            for pt_i in range(len(wave_pts) - 1):
                draw.line([wave_pts[pt_i], wave_pts[pt_i + 1]], fill=w_col, width=2)
            
            # Luminous energy bead on wave
            bead_idx = int(((t * w_speed + wave_idx * 0.33) % 1.0) * len(wave_pts))
            bx, by = wave_pts[bead_idx]
            draw.ellipse([(bx - 5, by - 5), (bx + 5, by + 5)], fill=col_white)

        # Central Multi-Ring Radiant Core
        core_pulse = 0.5 + 0.5 * math.sin(phase)
        cr = int(28 + 6 * core_pulse)
        draw.ellipse([(orb_cx - cr - 10, orb_cy - cr - 10), (orb_cx + cr + 10, orb_cy + cr + 10)], outline=(60, 100, 160), width=2)
        draw.ellipse([(orb_cx - cr, orb_cy - cr), (orb_cx + cr, orb_cy + cr)], fill=(22, 36, 62), outline=col_cyan, width=3)
        draw.ellipse([(orb_cx - 10, orb_cy - 10), (orb_cx + 10, orb_cy + 10)], fill=col_amber)
        draw.ellipse([(orb_cx - 4, orb_cy - 4), (orb_cx + 4, orb_cy + 4)], fill=col_white)

        # Orbiting 3D Holographic Technology Nodes
        for node in nodes:
            curr_angle = math.radians(node["offset"]) + (phase * node["speed"])
            nx = orb_cx + node["orbit_r"] * math.cos(curr_angle)
            ny = orb_cy + node["orbit_r"] * 0.72 * math.sin(curr_angle)  # perspective tilt

            # Energy tether connecting node to core
            draw.line([(orb_cx, orb_cy), (nx, ny)], fill=(35, 55, 85), width=1)

            # Node card dimensions
            bbox = font_tech.getbbox(node["name"])
            nw = bbox[2] - bbox[0] + 56
            nh = 46
            x0, y0 = nx - nw // 2, ny - nh // 2
            x1, y1 = x0 + nw, y0 + nh

            # Draw card
            draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=10,
                                   fill=(18, 28, 46), outline=(60, 88, 136), width=2)

            # 3D Tech Jewel Orb
            jewel_cx = x0 + 20
            jewel_cy = y0 + nh // 2
            draw_glowing_orb(draw, jewel_cx, jewel_cy, r=10, base_col=node["base"], highlight_col=node["accent"])

            # Node name
            draw.text((x0 + 36, y0 + 11), node["name"], font=font_tech, fill=col_white)

        # Downsample with Lanczos for retina display clarity
        im_down = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im_palette = im_down.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
        frames.append(im_palette)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=65,  # ~15 fps
        loop=0,
        optimize=True
    )
    print(f"Generated {output_path}: {os.path.getsize(output_path)} bytes with {len(frames)} frames.")

if __name__ == "__main__":
    out = r"C:\GitHub\AbhayDw\assets\profile-header.gif"
    create_cinematic_motion_header(out)
