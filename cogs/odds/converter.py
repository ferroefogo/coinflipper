from PIL import Image, ImageDraw, ImageFont


def converter(number):
    
    img = Image.new('RGB', (457, 457))
    W,H = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('Arial.ttf', 200)
    _, _, w, h = d.textbbox((0,0), str(number), font=font)
    d.text(((W-w)/2, (H-h)/2), str(number), font=font, fill=(255, 255, 255))

    img.save("./number.png")
