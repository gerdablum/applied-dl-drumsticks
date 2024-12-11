import os.path
from xml.dom import minidom
import cv2
import shutil

# this script is adapted from https://github.com/computervisioneng/pose-detection-keypoints-estimation-yolov8/blob/main/CVAT_to_cocoKeypoints.py

# creates labels in coco format: one txt file per image with the same name as the image
# out of a single cvat annotation file with a bounding box and keypoints
# it currently supports only two classes
# when flip flag is set to true, bounding box values are flipped horizontally
def create_labels(out_dir, annotation_filepath, flip=False):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    file = minidom.parse(annotation_filepath)

    images = file.getElementsByTagName('image')

    labels = ["left_stick", "right_stick"]

    for image in images:

        width = int(image.getAttribute('width'))
        height = int(image.getAttribute('height'))
        name = image.getAttribute('name')
        elem = image.getElementsByTagName('polyline')
        bbox = image.getElementsByTagName('box')
        # in some annotation files names are with, in other without .jpg specification
        if name.endswith(('.jpg', '.png', '.jpeg')):
            name = name[:-4]
        if flip:
            name += "_flip"
        label_file = open(os.path.join(out_dir, name + '.txt'), 'w')

        for box in bbox:

            xtl = int(float(box.getAttribute('xtl')))
            ytl = int(float(box.getAttribute('ytl')))
            xbr = int(float(box.getAttribute('xbr')))
            ybr = int(float(box.getAttribute('ybr')))

            label = box.attributes['label'].nodeValue
            curr_label = labels.index(label)
            w = xbr - xtl
            h = ybr - ytl
            if flip:
                # flip the x values
                xtl = width - xbr
                xbr = width - xtl
                # change the label value as well
                curr_label = 1 - curr_label
            
            label_file.write('{} {} {} {} {} '.format(curr_label, str((xtl + (w / 2)) / width), str((ytl + (h / 2)) / height),
                                                    str(w / width), str(h / height)))
    
            for e in elem:
                if e.getAttribute("label") == label:
                    points = e.attributes['points']
                    points = points.value.split(';')
                    for p in points:
                        p = p.split(',')
                        x, y = p
                        # filp horizontally (only x)
                        if (flip):
                            x = width - float(x)
                        # normalize points
                        x = float(x) / width
                        y = float(y) / height
                        # yolov8 can also work without visibility values! maybe this is better in my case
                        #visibility = 2
                        #if e.getAttribute("occluded") == 1:
                            #visibility = 1
                        #label_file.write(f"{x} {y} {visibility} ")
                        label_file.write(f"{x} {y} ")
            label_file.write('\n')
                

# flips all images in input folder horizontally and copies them to specified output folder
def flip_images(source_dir, dest_dir):
    files = os.listdir(source_dir)

    for img in files:
        old_file_path = os.path.join(source_dir, img)
        image = cv2.imread(old_file_path)
        image = cv2.flip(image, 1)
        new_file_path = dest_dir + "/" + img[:-4] + "_flip.jpg"
        cv2.imwrite(new_file_path, image)
        print(f'Copied and flipped "{img}" to "{new_file_path}"')

# copies every xth file, if number =2 every second file, number=3 every third file and so on to a specified location.
# This is usefull if in CVAT not every frame gets annotated (you can specify this in CVAT)
def copy_every_Xth_file(source_dir, dest_dir, number=5):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    files = sorted(os.listdir(source_dir))  # Sorting to maintain order
    
    for i in range(0, len(files), number): 
        file_path = os.path.join(source_dir, files[i])
        destination_path = os.path.join(dest_dir, files[i])
        
        shutil.copy2(file_path, destination_path)
        print(f'Copied "{files[i]}" to "{dest_dir}"')


INPUT_FOLDER = "C:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/data/images/val"
OUTPUT_FOLDER = "C:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/data_preparation/out"
OUTPUT_FOLDER_LABELS = "C:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/data_preparation/out/labels"
ANNOTATIONS = 'c:/Users/alina/Master-Projects/applied-dl/applied-dl-drumsticks/data_preparation/annotations/annotations-val.xml'
#flip_images(INPUT_FOLDER, OUTPUT_FOLDER)
create_labels(OUTPUT_FOLDER_LABELS, ANNOTATIONS, flip=True)
