def email_list(domains):
	emails = []

	for domain, users in domains.items():
	  for user in users:
	    emails.append(user + '@' + domain)

	return(emails)