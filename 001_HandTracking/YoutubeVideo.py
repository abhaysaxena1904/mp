import pafy
import cv2
# from __future__ import unicode_literals
import youtube_dl
import mediapipe as mp
import time
import HandTrackingModule as htm
from vidgear.gears import CamGear

# url = "https://www.youtube.com/watch?v=6rsFKvq8zwI&ab_channel=warikoo"
url = "https://www.youtube.com/watch?v=Jd4AX3K5TPE&ab_channel=AajTak"
# url = "https://www.youtube.com/shorts/JCztjGKg7Ms"

video = pafy.new(url)
best = video.getbest(preftype="mp4")

options = {"STREAM_RESOLUTION": "240", "CAP_PROP_FRAME_WIDTH":50, "CAP_PROP_FRAME_HEIGHT":30}
stream = CamGear(source=url, stream_mode = True, **options).start() # YouTube Video URL as input


cap = cv2.VideoCapture(best.url)

# pTime = 0
# cTime = 0

detector = htm.handDetector()
while True:
    # success, img = cap.read()
    img = stream.read()

    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img)
    # if len(lmList) != 0:
    #     print(lmList[4])

    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)
    
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)        
    cv2.resizeWindow("Image", 1000, 600)
    cv2.imshow("Image", img)
    cv2.waitKey(1)



# # When everything done, release
# # the video capture object
# cap.release()
# # stream.stop()
# # Closes all the frames
# cv2.destroyAllWindows()