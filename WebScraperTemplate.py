import requests
import bs4 as beautiful_soup

page = requests.get('https://www.includehelp.com/mcq/oops-mcqs.aspx')
soup = beautiful_soup.BeautifulSoup(page.content, 'html.parser')

# SCRAPING QUESTIONS FROM THE WEBPAGE
questions = soup.select("p b")

qbank = []
i = 0
for s in questions:
    i = i + 1
    if i % 3 == 1:
        qbank.append(s.text)

# WRITING THE DATA INSIDE A TEXT FILE
with open('questions.txt', 'w') as f:
    for i in range(0, 100):
        f.write(qbank[i])
        f.write("\n")

# SCRAPING EXPLANATIONS FROM THE WEBSITE
explanations = soup.select("p")
ebank = []

s = ""
for i in range(0, 504):
    s = explanations[i].text
    if s.__contains__("Explanation:"):
        ebank.append(explanations[i + 1])

# AGAIN WRITING THE DATA INSIDE A TEXT FILE
with open('explanations.txt', 'w') as f:
    for i in range(0, 100):
        f.write(ebank[i].text)
        f.write("\n")
