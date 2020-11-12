from PIL import Image, ImageDraw


def mapCoordinates(left,down,img):
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
    xFactor = (whitePadding + FloorWidth ) / imgWidth
    #(with pading from left and top)
    # for width  = 9.5 pixels per cm   
    # for height =  10 pixels per cm

    x = int(left / xFactor)
    y = int(down / yFactor) 
    return (x,y)

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
def drawCircle(img,radius,coordinates,saveTo):
    with Image.open(img) as im:
        draw = ImageDraw.Draw(im,'RGBA')
        
        p1 = (coordinates[0] - radius , coordinates[1] - radius)
        p2 = (coordinates[0] + radius , coordinates[1] + radius)
        p3 = (coordinates[0] - (radius * 5) , coordinates[1] - (radius * 5))
        p4 = (coordinates[0] + (radius * 5) , coordinates[1] + (radius * 5))
        # outter
        draw.ellipse([p3,p4],fill=(0,0,0,100))
        # inner
        draw.ellipse([p1,p2], fill=(0,250,0,255))
        im.save(saveTo, "PNG")  

if __name__ == "__main__":
    

    img = "departmentFloorMap.jpg"
    saved = "modified.png"

    # Down Hallway starts at (1426,3054)

    coords = mapCoordinates(1470,5700,img)
    drawCircle(img,6,coords,saved)