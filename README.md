# Google Images for AutoMl Vision

Want to train a model but don't have enough images? Want more images for your model than the ones you have taken? 
I decided to make this repository after struggling to have a large enough dataset to get good results off of the Google AutoML Vision API.

At the moment it is a rough guide as I have only just got it to work myself.

## Overview

* **[Getting Started](#getting-started)**
  * [Setting up the Compute Engine](#setting-up-the-compute-engine)
* **[scraper py](#scraper-py)**
* **[Method 1](#method-1)** - involves manually cleaning your images on AutoML at the end
  * [bucket_to_csv py](#bucket_to_csv-py)
  * [Running bucket_to_csv py](#running-bucket_to_csv-py)
* **[Method 2](#method-2)** - images are automatically cleaned before uploading to your cloud bucket
  * [sort_images py](#sort_images-py)
  * [clean py](#clean-py)
  * [csv_formatting py](#csv_formatting-py)
* **[Uploading your files to the bucket](#uploading-your-files-to-the-bucket)**
* **[Next Steps](#next-steps)**

## Getting Started

Its best if you have a basic understanding of Google Cloud, AutoML, compute engines and storage buckets, as I will not go into detail in these areas.
Before you use the code in this repository you should...
* have a Google Cloud project set up
* create a compute engine
* enable AutoML Vision API
* create a storage bucket
* make sure these are all connected with your service account

### Setting up the Compute Engine

* After having created an instance, follow [Google's guide](https://cloud.google.com/python/setup) on setting up a python environment.

* Next, go ahead and pip install google_images_download:

```
pip install google_images_download
```

* Create a file called install.sh and copy the contents of install.sh from [this link](https://gist.github.com/ziadoz/3e8ab7e944d02fe872c3454d17af31a5) and run:

```
chmod +x ./install.sh
./install.sh
```

* Follow the instructions [here](https://christopher.su/2015/selenium-chromedriver-ubuntu/) **except for the last step** where they create a python file.

## scraper py

Create a file scraper.py and add the contents of [scraper.py](https://github.com/SamuelBroughton/google_images_for_autoML/blob/master/scraper.py)

Alter the following:
* **arguments** - this should include the things you wish to search for on Google images. For example if your project was to distinguish different types of trees, arguments might include "oak tree, palm tree, maple tree".
* **folder** - this is the output directory your want all your downloads to go into. Keeping in mind the tree project, you might want to call this folder trees.
* **limit** - this is the number of images you which to download for each search category. It is set at 500 by default.

You can now run:

```
python2 scraper.py
```

to collect all your images. NB: this will take a long time.

## Method 1

### bucket_to_csv py

Now that you have your scraped images, you should have a file structure similar to this (keeping in mind the trees example from before):

**trees > oak tree > (lots of images)**

**trees > palm tree > (lots of images)**

**trees > maple tree > (lots of images)**

bucket_to_csv.py iterates through all these files and...
* removes any files that are not of type .jpg .jpeg .png .webp
* alters folder and file names to conform to AutoML naming
* produces a csv file with the exact location of the images to where they will be found in your cloud storage bucket
* attatches two labels for each image, in the trees example you might find an image with labels: tree and palm tree.

**NB: On line 32 you must replace YOUR-BUCKET-NAME with your actual cloud bucket name**

### Running bucket_to_csv.py

```
python3 bucket_to_csv
```

Will return the following prompt:

```
Output directory (e.g. 'trees'):
```

Here you need to enter the output directory folder name you specified in scraper.py, following our trees example:

```
Output directory (e.g. 'trees'): trees
```

## Method 2

### sort_images py

Coming soon!

### clean py

Coming soon!

### csv_formatting py

Coming soon!

## Uploading your files to the bucket

Becuase you will probably have a lot of images to upload to your bucket, run the following as Google recommends:

```
gsutil -m cp -r [SOURCE_DIRECTORY] gs://[BUCKET_NAME]
```

This will take a while.

Now all your images are in your bucket you need to upload the csv file that bucket_to_csv.py created. It has been named **bucket.csv** by default.

```
gsutil cp [SOURCE_DIRECTORY]/bucket.csv gs://my-bucket
```

## Next Steps

Now you can transfer your dataset to AutoML and train your model!
