
import qrcode
data = "Replace with a link"  #replace with a link
img = qrcode.make(data)
img.save('/Users/anoushkabhat/Downloads/qrcodes/qrcode')
