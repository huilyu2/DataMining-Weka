########
# Viewing images from raw data
# http://ftp.ics.uci.edu/pub/machine-learning-databases/optdigits/  
#
# Make sure you have a file named optdigits.tra.csv in the same directory
#  as this Python program
#
# Note that this program was written in haste
#  -- the images look to be rotated and mirrored
# 
# by Vetle Torvik 3/2017
# tested with Python 2.7.3 on Windows 7

from cImage import *

#blow up an image by a factor of x
def blowUp(image,x):
    w = image.getWidth()
    h = image.getHeight()
    newimage = EmptyImage(w*x,h*x)

    for row in range(h):
        for col in range(w):
            px = image.getPixel(col,row)
            for i in range(col*x,col*x+x):
                for j in range(row*x,row*x+x):
                    newimage.setPixel(i,j,px)
                    #print row,col,i,j
    return newimage

#training data
#fn = 'optdigits.tra.csv'

#testing data
fn = 'optdigits.tes.csv'

fh = open(fn,'r')
#first line in file is just header, not data
header = fh.readline()
print header


#read all data into array then close file
lines = fh.readlines()
fh.close()

#check out instance number 1469
# it was predicted 9 but actually an 8 (based on IBk, k=5)
lines = lines[1468:1469]

#images are all 8 by 8
sz = 8

cnt = 0
#loop over each image (row in dataset)
for line in lines:
    line = line.replace('\n','')
    cnt += 1
    x = line.split(',')
    print cnt,x
                
    #create a blank image
    digitImage = EmptyImage(sz,sz)
    i = -1
    #create pixels and populate image
    for row in range(sz):
        for col in range(sz):
            i += 1
            val = int(x[i])

            #change scale from 0-16 to 255-0
            intensity = int(((16-val)/16.0)*255)
            print row,col,i,val,intensity
            px = Pixel(intensity,intensity,intensity)
            digitImage.setPixel(col,row,px)
    digit = int(x[i+1])

    digitImage2 = blowUp(digitImage,50)
    #display image
    ti = 'Instance: ' + str(cnt) + 'Digit:' + str(digit) 
    myWin = ImageWin(ti,sz*50,sz*50)
    digitImage2.draw(myWin)
    myWin.exitOnClick()
    dum = raw_input('Hit Enter to continue\n')







