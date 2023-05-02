import requests
from .scrape import get_pages, get_data

# base url for searching vacancies
BASE_URL = "https://hh.ru/search/vacancy?area=113&search_field=name&search_field=description&only_with_salary=true&text="


# have to use headers here because hh.ru responds 404 without User-Agent header
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


# combine all pages into single string to scrap all data together
def get_full_html(html, request_url):
    pages = get_pages(html)
    # might try to change selector to avoid this if
    if pages == "Фильтры":
        pages = 1
    else:
        pages = int(pages)
    # will try to change this to avoid getting way to high mem usage
    full_html = f"{html}"
    # collect data from all pages for query
    for page_num in range(1, pages):
        response = requests.get(f"{request_url}&page={page_num}", headers=HEADERS)
        page = response.text
        full_html += page
    return get_data(full_html)


# get first page
def get_first_page(query):
    # concat base url with query
    request_url = BASE_URL + f"{query}"
    # make request and get html
    response = requests.get(request_url, headers=HEADERS)
    first_page = response.text
    return get_full_html(first_page, request_url)


if __name__ == "__main__":
    print(get_first_page(("junior python").replace(" ", "+")))
