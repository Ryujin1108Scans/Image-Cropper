from PIL import Image
import os


def crop_image(old_image_path, new_image_path, left=0, right=0, top=0, bottom=0):
    img = Image.open(old_image_path)
    width, height = img.size
    cropped_img = img.crop((left, top, width - right, height - bottom))  # box[left, top, right, bottom]
    cropped_img.save(new_image_path)


def get_images(raw_folder_path, left=0, right=0, top=0, bottom=0):
    new_folder = os.path.join(raw_folder_path, "cropped_images")
    if not os.path.exists(new_folder):
        os.mkdir(path=new_folder)
    image_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    image_files = []
    for root, _, files in os.walk(raw_folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                new_tuple = [os.path.join(root, file), os.path.join(new_folder, file)]
                image_files.append(new_tuple)
    for file, new_file in image_files:
        crop_image(file, new_file, left, right, top, bottom)


folder_path = input("Enter Path to the directory: ")
left_pixel = int(input("Enter pixels to crop from left: "))
right_pixel = int(input("Enter pixels to crop from right: "))
top_pixel = int(input("Enter pixels to crop from top: "))
bottom_pixel = int(input("Enter pixels to crop from bottom: "))
get_images(raw_folder_path=folder_path, left=left_pixel, right=right_pixel, top=top_pixel, bottom=bottom_pixel)
