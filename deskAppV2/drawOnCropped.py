from PIL import Image, ImageDraw

HallwayH = 456.4
HallwayW = 2522.1
TAofficeH = 619.7
# TAofficeW = 776.1
NlabH = 567.7 
ElabH = 447
roomsH = 900 + 350 
croppedFloorHeight  = HallwayH + TAofficeH + NlabH + ElabH + roomsH
croppedFloorWidth  = HallwayW

def mapCoordinates(right,down,img):
    """
        Maps the coordinates from cm to Pixels fitted to the Floor image, 
        coordinates are measured from top left corner
    """
    img = Image.open(img)

    imgWidth = img.size[0] 
    imgHeight = img.size[1] 


    yFactor = croppedFloorHeight / imgHeight
    xFactor = croppedFloorWidth / imgWidth

    x = int(right / xFactor)
    y = int(down / yFactor) 
    return (x,y)


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


def reMapOrigin(modelCoordinates):
    modelX = modelCoordinates[0] 
    modelY = modelCoordinates[1]
    print(f'modelX: {modelX}')
    print(f'modelY:{modelY}')
    boxH = 280 
    boxW = 500 
    if modelY == 11:
        modelX = 1
        modelY = 5
    if modelY == 12:
        modelX = 2
        modelY = 5
    if modelY == 13:
        modelX = 1
        modelY = 7
    X =  ( HallwayW / 2) - (modelX * boxW) + 100 # fitting
    Y = croppedFloorHeight - (modelY * boxH)  - 100  
    return (X,Y)

def track(modelCords,initImg,modifiedImg,circleRad):
    x,y = reMapOrigin(modelCords)
    pixelX,pixelY = mapCoordinates(x,y,initImg)
    drawCircle(initImg,circleRad,(pixelX,pixelY),modifiedImg)

     

if __name__ == "__main__":
    

    img = "dFloorMapEdited.jpg"
    saved = "modified.png"

    # track((0,10),img,saved,6)
    # for i in range(10):
    #     track((0,i/10),saved,saved,6)
