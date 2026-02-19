from concurrent.futures import ThreadPoolExecutor
from scraper.scraper import *
from scraper.translator import translate_titles
from scraper.analyzer import analyze_words
import traceback


def run_test(thread_id):
    try:
        print(f"\nStarting BrowserStack session {thread_id}")

        driver = get_browserstack_driver(thread_id)

        print(f"Session {thread_id} -> Driver started")

        open_opinion_section(driver)
        links = get_first_five_article_links(driver)

        spanish_titles = []
        for idx, link in enumerate(links):
            title = scrape_single_article(driver, link, idx)
            spanish_titles.append(title)

        driver.quit()

        english_titles = translate_titles(spanish_titles)
        analyze_words(english_titles)

        print(f"Session {thread_id} completed")

    except Exception as e:
        print(f"\nERROR in thread {thread_id}")
        traceback.print_exc()


if __name__ == "__main__":
    for i in range(5):
        run_test(i)
    # run_test(0)

