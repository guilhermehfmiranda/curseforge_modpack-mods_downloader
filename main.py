# standard packages
import json
from pathlib import Path
import time

# external packages
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# code
with open('manifest.json', 'r') as f:
    manifest_json = json.loads(f.read())

file_ids = []
for id in manifest_json['files']:
    file_ids.append(id['fileID'])

with open('modlist.html', 'r') as f:
    modlist_html = BeautifulSoup(f.read(), 'html.parser')

project_links = []
for link in modlist_html.find_all('a'):
    project_links.append(link.get('href'))

try:
    def enable_download_headless(browser,download_dir):
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)

    current_dir = str(Path(__file__).parent)
    download_dir =  current_dir + "\\downloads"
    chromedriver_version = 96

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=200x200")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_experimental_option("prefs", {
            "download.default_directory": f"{download_dir}",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
    })

    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = f"{current_dir}\\chromedriver_{chromedriver_version}\\chromedriver.exe")    
    enable_download_headless(driver, download_dir)
    
    print("---- ---- ---- ----")
    for i, mod in enumerate(project_links):
        print(f"{i+1} ---- downloading: {mod}")
        url = f"{mod}/download/{file_ids[i]}/file"
        driver.get(url)
        time.sleep(10)

finally:
    print("---- ---- ---- ----")
    input("Press Enter to close [ chromedriver ] . . .")
    driver.quit()