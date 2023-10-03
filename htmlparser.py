from bs4 import BeautifulSoup
import requests


resp = requests.get("https://leaderboard.lugvitc.org/api/recruitment")

# get the response text. in this case it is HTML
html_content = resp.text



# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element containing the applicant data
table = soup.find('table')

# Initialize a list to store applicant records
applicant_records = []

# Find all rows in the table except the header row
rows = table.find_all('tr')[1:]

# Loop through each row and extract data into a dictionary
for row in rows:
    cols = row.find_all('td')
    applicant = {
        'id': cols[0].text.strip(),
        'name': cols[1].text.strip(),
        'email': cols[2].text.strip(),
        'contact': cols[3].text.strip(),
        'prefDept': cols[4].text.strip(),
        'prefDept2': cols[5].text.strip(),
        'regno': cols[6].text.strip(),
        'whatLinux': cols[7].text.strip(),
        'whyLinux': cols[8].text.strip(),
        'expLinux': cols[9].text.strip(),
        'tech1': cols[10].text.strip(),
        'tech2': cols[11].text.strip(),
        'tech3': cols[12].text.strip(),
        'mang1': cols[13].text.strip(),
        'mang2': cols[14].text.strip(),
        'ops1': cols[15].text.strip(),
        'ops2': cols[16].text.strip(),
        'media1': cols[17].text.strip(),
        'media2': cols[18].text.strip(),
        'content1': cols[19].text.strip(),
        'content2': cols[20].text.strip(),
    }
    applicant_records.append(applicant)

# Print the list of applicant records
for applicant in applicant_records:
    print(applicant)
    break