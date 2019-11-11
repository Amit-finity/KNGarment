import msg91_sms as msgsms
msg = msgsms.Cspd_msg91(apikey='303210AOau2yoqQyLI5dc91905')
otp_sms_txt = "Your otp code is ##OTP##"
send_otp_sms_resp = msg.send_otp('TXTIN',919082895309,otp_sms_txt)
print(send_otp_sms_resp)
