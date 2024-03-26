import requests
from bs4 import BeautifulSoup

#create function to scrape the heights of teams
#can call it multiple times for other teams
def scrape_heights(url):
  page = requests.get(url) #make the request to the server
  page.status_code #check status code| status code of 200 mean request is successful
  heights = [] #create list
  if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')

    height_tags = soup.find_all('td', class_= 'height') #find the tags = td and class = height

    for height_tag in height_tags:
      feet = float(height_tag.get_text()[0]) #gets only the feet
      inches = float(height_tag.get_text()[2:]) #gets only the inches
      height_in_inches = feet * 12 + inches #changes feet&inches to inches
      #another way is heights.append(float(height_tag.get_text()[0]) * 12 + float(height_tag.get_text()[2:]))

      heights.append(height_in_inches) #adds each height in inches to the end of the list

    return heights

#scraping heights for men's swimming team
url = "https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster"
scrape_heights(url)
#average the heights
avg_height_mst = sum(scrape_heights(url)) / len(scrape_heights(url))
print(f"Average height of Baruch Men's Swimming Team: {avg_height_mst:.2f} inches") #formated to 2 decimal places

#scraping heights of men's volleyball team
url = "https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster"
scrape_heights(url)
#average the heights
avg_height_mvt = sum(scrape_heights(url)) / len(scrape_heights(url))
print(f"Average height of Baruch Men's Volleyball Team: {avg_height_mvt:.2f} inches")

#scraping heights of women's swimming team
url = "https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster"
scrape_heights(url)
#average the heights
avg_height_wst = sum(scrape_heights(url)) / len(scrape_heights(url))
print(f"Average height of Baruch Women's Swimming Team: {avg_height_wst:.2f} inches")

#scraping heights of women's volleyball team
url = "https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster"
scrape_heights(url)
#average the heights
avg_height_wvt = sum(scrape_heights(url)) / len(scrape_heights(url))
print(f"Average height of Baruch Women's Volleyball Team: {avg_height_wvt:.2f} inches")

#find the average of both men and women's swim teams
avg_height_swim = (avg_height_mst+avg_height_wst)/2
print(f"Average height of both swim teams: {avg_height_swim:.2f} inches")

#find the average of both men and women's volleyball teams
avg_height_volley = (avg_height_mvt+avg_height_wvt)/2
print(f"Average height of both volleyball teams: {avg_height_volley:.2f} inches")
