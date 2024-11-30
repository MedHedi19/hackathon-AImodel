import requests
import cv2
import time
import base64

imagePath = "temp.png"

def postImg():
    print("Opening Camera.")
    cap = cv2.VideoCapture(0)
    time.sleep(2)
    
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(imagePath, frame)
        print("Image Captured!")
    else:
        print("Failed to capture image.")
    
    cap.release()
    
    with open(imagePath, "rb") as imageFile:
        imageBytes = base64.b64encode(imageFile.read())
        print("Sending image to cloud server for analysis.")
        response = requests.post(
            "http://localhost/detect",
            data=imageBytes
        )
    
        print("Response received!")
        response_data = response.json()
        print(response_data)    
            
def main():
    postImg()

if __name__ == '__main__':
    main()