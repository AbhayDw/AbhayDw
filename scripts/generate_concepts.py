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

PREVIEWS_DIR = r"C:\GitHub\AbhayDw\previews"
os.makedirs(PREVIEWS_DIR, exist_ok=True)

# Common dimensions (960 x 300, 2x supersampled to 1920 x 600)
W, H = 1920, 600
TARGET_W, TARGET_H = 960, 300

# -------------------------------------------------------------
# CONCEPT A: EDITORIAL CINEMA (Film Title Sequence)
# -------------------------------------------------------------
def render_concept_a(output_base, num_frames=24):
    font_kicker = get_font("consola.ttf", 22)
    font_name = get_font("georgia.ttf", 80)
    if font_name == ImageFont.load_default():
        font_name = get_font("times.ttf", 80)
    font_sub = get_font("segoeui.ttf", 26)
    font_meta = get_font("segoeui.ttf", 21)
    font_num = get_font("georgia.ttf", 28)

    col_bg = (250, 248, 245)         # Archival Museum Bone
    col_ink = (17, 24, 39)           # Deep Sumi-e Ink
    col_slate = (100, 116, 139)      # Archival Slate
    col_red = (185, 28, 28)          # Vermilion Red Seal Accent
    col_rule = (214, 211, 204)       # Hairline Paper Rule

    frames = []
    keyframe_indices = [0, num_frames // 2, num_frames - 1]

    for f_idx in range(num_frames):
        t = f_idx / (num_frames - 1) if num_frames > 1 else 0
        im = Image.new("RGB", (W, H), color=col_bg)
        draw = ImageDraw.Draw(im)

        # Subtle paper grain / framing
        draw.rectangle([(30, 30), (W - 30, H - 30)], outline=col_rule, width=2)
        # Editorial corner registration crosses
        for cx, cy in [(30, 30), (W - 30, 30), (30, H - 30), (W - 30, H - 30)]:
            draw.line([(cx - 14, cy), (cx + 14, cy)], fill=col_ink, width=2)
            draw.line([(cx, cy - 14), (cx, cy + 14)], fill=col_ink, width=2)

        # Animated cinematic letter tracking & reveal
        tracking_offset = int((1 - t) * 30)
        reveal_alpha = min(1.0, t * 1.5)

        # Film header kicker
        draw.text((90, 70), "PORTFOLIO &amp; MONOGRAPH // ACT I", font=font_kicker, fill=col_red)
        draw.text((W - 380, 70), "FILM TITLE REF. MMXXVI", font=font_kicker, fill=col_slate)

        # Title: ABHAY DWIVEDI
        name_str = "ABHAY DWIVEDI"
        # Render with deliberate letter spacing
        curr_x = 90
        for char in name_str:
            draw.text((curr_x, 140), char, font=font_name, fill=col_ink)
            c_bbox = font_name.getbbox(char)
            curr_x += (c_bbox[2] - c_bbox[0]) + 18 + tracking_offset

        # Fine dividing hairline with animated extension
        line_len = int(90 + (W - 180) * min(1.0, t * 1.2))
        draw.line([(90, 255), (line_len, 255)], fill=col_ink, width=3)
        draw.line([(line_len, 255), (W - 90, 255)], fill=col_rule, width=1)
        # Red seal mark on the rule
        draw.rectangle([(90, 252), (120, 258)], fill=col_red)

        # Role subtitle
        draw.text((90, 280), "Technology &amp; Digital Solutions Professional", font=font_sub, fill=col_ink)

        # Narrative Pillars
        pillars = "Government Digital Initiatives  &bull;  Software Implementation  &bull;  Client Coordination  &bull;  Applied AI"
        draw.text((90, 340), pillars, font=font_sub, fill=col_slate)

        # Editorial Meta footer
        draw.text((90, 440), "Location: Bhopal, Madhya Pradesh, India", font=font_meta, fill=col_slate)
        draw.text((90, 475), "Selected Engagements: MP Higher Education (SCMS / 67+ PMCOE) &bull; e-Setu Agriculture", font=font_meta, fill=col_ink)

        # Right-side vermilion seal / monograph emblem
        seal_x, seal_y = W - 320, 360
        draw.rectangle([(seal_x, seal_y), (seal_x + 230, seal_y + 110)], outline=col_red, width=3)
        draw.text((seal_x + 20, seal_y + 20), "VERIFIED MANDATE", font=font_kicker, fill=col_red)
        draw.text((seal_x + 20, seal_y + 55), "STATE TRANSFORMATION", font=font_meta, fill=col_ink)

        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

        if f_idx == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_a_opening.png"))
        elif f_idx == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_a_middle.png"))
        elif f_idx == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_a_ending.png"))

    # Save animated GIF
    frames_p = [f.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for f in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_a.gif"), save_all=True,
                     append_images=frames_p[1:], duration=80, loop=0)
    print("Generated Concept A assets.")

# -------------------------------------------------------------
# CONCEPT B: VISUAL STORYTELLING (The Blueprint & The Spectrum)
# -------------------------------------------------------------
def render_concept_b(output_base, num_frames=24):
    font_mono = get_font("consola.ttf", 22)
    font_name = get_font("bahnschrift.ttf", 74)
    font_sub = get_font("segoeuib.ttf", 32)
    font_desc = get_font("segoeui.ttf", 22)
    font_step = get_font("consola.ttf", 18)

    col_bg = (244, 245, 247)         # Blueprint Canvas Bone
    col_navy = (11, 25, 44)          # Deep Prussian Navy
    col_blue = (30, 86, 160)         # Architectural Drafting Blue
    col_terracotta = (194, 65, 12)   # Burnt Saffron / Terracotta
    col_emerald = (16, 120, 80)      # Human Delivery Emerald
    col_grid = (225, 228, 234)       # Drafting grid

    frames = []

    for f_idx in range(num_frames):
        t = f_idx / (num_frames - 1) if num_frames > 1 else 0
        phase = t * 2 * math.pi
        im = Image.new("RGB", (W, H), color=col_bg)
        draw = ImageDraw.Draw(im)

        # Drafting coordinate grid
        for gx in range(0, W, 60):
            draw.line([(gx, 0), (gx, H)], fill=col_grid, width=1)
        for gy in range(0, H, 60):
            draw.line([(0, gy), (W, gy)], fill=col_grid, width=1)

        # Left Section: The Blueprint (Governance & Architecture)
        draw.text((90, 60), "STAGE I // POLICY &amp; SYSTEM BLUEPRINT", font=font_mono, fill=col_blue)
        draw.text((90, 110), "Abhay Dwivedi", font=font_name, fill=col_navy)
        draw.text((92, 195), "Technology &amp; Digital Solutions Professional", font=font_sub, fill=col_blue)

        # The Storyline Rail: From Institutional Policy -> Implementation -> Human Impact
        rail_y = 300
        draw.line([(90, rail_y), (W - 90, rail_y)], fill=(180, 190, 205), width=3)

        stages = [
            ("01. STATE INITIATIVES", "e-Setu &bull; Agriculture Mandates", col_blue, 90),
            ("02. SCMS ROLLOUT", "67+ PMCOE &bull; UAT &bull; Validation", col_terracotta, 540),
            ("03. HUMAN ENABLEMENT", "Faculty &bull; Staff Training", col_emerald, 990),
            ("04. APPLIED AI &amp; TECH", "Data Science &bull; Scaled Delivery", col_navy, 1440)
        ]

        # Animated signal traversing the narrative line
        signal_x = 90 + ((t * 1.2) % 1.0) * (W - 180)
        draw.line([(max(90, signal_x - 120), rail_y), (signal_x, rail_y)], fill=col_terracotta, width=5)
        draw.ellipse([(signal_x - 8, rail_y - 8), (signal_x + 8, rail_y + 8)], fill=col_terracotta)
        draw.ellipse([(signal_x - 3, rail_y - 3), (signal_x + 3, rail_y + 3)], fill=(255, 255, 255))

        for s_title, s_desc, s_color, sx in stages:
            # Stage node
            is_active = abs(signal_x - (sx + 40)) < 160
            node_c = s_color if is_active else (150, 160, 175)
            draw.circle((sx + 30, rail_y), 12, fill=(255, 255, 255), outline=node_c, width=3)
            if is_active:
                draw.circle((sx + 30, rail_y), 6, fill=s_color)

            # Stage card below rail
            draw.rounded_rectangle([(sx, rail_y + 35), (sx + 370, rail_y + 130)],
                                   radius=8, fill=(255, 255, 255), outline=(210, 215, 225), width=1)
            draw.text((sx + 16, rail_y + 48), s_title, font=font_step, fill=s_color)
            draw.text((sx + 16, rail_y + 80), s_desc, font=font_desc, fill=col_navy)

        # Meta footer
        draw.text((90, 520), "LOC: Bhopal, Madhya Pradesh, India", font=font_mono, fill=col_blue)
        draw.text((650, 520), "ETHOS: Technology succeeds only when institutional adoption is complete.", font=font_desc, fill=col_navy)

        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

        if f_idx == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_b_opening.png"))
        elif f_idx == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_b_middle.png"))
        elif f_idx == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_b_ending.png"))

    frames_p = [f.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for f in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_b.gif"), save_all=True,
                     append_images=frames_p[1:], duration=80, loop=0)
    print("Generated Concept B assets.")

# -------------------------------------------------------------
# CONCEPT C: EXPERIMENTAL MOTION DESIGN (The Kinetic Monolith)
# -------------------------------------------------------------
def render_concept_c(output_base, num_frames=24):
    font_mono = get_font("consola.ttf", 20)
    font_mono_bold = get_font("consola.ttf", 24)
    font_massive = get_font("bahnschrift.ttf", 94)
    font_title = get_font("segoeuib.ttf", 36)
    font_pill = get_font("segoeuib.ttf", 20)

    col_bg = (255, 255, 255)         # Pure White Stark Minimalist
    col_black = (10, 10, 12)         # Pitch Charcoal Black
    col_slate = (110, 115, 125)
    col_cobalt = (29, 78, 216)       # Stark Cobalt (#1D4ED8)
    col_saffron = (245, 158, 11)     # Sharp Amber Flare

    frames = []

    for f_idx in range(num_frames):
        t = f_idx / (num_frames - 1) if num_frames > 1 else 0
        im = Image.new("RGB", (W, H), color=col_bg)
        draw = ImageDraw.Draw(im)

        # Monolithic border frame with precise measurement hash marks
        draw.rectangle([(25, 25), (W - 25, H - 25)], outline=(220, 224, 230), width=2)
        for my in range(25, H - 25, 40):
            draw.line([(25, my), (35, my)], fill=col_black, width=1)
            draw.line([(W - 35, my), (W - 25, my)], fill=col_black, width=1)

        # Left Column: Massive Kinetic Monolith Typography
        draw.text((80, 60), "[ PERSONAL BRAND // MMXXVI ]", font=font_mono, fill=col_cobalt)

        # Anamorphic projector beam sweep across name
        beam_prog = (t * 1.3) % 1.0
        beam_x = 80 + beam_prog * (W - 160)

        # Name
        draw.text((80, 110), "ABHAY DWIVEDI", font=font_massive, fill=col_black)
        draw.text((82, 225), "TECHNOLOGY &amp; DIGITAL SOLUTIONS PROFESSIONAL", font=font_title, fill=col_cobalt)

        # Monolithic bar with sliding mask
        draw.rectangle([(80, 280), (W - 80, 286)], fill=(235, 238, 242))
        bar_len = int((W - 160) * min(1.0, t * 1.5))
        draw.rectangle([(80, 280), (80 + bar_len, 286)], fill=col_black)
        draw.rectangle([(80, 280), (160, 286)], fill=col_saffron)

        # Asymmetrical Editorial Grid Cards
        pillars = [
            ("GOVERNMENT SYSTEMS", "MP Higher Ed (67+ PMCOE) &bull; e-Setu", col_black),
            ("SOFTWARE IMPLEMENTATION", "Multi-tier UAT &bull; Client Coordination", col_cobalt),
            ("APPLIED AI &amp; DATA", "Model Delivery &bull; Institutional Workflows", col_saffron),
        ]

        card_x = 80
        for p_title, p_desc, p_c in pillars:
            draw.rounded_rectangle([(card_x, 320), (card_x + 550, 430)], radius=6,
                                   fill=(250, 251, 252), outline=(225, 228, 235), width=1)
            draw.rectangle([(card_x + 18, 340), (card_x + 24, 410)], fill=p_c)
            draw.text((card_x + 36, 340), p_title, font=font_mono_bold, fill=col_black)
            draw.text((card_x + 36, 375), p_desc, font=font_mono, fill=col_slate)
            card_x += 580

        # Footer coordinates
        draw.text((80, 485), "GEO: 23&deg;15'N 77&deg;25'E // BHOPAL, MADHYA PRADESH, INDIA", font=font_mono, fill=col_black)
        draw.text((W - 540, 485), "STATUS: DEPLOYMENT ACTIVE &bull; STRATEGY READY", font=font_mono, fill=col_cobalt)

        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

        if f_idx == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_c_opening.png"))
        elif f_idx == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_c_middle.png"))
        elif f_idx == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_c_ending.png"))

    frames_p = [f.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for f in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_c.gif"), save_all=True,
                     append_images=frames_p[1:], duration=80, loop=0)
    print("Generated Concept C assets.")

# -------------------------------------------------------------
# CONCEPT D: CINEMATIC DIGITAL WORLD (Horizon Luminescence)
# -------------------------------------------------------------
def render_concept_d(output_base, num_frames=24):
    font_kicker = get_font("consola.ttf", 22)
    font_name = get_font("bahnschrift.ttf", 78)
    font_title = get_font("segoeuib.ttf", 34)
    font_sub = get_font("segoeui.ttf", 23)
    font_meta = get_font("segoeui.ttf", 20)

    # Clean Titanium / Twilight Alabaster Palette (Sophisticated, NOT pitch dark)
    col_bg_top = (238, 242, 246)      # Frosted Alabaster Titanium
    col_bg_bot = (226, 232, 240)      # Slate mist
    col_ink = (15, 23, 42)            # Charcoal Ink
    col_indigo = (79, 70, 229)        # Royal Iris / Indigo (#4F46E5)
    col_amber = (217, 119, 6)         # Topaz Amber Horizon
    col_emerald = (16, 185, 129)

    frames = []

    for f_idx in range(num_frames):
        t = f_idx / (num_frames - 1) if num_frames > 1 else 0
        phase = t * 2 * math.pi
        im = Image.new("RGB", (W, H), color=col_bg_top)
        draw = ImageDraw.Draw(im)

        # Smooth titanium gradient
        for y in range(H):
            prog = y / float(H)
            r = int(col_bg_top[0] * (1 - prog) + col_bg_bot[0] * prog)
            g = int(col_bg_top[1] * (1 - prog) + col_bg_bot[1] * prog)
            b = int(col_bg_top[2] * (1 - prog) + col_bg_bot[2] * prog)
            draw.line([(0, y), (W, y)], fill=(r, g, b))

        # Horizon Luminescence Line
        horizon_y = 280
        draw.line([(0, horizon_y), (W, horizon_y)], fill=(203, 213, 225), width=2)

        # Traveling golden sunrise horizon flare
        flare_x = int(W * 0.15 + ((t * 1.1) % 1.0) * (W * 0.7))
        for fr in range(120, 10, -15):
            alpha = (120 - fr) / 120.0
            flare_col = (int(217 * alpha + 230 * (1 - alpha)), int(119 * alpha + 235 * (1 - alpha)), int(6 * alpha + 240 * (1 - alpha)))
            draw.ellipse([(flare_x - fr * 2, horizon_y - fr // 2), (flare_x + fr * 2, horizon_y + fr // 2)], outline=flare_col, width=1)

        # Frame border
        draw.rectangle([(25, 25), (W - 25, H - 25)], outline=(203, 213, 225), width=2)

        # Typography
        draw.text((90, 65), "// PERSONAL BRAND &amp; DIGITAL LEADERSHIP", font=font_kicker, fill=col_indigo)
        draw.text((90, 115), "Abhay Dwivedi", font=font_name, fill=col_ink)
        draw.text((92, 205), "Technology &amp; Digital Solutions Professional", font=font_title, fill=col_indigo)

        # Below horizon: Connected Ecosystem Pillars
        draw.text((92, 330), "STRATEGIC DOMAINS &bull; INSTITUTIONAL IMPACT", font=font_kicker, fill=col_amber)

        pillars = [
            ("GOVERNMENT TRANSFORMATION", "e-Setu &bull; MP Higher Ed SCMS (67+ PMCOE)"),
            ("SOFTWARE DELIVERY &amp; UAT", "Multi-Tier Stakeholder Training &bull; Adoption"),
            ("APPLIED AI &amp; DATA SYSTEMS", "Data Science &bull; Scaled Engineering Solutions"),
        ]

        bx = 90
        for p_h, p_d in pillars:
            draw.rounded_rectangle([(bx, 370), (bx + 540, 480)], radius=10,
                                   fill=(255, 255, 255), outline=(215, 222, 232), width=1)
            draw.ellipse([(bx + 20, 395), (bx + 30, 405)], fill=col_indigo)
            draw.text((bx + 40, 390), p_h, font=font_sub, fill=col_ink)
            draw.text((bx + 40, 430), p_d, font=font_meta, fill=(100, 116, 139))
            bx += 570

        # Footer
        draw.text((90, 525), "📍 Bhopal, Madhya Pradesh, India &bull; Available for Strategic Deployments", font=font_meta, fill=col_ink)

        im_down = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        frames.append(im_down)

        if f_idx == 0:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_d_opening.png"))
        elif f_idx == num_frames // 2:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_d_middle.png"))
        elif f_idx == num_frames - 1:
            im_down.save(os.path.join(PREVIEWS_DIR, "concept_d_ending.png"))

    frames_p = [f.convert("P", palette=Image.Palette.ADAPTIVE, colors=64) for f in frames]
    frames_p[0].save(os.path.join(PREVIEWS_DIR, "concept_d.gif"), save_all=True,
                     append_images=frames_p[1:], duration=80, loop=0)
    print("Generated Concept D assets.")

if __name__ == "__main__":
    render_concept_a(PREVIEWS_DIR)
    render_concept_b(PREVIEWS_DIR)
    render_concept_c(PREVIEWS_DIR)
    render_concept_d(PREVIEWS_DIR)
    print("All 4 cinematic concepts rendered successfully!")

