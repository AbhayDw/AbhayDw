import math
import os
import random
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    font_path = os.path.join(r"C:\Windows\Fonts", name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def draw_lens_flare(draw, cx, cy, w, h, flare_progress):
    """Draws a Hollywood/IMAX anamorphic lens flare sweeping across the frame."""
    # Anamorphic streak (long horizontal beam)
    streak_len = int(w * 0.7)
    for sw in range(6, 0, -1):
        alpha = (7 - sw) / 6.0
        streak_col = (int(56 * alpha), int(189 * alpha), int(248 * alpha))
        draw.line([(cx - streak_len, cy), (cx + streak_len, cy)], fill=streak_col, width=sw)
    
    # White core hot-spot
    draw.line([(cx - 140, cy), (cx + 140, cy)], fill=(255, 255, 255), width=3)
    draw.ellipse([(cx - 18, cy - 8), (cx + 18, cy + 8)], fill=(255, 255, 255))
    
    # Secondary optical halos and chromatic rings
    for r in [35, 70, 120, 180]:
        halo_col = (int(245 * (1 - r/200)), int(158 * (1 - r/200)), int(11 * (1 - r/200)))
        draw.ellipse([(cx - r, cy - r // 2), (cx + r, cy + r // 2)], outline=halo_col, width=1)
        
    # Vertical anamorphic glare spike
    draw.line([(cx, cy - 45), (cx, cy + 45)], fill=(255, 255, 255), width=2)

def create_cinematic_master(output_path, num_frames=36):
    # 2x supersampling: 1920 x 680 -> 960 x 340 (true 21:9 cinematic aspect)
    w, h = 1920, 680
    target_w, target_h = 960, 340

    font_kicker = get_font("consola.ttf", 22)
    font_massive = get_font("bahnschrift.ttf", 88)
    font_sub_cinematic = get_font("segoeuib.ttf", 36)
    font_pill = get_font("segoeuib.ttf", 20)
    font_meta = get_font("segoeui.ttf", 22)
    font_geo = get_font("consola.ttf", 18)

    # Cinematic Palette: Deep Obsidian Void + Anamorphic Horizon Glow + Molten Gold & Electric Cyan
    col_void = (6, 9, 15)            # Deepest Cinema Black
    col_horizon = (18, 30, 56)       # Sapphire Twilight Horizon
    col_cyan_glow = (56, 189, 248)   # Anamorphic Cyan
    col_gold = (245, 158, 11)        # Topaz Molten Gold (#F59E0B)
    col_gold_light = (254, 215, 120) # Champagne Highlight
    col_border = (34, 48, 72)

    # Deterministic particle stars for atmospheric depth
    random.seed(42)
    particles = []
    for _ in range(65):
        particles.append({
            "x": random.randint(40, w - 40),
            "y": random.randint(40, h - 40),
            "r": random.choice([1, 2, 3]),
            "speed": random.uniform(0.4, 1.2),
            "alpha": random.uniform(0.3, 0.9)
        })

    frames = []

    for frame_idx in range(num_frames):
        t = frame_idx / float(num_frames)
        phase = t * 2 * math.pi

        im = Image.new("RGB", (w, h), color=col_void)
        draw = ImageDraw.Draw(im)

        # 1. Cinematic Anamorphic Horizon Gradient
        horizon_y = int(h * 0.42)
        for y in range(h):
            dist_to_h = abs(y - horizon_y)
            glow_factor = max(0.0, 1.0 - (dist_to_h / 240.0)) ** 1.8
            r = int(col_void[0] + (col_horizon[0] - col_void[0]) * glow_factor)
            g = int(col_void[1] + (col_horizon[1] - col_void[1]) * glow_factor)
            b = int(col_void[2] + (col_horizon[2] - col_void[2]) * glow_factor)
            draw.line([(0, y), (w, y)], fill=(r, g, b))

        # 2. Cinematic Atmospheric Light Motes (Particles in subtle 3D parallax)
        for p in particles:
            py = int((p["y"] + math.sin(phase + p["x"]) * 8) % (h - 60)) + 30
            px = int((p["x"] + t * 40 * p["speed"]) % (w - 60)) + 30
            p_brightness = int(255 * (0.4 + 0.6 * math.sin(phase * p["speed"] + p["x"])))
            p_col = (p_brightness, p_brightness, int(p_brightness * 0.9))
            draw.ellipse([(px - p["r"], py - p["r"]), (px + p["r"], py + p["r"])], fill=p_col)

        # 3. Precision Film Framing & Anamorphic Letterbox Ticks
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=col_border, width=2)

        # Film aspect tick marks
        tick_len = 36
        draw.line([(20, 20), (20 + tick_len, 20)], fill=col_cyan_glow, width=4)
        draw.line([(20, 20), (20, 20 + tick_len)], fill=col_cyan_glow, width=4)
        draw.line([(w - 20 - tick_len, 20), (w - 20, 20)], fill=col_gold, width=4)
        draw.line([(w - 20, 20), (w - 20, 20 + tick_len)], fill=col_gold, width=4)
        draw.line([(20, h - 20 - tick_len), (20, h - 20)], fill=col_gold, width=4)
        draw.line([(20, h - 20), (20 + tick_len, h - 20)], fill=col_gold, width=4)
        draw.line([(w - 20 - tick_len, h - 20), (w - 20, h - 20)], fill=col_cyan_glow, width=4)
        draw.line([(w - 20, h - 20 - tick_len), (w - 20, h - 20)], fill=col_cyan_glow, width=4)

        # 4. Cinematic Top Header Bar
        draw.text((80, 50), "FILM OPENING // CINEMATIC IDENTITY &amp; SYSTEMS ARCHITECTURE", font=font_kicker, fill=col_cyan_glow)
        draw.text((w - 380, 50), "23&deg;15'N 77&deg;25'E &bull; BHOPAL, MP", font=font_geo, fill=col_gold)

        # 5. Monumental Name Typography: ABHAY DWIVEDI
        name_x = 80
        name_y = 110

        # Slow cinematic camera zoom push-in simulation
        zoom_scale = 1.0 + 0.02 * math.sin(phase)

        # Drop shadow depth
        draw.text((name_x + 4, name_y + 4), "ABHAY DWIVEDI", font=font_massive, fill=(3, 5, 8))
        # Titanium white foreground letterforms
        draw.text((name_x, name_y), "ABHAY DWIVEDI", font=font_massive, fill=(255, 255, 255))

        # 6. Sweeping Anamorphic Flare Light Across the Title
        flare_travel_x = int(name_x - 100 + ((t * 1.3) % 1.0) * (w - 200))
        draw_lens_flare(draw, flare_travel_x, name_y + 45, w, h, t)

        # 7. Dual-Tone Luminous Horizon Accent Rule
        rule_y = name_y + 110
        draw.line([(name_x, rule_y), (name_x + 360, rule_y)], fill=col_cyan_glow, width=4)
        draw.line([(name_x + 360, rule_y), (name_x + 820, rule_y)], fill=col_gold, width=3)
        draw.line([(name_x + 820, rule_y), (w - 80, rule_y)], fill=(38, 54, 82), width=2)
        draw.ellipse([(name_x + 357, rule_y - 3), (name_x + 363, rule_y + 3)], fill=(255, 255, 255))

        # 8. Professional Title Subtitle
        draw.text((82, rule_y + 24), "Technology &amp; Digital Solutions Professional", font=font_sub_cinematic, fill=col_gold_light)

        # 9. Four Executive Domain Pillars in Brushed-Titanium Cards
        pillars = [
            ("GOVERNMENT INITIATIVES", col_cyan_glow, (20, 32, 54)),
            ("SOFTWARE IMPLEMENTATION", col_gold, (30, 38, 48)),
            ("APPLIED AI &amp; DATA SYSTEMS", (236, 72, 153), (32, 28, 48)),
            ("CLIENT &amp; STAKEHOLDER COORDINATION", (16, 185, 129), (20, 38, 38)),
        ]
        card_x = 82
        card_y = rule_y + 92
        for p_title, p_glow, p_card_bg in pillars:
            bbox = font_pill.getbbox(p_title)
            cw = bbox[2] - bbox[0] + 44
            ch = 44
            # Glass card outline & fill
            draw.rounded_rectangle([(card_x, card_y), (card_x + cw, card_y + ch)],
                                   radius=8, fill=p_card_bg, outline=(50, 72, 108), width=1)
            # Glowing indicator gem
            draw.ellipse([(card_x + 14, card_y + 16), (card_x + 24, card_y + 26)], fill=p_glow)
            draw.ellipse([(card_x + 17, card_y + 19), (card_x + 21, card_y + 23)], fill=(255, 255, 255))
            draw.text((card_x + 32, card_y + 10), p_title, font=font_pill, fill=(245, 248, 252))
            card_x += cw + 18

        # 10. Cinematic Meta & Verified Scope Footer
        footer_y = card_y + 72
        draw.text((82, footer_y), "LOC:", font=font_kicker, fill=col_gold)
        draw.text((140, footer_y - 2), "Bhopal, Madhya Pradesh, India", font=font_meta, fill=(240, 246, 252))

        draw.text((540, footer_y), "STATUS:", font=font_kicker, fill=col_cyan_glow)
        draw.text((630, footer_y - 2), "Available for Institutional Deployments &amp; Strategic Advisory", font=font_meta, fill=(180, 200, 225))

        draw.text((82, footer_y + 44), "// VERIFIED STATE SCOPE: 67+ PMCOE COLLEGES &bull; SCMS ROLLOUT &bull; e-SETU INITIATIVE &bull; APPLIED ML",
                  font=font_kicker, fill=(90, 115, 150))

        # Downsample with Lanczos for razor-sharp retina display
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
    print(f"Generated Cinematic Master {output_path}: {os.path.getsize(output_path)} bytes with {len(frames)} frames.")

if __name__ == "__main__":
    out_gif = r"C:\GitHub\AbhayDw\assets\profile-header.gif"
    create_cinematic_master(out_gif)
