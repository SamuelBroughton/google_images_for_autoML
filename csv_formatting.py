import io
import os
import csv
import uuid

""" Renames folders that do not conform to AutoML naming structure """
def check_folder_names(dir):
    for root, dirs, files in os.walk(dir):
        output_dir = os.fsdecode(dir[2:])
        current_folder_name = os.fsdecode(os.path.basename(os.path.normpath(root)))

        new_folder_name = current_folder_name.lower()
        new_folder_name = new_folder_name.lstrip()
        new_folder_name = new_folder_name.replace(" ", "_")
        new_folder_name = new_folder_name.replace("-", "_")

        if new_folder_name != current_folder_name:
            old_path = output_dir + "/" + current_folder_name
            new_path = output_dir + "/" + new_folder_name
            os.rename(old_path, new_path)

    return

""" Renames all images to conform to AutoML naming structure """
def rename_images(dir):
    output_dir = os.fsdecode(dir[2:])

    for root, dirs, files in os.walk(dir):
        for name in files:

            folder_name = os.fsdecode(os.path.basename(os.path.normpath(root)))
            file_name, file_extension = os.path.splitext(os.fsdecode(name))

            new_file_name = str(uuid.uuid4())
            new_file_name = new_file_name.replace("-", "_")
            old_file_path = output_dir + "/" + folder_name + "/" + file_name + file_extension
            new_file_path = output_dir + "/" + folder_name + "/" + new_file_name + file_extension
            os.rename(old_file_path, new_file_path)

    return

""" Writes paths of where images will be stored in gcloud bucket  """
def create_csv_paths(dir, csv_file, BUCKET_NAME):
    folders_completed = 0
    csv_writer = csv.writer(csv_file)
    output_dir = os.fsdecode(dir[2:])

    for root, dirs, files in os.walk(dir):
        for name in files:
            folder_name = os.fsdecode(os.path.basename(os.path.normpath(root)))
            file_name, file_extension = os.path.splitext(os.fsdecode(name))

            cloud_path = BUCKET_NAME + output_dir + "/" + folder_name + "/" + file_name + file_extension
            label1 = folder_name
            label2 = output_dir

            csv_writer.writerow([cloud_path, label1, label2])

        print("Folders completed: " + str(folders_completed))
        folders_completed += 1

    return
