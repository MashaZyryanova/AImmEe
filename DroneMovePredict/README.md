If you want to retrain the model using your date run retrain.py
Create follwoing folders before start:
-training_images (inside training images create subfolders to hold differenta classes of data, for examples when I trained the model I used to folders named "fire" and "nofire" that contained corresponding images. I had roughly 500 images in each folder
-test_images

The label for each image is taken from the name of the subfolder it's
in.

To do a test run, use runTest.py. You will need to insert a valid runId into a variable runID, and create empty folders in the project directory with names (drone1, drone2, drone3, drone4, drone5, drone6, drone7, drone8)

dependencies:
tensorflow 1.14
