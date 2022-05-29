import pygame
import os
from sys_info import white

img_dir = "./images"

def load_image(path, transparency = white):
    """Formats images for Pygame.  Returns the formatted image."""
    image = pygame.image.load(path)
    image.set_colorkey(transparency)
    image.convert_alpha()
    return image

def create_dict(directory):
    """Adds image from specified directory to a dictionary.  
    Key is the image name.  Returns a dict"""
    dictionary = dict()
    for image_name in os.listdir(directory):
        image_path = os.path.join(directory, image_name)
        dictionary[image_name.split(".")[0]] = load_image(image_path)
    return dictionary

class Image_Collection():
    """Given an image directory, loads images and generates a dictionary."""
    def __init__(self, img_dir):
        self._img_dir = img_dir
        
    def load_directory(self):
        self._images = create_dict(self._img_dir)
        print("Image directory created")

    def get_img(self, name):
        return self._images[name]
    
assets = Image_Collection(img_dir)