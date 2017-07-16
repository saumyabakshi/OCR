from skimage import io, color
img = io.read('streetsign4.jpg')
dimensions = color.guess_spatial_dimensions(img)
print (dimensions)