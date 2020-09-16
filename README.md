# ConvertDataturkData-To-COCO
Code to convert dataturk data to PascalVOOC and then to COCO dataset format


# How to Use

## Long Procedure Incoming !!
#### Sorry for that !!

<details open>
    <summary><b>STEP 1</b></summary>
    <br>
    <h3><b># STEP 1</b></h3>
    <br>
    <ul><li> First create the folder structure</li></ul>
    Create a folder downloads , pascal_voc and pascal_voc/downloads
    
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
    
</details>
<details open>
    <summary><b>STEP 2</b></summary>
    <br>
    <h3><b># STEP 2</b></h3>
    <ul>
        <li>Open terminal go to this folder.</li>
               
            python convertData.py dataturk.json downloads pascal
            
            This will fill files in the downloads folder and pascal
            Cut paste downloaded images from downloads folder to pascal/downloads
            
   <li>Convert it to CSV.</li>
   
             python xml_to_csv.py
        
   </ul>
</details>


<details open>
    <summary><b>STEP 3</b></summary>
    <br>
    <h3><b># STEP 3</b></h3>
    <ul>
        <li>Before converting to coco we need to create labels.txt and ids.txt</li>
               
        
                python createids.py
  
            For labels.txt add your own labels in the file.
            
   <li>Note : It is advised to add the labels into the list  in LINE NO. 22 of  ```convertJsontoCOCOformat.py```</li>
   
   <li>The reason is some times text file is not read with next line character so you may face this issue, better add the labels manually</li>
        
   </ul>
</details>
   
<details open>
    <summary><b>STEP 4</b></summary>
    <br>
    <b># STEP 4</b>
    <br>
    <ul><li>Now paste labels.txt and ids.txt into pascal and new filestructure is:</li></ul>
    
    
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
    
</details>

<details open>
    <summary><b>STEP 5</b></summary>
    <br>
    <h3><b># STEP 5</b></h3>
    <ul>
    <li>Now run the main coco convert file.</li>
               
             python convertJsontoCOCOformat.py  --ann_dir pascal --ann_ids pascal/ids.txt --labels pascal/labels.txt --output  mainTrain.json

            
   <li>Now you will get your COCO format json end.</li>
 
        
   </ul>
   <b><h2>Note: if using with Fastai , run the get_annotations functions and print the images</h2></b>
        
        Some images get rejected, so we need to remove that completely.
        Copy the output of images from get_annotation function and paste it as list l in the file removeUselessFilesRejectedbymodel.py
   
</details>

<details>
    <summary><b>EXTRA STEP 6</b></summary>
    <br>
    <h3><b># STEP 6</b></h3>
    <ul>
    <li>So you will run command below if you you dont have fastai locally and will run get_annotations in some different environment like google colab or kaggle kernel</li>
    <li>Run</li>           
        
                python removeUselessFilesRejectedbymodel.py
  
            
   <li>If you have Fastai locally run</li>
                
                cd code
                python getimageslist.py
   
   <li>This gives you a folder untagged, remove that folder from pascal directory and save it somewhere else if you want it else delete the whole folder.</li>
        
   </ul>
</details>

---
## Now we need to repeat Step 3 till step 5 again
---

## Once useless images are removed you need to run STEP 3 Again since Ids are basically filenames
## After that again paste that ids.txt in the pascal folder that is Step 4
## Run Step 5 again


# Finally your Dataset will contain
```
root    
├──pascal
   ├──downloads
       ├──Multiple Images
   ├──Multiple XMLS
   ├──ids.txt
   ├──labels.txt
├──dataturk.json
├──mainout.json
```

# Finally it can be used in Fastai
