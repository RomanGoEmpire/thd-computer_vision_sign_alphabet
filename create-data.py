import os
import pickle

import cv2
import mediapipe as mp

DATA_DIR = 'data'
data = []
labels = []

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)

for dir_ in os.listdir(DATA_DIR):
    print(f'starting {dir_}')
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                min_x = min(x_)
                min_y = min(y_)
                max_x = max(x_)
                max_y = max(y_)
                distance_x = max_x - min_x
                distance_y = max_y - min_y

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    new_x = x / distance_x
                    new_y = y / distance_y

                    data_aux.append(new_x)
                    data_aux.append(new_y)

            if len(data_aux) == 42:
                data.append(data_aux)
                labels.append(dir_)

f = open('new_data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
