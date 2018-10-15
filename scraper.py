#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from pyvirtualdisplay import Display
from google_images_download import google_images_download

# Add following 2 line before start the Chrome
display = Display(visible=0, size=(800, 800))
display.start()
driver = webdriver.Chrome()
driver.get("http://www.google.com")

# arguments are searches seperated by commas
# e.g. "oak tree, palm tree, maple tree" will return 3 folders of images containing pizza's, boats and trees
arguments = ""

# the new directory that all your downloaded folders will go into
folder = ""

# how many images you want to download per search
limit = 500

response = google_images_download.googleimagesdownload()
absolute_image_paths = response.download({"keywords":arguments,"limit":limit,"output_directory":folder,"chromedriver":"/usr/local/bin/chromedriver"})

driver.quit()
display.stop()
