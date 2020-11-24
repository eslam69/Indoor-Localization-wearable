from PIL import Image, ImageDraw


def mapCoordinates(left, down, img):
    """
        Maps the coordinates from cm to Pixels fitted to the Floor image, 
        coordinates are measured from top left corner
    """
    # image width  = 299 pixels
    # image height  = 730 pixels

    img = Image.open(img)

    imgWidth = img.size[0]
    imgHeight = img.size[1]
    # floor height // till H-hallway = (4465.7) cm

    # floor width = (2509.9) cm
    # floor height = (4465.7) + 2347.6 = (6814.8) cm
    FloorWidth = 2509.9    # CM
    FloorHeight = 6814.8   # CM

    # White padding : 250 cm left , 250 cm down
    whitePadding = 250     # CM
    # (without padding)
    # for width = Each cm eq. to ~ 8.5 pixels
    # for height = Each cm eq. to ~ 9.5 pixels
    yFactor = (whitePadding + FloorHeight) / imgHeight
    xFactor = (whitePadding + FloorWidth) / imgWidth
    # (with pading from left and top)
    # for width  = 9.5 pixels per cm
    # for height =  10 pixels per cm

    x = int(left / xFactor)
    y = int(down / yFactor)
    return (x, y)

# def drawSqaure(img,coordinates,saveTo):
#     with Image.open(img) as im:
#         draw = ImageDraw.Draw(im)
#         #AT 1176 cm left / 3423.7 should be at net lab
#         #(138,360)
#         # draw.point((133,266),fill=128)
#         p1 = coordinates
#         p2 = (coordinates[0] + 10 , coordinates[1] + 10)
#         draw.rectangle([p1,p2],outline=128,fill=128,width=10)
#         im.save(saveTo, "PNG")


def drawCircle(img, radius, coordinates, saveTo):
    with Image.open(img) as im:
        draw = ImageDraw.Draw(im, 'RGBA')

        p1 = (coordinates[0] - radius, coordinates[1] - radius)
        p2 = (coordinates[0] + radius, coordinates[1] + radius)
        p3 = (coordinates[0] - (radius * 5), coordinates[1] - (radius * 5))
        p4 = (coordinates[0] + (radius * 5), coordinates[1] + (radius * 5))
        # outter
        draw.ellipse([p3, p4], fill=(0, 0, 0, 100))
        # inner
        draw.ellipse([p1, p2], fill=(0, 250, 0, 255))
        # draw.line([(0,coordinates[1]),(im.width,coordinates[1])],fill=(250,0,0,250))

        im.save(saveTo, "PNG")


if __name__ == "__main__":

    img = "allpoints.png"
    saved = "allpoints.png"

    # Down Hallway starts at (1470,3054)
    # Down Hallway ends  at (1470,5700)
    # left room edge  at (240,-)
    # right room edge  at (1320,-)

    # TA room preferred point  at (1100, 3200)
    # Lab room preferred point  at (900, 4350)
    
    # 11 cell per (5700-2800)

    coords = mapCoordinates(900, 4350, img)
    drawCircle(img, 8, coords, saved)
