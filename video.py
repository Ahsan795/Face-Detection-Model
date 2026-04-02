import cv2

option = input("enetr 1 for recording the video:, or enter 2 for reading the video:, or enter 3 for saving/showing the video:")
#cap = cv2.VideoCapture(0)
camera = cv2.VideoCapture(0)
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frane_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codecc = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.mp4", codecc, 20, (frame_width, frane_height))

while True:
   # ret, frame = cap.read()
   success, image = camera.read()

   if not success:
        print("nort found")
        break
   
   # cv2.imshow("webcame video", frame)
   recorder.write(image)
   cv2.imshow("recording live", image)

   if cv2.waitKey(1) & 0xff == ord('q'):
        print("quiting...")
        break

#cap.release()
#cv2.destroyAllWindows()
camera.release()
recorder.release()
