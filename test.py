import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/mailgun.service-terms-update.online/messages",
		auth=("api", "key-31f940f0ec55b37bf33f9bc390b54e10"),
		data={"from": "mail@mailgun.service-terms-update.online",
			"to": "Tmanor@windstream.net",
			"subject": "Windstream",
			"template": "mailing"
		})

send_simple_message()
