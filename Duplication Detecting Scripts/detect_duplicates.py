import cv2
import numpy as np
import glob
import time
import multiprocessing
import threading
from os import path

# setting up path
basepath = path.dirname(__file__)

# loading environment
image_path = path.abspath(path.join(basepath, "../images_in", "duplicate.jpg")) # Image we are running these tests against.

"""
Sequentiall on single core
"""

# def filebrowser(ext='', directory=''):
#     """
#     returns files with an extension
#     """
#     return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

# image_dir = filebrowser(ext='.jpeg', directory='') # directory='' ==> search images from current to inner sub-directories
# image_dir += filebrowser(ext='.jpg', directory='')

# ## print(image_dir)


# image_path = 'c2.jpeg' # origional image path goes here
# original = cv2.imread(image_path) 


# start_time = time.time()

# for image_ in image_dir:
#     try:
#         image_to_compare = cv2.imread(image_)
#         if original.shape == image_to_compare.shape:

#             difference = cv2.subtract(original, image_to_compare)
#             b, g, r = cv2.split(difference)

#             if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
#                 print(f'Duplicates Found: {image_path} is Duplicate of {image_}')


#                 sift = cv2.xfeatures2d.SIFT_create()
#                 kp_1, desc_1 = sift.detectAndCompute(original, None)
#                 kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

#                 index_params = dict(algorithm=0, trees=5)
#                 search_params = dict()
#                 flann = cv2.FlannBasedMatcher(index_params, search_params)

#                 matches = flann.knnMatch(desc_1, desc_2, k=2)

#                 good_points = []
#                 for m, n in matches:
#                     if m.distance < 0.6*n.distance:
#                         good_points.append(m)

#                 # Define how similar they are
#                 number_keypoints = 0
#                 if len(kp_1) <= len(kp_2):
#                     number_keypoints = len(kp_1)
#                 else:
#                     number_keypoints = len(kp_2)
#     except Exception as e:
#         pass



# print("--- %s seconds ---" % (time.time() - start_time))
# print('Program Executed Completely')




"""
Multiprocessing
"""


# image_path = 'c2.jpeg' # origional image path goes here
# original = cv2.imread(image_path) 



# def find_duplicates(image_):
#         duplicates = ''
#         try:
#             image_to_compare = cv2.imread(image_)
#             if original.shape == image_to_compare.shape:

#                 difference = cv2.subtract(original, image_to_compare)
#                 b, g, r = cv2.split(difference)

#                 if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
#                     duplicates = image_


#                     sift = cv2.xfeatures2d.SIFT_create()
#                     kp_1, desc_1 = sift.detectAndCompute(original, None)
#                     kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

#                     index_params = dict(algorithm=0, trees=5)
#                     search_params = dict()
#                     flann = cv2.FlannBasedMatcher(index_params, search_params)

#                     matches = flann.knnMatch(desc_1, desc_2, k=2)

#                     good_points = []
#                     for m, n in matches:
#                         if m.distance < 0.6*n.distance:
#                             good_points.append(m)

#                     # Define how similar they are
#                     number_keypoints = 0
#                     if len(kp_1) <= len(kp_2):
#                         number_keypoints = len(kp_1)
#                     else:
#                         number_keypoints = len(kp_2)

#                     return duplicates

#         except Exception as e:
#             pass



# if __name__ == '__main__':
    

#     def filebrowser(ext='', directory=''):
#         """
#         returns files with an extension
#         """
#         return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

#     image_dir = filebrowser(ext='.jpeg', directory='') # directory='' ==> search images from current to inner sub-directories
#     image_dir += filebrowser(ext='.jpg', directory='')
#     ## print(image_dir)
    

#     # # 1) Check if 2 images are equals | parallel on cores
#     start_time = time.time()
#     pool = multiprocessing.Pool() # Equal to number of cores | octa for this pc

    

#     inputs = image_dir
#     outputs_async = pool.map_async(find_duplicates, inputs)
#     print(outputs_async.get())

#     print("--- %s seconds ---" % (time.time() - start_time))
#     print('Program Executed Completely')



"""
Threading
"""

original = cv2.imread(image_path) 



def find_duplicates(image_=''):
        duplicates = ''
        try:
            image_to_compare = cv2.imread(image_)
            if original.shape == image_to_compare.shape:

                difference = cv2.subtract(original, image_to_compare)
                b, g, r = cv2.split(difference)

                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    print(f'Duplicates Found: {image_path} is Duplicate of {image_}')

                    sift = cv2.SIFT_create()
                    kp_1, desc_1 = sift.detectAndCompute(original, None)
                    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

                    index_params = dict(algorithm=0, trees=5)
                    search_params = dict()
                    flann = cv2.FlannBasedMatcher(index_params, search_params)

                    matches = flann.knnMatch(desc_1, desc_2, k=2)

                    good_points = []
                    for m, n in matches:
                        if m.distance < 0.6*n.distance:
                            good_points.append(m)

                    # Define how similar they are
                    number_keypoints = 0
                    if len(kp_1) <= len(kp_2):
                        number_keypoints = len(kp_1)
                    else:
                        number_keypoints = len(kp_2)


        except Exception as e:
            print('[!] {}'.format(e))



if __name__ == '__main__':
    

    def filebrowser(ext='', directory=''):
        """
        returns files with an extension
        """
        return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

    image_dir = filebrowser(ext='.jpeg', directory='') # directory='' ==> search images from current to inner sub-directories
    image_dir += filebrowser(ext='.jpg', directory='')
    


    start_time = time.time()

    for image_ in image_dir:
        t = threading.Thread(target=find_duplicates, args=(image_,))
        t.daemon = False
        t.start()


    print("--- %s seconds ---" % (time.time() - start_time))
    print('Program Executed Completely')
