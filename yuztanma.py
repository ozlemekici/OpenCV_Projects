import cv2

#Haar cascade classifier yukle
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#kamera okumak icin
video_capture = cv2.VideoCapture(0)

while True:
	ret,frame = video_capture.read() #frame oku
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #siyah-beyaz yap
	faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(100,100)) #yuzleri bul
	for (x,y,w,h) in faces: #yuzleri isaretle
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)
		cv2.putText(frame, "insan", (x,y+h+20), cv2.FONT_HERSHEY_DUPLEX, .5, (0,255,0))

	#esc ile cik
	cv2.imshow('Video', frame)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

video_capture.release()
cv2.destroyAllWindows()
