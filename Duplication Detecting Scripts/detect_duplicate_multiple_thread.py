import cv2
import numpy as np
import glob
import time
import multiprocessing
import threading



"""
Threading
"""



image_name = 'c2.jpeg' # origional image path goes here
original = cv2.imread(image_name) 



def find_duplicates(image_=''):
        duplicates = ''
        try:
            image_to_compare = cv2.imread(image_)
            if original.shape == image_to_compare.shape:

                difference = cv2.subtract(original, image_to_compare)
                b, g, r = cv2.split(difference)

                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    print(f'Duplicates Found: {image_name} is Duplicate of {image_}')

                    sift = cv2.xfeatures2d.SIFT_create()
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
            pass



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






# import cv2
# import numpy as np
# import glob
# import time
# import multiprocessing
# import threading
# from queue import Queue



# """
# Threading
# """



# image_name = 'c2.jpeg' # origional image path goes here
# original = cv2.imread(image_name) 

# start_time = time.time()



# def filebrowser(ext='', directory=''):
#     """
#     returns files with an extension
#     """
#     return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]






# class DuplicateFinder(threading.Thread):

#     def __init__(self, queue):
#         """Initialize the thread"""
#         threading.Thread.__init__(self)
#         self.queue = queue
    
#     def run(self):
#         """Run the Thread"""
#         while True:
#             image_path = self.queue.get()

#             self.check_duplicate(image_path)

#             # send a signal to the queue that the job is done
#             self.queue.task_done()

    
#     def check_duplicate(self, image_):
#         """Prints Duplicate Image Name"""
#         try:
#             image_to_compare = cv2.imread(image_)
#             if original.shape == image_to_compare.shape:

#                 difference = cv2.subtract(original, image_to_compare)
#                 b, g, r = cv2.split(difference)

#                 if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
#                     print('Duplicate Found')
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

#         except Exception as e:
#             pass

# def main(image_dir):
#     """
#     Run the program
#     """

#     queue = Queue()

#     # create a thread pool and give them a queue
#     for i in range(100): # I don't won't my virtual memory to get bunked up
#         t = DuplicateFinder(queue)
#         t.setDaemon(True)
#         t.start()

#     #give the queue some data | consumer and producer code huh
#     for image_ in image_dir:
#         queue.put(image_)
    
#     # wait for the queue to finish
#     queue.join()

# if __name__ == "__main__":

#     image_dir = filebrowser(ext='.jpeg', directory='') # directory='' ==> search images from current to inner sub-directories
#     image_dir += filebrowser(ext='.jpg', directory='')

#     main(image_dir)



# print("--- %s seconds ---" % (time.time() - start_time))
# print('Program Executed Completely')
