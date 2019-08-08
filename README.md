RUN AND OPERATE DRONE AND GET PREDICTIONS
If you want to retrain the model using your data run retrain.py Create follwoing folders before start: 
-training_images (inside training images create subfolders to hold different classes of data, for example when I trained the model I used two folders named "fire" and "nofire" that contained corresponding images. I had roughly 500 images in each folder 
-test_images

To do a test run, use runTest.py. You will need to insert a valid runId into a variable runID, and create empty folders in the project directory with names (drone1, drone2, drone3, drone4, drone5, drone6, drone7, drone8)

dependencies: tensorflow 1.14

FOR FRONT END USE BUILD FOLDER

npm install -g serve
serve -s build

The last command shown above will serve a static site on the port 5000. Like many of serve’s internal settings, the port can be adjusted using the -l or --listen flags:
