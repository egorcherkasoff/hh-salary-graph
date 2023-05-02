from bs4 import BeautifulSoup


# get num of pages for query
def get_pages(html):
    soup = BeautifulSoup(html, "html.parser")
    page_btn = soup.select(".bloko-button span")[-1].getText()
    # will try to change this to data-qs selector later
    if page_btn != "дальше":
        pages = page_btn
    elif page_btn == "Откликнуться":
        pages = "1"
    else:
        pages = soup.select(".bloko-button span")[-2].getText()
    return pages


# get salary and cities data
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    # get html elements with cities names
    raw_cities = soup.select("div[data-qa='vacancy-serp__vacancy-address']")
    # cretate new list with cities names, where we split City name and addict. info like
    # metro station
    cities = [city.getText().split(",")[0] for city in raw_cities]
    # get html elements with salary
    raw_salaries = soup.select("span.bloko-header-section-3")
    salaries_text = [salary.getText().replace("\u202f", "") for salary in raw_salaries]
    # create new list for cleaned int values
    salaries_values = []
    for salary in salaries_text:
        if "–" in salary:
            salary = salary.split("–")[1][:-5]
        else:
            salary = salary[3:-5]
        salaries_values.append(int(salary))
    return cities, salaries_values


if __name__ == "__main__":
    pass
