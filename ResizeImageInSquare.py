from PIL import Image, ImageDraw,ImageFilter



def makeSquare(rect_img,bg_color):
    width, height = rect_img.size
    if width == height:
        return rect_img
    elif width > height:
        bg_img = Image.new(rect_img.mode,(width,width),bg_color ) 
        bg_img.paste(rect_img,(0,(width-height)//2))
        return bg_img
    else:
        bg_img = Image.new(rect_img.mode,(height,height),bg_color ) 
        bg_img.paste(rect_img,((width-height)//2),0)
        return bg_img

img = Image.open("g.PNG")
width = 800
new_img = makeSquare(img,(255,255,255)).resize((width,width),Image.LANCZOS)

new_img.save("reized.png",quality = 95)
