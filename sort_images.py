import os
import csv
from google.cloud import vision
from google.cloud.vision import types
from clean import *
from csv_formatting import *


print("Connecting to Google Vision Client...")
client = vision.ImageAnnotatorClient()

# this input is the exact name of the output directory used in scraper.py
target = input("Output directory name (e.g. 'tree_types'): ")
dir = os.fsencode('./' + target)
bucket_name = input("Name of your bucket (e.g. 'tree-recognition-vcm'): ")

print("Checking / Renaming folder names...")
check_folder_names(dir)

print("Removing bad images... This may take a while...")
MAX_IMAGE_SIZE = 10485760
clean_images(dir, client, MAX_IMAGE_SIZE)
print("All files clean!")

print("Renaming images...")
rename_images(dir)

print("Creating filtered_" + target + ".csv...")
csv_file = open(target + ".csv", "a")
csv_writer = csv.writer(csv_file)
print("Writing AutoML paths to csv...")
BUCKET_NAME = "gs://" + bucket_name + "/"
create_csv_paths(dir, csv_file, BUCKET_NAME)

csv_file.close()
print("FINISHED")
