import os
import shutil
import random
from PIL import Image

# Function to check if an image is readable
def is_image_readable(image_path):
    try:
        img = Image.open(image_path)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False

# Function to split images
def split_images(input_folder, output_folder, test_percent, validation_percent):
    # Create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_list = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    random.shuffle(image_list)

    total_images = len(image_list)
    test_split = int(total_images * test_percent)
    validation_split = int(total_images * validation_percent)

    train_images = image_list[validation_split + test_split:]
    validation_images = image_list[:validation_split]
    test_images = image_list[validation_split:validation_split + test_split]

    for image in train_images:
        if is_image_readable(os.path.join(input_folder, image)):
            # Save train images in a subfolder with the same name as the input folder
            input_subfolder_name = os.path.basename(input_folder)
            train_subfolder = os.path.join(output_folder, 'train', input_subfolder_name)
            os.makedirs(train_subfolder, exist_ok=True)
            shutil.copy(os.path.join(input_folder, image), os.path.join(train_subfolder, image))
    
    for image in validation_images:
        if is_image_readable(os.path.join(input_folder, image)):
            # Save validation images in a subfolder with the same name as the input folder
            input_subfolder_name = os.path.basename(input_folder)
            validation_subfolder = os.path.join(output_folder, 'validation', input_subfolder_name)
            os.makedirs(validation_subfolder, exist_ok=True)
            shutil.copy(os.path.join(input_folder, image), os.path.join(validation_subfolder, image))
    
    for image in test_images:
        if is_image_readable(os.path.join(input_folder, image)):
            # Save test images in a subfolder with the same name as the input folder
            input_subfolder_name = os.path.basename(input_folder)
            test_subfolder = os.path.join(output_folder, 'test', input_subfolder_name)
            os.makedirs(test_subfolder, exist_ok=True)
            shutil.copy(os.path.join(input_folder, image), os.path.join(test_subfolder, image))


# Input and output folders
input_folder = r'D:\Git Projects\Peppermint-Identification-and-Classification-Model\Data\Tulsi'
output_folder = r'D:\Git Projects\Peppermint-Identification-and-Classification-Model\Identification\Data'
test_percent = 0.15
validation_percent = 0.15

# Split and copy images
split_images(input_folder, output_folder, test_percent, validation_percent)
