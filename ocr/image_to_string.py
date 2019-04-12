import pytesseract
from PIL import Image
import datefinder


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

img = Image.open('test.jpg')

result = pytesseract.image_to_string(img)
print(result)

with open('text.txt', mode='w') as file:
    file.write(result)

matches = list(datefinder.find_dates(result))

if len(matches) > 0:

    date = matches[0]
    print (date)
else:
    print ('No dates found')

ix= result.find('TOTAL')
ix=ix+6
price= result[ix]+result[ix+1]+result[ix+2]+result[ix+3]
print(price)

