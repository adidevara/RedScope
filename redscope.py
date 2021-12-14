from PIL import Image

im = Image.open('pic.jpg', 'r')
neon_green=(57,255,20)

def is_pixel_black(pixel):
  return pixel[0] < 5 and pixel[1] < 5 and  pixel[2] < 5  

def is_pixel_white(pixel):
  return pixel[0] > 235 and pixel[1] > 235 and pixel[2] > 235 

red_values=[]
for x in range(im.width):
  for y in range(im.height):
    pixel = im.getpixel((x,y))
    if not is_pixel_black(pixel) and not is_pixel_white(pixel):
      red_values.append(pixel[0])

average_red_value= sum(red_values) / len(red_values)
print(average_red_value)

for x in range(im.width):
  for y in range(im.height):
    red_value_of_pixel = im.getpixel((x,y))[0]
    green_value_of_pixel = im.getpixel((x,y))[1]
    blue_value_of_pixel = im.getpixel((x,y))[2]
    if red_value_of_pixel > 3* green_value_of_pixel and red_value_of_pixel > 3 * blue_value_of_pixel and not is_pixel_black(im.getpixel((x,y))):
      im.putpixel((x,y),neon_green)
