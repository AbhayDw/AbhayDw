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

def create_profile_header(output_path, num_frames=30):
    # Base dimensions (2x supersampling for high-DPI crispness)
    w, h = 1880, 540
    target_w, target_h = 940, 270

    # Fonts
    font_mono_meta = get_font("consola.ttf", 20)
    font_mono_small = get_font("consola.ttf", 18)
    font_title = get_font("bahnschrift.ttf", 62)
    font_subtitle = get_font("segoeuib.ttf", 30)
    font_pillar = get_font("segoeui.ttf", 21)
    font_meta = get_font("segoeui.ttf", 22)
    font_node_title = get_font("segoeuib.ttf", 20)
    font_node_sub = get_font("consola.ttf", 16)

    # Color Palette: Deep Slate Graphite / Warm Ivory / Cobalt / Amber
    col_bg = (15, 18, 22)           # Editorial Deep Slate
    col_grid = (24, 30, 38)         # Architectural Grid Lines
    col_border = (40, 50, 64)       # Hairline Slate Border
    col_ivory_bright = (252, 250, 246) # Warm Ivory
    col_ivory_sub = (220, 214, 202) # Subtitle Ivory
    col_ivory_muted = (150, 160, 174) # Muted Text
    col_cobalt = (43, 108, 176)     # Muted Cobalt
    col_cobalt_light = (74, 144, 226) # Bright Cobalt Signal
    col_amber = (217, 119, 6)       # Warm Editorial Amber Accent
    col_amber_glow = (245, 158, 11)  # Signal Amber
    col_node_bg = (21, 26, 34)
    col_node_border = (44, 56, 72)

    # Architectural nodes layout in right illustration panel
    nodes = [
        {"id": "gov", "x": 1180, "y": 140, "name": "STATE PLATFORMS", "sub": "e-Setu • SCMS • 67+ PMCOE"},
        {"id": "ops", "x": 1610, "y": 140, "name": "CLIENT COORDINATION", "sub": "UAT • Faculty Enablement"},
        {"id": "hub", "x": 1395, "y": 270, "name": "SOLUTIONS & TRAINING", "sub": "Technical Delivery Core"},
        {"id": "ai", "x": 1180, "y": 400, "name": "AI & DATA SYSTEMS", "sub": "ML Models • Analytics"},
        {"id": "impact", "x": 1610, "y": 400, "name": "INSTITUTIONAL ADOPTION", "sub": "Public Delivery & Scaling"},
    ]

    traces = [
        # gov -> hub
        [(1180, 140), (1270, 140), (1330, 220), (1395, 270)],
        # ops -> hub
        [(1610, 140), (1520, 140), (1460, 220), (1395, 270)],
        # hub -> ai
        [(1395, 270), (1330, 320), (1270, 400), (1180, 400)],
        # hub -> impact
        [(1395, 270), (1460, 320), (1520, 400), (1610, 400)],
        # Top highway
        [(1180, 140), (1395, 96), (1610, 140)],
        # Bottom highway
        [(1180, 400), (1395, 444), (1610, 400)],
    ]

    frames = []

    for frame_idx in range(num_frames):
        t = frame_idx / num_frames
        im = Image.new("RGB", (w, h), color=col_bg)
        draw = ImageDraw.Draw(im)

        # 1. Subtle Architectural Grid
        grid_step = 60
        for gx in range(0, w, grid_step):
            draw.line([(gx, 0), (gx, h)], fill=col_grid, width=1)
        for gy in range(0, h, grid_step):
            draw.line([(0, gy), (w, gy)], fill=col_grid, width=1)

        # Outer frame
        draw.rectangle([(18, 18), (w - 18, h - 18)], outline=col_border, width=2)
        # Precision corner registration ticks
        c_len = 28
        draw.line([(18, 18), (18 + c_len, 18)], fill=col_amber, width=4)
        draw.line([(18, 18), (18, 18 + c_len)], fill=col_amber, width=4)

        draw.line([(w - 18 - c_len, 18), (w - 18, 18)], fill=col_cobalt_light, width=4)
        draw.line([(w - 18, 18), (w - 18, 18 + c_len)], fill=col_cobalt_light, width=4)

        draw.line([(18, h - 18 - c_len), (18, h - 18)], fill=col_cobalt_light, width=4)
        draw.line([(18, h - 18), (18 + c_len, h - 18)], fill=col_cobalt_light, width=4)

        draw.line([(w - 18 - c_len, h - 18), (w - 18, h - 18)], fill=col_amber, width=4)
        draw.line([(w - 18, h - 18 - c_len), (w - 18, h - 18)], fill=col_amber, width=4)

        # Asymmetric editorial section divider between Identity and Illustration
        sep_x = 1000
        draw.line([(sep_x, 40), (sep_x, h - 40)], fill=(32, 40, 52), width=2)
        for tick_y in [140, 270, 400]:
            draw.line([(sep_x - 10, tick_y), (sep_x + 10, tick_y)], fill=col_border, width=2)
            draw.ellipse([(sep_x - 3, tick_y - 3), (sep_x + 3, tick_y + 3)], fill=col_amber)

        # ----------------- LEFT PANEL: EDITORIAL IDENTITY -----------------
        # Monospace category header
        draw.text((76, 56), "// PROFESSIONAL IDENTITY & SYSTEMS ARCHITECTURE", font=font_mono_meta, fill=col_cobalt_light)

        # Name
        draw.text((76, 92), "ABHAY DWIVEDI", font=font_title, fill=col_ivory_bright)

        # Positioning Subtitle
        draw.text((78, 174), "Technology & Digital Solutions Professional", font=font_subtitle, fill=col_ivory_sub)

        # Fine rule divider
        draw.line([(78, 226), (320, 226)], fill=col_amber, width=4)
        draw.line([(320, 226), (920, 226)], fill=(44, 55, 70), width=2)

        # Pillars bar
        pillars = [
            "GOVERNMENT TECHNOLOGY",
            "SOFTWARE IMPLEMENTATION",
            "AI & DATA SOLUTIONS",
            "CLIENT COORDINATION"
        ]
        px = 78
        py = 252
        for i, pil in enumerate(pillars):
            if i == 2:
                px = 78
                py = 310
            card_w = 400
            card_h = 44
            draw.rectangle([(px, py), (px + card_w, py + card_h)], fill=(20, 25, 33), outline=(42, 54, 70), width=2)
            # Dot indicator
            dot_c = col_amber_glow if i in (0, 3) else col_cobalt_light
            draw.ellipse([(px + 14, py + 18), (px + 24, py + 28)], fill=dot_c)
            draw.text((px + 36, py + 10), pil, font=font_pillar, fill=(205, 215, 228))
            px += card_w + 16

        # Location and availability indicator
        status_y = 392
        draw.text((78, status_y), "LOCATION:", font=font_mono_small, fill=col_amber)
        draw.text((170, status_y - 2), "Bhopal, Madhya Pradesh, India", font=font_meta, fill=col_ivory_sub)

        # Subtle live pulse indicator
        pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
        pulse_r = int(5 + 3 * pulse)
        draw.ellipse([(78 + 6 - pulse_r, status_y + 44 - pulse_r), (78 + 6 + pulse_r, status_y + 44 + pulse_r)],
                     fill=(int(43 + 30 * pulse), int(108 + 40 * pulse), 176))
        draw.ellipse([(78 + 3, status_y + 41), (78 + 9, status_y + 47)], fill=col_amber_glow)

        avail_text = "Verified Scope: Multi-tier Stakeholder Training • 67+ PMCOE • Applied AI"
        draw.text((106, status_y + 36), avail_text, font=font_meta, fill=col_ivory_muted)

        # Footer meta stamp
        draw.text((78, 480), "SYSTEM IDENTIFIER: AD-SYS-2026 // PRODUCTION DIGITAL INITIATIVES", font=font_mono_small, fill=(70, 85, 102))

        # ----------------- RIGHT PANEL: TECHNICAL SYSTEMS ILLUSTRATION -----------------
        draw.text((1050, 56), "DISTRIBUTED DELIVERY & GOVERNANCE ECOSYSTEM", font=font_mono_meta, fill=col_cobalt_light)
        draw.text((1750, 56), "V3.0", font=font_mono_meta, fill=col_amber)

        # Draw traces
        for trace in traces:
            for p_i in range(len(trace) - 1):
                draw.line([trace[p_i], trace[p_i + 1]], fill=(35, 45, 58), width=3)

        # Draw animated data signals along traces
        for tr_idx, trace in enumerate(traces):
            segments = []
            total_len = 0.0
            for p_i in range(len(trace) - 1):
                dx = trace[p_i + 1][0] - trace[p_i][0]
                dy = trace[p_i + 1][1] - trace[p_i][1]
                seg_len = math.hypot(dx, dy)
                segments.append((trace[p_i], trace[p_i + 1], seg_len))
                total_len += seg_len

            pulse_offset = (t + tr_idx * 0.16) % 1.0
            dist = pulse_offset * total_len

            cur_dist = 0.0
            px, py = trace[0]
            for p1, p2, seg_len in segments:
                if cur_dist + seg_len >= dist:
                    ratio = (dist - cur_dist) / max(seg_len, 0.001)
                    px = p1[0] + ratio * (p2[0] - p1[0])
                    py = p1[1] + ratio * (p2[1] - p1[1])
                    break
                cur_dist += seg_len

            pkt_col = col_amber_glow if tr_idx % 2 == 1 else col_cobalt_light
            draw.ellipse([(px - 6, py - 6), (px + 6, py + 6)], fill=pkt_col)
            draw.ellipse([(px - 2, py - 2), (px + 2, py + 2)], fill=col_ivory_bright)

        # Draw the nodes
        for node in nodes:
            nx, ny = node["x"], node["y"]
            is_hub = (node["id"] == "hub")
            nw = 226 if not is_hub else 268
            nh = 86 if not is_hub else 94

            x0, y0 = nx - nw // 2, ny - nh // 2
            x1, y1 = nx + nw // 2, ny + nh // 2

            draw.rectangle([(x0, y0), (x1, y1)], fill=col_node_bg, outline=col_node_border, width=2)

            if is_hub:
                hub_pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
                hub_border = (int(43 + 30 * hub_pulse), int(108 + 40 * hub_pulse), 176)
                draw.rectangle([(x0, y0), (x1, y1)], outline=hub_border, width=3)
                # Corner markers
                draw.line([(x0, y0 + 10), (x0, y0), (x0 + 10, y0)], fill=col_amber, width=3)
                draw.line([(x1 - 10, y0), (x1, y0), (x1, y0 + 10)], fill=col_amber, width=3)
                draw.line([(x0, y1 - 10), (x0, y1), (x0 + 10, y1)], fill=col_amber, width=3)
                draw.line([(x1 - 10, y1), (x1, y1), (x1 - 10, y1)], fill=col_amber, width=3)

            # Icon Box
            ibx, iby = x0 + 14, y0 + 20
            draw.rectangle([(ibx, iby), (ibx + 44, iby + 44)], fill=(14, 18, 24),
                           outline=col_cobalt if not is_hub else col_amber, width=2)
            draw.ellipse([(ibx + 16, iby + 16), (ibx + 28, iby + 28)],
                         fill=col_cobalt_light if not is_hub else col_amber_glow)

            tx = ibx + 56
            draw.text((tx, y0 + 18), node["name"], font=font_node_title, fill=col_ivory_bright)
            draw.text((tx, y0 + 46), node["sub"], font=font_node_sub, fill=(138, 150, 166))

        # Downsample with Lanczos for retina display sharpness
        im_down = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im_palette = im_down.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
        frames.append(im_palette)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=70,
        loop=0,
        optimize=True
    )
    print(f"Generated {output_path}: {os.path.getsize(output_path)} bytes")

def create_data_flow(output_path, num_frames=24):
    w, h = 1760, 220
    target_w, target_h = 880, 110

    font_stage_num = get_font("consola.ttf", 24)
    font_stage_title = get_font("segoeuib.ttf", 23)
    font_stage_desc = get_font("segoeui.ttf", 18)

    col_bg = (15, 18, 22)
    col_border = (36, 46, 58)
    col_card = (21, 26, 33)
    col_cobalt_glow = (74, 144, 226)
    col_cobalt = (43, 108, 176)
    col_amber = (217, 119, 6)
    col_amber_glow = (245, 158, 11)
    col_ivory = (250, 248, 244)
    col_muted = (145, 155, 168)

    stages = [
        {"num": "01", "title": "GOVERNMENT INITIATIVES", "desc": "e-Setu • MP Higher Ed SCMS"},
        {"num": "02", "title": "IMPLEMENTATION & UAT", "desc": "67+ PMCOE • Faculty Enablement"},
        {"num": "03", "title": "AI & DATA SYSTEMS", "desc": "Predictive Models • Scikit • RAG"},
        {"num": "04", "title": "INSTITUTIONAL ADOPTION", "desc": "Statewide Public Value & Impact"},
    ]

    frames = []

    for f_idx in range(num_frames):
        t = f_idx / num_frames
        im = Image.new("RGB", (w, h), color=col_bg)
        draw = ImageDraw.Draw(im)

        for gx in range(0, w, 50):
            draw.line([(gx, 0), (gx, h)], fill=(22, 27, 34), width=1)

        draw.rectangle([(10, 10), (w - 10, h - 10)], outline=col_border, width=2)
        draw.line([(10, 26), (10, 10), (26, 10)], fill=col_amber, width=3)
        draw.line([(w - 26, 10), (w - 10, 10), (w - 10, 26)], fill=col_cobalt_glow, width=3)
        draw.line([(10, h - 26), (10, h - 10), (26, h - 10)], fill=col_cobalt_glow, width=3)
        draw.line([(w - 26, h - 10), (w - 10, h - 10), (w - 10, h - 26)], fill=col_amber, width=3)

        rail_y = 110
        draw.line([(60, rail_y), (w - 60, rail_y)], fill=(36, 46, 60), width=4)

        start_x = 75
        spacing = 425

        pulse_pos_x = 60 + ((t * 1.2) % 1.0) * (w - 120)
        draw.line([(max(60, pulse_pos_x - 70), rail_y), (pulse_pos_x, rail_y)], fill=col_cobalt_glow, width=4)
        draw.ellipse([(pulse_pos_x - 8, rail_y - 8), (pulse_pos_x + 8, rail_y + 8)], fill=col_amber_glow)
        draw.ellipse([(pulse_pos_x - 3, rail_y - 3), (pulse_pos_x + 3, rail_y + 3)], fill=col_ivory)

        for i, stg in enumerate(stages):
            sx = start_x + i * spacing
            sy = 22
            sw = 360
            sh = 176

            center_x = sx + sw // 2
            is_active = abs(pulse_pos_x - center_x) < 140

            card_border = col_amber if is_active and i % 2 == 1 else (col_cobalt_glow if is_active else col_border)
            draw.rectangle([(sx, sy), (sx + sw, sy + sh)], fill=col_card, outline=card_border, width=2 if not is_active else 3)

            num_fill = col_amber if is_active else (26, 34, 44)
            draw.rectangle([(sx + 14, sy + 14), (sx + 64, sy + 54)], fill=num_fill, outline=col_border, width=1)
            draw.text((sx + 24, sy + 20), stg["num"], font=font_stage_num, fill=col_ivory)

            draw.text((sx + 74, sy + 22), stg["title"], font=font_stage_title, fill=col_ivory)
            draw.line([(sx + 14, sy + 68), (sx + sw - 14, sy + 68)], fill=(34, 44, 56), width=2)
            draw.text((sx + 16, sy + 84), stg["desc"], font=font_stage_desc, fill=col_muted)

            if i < len(stages) - 1:
                arrow_x = sx + sw + 16
                arrow_y = rail_y
                draw.polygon([(arrow_x, arrow_y - 8), (arrow_x + 14, arrow_y), (arrow_x, arrow_y + 8)],
                             fill=col_amber if is_active else col_cobalt)

        im_down = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im_palette = im_down.convert("P", palette=Image.Palette.ADAPTIVE, colors=96)
        frames.append(im_palette)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=70,
        loop=0,
        optimize=True
    )
    print(f"Generated {output_path}: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    create_profile_header(r"C:\GitHub\AbhayDw\assets\profile-header.gif")
    create_data_flow(r"C:\GitHub\AbhayDw\assets\data-flow.gif")
