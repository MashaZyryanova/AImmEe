import firedrone.client as fdc
from firedrone.client.errors import FireDroneClientHttpError
import os
import tensorflow as tf
import numpy as np
import cv2
import json

RETRAINED_LABELS_TXT_FILE_LOC = os.getcwd() + "/" + "retrained_labels.txt"
RETRAINED_GRAPH_PB_FILE_LOC = os.getcwd() + "/" + "retrained_graph.pb"
DATA_DIR = os.getcwd() + "/drone"

workspace = fdc.Workspace('7#ogORpZ1j9CRAT$-AYVoG4SgVXnkjf&rC6Xg2kADk^ece-_gM9X5bp1HXA%%C!S' )
runId = ''
classifications = ['fire','nofire']

# Move left once to get MOVE_RESULT in order to start the loop
move_result = workspace.directrun_move_left(runId)
# move drone to the bottom left corner
move_result['success']=True
while move_result['success']:
    move_result = workspace.directrun_move_left(runId)
# ___________________________________________________________
#  Drone at the bottom left corner. Ready to start work
row=0
move_result['success']=True

# load the graph from file
with tf.gfile.FastGFile(RETRAINED_GRAPH_PB_FILE_LOC, 'rb') as retrainedGraphFile:
    # instantiate a GraphDef object
    graphDef = tf.GraphDef()
    # read in retrained graph into the GraphDef object
    graphDef.ParseFromString(retrainedGraphFile.read())
    # import the graph into the current default Graph, note that we don't need to be concerned with the return value
    _ = tf.import_graph_def(graphDef, name='')
results=[]
run = True
dirOdd = 1
dirEven = 2
#start the main loop
#while the run is in process, the drone keeps moving, takes pictures, and processes them

while(run):
    # Get FOV and start the move to the right
    DATA_DIR = os.getcwd() + "/drone%d" %dirOdd
    print(DATA_DIR)
    count = 0
    frame = workspace.get_drone_fov_image(runId)
    with open('./drone%d/frame%d_%d.jpg' %(dirOdd,row, count), 'wb') as f:
        f.write(frame)

 #----------------------------------------------------------------------
    # 1. Move all the way right. Collect data in folders with odd numbers
    
    move_result['success']=True
    while move_result['success']:
        move_result = workspace.directrun_move_right(runId)
        count+=1
        frame = workspace.get_drone_fov_image(runId)
        with open('./drone%d/frame%d_%d.jpg' %(dirOdd,row,count), 'wb') as f:
            f.write(frame)
    
    with tf.Session() as sess:
        for fileName in os.listdir(DATA_DIR):
            print(fileName)
            # get the file name and full path of the current image file
            imageFileWithPath = os.path.join(DATA_DIR, fileName)
            # attempt to open the image with OpenCV
            openCVImage = cv2.imread(imageFileWithPath)


            # get the final tensor from the graph
            finalTensor = sess.graph.get_tensor_by_name('final_result:0')

            # convert the OpenCV image (numpy array) to a TensorFlow image
            tfImage = np.array(openCVImage)[:, :, 0:3]
            
            # run the network to get the predictions
            predictions = sess.run(finalTensor, {'DecodeJpeg:0': tfImage})

            # sort predictions from most confidence to least confidence
            sortedPredictions = predictions[0].argsort()[-len(predictions[0]):][::-1]

            print("---------------------------------------")
            onMostLikelyPrediction = True
            # for each prediction . . .
            for prediction in sortedPredictions:
                

                
                strClassification = classifications[prediction]

                # get confidence, then get confidence rounded to 2 places after the decimal
                confidence = predictions[0][prediction]

                # if we're on the first (most likely) prediction, state what the object appears to be and show a % confidence to two decimal places
                if onMostLikelyPrediction:
                    if(strClassification=='fire'):
                        print('need to score')
                        score_result = workspace.directrun_score(runId, True)
                        print(score_result)
                    #save prediction into json file:prediction 0 maps to fire , prediction 1 maps to no fire
                    print("<<<<<<<<<<<<<<<<<<<<<<<")
                    print("The orediction is =")
                    print(prediction)
                    results.append(prediction)
                    print(results)
                    scoreAsAPercent = confidence * 100.0
                    
                    print( strClassification + " detected, " + "{0:.2f}".format(scoreAsAPercent) + "% confidence")
                    
                    onMostLikelyPrediction = False
                
                
                print(strClassification + " (" +  "{0:.5f}".format(confidence) + ")")
    dirOdd = dirOdd +2    
 #-------------------------------------------------------------------------
    #Move up to the next row # Increment row count #Get FOV
    row+=1
    count = 0
    move_result = workspace.directrun_move_up(runId)
    #if can't move up anymore, end the run
    if(move_result['success']== False):
        run = False
        #if can't move up anymore, write data to a file and exit
        results =np.array(results).tolist()
        json_string=json.dumps(results)
        print("writing data to file. Drone on the left")
        with open('data.json', 'w') as json_file:
            json.dump(json_string, json_file)
        workspace.directrun_end(runId)
    else:
        
        #else continue
        DATA_DIR = os.getcwd() + "/drone%d" %dirEven
        frame = workspace.get_drone_fov_image(runId)
        with open('./drone%d/frame%d_%d.jpg' %(dirEven,row,count), 'wb') as f:
            f.write(frame)

        #----------------------------------------------------------------    
        # Move all the way left on a new row
        move_result['success']=True
        while move_result['success']:
            move_result = workspace.directrun_move_left(runId)

            count+=1
            
            frame = workspace.get_drone_fov_image(runId)
            with open('./drone%d/frame%d_%d.jpg' %(dirEven,row,count), 'wb') as f:
                f.write(frame)
        with tf.Session() as sess:
        # for each file in the test images directory . . .
            for fileName in os.listdir(DATA_DIR):
                


                # get the file name and full path of the current image file
                imageFileWithPath = os.path.join(DATA_DIR, fileName)
                # attempt to open the image with OpenCV
                openCVImage = cv2.imread(imageFileWithPath)


                # get the final tensor from the graph
                finalTensor = sess.graph.get_tensor_by_name('final_result:0')

                # convert the OpenCV image (numpy array) to a TensorFlow image
                tfImage = np.array(openCVImage)[:, :, 0:3]
                
                # run the network to get the predictions
                predictions = sess.run(finalTensor, {'DecodeJpeg:0': tfImage})

                # sort predictions from most confidence to least confidence
                sortedPredictions = predictions[0].argsort()[-len(predictions[0]):][::-1]

                
                onMostLikelyPrediction = True
                # for each prediction . . .
                for prediction in sortedPredictions:
                    strClassification = classifications[prediction]
                    print(strClassification)
                    
                    

                    # get confidence, then get confidence rounded to 2 places after the decimal
                    confidence = predictions[0][prediction]

                    # if we're on the first (most likely) prediction, state what the object appears to be and show a % confidence to two decimal places
                    if onMostLikelyPrediction:
                        if(strClassification=='fire'):
                            print('need to score')
                            score_result = workspace.directrun_score(runId, True)
                            print(score_result)
                        #append prediction result to results list so it could be send to the server
                        results.append(prediction)
                        print(results)
                        # get the score as a %
                        scoreAsAPercent = confidence * 100.0
                        # show the result to std out
                        print("OBJECT IS " + strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence")
                        # write the result on the image
                        #writeResultOnImage(openCVImage, strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence")
                        # finally we can show the OpenCV image
                        #cv2.imshow(fileName, openCVImage)
                        # mark that we've show the most likely prediction at this point so the additional information in
                        # this if statement does not show again for this image
                        onMostLikelyPrediction = False
                print("---------------------------------------")
        dirEven +=2
        #------------------------------------------------------------


        move_result = workspace.directrun_move_up(runId)
        if(move_result['success'] == False):
            run = False
            results =np.array(results).tolist()
            json_string=json.dumps(results)
            print("writing data to a file. Drone on the right")
            with open('data.json', 'w') as json_file:
                json.dump(json_string, json_file)
            workspace.directrun_end(runId)
        else:
            row+=1
            print("@@@@@@@@@@@@@@@")
            print(len(results))





   
    
    


