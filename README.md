# BitFix
BitFix is a service that connects open source social good projects that need more hands on deck with volunteers that want to donate their time, skill, and energy to such projects

# Database
- Volunteer Table
- Project Table

# GitHub Reader
- Calls to GitHub API or Webscrapes Issues from Projects

# Comparer
- Compares open Issues with Volunteers to find overlapping interests

# Emailer
- Sends the Issues to Volunteers over email
- Automatically sends email to Volunteers every morning

# Devpost COVID-19 Hackathon Entries Web Scraper
- Grabs all the project submissions to COVID-19 related hackathons, follows their Github link to their repository, and saves the 
  project if it is open-source and has outstanding issues

# Spreadsheet
- Reads spreadsheet containing volunteer and project manager information directly, rather than parsing a downloaded .csv file

# Potential further features to add
- Can also send them a welcome/confirmation email for BitFix
- Need to make an email service for project managers as well, maybe about the number of people working on their project?
- Can also send a sorry email to someone in the beginning of the day if we found no matches, 
  or we can suggest another issue to them outside of their comfort zone and say this is available 
  if they want to get out of their comfort zone and give it a try
- Should trim the name, email, github link, etc. entries. Should also make the names in the proper case-format,
  such as "John Smith" instead of "JoHN SMith" or "JOHN SMITH"
- Have the last question in the form be required, so that if we get an answer for it, all the data in the sheet will be saved