import qrcode
try:
    image = str(input("Enter your URL: "))
    qrimg = qrcode.make(image)
    qrimg.save("QR.png", "PNG")
except Exception as e:
    print("please enter a valid input")