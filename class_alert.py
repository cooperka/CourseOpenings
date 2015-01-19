import urllib.request
import smtplib
import re

def email(num):
	server = 'smtp.gmail.com'
	port = 587

	sender = 'YOUR_SENDER_EMAIL@gmail.com'
	pwd = 'YOUR_SENDER_PASSWORD'
	recipient = 'YOUR_PERSONAL_EMAIL@gmail.com'
	subject = 'Class Opening'
	body = 'Class opening: ' + str(num) + ' spot(s)'

	headers = [
		"From: " + sender,
		"Subject: " + subject,
		"To: " + recipient,
		"MIME-Version: 1.0",
		"Content-Type: text/html"
	]
	headers = "\r\n".join(headers)

	session = smtplib.SMTP(server, port)

	session.ehlo()
	session.starttls()
	session.ehlo()
	session.login(sender, pwd)

	session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
	session.quit()

def website():
	# URL no longer works
	base_url = 'http://www.lsa.umich.edu/cg/cg_sections.aspx'
	params = '?content=1960AMCULT219001'

	req = urllib.request.Request(url + params)
	response = urllib.request.urlopen(req)
	html = response.read()

	# Outdated regex
	m = re.search('\s\s\s\s(\d(\d?))\D\D\D\D\s\s\s\s', str(html))
	#print(html)
	#print("Found: ", m.group(1))

	val = int(m.group(1))

	if val >= 1:
		print("Sending email (", val, " spots)...")
		email(val)
		print("Sent.")

website()
