from gmail_api_wrapper.crud.write import GmailAPIWriteWrapper

class Test:
    def set_store(self, yeet):
        print(vars(yeet))
        return 'lol'

    invalid = 'beast'

class EmailClass:
    def from_json(self):
        return Test()

def send_email():

    api = GmailAPIWriteWrapper()

    body = """
           # body of the email goes here. And send them a link based on their email account using the comaparer file
           """

    # get email from comparer here
    emails = "projectbitfix@gmail.com" 

    # compose new mail
    api.compose_mail(subject='Your Daily BitFix Project Issues!', body=body, to=emails)


send_email()