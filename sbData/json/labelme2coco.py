# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "E:/paper_exm/labelme/sbData/json/object1"

# set path for coco json to be saved
save_json_path = "E:/paper_exm/labelme/sbData/json/coco/coco.json"

# convert labelme annotations to coco
labelme2coco(labelme_folder, save_json_path)
