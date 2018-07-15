import sendgrid
import os, sys
from sendgrid.helpers.mail import *

def main(args):
    apikey = args.get("apikey", "no_apikey_provided")
    if apikey == "no_apikey_provided":
        print "No api key provided, exit..."
        sys.exit(1)

    
    sg = sendgrid.SendGridAPIClient(apikey=apikey)
    from_email = Email('cloud_resource_keeper@mattcui.com')
    to_email = Email('cuixuex@cn.ibm.com')
    subject = 'Mail test from sendgrid'
    content = Content('text/plain', 'Sent for test by cloud resource keeper powered by SendGrid')
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

    result={}
    result['to']='cuixuex@cn.ibm.com'
    result['subject']='Mail test from sendgrid'
    result['desc']='Sent for test by cloud resource keeper powered by SendGrid'

    return result
