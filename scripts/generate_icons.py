from PIL import Image, ImageDraw, ImageFont
import math

S = 1024

def new_img():
    return Image.new("RGBA", (S, S), (0, 0, 0, 0)), ImageDraw.Draw(Image.new("RGBA", (S, S), (0, 0, 0, 0)))

def save(img, path):
    img.save(path)
    img2 = img.resize((2048, 2048), Image.LANCZOS)
    img2.save(path.replace("icon.png", "icon@2x.png"))

# ---------- time_of_light: clock with sun rays ----------
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
amber = (255, 179, 0, 255)
dark = (255, 138, 0, 255)
cx, cy = 512, 512
R = 330
# sun rays
for i in range(12):
    a = math.radians(i * 30)
    x1 = cx + math.cos(a) * (R + 60)
    y1 = cy + math.sin(a) * (R + 60)
    x2 = cx + math.cos(a) * (R + 150)
    y2 = cy + math.sin(a) * (R + 150)
    d.line([x1, y1, x2, y2], fill=amber, width=44)
# clock face
d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=amber, width=44)
d.ellipse([cx - R + 40, cy - R + 40, cx + R - 40, cy + R - 40], outline=dark, width=16)
# hands (10:10)
d.line([cx, cy, cx, cy - 180], fill=amber, width=36)
d.line([cx, cy, cx + 130, cy + 90], fill=amber, width=36)
d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], fill=dark)
save(img, "/tmp/opencode/icons_dom/time_of_light/icon.png")

# ---------- off_light: lightbulb + motion waves ----------
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
blue = (3, 169, 244, 255)
darkblue = (13, 71, 161, 255)
# lightbulb (left)
bx, by = 390, 500
d.ellipse([bx - 150, by - 150, bx + 150, by + 150], outline=blue, width=40)      # bulb
d.polygon([(bx - 80, by + 110), (bx + 80, by + 110), (bx + 40, by + 240), (bx - 40, by + 240)], outline=blue, width=36)  # base
d.line([bx - 60, by - 30, bx - 20, by - 30], fill=blue, width=28)  # filament
d.line([bx + 20, by - 30, bx + 60, by - 30], fill=blue, width=28)
# motion waves (right)
for i, rr in enumerate([140, 240, 340]):
    d.arc([700 - rr, 620 - rr, 700 + rr, 620 + rr], start=-100, end=100, fill=darkblue, width=40)
save(img, "/tmp/opencode/icons_dom/off_light/icon.png")

# ---------- frame_control: tablet/frame with controls ----------
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
purple = (156, 39, 176, 255)
darkpurple = (74, 20, 140, 255)
# frame / tablet
d.rounded_rectangle([140, 180, 884, 820], radius=70, outline=purple, width=56)
d.rounded_rectangle([230, 280, 794, 720], radius=30, outline=darkpurple, width=20)
# display content: mountains (landscape)
d.polygon([(230, 720), (430, 430), (560, 560), (660, 470), (794, 720)], fill=darkpurple)
# controls dots at bottom
for i, x in enumerate([400, 512, 624]):
    d.ellipse([x - 28, 860, x + 28, 916], fill=purple)
save(img, "/tmp/opencode/icons_dom/frame_control/icon.png")

from PIL import Image, ImageDraw
import math

S = 1024

def save(img, path):
    img.save(path)
    img.resize((2048, 2048), Image.LANCZOS).save(path.replace("icon.png", "icon@2x.png"))

# ---------- programmable_thermostat: thermometer + schedule ----------
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
orange = (255, 138, 0, 255); red = (211, 47, 47, 255)
cx, cy = 430, 500
# thermometer
d.rounded_rectangle([cx - 70, cy - 250, cx + 70, cy + 250], radius=70, outline=orange, width=44)
d.ellipse([cx - 110, cy + 120, cx + 110, cy + 340], outline=orange, width=44)  # bulb
d.ellipse([cx - 70, cy + 160, cx + 70, cy + 300], fill=red)                     # mercury
d.line([cx, cy - 180, cx, cy + 100], fill=red, width=30)
# schedule bars (right)
bx = 700
for i, h in enumerate([220, 340, 150, 280]):
    y0 = 800 - h
    d.rounded_rectangle([bx - 60 + i * 80, y0, bx + 20 + i * 80, 800], radius=20, fill=orange)
d.line([bx - 60, 800, bx + 300, 800], fill=orange, width=28)
save(img, "/tmp/opencode/icons_dom/programmable_thermostat/icon.png")

# ---------- smartlife: blue rounded square + socket/switch ----------
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
blue = (0, 145, 234, 255); white = (255, 255, 255, 255)
d.rounded_rectangle([120, 120, 904, 904], radius=200, fill=blue)
# socket icon (power + light) — simple power symbol + dot
d.arc([360, 300, 664, 604], start=210, end=330, fill=white, width=64)   # power arc
d.line([512, 560, 512, 700], fill=white, width=56)                       # power stem
d.ellipse([462, 700, 562, 800], fill=white)                              # base/socket
save(img, "/tmp/opencode/icons_dom/smartlife/icon.png")

# ---------- yabackup: Yandex red cloud + backup arrow ----------
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
red = (252, 63, 29, 255); dark = (200, 40, 20, 255)
# cloud
d.ellipse([200, 420, 480, 700], fill=red)
d.ellipse([380, 340, 700, 640], fill=red)
d.ellipse([620, 400, 840, 640], fill=red)
d.rectangle([200, 560, 840, 660], fill=red)
# up arrow (backup)
d.polygon([(512, 230), (360, 420), (664, 420)], fill=white)
d.rectangle([456, 300, 568, 560], fill=white)
save(img, "/tmp/opencode/icons_dom/yabackup/icon.png")

print("done")
