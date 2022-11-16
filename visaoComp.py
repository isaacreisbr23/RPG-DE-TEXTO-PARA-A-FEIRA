import cv2
import mediapipe as mp
from pynput.keyboard import *
import math


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


kb = Controller()


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.

      continue




    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)





    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    lmList = []
    if results.multi_hand_landmarks:
      myHand = results.multi_hand_landmarks[0]
      for id, lm in enumerate(myHand.landmark):
        h, w, c = image.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        lmList.append([id, cx, cy])          

    # Assigning variables for Thumb and Index finger position
    if len(lmList) != 0:
      x1, y1 = lmList[4][1], lmList[4][2]#dedao
      x2, y2 = lmList[8][1], lmList[8][2]#indicador
      x3, y3 = lmList[5][1], lmList[5][2]#lateral da mao
      x4,y4 = lmList[12][1], lmList[12][2]#ponta do dedio medio
      x5,y5 = lmList[9][1], lmList[9][2]#base do dedio medio
      x6,y6 = lmList[16][1], lmList[16][2]
      x7,y7 = lmList[13][1], lmList[13][2]

      # DEDAO E LATERAL DA MAO
      cv2.circle(image, (x1,y1),15,(255,255,255))  
      cv2.circle(image, (x3,y3),15,(255,255,255))   
      cv2.line(image,(x1,y1),(x3,y3),(255,0,0),3)

      #INDICADOR E BASE
      cv2.circle(image, (x2,y2),15,(255,255,255))  
      cv2.circle(image, (x3,y3),15,(255,255,255))   
      cv2.line(image,(x2,y2),(x3,y3),(255,0,0),3)

      #MEDIO E BASE
      cv2.circle(image, (x4,y4),15,(255,255,255))  
      cv2.circle(image, (x5,y5),15,(255,255,255))   
      cv2.line(image,(x4,y4),(x5,y5),(255,0,0),3)      


      #MEDIO E BASE
      cv2.circle(image, (x6,y6),15,(255,255,255))  
      cv2.circle(image, (x7,y7),15,(255,255,255))   
      cv2.line(image,(x6,y6),(x7,y7),(255,0,0),3) 

      sound_mode = False

      length_sound_mode = math.hypot(x3-x1,y3-y1)

      length_pause_mode = math.hypot(x3-x2,y3-y2)

      length_return_media = math.hypot(x5-x4,y5-y4)

      length_next_media = math.hypot(x7-x6,y7-y6)


      if length_sound_mode < 50:
        cv2.line(image,(x1,y1),(x3,y3),(0,0,0),3)
        if sound_mode == False:
          sound_mode = True

      if length_pause_mode < 40 and sound_mode == False:
        cv2.line(image,(x2,y2),(x3,y3),(0,0,0),3)
        kb.press(Key.media_play_pause)
        kb.release(Key.media_play_pause)


      if length_pause_mode < 40 and sound_mode == True: # ABAIXAR O SOM
        cv2.line(image,(x2,y2),(x3,y3),(0,0,0),3)
        kb.press(Key.media_volume_down)
        kb.release(Key.media_volume_down)

      if length_pause_mode > 60 and sound_mode == True: # AUMENTAR O SOM
        cv2.line(image,(x2,y2),(x3,y3),(255,45,0),3)
        kb.press(Key.media_volume_up)
        kb.release(Key.media_volume_up)  
      
      if length_return_media < 50:
        cv2.line(image,(x4,y4),(x5,y5),(0,0,0),3)
        kb.press(Key.media_previous)
        kb.release(Key.media_previous)

      if length_next_media < 50:
        cv2.line(image,(x6,y6),(x7,y7),(0,0,0),3)
        kb.press(Key.media_next)
        kb.release(Key.media_next)

      #Pos = mp.interp(length, [50, 220], [0, 100])
      #Posgripper= (round(Pos))
      #print(Posgripper)
      #converted_Posgripper = str(Posgripper)
      #cv2.putText(image, str(Posgripper), (50, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0))
      #cv2.line(image, 320, 320, (0,0,0), 2)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()