# Team Heights
# Objective
This project aims to provide a data-driven solution to determine whether CUNY Baruch varsity swimmers are taller on average than their volleyball counterparts. The solution involves web scraping to collect height data from men's and women's swimming and volleyball teams, followed by analysis to calculate average heights and draw conclusions.

# Methodology
To accomplish this task, I utilized web scraping techniques to gather height data from CUNY Baruch's swimming and volleyball rosters. The following steps outline the process:

**Web Scraping**: I employed Python's requests library for making HTTP requests and BeautifulSoup from bs4 to extract data from web pages.

**Function Creation**: To streamline the scraping process, I created a function to scrape height data from each team's roster page. 

**Data Extraction**: The scraping function retrieves height data by identifying specific HTML tags and classes associated with height information on the web pages.

**Calculation**: After scraping heights from each team's roster, I calculated the average height for both men's and women's swimming and volleyball teams.

**Analysis**: By comparing the average heights of Baruch's swimming and volleyball teams, I determined whether one group tends to be taller than the other.

# Results
Based on the collected data and analysis, the following conclusions were drawn:

**Men's Teams**: The men's volleyball team has an average height of 72.25 inches, while the men's swimming team has an average height of 70.74 inches. The men's volleyball team is, on average, taller than the men's swimming team by 1.51 inches.

**Women's Teams**: The women's volleyball team has an average height of 67.25 inches, whereas the women's swimming team has an average height of 64.33 inches. The women's volleyball team is, on average, taller than the women's swimming team by 2.92 inches.

**Overall Comparison**: When comparing the average heights of all players, regardless of gender, the volleyball players have an average height of 69.75 inches, whereas the swimmers have an average height of 67.5 inches. The volleyball players, on average, are taller than the swimmers by 2.25 inches.
# Conclusion
The analysis reveals that, on average, Baruch varsity volleyball players are taller than their swimming counterparts by approximately 2.25 inches. 

# Sources
[Men's Swimming](https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster)
[Men's Volleyball](https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster)
[Women's Swimming](https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster)
[Women's Volleyball](https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster)
