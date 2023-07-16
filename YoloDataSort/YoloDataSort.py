from csv import excel_tab
from gc import is_finalized
import os
import glob
import pathlib
import shutil
import sys

dir_for_yolo_sorted_data = os.getcwd()+"\\"+"YoloReadyToTrain"

def create_custom_yaml_file():
    if not os.path.isfile(dir_for_yolo_sorted_data+"/"+"custom.yaml"):
        with open(dir_for_yolo_sorted_data+"/"+"custom.yaml","w") as file:
            file.write("train: " + dir_for_yolo_sorted_data+"\\images\\train" + "\n")
            file.write("val: " +dir_for_yolo_sorted_data+"\\images\\val" + "\n")
            file.write("test: " +dir_for_yolo_sorted_data+"\\images\\test" + "\n")
            file.write("#Classes\n")
            file.write("nc: 1 #number of classes\n")
            file.write("#Classes names\n")
            file.write("names: ['your_class']\n")

def create_folders_if_not_exits(PATH):
    if os.path.exists(PATH):
        return True
    else:
        try:
            os.mkdir(PATH)
        except:
            print("Cannot create a folder!")
            exit(1)
        return create_folders_if_not_exits(PATH)

def check_if_dirs_exist():
    current_path = os.getcwd()
    create_folders_if_not_exits(dir_for_yolo_sorted_data)

    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/images")
    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/images/train")
    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/images/val")
    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/images/test")

    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/labels")
    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/labels/train")
    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/labels/val")
    create_folders_if_not_exits(dir_for_yolo_sorted_data+"/labels/test")

    return [current_path+"/YoloReadyToTrain/images/train"
            ,current_path+"/YoloReadyToTrain/images/val"
            ,current_path+"/YoloReadyToTrain/images/test"]

def get_numbers_of_data_from_dataset(PATH):
    img_extensions = ["*.jpg","*.jpeg","*.png"]
    img_files = []

    for extension in img_extensions:
        img_files.extend(glob.glob(os.path.join(PATH,extension)))
    return len(img_files)

def automatically_give_img_away(train_images:int,test_images:int,valid_images:int,num_elemetns_in_file:int)->list:
    if (valid_images+num_elemetns_in_file)>train_images:
        train_images += num_elemetns_in_file // 4
        num_elemetns_in_file -= num_elemetns_in_file // 4

        valid_images += num_elemetns_in_file // 2
        num_elemetns_in_file -= num_elemetns_in_file // 2

        test_images += num_elemetns_in_file

        return [int(train_images), int(test_images), int(valid_images)]
        #idk but need some logic    
    if (valid_images + num_elemetns_in_file) < (train_images+num_elemetns_in_file//2):
        if test_images < valid_images:
            test_images += num_elemetns_in_file // 2
            num_elemetns_in_file -= num_elemetns_in_file // 2
            valid_images += num_elemetns_in_file
            num_elemetns_in_file = 0

        else:
            valid_images += num_elemetns_in_file //2
            num_elemetns_in_file -= num_elemetns_in_file //2
            test_images += num_elemetns_in_file
            num_elemetns_in_file = 0

        #same but swap valid_images -> train_images

    if valid_images > train_images:
        if (train_images+num_elemetns_in_file)>valid_images:
            valid_images += num_elemetns_in_file // 4
            num_elemetns_in_file -= num_elemetns_in_file // 4

            train_images += num_elemetns_in_file // 4
            num_elemetns_in_file -= num_elemetns_in_file // 2

            test_images += num_elemetns_in_file

            return [int(train_images), int(test_images), int(valid_images)]

        #idk but need some logic
        if (train_images + num_elemetns_in_file) < (valid_images+num_elemetns_in_file//2):
            if test_images < train_images:
                test_images += num_elemetns_in_file // 2
                num_elemetns_in_file -= num_elemetns_in_file // 2
                train_images += num_elemetns_in_file
                num_elemetns_in_file = 0
            else:
                train_images += num_elemetns_in_file //2
                num_elemetns_in_file -= num_elemetns_in_file //2
                test_images += num_elemetns_in_file
                num_elemetns_in_file = 0

    return [int(train_images), int(test_images), int(valid_images)]

def choose(inp:int,src_path:str):
    num_elements_in_file = get_numbers_of_data_from_dataset(src_path)
    const_neif = num_elements_in_file
    if inp == 0:
        train_images = num_elements_in_file//2
        num_elements_in_file -= num_elements_in_file//2

        test_images = num_elements_in_file//4
        num_elements_in_file -=num_elements_in_file//4

        valid_images = num_elements_in_file
        num_elements_in_file =0
        var_list = [train_images,test_images,valid_images]
    if inp == 1:
        valid_images = num_elements_in_file//2
        num_elements_in_file -= num_elements_in_file//2

        test_images = num_elements_in_file//4
        num_elements_in_file -= num_elements_in_file//4

        train_images = num_elements_in_file
        num_elements_in_file =0
        var_list = [train_images,test_images,valid_images]

    if inp == 2:
        print(f"Number of images->{num_elements_in_file}")
        train_images = int(input("> Type number for train images "))

        num_elements_in_file = num_elements_in_file - train_images
        print(f"Number of images remain->{num_elements_in_file}")

        test_images = int(input("> Type number for test images "))

        num_elements_in_file = num_elements_in_file - test_images
        print(f"Number of images remain->{num_elements_in_file}")

        valid_images = int(input("> Type number for valid images "))
        num_elements_in_file = num_elements_in_file - valid_images

        if (valid_images+test_images+train_images) > const_neif:
            print("u type more then remain all of remaining imges will go to valid folder")
            valid_images = num_elements_in_file
            num_elements_in_file = num_elements_in_file - valid_images
            var_list = [train_images,test_images,valid_images]
        if (valid_images+test_images+train_images) < const_neif:
            print(f"u have free images to give away {num_elements_in_file} do you want to automatically give them away(0)? or leave them(1)")
            inp = int(input("> "))
            if inp == 1:
                pass
            if inp == 0:
                var_list = automatically_give_img_away(train_images,test_images,valid_images,num_elements_in_file)
    return var_list

def move_random_file_to_dataset_dir(src_path,dst_path,list_of_data_amount):
    loda = list_of_data_amount
    for x in range((loda[0] + loda[1] + loda[2])):
        for a in range(loda[0]):
            try:
                random_file = next(os.scandir(src_path))
                file_extension = pathlib.Path(random_file.name).suffix
                shutil.move(src_path+"/"+random_file.name,dst_path[0]+'/'+str(a)+file_extension)
            except StopIteration:
                break;
        for b in range(loda[1]):
            try:
                random_file = next(os.scandir(src_path))
                file_extension = pathlib.Path(random_file.name).suffix
                shutil.move(src_path+"/"+random_file.name,dst_path[1]+'/'+str(b)+file_extension)
            except StopIteration:
                break;
        for c in range(loda[2]):
            try:
                random_file = next(os.scandir(src_path))
                file_extension = pathlib.Path(random_file.name).suffix
                shutil.move(src_path+"/"+random_file.name,dst_path[2]+'/'+str(c)+file_extension)
            except StopIteration:
                break;



print("I:train|T:test|V:valid")

print("how mutch images u want to have in Train\Test\Valid folders ")
print("0-(I:50%/T:25%/V:25%)")
print("1-(I:25%/T:25%/V:50%)")
print("2-Custom")

inp = int(input("> u can pick preset or type custom numbers "))

list_of_data_amount= choose(inp,sys.argv[1])
print(list_of_data_amount[0]+list_of_data_amount[1]+list_of_data_amount[2])
print(f"I:{list_of_data_amount[0]},T:{list_of_data_amount[1]},V:{list_of_data_amount[2]}")

list_of_created_dirs = check_if_dirs_exist()
move_random_file_to_dataset_dir(sys.argv[1],list_of_created_dirs,list_of_data_amount)
create_custom_yaml_file()