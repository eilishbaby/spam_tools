import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/mailgun.system-information-report.online/messages",
		auth=("api", "key-2c51ec26596ea60f5baeb974669d4c18"),
		data={"from": "mail@mailgun.system-information-report.online",
			"to": "unadillafire@windstream.net",
			"subject": "Update",
			"template": "mailing"
		})

send_simple_message()
