
######## Potential further features to add #############
# 1. can also send them a welcome/confirmation email for BitFix
# 2. need to make an email service for project managers as well, maybe about the number of people working on their project?
# 3. can also send a sorry email to someone in the beginning of the day if we found no matches, 
# 	or we can suggest another issue to them outside of their comfort zone and say this is available 
# 	if they want to get out of their comfort zone and give it a try

from emailer import run
from database import populate
from comparer import compare

def main():
	# populate()
	assignments = compare()
	print(assignments) # {volEmail: [project links]}

	subject = "BitFix - Personalized Github Issues for the Day!"

	# can also add the name of the person in the hello statement later
	msg = """Hello!
	Here are some issues from Github projects that require your attention!

	"""



	# consolidate all the emails you need to send the email to
	# emails = []
	# run(subject, msg, emails)
	# print(msg)

if __name__ == '__main__':
    main()