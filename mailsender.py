from mailersend import emails

mailer = emails.NewEmail(mailersend_api_key='')

# mail_body = 

# mail_from = {
    # "name": "Domain-Guard",
    # "email": "support@atilova.com",
# }

# recipients = [
    # {        
        # "name": "Your Client",
        # "email": "ati2lova3@gmail.com",
    # }
# ]

# mailer.set_mail_from(mail_from, mail_body)
# mailer.set_mail_to(recipients, mail_body)
# mailer.set_subject("Hello!", "Confirm AUTH")
# mailer.set_html_content("This is the HTML content", mail_body)
# mailer.set_plaintext_content("This is the text content", mail_body)
# mailer.set_reply_to(reply_to, mail_body)

# using print() will also return status code and data

print(mailer.send({
    "from": {
      'email': 'noreply@atilova.com',
      'name': 'Domain-Guard'
    },
    'to': [{
        'email': 'ati2lova3@gmail.com',
      }],
    'reply_to': None,
    'subject': 'Confirm email',
    'html': '<p>Please confirm email: <a href="https://atilova.com/">Confirm</a></p>',
}))