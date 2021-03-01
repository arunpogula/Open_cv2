import cv2
import os 


def change_format():
  
    # Image path 
    image_path = r'C:\Users\pc\Desktop\sonarcube.png' 
    # Image directory 
    directory = r'C:\Users\pc\Desktop'
    # reading the image
    img = cv2.imread(image_path) 
    
    # Change the directiory
    os.chdir(directory) 
    # List files and directories    
    print("Before saving image:")   
    print(os.listdir(directory))   
    
    # Filename 
    filename = 'sonarcube1.jpg'  
    # Saving the image 
    cv2.imwrite(filename, img)   
    print(os.listdir(directory))     
    print('Successfully saved') 
    
change_format()