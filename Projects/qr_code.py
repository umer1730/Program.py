import qrcode
upi_id = input("Enter your UPI ID = ")
    #{pn} means recipent ka name            {am} means how many amount you enter  {tn} message box after payment
#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#{pa} means ye wo Upi id ha jis me hme payment krni ha       {cu}means which currency you enetr

#Defining the payment url based on the upi id and the payment app
#You can modify these url's based on the payment apps you want to support

#(you can add amount etc )   upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am=100&cu=INR&tn=Thanks%20for%20your%20support"

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"      # mc = merchant code
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

phonepe_qr = qrcode.make(phonepe_url)                # this line creates a qr code image from the upi link
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save  the qr code to image file (optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")               # Saves the QR code image to a file so you can share or print it.
google_pay_qr.save("google_pay_qr.png")

phonepe_qr.show()
paytm_qr.show()             # Opens the QR image in your system’s image viewer.
google_pay_qr.show()