from bs4 import BeautifulSoup


# get num of pages for query
def get_pages(html):
    soup = BeautifulSoup(html, "html.parser")
    page_btn = soup.select(".bloko-button span")[-1].getText()
    if page_btn != "дальше":
        pages = page_btn
    else:
        pages = soup.select(".bloko-button span")[-2].getText()
    return pages


# get salary and cities data
def get_data(html):
    return


if __name__ == "__main__":
    pass
