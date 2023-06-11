import datetime

import cv2
import os

labels_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 10: "K", 11: "L", 12: "M",
               13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
               20: "U", 21: "V", 22: "W", 23: "X", 24: "Y",25:"_",26:"."}

current_letter = input('What letter do you want to Record?\n').upper()
current_dir = list(labels_dict.keys())[list(labels_dict.values()).index(current_letter)]
path = os.path.join('data',f'{current_dir}')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to read camera feed")

if not os.path.exists(path):
    os.mkdir(path)

recording = False
frame_counter = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if recording:
        filename = os.path.join(f'{path}',f'{current_dir}_{datetime.datetime.now().strftime("%d%m%Y_%H_%M")}_{frame_counter}.png')
        print(filename)
        cv2.imwrite(filename, frame)
        frame_counter += 1

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('s'):
        recording = not recording
        if recording:
            print('starting recording')
        else:
            print('stopped recording')

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
