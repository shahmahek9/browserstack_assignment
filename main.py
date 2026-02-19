from scraper.scraper import *
from scraper.translator import translate_titles
from scraper.analyzer import analyze_words

driver = get_local_driver()
open_opinion_section(driver)

links = get_first_five_article_links(driver)

spanish_titles = []
for idx, link in enumerate(links):
    title = scrape_single_article(driver, link, idx)
    spanish_titles.append(title)

driver.quit()

english_titles = translate_titles(spanish_titles)
analyze_words(english_titles)
