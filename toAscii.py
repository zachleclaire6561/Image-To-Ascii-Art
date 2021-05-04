from PIL import Image
from matplotlib import pyplot
from numpy import asarray
import numpy as np
import sys
import math

'''
Error codes:
-1: error with parameters
-2: user input error
-3: problem with image
'''

def to_ascii(image_name, background, scale, is_terminal):
    # checking data supplied
    scale = float(scale)/(100.0)

    if(type(image_name) != str or type(background) != str or type(scale) != float or scale > 0.3):
        return -2
    bg = (0,0,0)
    if(background == "white"):
        bg = (255,255,255)

    try: 
        image = Image.open('images/'+image_name)
        size = image.size

        #determine new size
        x_size = int(size[0]*scale)
        y_size = int(size[1]*scale)
        new_vals = np.ndarray(shape=(x_size,y_size))
        chars = ['@', '%', '#', '&', '=', '+', '-', ':', ',', '.']
        #converting image to array
        im_arr = asarray(image)
        print('shape: ', im_arr.shape, 'x,y', x_size, y_size)
        for x in range(x_size):
            for y in range(y_size):
                #sub array ranges each chunk aka 1 unit of 1/scale
                sub_arr = im_arr[int(x/scale):int((x+1)/scale),int(y/scale):int((y+1)/scale)]
                
                red,green,blue = 0,0,0

                red_arr = sub_arr[:,0]
                green_arr = sub_arr[:,1]
                blue_arr = sub_arr[:,2]

                if(len(red_arr) > 0 and len(green_arr) > 0 and len(blue_arr) > 0):
                    red = np.mean(red_arr)
                    green = np.mean(green_arr)
                    blue = np.mean(blue_arr)
                    #rgb value distance from background color
                    dist = math.sqrt((bg[0]-red)**2+(bg[1]-blue)**2+(bg[2]-green)**2)
                    print(chars[int(dist/(255*math.sqrt(3))*(len(chars)-1))], end=' ')

            #> is used to indicate new lines
            if(not is_terminal):
                print(">")
            else: 
                print("")

    except:
        return -3

    return 0
    

# python main.py [file-name] [black/white] [scaling_factor] 

if __name__== '__main__':
    
    count = len(sys.argv)
    val = (sys.argv[1] == "True")
        
    error_code = 0
    if(count == 3):
        error_code = to_ascii(sys.argv[2], "black", 20, val)
    elif(count == 4):
        error_code = to_ascii(sys.argv[2], sys.argv[3], 20, val)
    elif(count == 5):
        error_code = to_ascii(sys.argv[2], sys.argv[3], sys.argv[4], val)
    else:  
        print('please supply the image name and output format')
        error_code = -1
    if(error_code != 0):
        print(error_code)
    
    #arr = np.array([[1,2,3,4],[1,2,3,4]])
    #print(arr[:,0])