import io
import os
import csv
import uuid

# method of renaming and sorting files into csv
def recognise_files(dir, csv_file):
  foldersCompleted = 0
  csvWriter = csv.writer(csv_file)

  output_d = os.fsdecode(dir[2:])

  # sort folder names
  for root, dirs, files in os.walk(dir):
    folder_name = os.fsdecode(os.path.basename(os.path.normpath(root)))
    folder_name = test_folder_name(folder_name, output_d)

  # sort files in folder categories
  for root, dirs, files in os.walk(dir):
    for name in files:
      folder_name = os.fsdecode(os.path.basename(os.path.normpath(root)))
      file_name, file_extension = os.path.splitext(os.fsdecode(name))

      # only accept image files, otherwise: remove the file
      # alter image file names to conform to AutoML naming
      # write them to the csv
      file = os.fsdecode(os.path.join(root, name))
      if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".webp"):
        new_name = str(uuid.uuid4())
        new_name = new_name.replace("-", "_")
        os.rename(output_d + "/" + folder_name + "/" + file_name + file_extension, output_d + "/" + folder_name + "/" + new_name + file_extension)
        csvWriter.writerow(["gs://YOUR-BUCKET-NAME/" + output_d + "/" + folder_name + "/" + new_name + file_extension, folder_name, output_d])
      else:
        os.remove(file)

    print("Folders completed: " + str(foldersCompleted))
    foldersCompleted += 1

  return

# method to change folder names to conform with AutoML naming structure
def test_folder_name(folder_name, output_d):
  new_folder_name = folder_name.lower()
  new_folder_name = new_folder_name.lstrip()
  new_folder_name = new_folder_name.replace(" ", "_")
  new_folder_name = new_folder_name.replace("-", "_")

  if new_folder_name != folder_name:
    os.rename(output_d + "/" + folder_name, output_d + "/" + new_folder_name)
    return new_folder_name
  else:
    return folder_name

#################################################################

print ("Creating bucket.csv ...")
csv_file = open("bucket.csv", "a")

csvWriter = csv.writer(csv_file)

# the input here needs to be the name of the output directory used in scraper.py
target = input("Output directory (e.g. 'trees'): ")
dir = os.fsencode('./' + target)

recognise_files(dir, csv_file)

csv_file.close()
print("FINISHED")
