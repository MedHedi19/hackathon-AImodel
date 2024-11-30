import requests
import base64

def postImg(): 
    
    imagePath = "testing.png"
    imageFile = open(imagePath, "rb")

    imageBytes = base64.b64encode(imageFile.read())

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