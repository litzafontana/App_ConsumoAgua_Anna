import cv2
import os
import getpass 

#parametros de acesso da camera
USERNAME = getpass.getpass('usuario:')
PASSWORD = getpass.getpass('senha:')
IP = '192.168.100.119'
PORT = '8554'

print ('USERNAME')
#so roda se for ffmpeg
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

#rtsp://admin:96136258@192.168.100.119:8554/profile0
#rtsp://admin:96136258@192.168.100.119:8554/profile0 (como endereço ficaria)
URL = 'rtsp://{}:{}@{}:{}/profile0'.format(USERNAME, PASSWORD, IP, PORT)
print('Conectando com: ' + URL)

cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Sem frame")
        break
    else:

       
        cv2.imshow('VIDEO', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # window, só fecha se apertar "q" no teclado
        break

cap.release()
cv2.destroyAllWindows()    
    
  
