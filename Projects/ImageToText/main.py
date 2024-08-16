import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 11 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("example.png"), config=myconfig)
print(text)

img = cv2.imread("naruto2.jpg")
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img,(int(box[1], height - int(box[2], int(box[3], int(box[4]))))))