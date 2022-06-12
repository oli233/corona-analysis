import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import DataDriver.DataDrive as DataDrive


# countries = []

class Fetch():

    def __init__(self):

        # check connection
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
        resp = requests.get("https://www.worldometers.info/coronavirus/", headers=headers);
        print(headers)
        print(resp.status_code)

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')


        self.browser = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.browser, 10)

    def retrive_data(self):
        browser = self.browser
        print("loading...")

        p = False

        while p == False:
            try:
                browser.get("https://www.worldometers.info/coronavirus/")
                p = True
            except:
                p = False

        trs = browser.find_elements_by_tag_name("tr")

        # data pool
        pool = DataDrive.DataDrive('35.189.101.119', '6350', 'er7886$')

        countrylist = []

        for tr in trs:
            tds = tr.find_elements_by_tag_name("td")
            # [print(td.text) for td in tds]
            if tds == [] or tds[0].text == "":
                print("not a valid data format")
            else:
                print("scanning " + str(tds[0].text.encode('UTF-8')))
                country_name = tds[0].text.encode('UTF-8')

                total_data = pool.number_formatter(tds[1].text)
                new_data = pool.number_formatter(tds[2].text)
                death_data = pool.number_formatter(tds[3].text)
                new_death_data = pool.number_formatter(tds[4].text)
                recover_data = pool.number_formatter(tds[5].text)

                country = {"country": country_name.decode('UTF-8'), "total": total_data, "new": new_data, "total_death": death_data,
                           "new_death": new_death_data,
                           "recovered": recover_data}
                # print(country)

                # print("date:", date)
                countrylist.append(country)
                # pool.pack(str(date), country_name, country)

                print("one roll added")
                # countries = countries.append(country)

        date = datetime.datetime.now().date()
        # print(countrylist)
        pool.pack(date, countrylist)
        print("done!")


if __name__ == '__main__':
    Fetch().retrive_data()
