import glob
from PIL import Image
import os

imagelist=[]
resized_imageList=[]
imagefiles=[]

#if you want to use this project, you should change the filelocation
for filename in glob.glob('/Users/ufukm/OneDrive/Masaüstü/images/*.png'):
 sentence=filename.split('.png')
 imagefiles.append(sentence[0])
 image=Image.open(filename)
 imagelist.append(image)


for images in imagelist:
      #image.show()
      image=images.resize((500,500))
      resized_imageList.append(image)

i=0
for resized in resized_imageList:


    resized.save('{}{}{}'.format(imagefiles[i],'_new','.png'))
    i=i+1