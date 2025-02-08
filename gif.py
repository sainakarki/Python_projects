import imageio.v3 as img
filenames = ['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png']
images = [ ]
for filename in filenames:
 images.append(img.imread(filename))

img.imwrite('photo1.gif', images, duration = 100, loop = 0)