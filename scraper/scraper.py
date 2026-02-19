import time, os, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

BASE_URL = "https://elpais.com"



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def get_browserstack_driver(thread_id=0):
    USERNAME = os.getenv("BROWSERSTACK_USERNAME")
    ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

    BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub"

    # 5 environments required by assignment
    environments = [
        # 0 Chrome Windows
        {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "11"
            }
        },
        # 1 Firefox Windows
        {
            "browserName": "Firefox",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "10"
            }
        },
        # 2 Safari Mac
        {
            "browserName": "Safari",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "OS X",
                "osVersion": "Sonoma"
            }
        },
        # 3 iPhone
        {
            "browserName": "Safari",
            "bstack:options": {
                "deviceName": "iPhone 14",
                "osVersion": "16"
            }
        },
        # 4 Android
        {
            "browserName": "Chrome",
            "bstack:options": {
                "deviceName": "Samsung Galaxy S23",
                "osVersion": "13"
            }
        }
    ]

    caps = environments[thread_id]

    # Create ChromeOptions object (works for all browsers in Selenium 4 remote)
    options = Options()

    # Add capabilities properly (Selenium 4 way)
    for key, value in caps.items():
        options.set_capability(key, value)

    # Metadata
    options.set_capability("name", f"ElPais Thread {thread_id}")
    options.set_capability("build", "ElPais Parallel Build")

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    return driver




# LOCAL driver only (used when running main.py)
def get_local_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def open_opinion_section(driver):
    driver.get(BASE_URL)
    time.sleep(3)

    # Accept cookies popup if present
    try:
        driver.find_element(By.ID, "didomi-notice-agree-button").click()
        time.sleep(1)
    except:
        pass

    driver.get("https://elpais.com/opinion/")
    time.sleep(3)


def get_first_five_article_links(driver):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    articles = soup.select("main article h2 a")

    links = []
    for a in articles[:5]:
        href = a.get("href")
        full_link = href if href.startswith("http") else BASE_URL + href
        links.append(full_link)

    return links


def download_image(url, idx):
    try:
        if url.startswith("//"):
            url = "https:" + url

        os.makedirs("images", exist_ok=True)
        img = requests.get(url, timeout=10).content

        with open(f"images/article_{idx}.jpg", "wb") as f:
            f.write(img)

        print("Saved image", idx)
    except:
        print("No image found")


def scrape_single_article(driver, url, idx):
    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Title
    title_tag = soup.select_one("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No title"

    # Content preview
    paragraphs = soup.select("article p")
    content = " ".join(p.get_text() for p in paragraphs[:10])

    print("\nSPANISH TITLE:", title)
    print("CONTENT PREVIEW:", content[:300])

    # Cover image
    img_tag = soup.select_one("figure img")
    if img_tag and img_tag.get("src"):
        download_image(img_tag["src"], idx)

    return title
