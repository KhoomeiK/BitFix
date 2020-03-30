from gmail_api_wrapper.crud.write import GmailAPIWriteWrapper

def send_email():

    api = GmailAPIWriteWrapper()

    body = """
           # body of the email goes here. And send them a link based on their email account using the comaparer file
           """

    emails = "paledale11@gmail.com" # get email from comparer here

    # compose new mail
    api.compose_mail(subject='Your Daily BitFix Project Issues!', body=body, to=emails)

send_email()