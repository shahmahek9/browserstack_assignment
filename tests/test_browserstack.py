import pytest
from scraper.scraper import (
    get_local_driver,
    open_opinion_section,
    get_first_five_article_links,
    scrape_single_article
)
from scraper.translator import translate_titles
from scraper.analyzer import analyze_words


# This fixture chooses driver automatically
@pytest.fixture
def driver(request):
    # If BrowserStack provides driver → use it
    if "browserstack_driver" in request.fixturenames:
        return request.getfixturevalue("browserstack_driver")

    # Otherwise run locally
    driver = get_local_driver()
    yield driver
    driver.quit()


@pytest.mark.browserstack
def test_elpais_scraper(driver):

    open_opinion_section(driver)

    links = get_first_five_article_links(driver)

    spanish_titles = []
    for idx, link in enumerate(links):
        title = scrape_single_article(driver, link, idx)
        spanish_titles.append(title)

    english_titles = translate_titles(spanish_titles)
    analyze_words(english_titles)

    assert len(spanish_titles) == 5
