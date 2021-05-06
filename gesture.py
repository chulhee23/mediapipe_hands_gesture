def recognizeHandGesture(landmarks):
    thumbState = 'UNKNOWN'
    indexFingerState = 'UNKNOWN'
    middleFingerState = 'UNKNOWN'
    ringFingerState = 'UNKNOWN'
    littleFingerState = 'UNKNOWN'
    gesture = 0

    pseudoFixKeyPoint = landmarks[2]['x']
    if (landmarks[3]['x'] < pseudoFixKeyPoint and landmarks[4]['x'] < landmarks[3]['x']):
        thumbState = 'OPEN'
    elif (pseudoFixKeyPoint < landmarks[3]['x'] and landmarks[3]['x'] < landmarks[4]['x']):
        thumbState = 'CLOSE'    

    pseudoFixKeyPoint = landmarks[6]['y']
    if (landmarks[7]['y'] < pseudoFixKeyPoint and landmarks[8]['y'] < landmarks[7]['y']):
        indexFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[7]['y'] and landmarks[7]['y'] < landmarks[8]['y']):
        indexFingerState = 'CLOSE'    

    pseudoFixKeyPoint = landmarks[10]['y']
    if (landmarks[11]['y'] < pseudoFixKeyPoint and landmarks[12]['y'] < landmarks[11]['y']):
        middleFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[11]['y'] and landmarks[11]['y'] < landmarks[12]['y']):
        middleFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[14]['y']
    if (landmarks[15]['y'] < pseudoFixKeyPoint and landmarks[16]['y'] < landmarks[15]['y']):
        ringFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[15]['y'] and landmarks[15]['y'] < landmarks[16]['y']):
        ringFingerState = 'CLOSE'
    
    pseudoFixKeyPoint = landmarks[18]['y']
    if (landmarks[19]['y'] < pseudoFixKeyPoint and landmarks[20]['y'] < landmarks[19]['y']):
        littleFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[19]['y'] and landmarks[19]['y'] < landmarks[20]['y']):
        littleFingerState = 'CLOSE'
        
    fingers = [thumbState, indexFingerState, middleFingerState, ringFingerState, littleFingerState]
    openedFingers = list(filter(lambda x: x == "OPEN", fingers))

    if len(openedFingers) == 1:
        gesture = 1
    elif len(openedFingers) == 2:
        gesture = 2
    elif len(openedFingers) == 3:
        gesture = 3
    elif len(openedFingers) == 4:
        gesture = 4
    elif len(openedFingers) == 5:
        gesture = 5
    
    return gesture

def getStructuredLandmarks(landmarks):
    coordinates = []
    for j in range(42):
        if( j % 2 == 1):
            coordinates.append({ 'x': landmarks[j - 1], 'y': landmarks[j] })
    return coordinates