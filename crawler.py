from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from selenium.webdriver.chrome.options import Options


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

with webdriver.Chrome(chrome_options=option,executable_path=r"C:\Users\ramang\Developer\battlefy-lol-stats-crawler\chromedriver_win32\chromedriver.exe") as driver:
    
    
    wait = WebDriverWait(driver, 30)
    driver.get("https://battlefy.com/esport-student-association/3e-liga-winter-2020/5f3a455d63cc1128e5f89e48/stage/5f7a48f6d141ee2b8a7f42be/match/5f7a495d574d9f3af70b19ad")   
    
    # print("#### LOOKING FOR SUBREDDIT ####")
    
    # searchBar = driver.find_element(By.ID, "header-search-bar")
    # searchBar.send_keys("leagueoflegends")
    # searchBar.send_keys(Keys.RETURN)
    # time.sleep(2)
    print("#### SEARCH DONE ####")

    try:
        # team 1
        for i in range(1,6):
                                                                        
            nameOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[1]/div/div[3]/div[1]/b")))
            print(nameOne.text)
            kdaOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[2]/div")))
            print(kdaOne.text.split("\n")[0])
            csOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[3]/div")))
            print(csOne.text.split("\n")[0])
            print(csOne.text.split("\n")[2])
            dmg = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[5]/div")))
            print(dmg.text.split("\n")[0])
            win = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/h2/small/span")))
            print(win.text)
            time = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/h4/span[1]")))
            print(time.text)
        # team 2
        for i in range(1,6):
                                                                        
            nameOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[1]/div/div[3]/div[1]/b")))
            print(nameOne.text)
            kdaOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[2]/div")))
            print(kdaOne.text.split("\n")[0])
            csOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[3]/div")))
            print(csOne.text.split("\n")[0])
            print(csOne.text.split("\n")[2])
            dmg = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[5]/div")))
            print(dmg.text.split("\n")[0])
            win = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[3]/div/h2/small/span")))
            print(win.text)
            time = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[1]/div/div/div[2]/div/h4/span[1]")))
            print(time.text)
        gameTwo = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/div/div/ul/li[3]/a")))
        gameTwo.click()
        for i in range(1,6):
                                                                        
            nameOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[1]/div/div[3]/div[1]/b")))
            print(nameOne.text)
            kdaOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[2]/div")))
            print(kdaOne.text.split("\n")[0])
            csOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[3]/div")))
            print(csOne.text.split("\n")[0])
            print(csOne.text.split("\n")[2])
            dmg = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[5]/div")))
            print(dmg.text.split("\n")[0])
            win = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/h2/small/span")))
            print(win.text)
            time = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/h4/span[1]")))
            print(time.text)
        # team 2
        for i in range(1,6):
                                                                        
            nameOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[1]/div/div[3]/div[1]/b")))
            print(nameOne.text)
            kdaOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[2]/div")))
            print(kdaOne.text.split("\n")[0])
            csOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[3]/div")))
            print(csOne.text.split("\n")[0])
            print(csOne.text.split("\n")[2])
            dmg = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[3]/div/div/table/tbody/tr["+str(i)+"]/td[5]/div")))
            print(dmg.text.split("\n")[0])
            win = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[3]/div/h2/small/span")))
            print(win.text)
            time = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats[2]/div/div/div[2]/div/h4/span[1]")))
            print(time.text)
    finally:
        print("#### DONE ####")
        driver.quit()
