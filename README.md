# ConvertDataturkData-To-COCO
Code to convert dataturk data to PascalVOOC and then to COCO dataset format


# How to Use

## Long Procedure Incoming !!
#### Sorry for that !!

#### STEP 1

- First create the folder structure
    Create a folder downloads , pascal_voc and pascal_voc/downloads
```
File Struture:
root
├──downloads
├──pascal_voc
   ├──downloads
├──convertData.py
├──convertJsontoCOCOformat.py
├──createids.py
├──dataturk.json
├──removeUselessFilesRejectedbymodel.py
├──xml_to_csv.py
```

#### STEP 2

- Open terminal go to this folder.
  ```bash
    python convertData.py dataturk.json downloads pascal_voc_op
  ```
  This will fill files in the downloads folder and pascal_voc
  Cut paste downloaded images from downloads folder to pascal_voc/downloads
 
- Convert it to CSV.
  ```bash
      python xml_to_csv.py
  ```
- Open train.csv

   **Step not Required CODE UPDATED**
   
   ~~Find and replace \ to /~~
   
 #### STEP 3
    
- Before converting to coco we need to create labels.txt and ids.txt
  ```bash
      python createids.py
  ```
  For labels.txt add your own labels in the file.

#### STEP 4

- Now paste labels.txt and ids.txt into pascal_voc and new filestructure is:

```
File Struture:
root
├──downloads
    ├──Multiple Images
├──pascal_voc
   ├──downloads
      ├──Multiple images copied from downloads folder
   ├──Multiple XMLS
   ├──ids.txt
   ├──labels.txt
├──convertData.py
├──convertJsontoCOCOformat.py
├──createids.py
├──dataturk.json
├──removeUselessFilesRejectedbymodel.py
├──train.csv   ------->Will come from xml_to_csv file
├──xml_to_csv.py
```

#### STEP 5

- Now run the main coco convert file

  ```bash
      python convertJsontoCOCOformat.py --ann_dir pascal_voc/downloads --ann_ids pascal_voc/ids.txt --labels pascal_voc/labels.txt --output mainout.json
  ```
  
 - Now you will get your COCO format json end
 
 
 ## Note: if using with Fastai , run the get_annotations functions and print the images
    Some images get rejected, so we need to remove that completely.
    Copy the output of images frmo get_annotation function and paste it as list l in the file removeUselessFilesRejectedbymodel.py
#### Extra Step 6

- Run 
```bash
          python removeUselessFilesRejectedbymodel.py
```
# RUN EVERYTHING AGAIN From STEP 1 to 5

# Finally it can be used in Fastai
