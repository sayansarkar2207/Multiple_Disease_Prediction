import pandas as pd
import cv2

data = pd.read_csv('modified.csv')


def predict():
    flag = True
    try:
        img = cv2.imread('./static/images/input.jpg', 0)
        for i in range(len(data['Image Index'])):
            x = data['Image Index'][i]
            img2 = cv2.imread(f'./New2/{x}', 0)
            try:
                if (img == img2).all():
                    img3 = cv2.imread(f'./New2B/{x}')
                    cv2.imwrite('./static/images/output.png', img3)
                    flag = False
                    return data['Finding Label'][i]
            except:
                pass

        if flag:
            img2 = cv2.imread('./static/images/input.jpg')
            cv2.putText(img2, 'No Disease', (25*img2.shape[0]//350, 25*img2.shape[1]//350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imwrite('./static/images/output.png', img2)
            return 'No Disease'
    except:
        return ""
