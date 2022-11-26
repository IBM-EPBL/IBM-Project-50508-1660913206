import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from twilio.rest import Client
from playsound import playsound
model = load_model(r'forest1.h5')
video = cv2.VideoCapture(0)
index = ['on fire','without fire']
while (1):
    sucess,frame = video.read()
    cv2.imwrite("image.jpg",frame)
    img = image.load_img('image.jpg',target_size=(64,64))
    x = image.img_to_array(img)
    x= np.expand_dims(x,axis=0)
    pred = model.predict(x)
    y=np.argmax(pred)
    print(pred)
    cv2.putText(frame,"The Forest is  "+str(index[y]),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),4)
    pred =model.predict(x)
    if np.argmax(pred)==1:
        account_sid ='ACae14ded1f366045e31c872cbae23885e'
        auth_token = '35cf6ec131fe14052443805ca1167c79'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body='Forest Fire is detected ,stay alert!',
        from_='+19136754656',
        to='+919789018422') 
        print(message.sid)
        print('Fire detecteed')
        print('SMS sent!')
        playsound(r"C:\Users\HP\OneDrive\Desktop\ibm\scary-siren-air-raid-tornado-nuke-7010.mp3")
    else:
        print('No Danger')
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF == ord('a'): 
        break
video.release()
cv2.destroyAllWindows()
