# *-*coding: utf-8 *-*

import cv2
import numpy as np

import glob
import sys
import multiprocessing



def filebrowser(ext=''):
    """
    returns files with an extension
    """

    target = "**/*.{}".format(ext)
    return [filepath for filepath in glob.iglob(target, recursive = True)] # Recursive from Current Directory


image_name = sys.argv[1] # origional image path goes here
original = cv2.imread(image_name)


def find_duplicates(image_):
        duplicates = ''
        try:
            image_to_compare = cv2.imread(image_)
            if original.shape == image_to_compare.shape:

                difference = cv2.subtract(original, image_to_compare)
                b, g, r = cv2.split(difference)

                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    
                    duplicates = image_

                    return duplicates

        except Exception as e:
            pass




if __name__ == '__main__':

    image_dir = filebrowser(ext='jpeg')
    image_dir += filebrowser(ext='jpg')
    image_dir += filebrowser(ext='png')
    image_dir += filebrowser(ext='gif')

    pool = multiprocessing.Pool()

    inputs = image_dir

    outputs_async = pool.map_async(find_duplicates, inputs)

    duplicates = outputs_async.get()

    for image in duplicates:
        if image is not None:
            print(image)
