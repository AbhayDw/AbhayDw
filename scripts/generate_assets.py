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

def create_profile_header(output_path, num_frames=28):
    # Base dimensions (2x supersampling for high-DPI sharpness)
    w, h = 1840, 540
    target_w, target_h = 920, 270

    # Fonts
    font_mono_small = get_font("consola.ttf", 22)
    font_title = get_font("bahnschrift.ttf", 64)
    font_subtitle = get_font("segoeuib.ttf", 30)
    font_tag = get_font("segoeui.ttf", 20)
    font_meta = get_font("segoeui.ttf", 22)
    font_node_title = get_font("segoeuib.ttf", 20)
    font_node_sub = get_font("consola.ttf", 16)

    # Color Palette: Graphite / Ivory / Cobalt / Amber
    col_bg = (17, 20, 24)          # Deep Graphite
    col_grid = (26, 32, 40)        # Faint architectural grid
    col_border = (42, 52, 65)      # Muted slate border
    col_ivory_bright = (251, 249, 245) # Warm Ivory
    col_ivory_muted = (210, 204, 192)  # Muted Ivory
    col_ivory_dim = (145, 153, 163)    # Subtle gray/ivory
    col_cobalt = (43, 108, 176)    # Muted Cobalt Blue
    col_cobalt_glow = (79, 148, 224) # Cobalt bright pulse
    col_amber = (217, 119, 6)      # Restrained Amber
    col_amber_glow = (245, 158, 11) # Amber highlight
    col_card_bg = (23, 29, 37)     # Node / card background
    col_card_border = (45, 58, 74)

    # Architectural nodes layout in right panel
    nodes = [
        {"id": "gov", "x": 1150, "y": 140, "name": "GOV INITIATIVES", "sub": "MP State Platforms", "type": "gov"},
        {"id": "impl", "x": 1580, "y": 140, "name": "CLIENT OPERATIONS", "sub": "SCMS • Training • UAT", "type": "ops"},
        {"id": "hub", "x": 1365, "y": 270, "name": "INTEGRATION CORE", "sub": "Solutions & Workflows", "type": "core"},
        {"id": "ai", "x": 1150, "y": 400, "name": "AI & DATA SCIENCE", "sub": "ML • Predictive Models", "type": "ai"},
        {"id": "adoption", "x": 1580, "y": 400, "name": "INSTITUTIONAL IMPACT", "sub": "User Adoption • Scaling", "type": "impact"},
    ]

    # Circuit traces connecting nodes (with 90 or 45 degree bends)
    traces = [
        # gov -> hub
        [(1150, 140), (1240, 140), (1300, 220), (1365, 270)],
        # impl -> hub
        [(1580, 140), (1490, 140), (1430, 220), (1365, 270)],
        # hub -> ai
        [(1365, 270), (1300, 320), (1240, 400), (1150, 400)],
        # hub -> adoption
        [(1365, 270), (1430, 320), (1490, 400), (1580, 400)],
        # gov -> impl cross-link
        [(1150, 140), (1365, 100), (1580, 140)],
        # ai -> adoption cross-link
        [(1150, 400), (1365, 440), (1580, 400)],
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

        # Outer editorial frame & corner tick marks
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=col_border, width=2)
        # Corner brackets
        bracket_len = 24
        draw.line([(20, 20 + bracket_len), (20, 20), (20 + bracket_len, 20)], fill=col_amber, width=4)
        draw.line([(w - 20 - bracket_len, 20), (w - 20, 20), (w - 20, 20 + bracket_len)], fill=col_cobalt_glow, width=4)
        draw.line([(20, h - 20 - bracket_len), (20, h - 20), (20 + bracket_len, h - 20)], fill=col_cobalt_glow, width=4)
        draw.line([(w - 20 - bracket_len, h - 20), (w - 20, h - 20), (w - 20, h - 20 - bracket_len)], fill=col_amber, width=4)

        # Subtle vertical separator line between Left text and Right illustration
        sep_x = 980
        draw.line([(sep_x, 40), (sep_x, h - 40)], fill=(32, 40, 50), width=2)
        # Crosshairs along separator
        for sy in [120, 270, 420]:
            draw.line([(sep_x - 8, sy), (sep_x + 8, sy)], fill=col_border, width=2)

        # ----------------- LEFT PANEL: IDENTITY & EDITORIAL HIERARCHY -----------------
        # Monospace system tag
        tag_text = "// PROFESSIONAL PROFILE & SYSTEM ARCHITECTURE"
        draw.text((70, 58), tag_text, font=font_mono_small, fill=col_cobalt_glow)

        # Main Name: ABHAY DWIVEDI
        draw.text((70, 96), "ABHAY DWIVEDI", font=font_title, fill=col_ivory_bright)

        # Subtitle: Technology & Digital Solutions Professional
        draw.text((72, 178), "Technology & Digital Solutions Professional", font=font_subtitle, fill=(225, 215, 198))

        # Restrained Amber rule divider
        draw.line([(72, 230), (280, 230)], fill=col_amber, width=4)
        draw.line([(280, 230), (880, 230)], fill=(45, 56, 70), width=2)

        # Four domain pill blocks
        pillars = [
            "GOVERNMENT DIGITAL INITIATIVES",
            "SOFTWARE IMPLEMENTATION",
            "AI & DATA SCIENCE",
            "CLIENT COORDINATION"
        ]
        px = 72
        py = 258
        for i, pillar in enumerate(pillars):
            if i == 2:
                px = 72
                py = 316
            pill_w = 390
            pill_h = 42
            draw.rectangle([(px, py), (px + pill_w, py + pill_h)], fill=(22, 28, 36), outline=(42, 54, 70), width=2)
            # Small indicator dot
            dot_col = col_cobalt_glow if i % 2 == 0 else col_amber_glow
            draw.ellipse([(px + 14, py + 16), (px + 24, py + 26)], fill=dot_col)
            draw.text((px + 36, py + 9), pillar, font=font_tag, fill=(195, 206, 218))
            px += pill_w + 16

        # Location and Live Status Indicator
        status_y = 396
        # Bhopal, MP
        draw.text((72, status_y), "LOC:", font=font_mono_small, fill=col_amber)
        draw.text((125, status_y - 2), "Bhopal, Madhya Pradesh, India", font=font_meta, fill=col_ivory_muted)

        # Subtle animated pulse dot for status
        pulse_val = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
        pulse_r = int(6 + 3 * pulse_val)
        draw.ellipse([(72 - pulse_r + 8, status_y + 45 - pulse_r), (72 + pulse_r + 8, status_y + 45 + pulse_r)],
                     fill=(int(43 + 36 * pulse_val), int(108 + 40 * pulse_val), 176))
        draw.ellipse([(76, status_y + 41), (84, status_y + 49)], fill=col_amber_glow)

        status_text = "Core Competencies: Institutional Rollouts • Stakeholder Training • ML Pipelines"
        draw.text((102, status_y + 36), status_text, font=font_meta, fill=(156, 168, 184))

        # Bottom tech stamp
        draw.text((72, 480), "STATUS: ACTIVE // VERIFIED CREDENTIALS & PRODUCTION CASE STUDIES", font=font_mono_small, fill=(75, 90, 108))

        # ----------------- RIGHT PANEL: TECHNICAL ILLUSTRATION & DATA FLOW -----------------
        # Title of the diagram
        draw.text((1030, 58), "DIGITAL ECOSYSTEM & WORKFLOW ARCHITECTURE", font=font_mono_small, fill=col_cobalt_glow)
        draw.text((1700, 58), f"REV 2.4", font=font_mono_small, fill=col_amber)

        # Draw circuit traces
        for trace in traces:
            for p_i in range(len(trace) - 1):
                p1 = trace[p_i]
                p2 = trace[p_i + 1]
                draw.line([p1, p2], fill=(36, 46, 58), width=3)

        # Draw animated data pulses traveling along each trace
        for tr_idx, trace in enumerate(traces):
            # Compute approximate polyline length
            segments = []
            total_len = 0.0
            for p_i in range(len(trace) - 1):
                dx = trace[p_i + 1][0] - trace[p_i][0]
                dy = trace[p_i + 1][1] - trace[p_i][1]
                seg_len = math.hypot(dx, dy)
                segments.append((trace[p_i], trace[p_i + 1], seg_len))
                total_len += seg_len

            # Pulse position based on frame and trace offset
            pulse_offset = (t + tr_idx * 0.17) % 1.0
            dist = pulse_offset * total_len

            # Find coordinates of pulse
            cur_dist = 0.0
            px, py = trace[0]
            for p1, p2, seg_len in segments:
                if cur_dist + seg_len >= dist:
                    ratio = (dist - cur_dist) / max(seg_len, 0.001)
                    px = p1[0] + ratio * (p2[0] - p1[0])
                    py = p1[1] + ratio * (p2[1] - p1[1])
                    break
                cur_dist += seg_len

            # Draw glowing packet
            packet_col = col_amber_glow if tr_idx % 2 == 1 else col_cobalt_glow
            draw.ellipse([(px - 6, py - 6), (px + 6, py + 6)], fill=packet_col)
            draw.ellipse([(px - 2, py - 2), (px + 2, py + 2)], fill=col_ivory_bright)

        # Draw the nodes
        for node in nodes:
            nx, ny = node["x"], node["y"]
            is_hub = (node["type"] == "core")
            nw = 220 if not is_hub else 260
            nh = 86 if not is_hub else 94

            x0, y0 = nx - nw // 2, ny - nh // 2
            x1, y1 = nx + nw // 2, ny + nh // 2

            # Background card
            draw.rectangle([(x0, y0), (x1, y1)], fill=col_card_bg, outline=col_card_border, width=2)

            if is_hub:
                # Active core indicator
                pulse_r = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
                hub_border = (int(43 + 30 * pulse_r), int(108 + 40 * pulse_r), 176)
                draw.rectangle([(x0, y0), (x1, y1)], outline=hub_border, width=3)
                # Corner accents on core
                draw.line([(x0, y0 + 10), (x0, y0), (x0 + 10, y0)], fill=col_amber, width=3)
                draw.line([(x1 - 10, y0), (x1, y0), (x1, y0 + 10)], fill=col_amber, width=3)
                draw.line([(x0, y1 - 10), (x0, y1), (x0 + 10, y1)], fill=col_amber, width=3)
                draw.line([(x1 - 10, y1), (x1, y1), (x1 - 10, y1)], fill=col_amber, width=3)
                node_title_col = col_ivory_bright
            else:
                node_title_col = (230, 225, 215)

            # Node icon / indicator box
            icon_box_x = x0 + 14
            icon_box_y = y0 + 20
            icon_w = 44
            icon_h = 44
            draw.rectangle([(icon_box_x, icon_box_y), (icon_box_x + icon_w, icon_box_y + icon_h)],
                           fill=(15, 20, 26), outline=col_cobalt if not is_hub else col_amber, width=2)
            # Dot inside icon box
            draw.ellipse([(icon_box_x + 16, icon_box_y + 16), (icon_box_x + 28, icon_box_y + 28)],
                         fill=col_cobalt_glow if not is_hub else col_amber_glow)

            # Node labels
            text_x = icon_box_x + icon_w + 12
            draw.text((text_x, y0 + 18), node["name"], font=font_node_title, fill=node_title_col)
            draw.text((text_x, y0 + 46), node["sub"], font=font_node_sub, fill=(135, 148, 163))

        # Downsample with Lanczos filter for crisp retina clarity
        im_down = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        # Convert to adaptive 256 palette for crisp GIF rendering
        im_palette = im_down.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
        frames.append(im_palette)

    # Save animated GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=70,  # ~14 fps
        loop=0,
        optimize=True
    )
    print(f"Generated {output_path} with {len(frames)} frames. Size: {os.path.getsize(output_path)} bytes")

def create_data_flow(output_path, num_frames=24):
    # Base dimensions (2x supersampling)
    w, h = 1760, 220
    target_w, target_h = 880, 110

    font_mono = get_font("consola.ttf", 20)
    font_stage_num = get_font("consola.ttf", 24)
    font_stage_title = get_font("segoeuib.ttf", 24)
    font_stage_desc = get_font("segoeui.ttf", 18)

    col_bg = (17, 20, 24)
    col_border = (38, 48, 60)
    col_card = (22, 28, 35)
    col_cobalt = (43, 108, 176)
    col_cobalt_glow = (79, 148, 224)
    col_amber = (217, 119, 6)
    col_amber_glow = (245, 158, 11)
    col_ivory = (248, 245, 238)
    col_muted = (145, 155, 168)

    stages = [
        {"num": "01", "title": "GOVERNMENT INITIATIVES", "desc": "e-Setu • MP Higher Ed SCMS"},
        {"num": "02", "title": "IMPLEMENTATION & UAT", "desc": "Training • Stakeholders • Adoption"},
        {"num": "03", "title": "DATA SCIENCE & AI", "desc": "Predictive Models • Scikit • NLP"},
        {"num": "04", "title": "OPERATIONAL IMPACT", "desc": "Statewide Institutional Value"},
    ]

    frames = []

    for f_idx in range(num_frames):
        t = f_idx / num_frames
        im = Image.new("RGB", (w, h), color=col_bg)
        draw = ImageDraw.Draw(im)

        # Background grid
        for gx in range(0, w, 50):
            draw.line([(gx, 0), (gx, h)], fill=(23, 28, 35), width=1)

        # Outer boundary
        draw.rectangle([(10, 10), (w - 10, h - 10)], outline=col_border, width=2)
        # Corner marks
        draw.line([(10, 26), (10, 10), (26, 10)], fill=col_amber, width=3)
        draw.line([(w - 26, 10), (w - 10, 10), (w - 10, 26)], fill=col_cobalt_glow, width=3)
        draw.line([(10, h - 26), (10, h - 10), (26, h - 10)], fill=col_cobalt_glow, width=3)
        draw.line([(w - 26, h - 10), (w - 10, h - 10), (w - 10, h - 26)], fill=col_amber, width=3)

        # Main horizontal data rail across stages
        rail_y = 110
        draw.line([(60, rail_y), (w - 60, rail_y)], fill=(38, 48, 62), width=4)

        # Stages positions
        stage_w = 380
        spacing = 425
        start_x = 75

        # Animated signal pulse moving along rail
        pulse_pos_x = 60 + ((t * 1.2) % 1.0) * (w - 120)
        draw.line([(max(60, pulse_pos_x - 70), rail_y), (pulse_pos_x, rail_y)], fill=col_cobalt_glow, width=4)
        draw.ellipse([(pulse_pos_x - 8, rail_y - 8), (pulse_pos_x + 8, rail_y + 8)], fill=col_amber_glow)
        draw.ellipse([(pulse_pos_x - 3, rail_y - 3), (pulse_pos_x + 3, rail_y + 3)], fill=col_ivory)

        for i, stg in enumerate(stages):
            sx = start_x + i * spacing
            sy = 22
            sw = 360
            sh = 176

            # Is this stage currently activated by pulse?
            center_x = sx + sw // 2
            dist_to_pulse = abs(pulse_pos_x - center_x)
            is_active = dist_to_pulse < 140

            card_border = col_amber if is_active and i % 2 == 1 else (col_cobalt_glow if is_active else col_border)
            draw.rectangle([(sx, sy), (sx + sw, sy + sh)], fill=col_card, outline=card_border, width=2 if not is_active else 3)

            # Stage number badge
            num_fill = col_amber if is_active else (28, 36, 46)
            draw.rectangle([(sx + 14, sy + 14), (sx + 64, sy + 54)], fill=num_fill, outline=col_border, width=1)
            draw.text((sx + 24, sy + 20), stg["num"], font=font_stage_num, fill=col_ivory)

            # Stage title
            title_col = col_ivory if not is_active else col_ivory
            draw.text((sx + 76, sy + 22), stg["title"], font=font_stage_title, fill=title_col)

            # Divider line inside card
            draw.line([(sx + 14, sy + 68), (sx + sw - 14, sy + 68)], fill=(35, 45, 58), width=2)

            # Stage description
            draw.text((sx + 16, sy + 84), stg["desc"], font=font_stage_desc, fill=col_muted)

            # Stage status / arrow
            if i < len(stages) - 1:
                arrow_x = sx + sw + 16
                arrow_y = rail_y
                draw.polygon([(arrow_x, arrow_y - 8), (arrow_x + 14, arrow_y), (arrow_x, arrow_y + 8)],
                             fill=col_amber if is_active else col_cobalt)

        # Downsample and convert to palette GIF
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
    print(f"Generated {output_path} with {len(frames)} frames. Size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    header_path = r"C:\GitHub\AbhayDw\assets\profile-header.gif"
    dataflow_path = r"C:\GitHub\AbhayDw\assets\data-flow.gif"
    create_profile_header(header_path)
    create_data_flow(dataflow_path)
