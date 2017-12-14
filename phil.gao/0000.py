from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open(r"C:\Users\hagao\Desktop\Koala.jpg").convert('RGBA')

#get image size 
size = base.size
# define the font size using points
Fsize = 80

#font position 
fpos = (size[0]-Fsize,0)

# get a font
fnt = ImageFont.truetype(r'C:\windows\Fonts\Arial.ttf', Fsize)
# get a drawing context
d = ImageDraw.Draw(base)

# draw text, left up point ,font , color using RGBA
d.text(fpos, "4", font=fnt, fill=(255,0,0,1))


base.save(r'C:\Users\hagao\Desktop\KoalaNum.bmp')
base.show()
