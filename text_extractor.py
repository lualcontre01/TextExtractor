#importing the necessary modules
import logging
import os
import pytesseract as pt
from PIL import Image

directory = '/opt/repos/TextExtractor/wetransfer_project_2022-03-05_1031/'
img = Image.open('/opt/repos/TextExtractor/wetransfer_project_2022-03-05_1031/IMG_0101.jpeg')
extracted = pt.image_to_string(img)

for image in os.listdir(directory):
    img = Image.open('/opt/repos/TextExtractor/wetransfer_project_2022-03-05_1031/{}'.format(image))
    with open('txt_{}.txt'.format(image[0:8]), 'w') as f:
        logging.info('Creating file for {}'.format(image))
        f.write(pt.image_to_string(img))
        f.close()
