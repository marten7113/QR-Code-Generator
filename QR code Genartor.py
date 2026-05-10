#import qr code library
import qrcode 

#make virablue and but in it the url 
data = input("Enter Url: ")

#make qrcode
img = qrcode.make(data)

#show qrcode
img.show()

#the name of qrcode
file_name = input("Enter file name to download (e.g., marten.png): ")

#download qrcode
img.save(file_name)


print(f"Successful! You downloaded your QR as {file_name}")
