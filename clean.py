import os
import io
from google.cloud import vision
from google.cloud.vision import types

""" Removes non image files, large files and unrelated images """
def clean_images(dir, client, MAX_IMAGE_SIZE):
    for root, dirs, files in os.walk(dir):
        for name in files:
            folder_name = os.fsdecode(os.path.basename(os.path.normpath(root)))
            file_name, file_extension = os.path.splitext(os.fsdecode(name))
            file = os.fsdecode(os.path.join(root, name))
            output_dir = os.fsdecode(dir)

            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".webp"):
                image_path = output_dir + "/" + folder_name + "/" + file_name + file_extension
                stat_info = os.stat(image_path)
                image_size = stat_info.st_size

                if image_size >= MAX_IMAGE_SIZE:
                    print(file + " removed due to SIZE")
                    os.remove(file)
                else:
                    with io.open(image_path, 'rb') as image_file:
                        content = image_file.read()

                    image = vision.types.Image(content=content)
                    response = client.label_detection(image=image)
                    labels = response.label_annotations

                    image_contains_object = False
                    for label in labels:
                        if label.description == "GENERAL LABEL1":
                            image_contains_object = True
                        elif label.description == "GENERAL LABEL2":
                            image_contains_object = True
                        elif label.description == "GENERAL LABEL3":
                            image_contains_object = True

                    if image_contains_object == False:
                        print(file + " removed due to CONTENTS")
                        os.remove(file)
                    else:
                        print(file)

            else:
                print(file + " removed due to TYPE")
                os.remove(file)

    return
