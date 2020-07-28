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
├──pascal
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
    python convertData.py dataturk.json downloads pascal
  ```
  This will fill files in the downloads folder and pascal
  Cut paste downloaded images from downloads folder to pascal/downloads
 
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

- Now paste labels.txt and ids.txt into pascal and new filestructure is:

```
File Struture:
root
├──downloads
    ├──Multiple Images
├──pascal
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
      python convertJsontoCOCOformat.py --ann_dir pascal/downloads --ann_ids pascal/ids.txt --labels pascal/labels.txt --output mainout.json
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
# Once useless images are removed you need to run STEP 3 Again since Ids are basically filenames
# After thats again paste that ids.txt in the pascal folder that is Step 4
# Run Step 5 again


# Finally your Dataset will contain
```
root    
├──pascal
   ├──downloads
       ├──Multiple Images
├──dataturk.json
├──mainout.json
```

# Finally it can be used in Fastai
