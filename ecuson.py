from PIL import Image, ImageDraw, ImageFont, ImageColor

f = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf", 12)

im = Image.open("ecuson.png")
draw = ImageDraw.Draw(im)

draw.text((100, 100), "Hello", fill=ImageColor.getrgb("black"), font=f)

im.save("ecuson_processed.png", "PNG")