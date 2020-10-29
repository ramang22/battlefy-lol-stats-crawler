from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from selenium.webdriver.chrome.options import Options
import xlsxwriter

NAME_COL = 0
K_COL = 1
D_COL = 2
A_COL = 3
CS_COL = 4
GOLD_COL = 5
DMG_COL = 6
WIN_COL = 7
TIME_COL = 8
ROW = 0


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

workbook = xlsxwriter.Workbook('lol_stats.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(ROW, NAME_COL, "Meno")
worksheet.write(ROW, K_COL, "Kills")
worksheet.write(ROW, D_COL, "Deaths")
worksheet.write(ROW, A_COL, "Assists")
worksheet.write(ROW, CS_COL, "CS")
worksheet.write(ROW, GOLD_COL, "GOLD")
worksheet.write(ROW, DMG_COL, "DMG")
worksheet.write(ROW, WIN_COL, "WIN")
worksheet.write(ROW, TIME_COL, "TIME")
ROW += 1

date_format = workbook.add_format({'num_format': "hh:mm:ss",
                                      'align': 'left'})

filepath = 'links.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       link = line.strip()
       with webdriver.Chrome(chrome_options=option,executable_path=r"C:\Users\ramang\Developer\battlefy-lol-stats-crawler\chromedriver_win32\chromedriver.exe") as driver:
        wait = WebDriverWait(driver, 3)
        driver.get(link)   
        print("#### SEARCH DONE {0} ####".format(str(cnt)))

        try:
            # team 1
            for page in range(1,4):
                if page == 2:
                    gameTwo = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/div/div/ul/li[3]/a")))
                    gameTwo.click()
                if page == 3:
                    try:
                        game3 = driver.find_element_by_xpath("/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/div/div/ul/li[4]/a")
                        game3.click()
                    except:
                        continue
                for team in range(2,4):
                    for i in range(1,6):
                                                                                    
                        nameOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats["+str(page)+"]/div/div/div["+str(team)+"]/div/div/table/tbody/tr["+str(i)+"]/td[1]/div/div[3]/div[1]/b")))
                        kdaOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats["+str(page)+"]/div/div/div["+str(team)+"]/div/div/table/tbody/tr["+str(i)+"]/td[2]/div")))
                        kda = kdaOne.text.split("\n")[0].split("/")
                        csOne = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats["+str(page)+"]/div/div/div["+str(team)+"]/div/div/table/tbody/tr["+str(i)+"]/td[3]/div")))
                        dmg = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats["+str(page)+"]/div/div/div["+str(team)+"]/div/div/table/tbody/tr["+str(i)+"]/td[5]/div")))
                        win = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats["+str(page)+"]/div/div/div["+str(team)+"]/div/h2/small/span")))
                        if "VICTORY" in win.text: 
                            win = 1
                        else :
                            win = 0
                        time = wait.until(presence_of_element_located((By.XPATH, "/html/body/bf-app/main/div/div/div/bf-tournament/div[2]/div/div[4]/div/div/div/div/div/bf-match/div/div[3]/div[2]/bfy-lol-match-stats/div/div/div/bfy-lol-stats["+str(page)+"]/div/div/div[2]/div/h4/span[1]")))
                        time = time.text.replace("m ",":").replace("s","").strip()
                        time = "00:"+time
                        worksheet.write(ROW, NAME_COL, nameOne.text)
                        worksheet.write(ROW, K_COL, int(kda[0].strip()))
                        worksheet.write(ROW, D_COL, int(kda[1].strip()))
                        worksheet.write(ROW, A_COL, int(kda[2].strip()))
                        worksheet.write(ROW, CS_COL, int(csOne.text.split("\n")[0].split("CS")[0].replace(",","")))
                        worksheet.write(ROW, GOLD_COL, int(csOne.text.split("\n")[2].split("Gold")[0].replace(",","")))
                        worksheet.write(ROW, DMG_COL, int(dmg.text.split("\n")[0].replace(",","")))
                        worksheet.write(ROW, WIN_COL, win)
                        worksheet.write(ROW, TIME_COL, time,date_format)
                        ROW += 1

        finally:
            print("#### DONE ####")
            driver.quit()
       line = fp.readline()
       cnt += 1
workbook.close()


