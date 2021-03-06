from emailer import send_email
from database import populate
from comparer import compare
from spreadsheet import get_sheet_data
import data_wrapper

def main():
    get_sheet_data()
    populate()
    assignments = compare()

    for email in assignments:
        # can also add the name of the person in the hello statement later
        msg = "Hello! Here are some issues from Github projects that require your attention!\n"
        subject = "BitFix - Personalized Github Issues for the Day!"
        issues = assignments[email]
        
        # if any issues assigned to the user, send it to them
        if len(issues) > 0:
            for issue in issues:
                msg = msg + "- " + issue + "\n"
        # else send sorry message that we couldn't find anything of relevance
        else:
            subject = "BitFix - No new issues today :("
            msg = "Sorry! We couldn't find any new issues for you today!\n"
        
        ######################### DO NOT UNCOMMENT THE NEXT LINE!!!!!!!! ##########################
        ######## We have to make sure we don't actually send the users an email by accident #######
        # send_email(subject, msg, email)
        
    # send_email(subject, msg, data_wrapper.get_email())

if __name__ == '__main__':
    main()