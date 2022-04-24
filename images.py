import pygame
import os

white = (255, 255, 255)

def load_image(path, transparency = white):
    """Formats images for Pygame.  
    Return formatted image."""
    image = pygame.image.load(path)
    image.set_colorkey(transparency)
    image.convert_alpha()
    return image

def create_dict(directory):
    """Adds image from specified directory to a dictionary.  Key generated from image name.
    Return a dict"""
    dictionary = dict()
    for image_name in os.listdir(directory):
        image_path = os.path.join(directory, image_name)
        dictionary[image_name.split(".")[0]] = load_image(image_path)
    return dictionary


class Image_Collection():
    """Given an image directory, loads images and generates a dictionary."""
    def __init__(self, img_dir):
        self._images = create_dict(img_dir)
        print("Image directory created")

    def get_img(self, name):
        return self._images[name]
    
