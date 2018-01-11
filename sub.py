import subprocess
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content
from sendgrid.helpers.mail import Personalization, Attachment

files = {'sublime_text_3':'/home/hari/Downloads',
		 'slack-desktop-3.0.2-amd64.deb':'/home/hari/Downloads',
		 'Ubuntu_Free_Culture_Showcase':'/usr/share/example-content',	
		 'a.py':'/home/hari/Desktop',
		 'w.py':'/home/hari/Desktop'}

allfiles = ''

for i in files:
	
	p = subprocess.Popen('du -sh "%s" "%s" ' % (i, files.get(i)), stdout=subprocess.PIPE, shell=True, cwd = files.get(i)).stdout.read()
	size = p.split('\t')
	
	text = "file: %s, path: %s and size: %s\n" % (i,files.get(i),size[0])
	allfiles = allfiles + text
	#print size[2],size[1],size[0]
	# print "%s %s %s\n"%(name,path,size)
print (allfiles)

SENDGRID_API_KEY = 'SG.L8kP5GvPRGG6BxUkIyE2QA.mg2AfI2J2BrcbGEavk7A4luUpalwL' +\
                  'DuZ18KOiqwWebw'

SENDGRID_FROM_MAIL = 'noreply@google.com'
SENDGRID_ID = 'hari'

def send_mail(subject, content, email_list_to, email_list_cc=[],
              email_list_bcc=[], attachment=None):
    email_to = set(email_list_to)
    email_cc = set(email_list_cc)
    email_bcc = set(email_list_bcc)
    mail = Mail()
    mail.from_email = Email(SENDGRID_FROM_MAIL, SENDGRID_ID)

    if not (subject and content):
        return False
    if attachment:
        mail.add_attachment(attachment)
    if subject:
        mail.subject = subject
    if content:
        mail.add_content(Content("text/html", content))
    personalization = Personalization()

    if email_to:
        for email in email_to:
            personalization.add_to(Email(email))

    if email_cc:
        email_cc = email_cc - email_to
        for email in email_cc:
            personalization.add_cc(Email(email))

    if email_bcc:
        email_bcc = email_bcc - email_to
        email_bcc = email_bcc - email_cc
        for email in email_bcc:
            personalization.add_cc(Email(email))
    mail.add_personalization(personalization)

    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code == 202:
        return True
    else:
        return False       

print send_mail('du notification', allfiles, ['hari.kumar@smartron.com'])
