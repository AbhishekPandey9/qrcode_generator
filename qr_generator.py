import qrcode
qr = qrcode.QRCode(
    version = 15,   # 15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10,  # size of the box where qr code will be displayed
    border = 5      # it is the white part of image -- border in all 4 sides with white color
)

data1= " https://www.linkedin.com/in/abhishek-pandey-060a7528a/ " \

data2 = " https://github.com/AbhishekPandey9 " \

data3 = "Abhishek created this Qr-Code-Generation Project using Python Programming Language. " \
"This project is used to generate QR code for any link or text." \
" You can use this project to generate QR code for your website, social media profiles, or any other link. " \
"This project is very easy to use and you can generate QR code in just a few seconds. " \
"You can also customize the color of the QR code and the background color." \



# as I have given the path of my linkdin & github  profile same way you can give anything
# if you don't want to redirect and create for normal text then  write text in the quotes

qr.add_data(data1)
qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "white")
img.save("QR-Generated.png")

qr.add_data(data2)
qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "white")
img.save("QR-Generated.png")

qr.add_data(data3)
qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "white")
img.save("QR-Generated.png")