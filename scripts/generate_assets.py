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

def create_editorial_header(output_path, num_frames=30):
    # Base dimensions (2x supersampling for razor-sharp retina rendering)
    w, h = 1920, 440
    target_w, target_h = 960, 220

    # Typography
    font_mono_kicker = get_font("consola.ttf", 20)
    font_name = get_font("georgia.ttf", 66)
    if font_name == ImageFont.load_default():
        font_name = get_font("times.ttf", 66)
    font_role = get_font("segoeui.ttf", 28)
    font_sub_pill = get_font("segoeuib.ttf", 20)
    font_meta = get_font("segoeui.ttf", 20)
    font_mono_small = get_font("consola.ttf", 16)

    # Refined Editorial Palette (Light / Neutral GitHub-native aesthetic)
    col_bg = (248, 250, 252)          # Soft crisp off-white / neutral ivory
    col_border = (226, 232, 240)      # Hairline border
    col_text_primary = (15, 23, 42)   # Deep charcoal / near black
    col_text_secondary = (71, 85, 105)# Muted slate
    col_text_muted = (148, 163, 184)  # Soft secondary slate
    col_cobalt = (29, 78, 216)        # Restrained cobalt blue
    col_orange_accent = (194, 65, 12) # Warm rust / amber accent (#C2410C)
    col_line_light = (203, 213, 225)  # Very subtle drafting lines

    frames = []

    # Architectural drafting line points (Right side of banner)
    # A refined isometric coordinate drafting structure representing digital implementation
    grid_origin_x = 1520
    grid_origin_y = 220

    for frame_idx in range(num_frames):
        t = frame_idx / num_frames
        im = Image.new("RGB", (w, h), color=col_bg)
        draw = ImageDraw.Draw(im)

        # 1. Subtle Outer Border & Corner Registration Marks
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=col_border, width=2)
        
        # Editorial corner ticks (minimalist drafting style)
        tick_len = 16
        draw.line([(20, 20), (20 + tick_len, 20)], fill=col_text_secondary, width=2)
        draw.line([(20, 20), (20, 20 + tick_len)], fill=col_text_secondary, width=2)

        draw.line([(w - 20 - tick_len, 20), (w - 20, 20)], fill=col_text_secondary, width=2)
        draw.line([(w - 20, 20), (w - 20, 20 + tick_len)], fill=col_text_secondary, width=2)

        draw.line([(20, h - 20 - tick_len), (20, h - 20)], fill=col_text_secondary, width=2)
        draw.line([(20, h - 20), (20 + tick_len, h - 20)], fill=col_text_secondary, width=2)

        draw.line([(w - 20 - tick_len, h - 20), (w - 20, h - 20)], fill=col_text_secondary, width=2)
        draw.line([(w - 20, h - 20 - tick_len), (w - 20, h - 20)], fill=col_text_secondary, width=2)

        # 2. Left Column: Typographic Identity
        # Top kicker
        draw.text((80, 56), "PORTFOLIO & PROFESSIONAL PROFILE", font=font_mono_kicker, fill=col_cobalt)

        # Full Name: ABHAY DWIVEDI
        draw.text((80, 94), "Abhay Dwivedi", font=font_name, fill=col_text_primary)

        # Title / Role
        draw.text((82, 180), "Technology & Digital Solutions Professional", font=font_role, fill=col_text_secondary)

        # Understated single horizontal rule
        draw.line([(82, 232), (960, 232)], fill=col_border, width=2)
        draw.line([(82, 232), (180, 232)], fill=col_orange_accent, width=3)

        # Pillars (Editorial clean text layout, not colorful badges)
        pillars_text = "Government Digital Initiatives  |  Software Implementation  |  AI & Data  |  Client Coordination"
        draw.text((82, 256), pillars_text, font=font_sub_pill, fill=(30, 41, 59))

        # Location and subtle meta
        draw.text((82, 330), "LOCATION", font=font_mono_small, fill=col_orange_accent)
        draw.text((166, 328), "Bhopal, Madhya Pradesh, India", font=font_meta, fill=col_text_secondary)

        draw.text((540, 330), "FOCUS", font=font_mono_small, fill=col_cobalt)
        draw.text((600, 328), "Institutional Systems & Applied AI Delivery", font=font_meta, fill=col_text_secondary)

        # 3. Right Column: Understated Geometric Technical Illustration
        # Subtle vertical separator
        draw.line([(1140, 40), (1140, h - 40)], fill=(241, 245, 249), width=2)

        # Clean geometric isometric cube & vector coordinate mesh (understated drafting)
        # Isometric projection angles: 30 deg
        rad30 = math.radians(30)
        cos30 = math.cos(rad30)
        sin30 = math.sin(rad30)
        scale = 120

        # Axes
        ax_len = 160
        # X-axis (down-left)
        p_x_end = (grid_origin_x - ax_len * cos30, grid_origin_y + ax_len * sin30)
        # Y-axis (down-right)
        p_y_end = (grid_origin_x + ax_len * cos30, grid_origin_y + ax_len * sin30)
        # Z-axis (up)
        p_z_end = (grid_origin_x, grid_origin_y - ax_len)

        # Draw light coordinate lines
        draw.line([(grid_origin_x, grid_origin_y), p_x_end], fill=col_line_light, width=2)
        draw.line([(grid_origin_x, grid_origin_y), p_y_end], fill=col_line_light, width=2)
        draw.line([(grid_origin_x, grid_origin_y), p_z_end], fill=col_line_light, width=2)

        # Draw clean isometric geometric framework
        box_size = 90
        # Vertices of an isometric prism
        c_x, c_y = grid_origin_x, grid_origin_y - 20
        v_top = (c_x, c_y - box_size)
        v_top_left = (c_x - box_size * cos30, c_y - box_size * sin30 - box_size * 0.5)
        v_top_right = (c_x + box_size * cos30, c_y - box_size * sin30 - box_size * 0.5)
        v_center = (c_x, c_y)
        v_bot_left = (c_x - box_size * cos30, c_y + box_size * sin30)
        v_bot_right = (c_x + box_size * cos30, c_y + box_size * sin30)
        v_bot = (c_x, c_y + box_size)

        # Wireframe prism lines
        wire_lines = [
            (v_top_left, v_top),
            (v_top, v_top_right),
            (v_top_right, v_center),
            (v_center, v_top_left),
            (v_top_left, v_bot_left),
            (v_center, v_bot),
            (v_top_right, v_bot_right),
            (v_bot_left, v_bot),
            (v_bot, v_bot_right),
        ]
        for p1, p2 in wire_lines:
            draw.line([p1, p2], fill=(203, 213, 225), width=2)

        # Subtle secondary concentric framing rings / circles
        for r in [130, 150]:
            draw.ellipse(
                [(grid_origin_x - r, grid_origin_y - r), (grid_origin_x + r, grid_origin_y + r)],
                outline=(238, 242, 246),
                width=1
            )

        # Restrained animated detail: A single quiet stylus pulse traveling around the top face of the prism
        # Top face path: v_center -> v_top_right -> v_top -> v_top_left -> v_center
        face_path = [v_center, v_top_right, v_top, v_top_left, v_center]
        
        # Calculate position along path
        num_segments = len(face_path) - 1
        seg_idx = int((t * num_segments) % num_segments)
        seg_ratio = (t * num_segments) - seg_idx
        p_start = face_path[seg_idx]
        p_finish = face_path[seg_idx + 1]

        dot_x = p_start[0] + seg_ratio * (p_finish[0] - p_start[0])
        dot_y = p_start[1] + seg_ratio * (p_finish[1] - p_start[1])

        # Active segment highlight
        draw.line([p_start, (dot_x, dot_y)], fill=col_cobalt, width=3)

        # Understated warm-orange single nodal point
        draw.ellipse([(dot_x - 5, dot_y - 5), (dot_x + 5, dot_y + 5)], fill=col_orange_accent)
        draw.ellipse([(dot_x - 2, dot_y - 2), (dot_x + 2, dot_y + 2)], fill=(255, 255, 255))

        # Precision coordinate marks
        for v in [v_top, v_top_left, v_top_right, v_center, v_bot]:
            draw.ellipse([(v[0] - 3, v[1] - 3), (v[0] + 3, v[1] + 3)], fill=col_text_secondary)

        # Minimalist caption under drafting
        draw.text((grid_origin_x - 80, h - 50), "FIG 1.0 — SYSTEMS GEOMETRY", font=font_mono_small, fill=col_text_muted)

        # Downsample with Lanczos for retina display sharpness
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
    print(f"Generated {output_path}: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    create_editorial_header(r"C:\GitHub\AbhayDw\assets\profile-header.gif")
