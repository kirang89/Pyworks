#
# Send mail using your gmail account
#

import smtplib
import traceback

sender = "<your gmail id>"
password = "<your gmail password>"
receiver = "<receiver gmail id>"
message = "This is an automated msg sent from Python"

try:
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,message)
except Exception:
    status = traceback.format_exc() 
else:
    status = "Sent mail successfully"
finally:
    print status
    smtp.close()
