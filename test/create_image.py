import Image
from PIL import Image
import ImageFont
img = Image.new("RGB", (1250, 480), (255, 255, 255))
import ImageDraw
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/System/Library/Fonts/Monaco.dfont", 20,  encoding="armn")
draw.text((20, 20), "<-  10  ->" * 10, font=font, fill="black")
draw.text((20, 40), "<-  10  ->" * 10, font=font, fill="black")
img.save("foo.jpg", "JPEG")
