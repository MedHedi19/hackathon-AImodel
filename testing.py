import classify
import os

def extractType(result):
  maxType = None
  maxValue = 0
  for key in result:
    if result[key] > maxValue:
      maxType = key
      maxValue = result[key]
  return maxType

imagesFolder = "test-images"

images = os.listdir(imagesFolder)

for image in images:
  imageName, imageExtension = os.path.splitext(image)
  imagePath = os.path.join(imagesFolder, image)
  result = classify.analyse(imagePath)
  type = extractType(result)
  print(imageName + imageExtension + " is probably " + type + " with a confidence of " + str(result[type] * 100) + "%")
