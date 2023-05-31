from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def index(request):
    # return HttpResponse(f"Hi")
    return render(request, "index.html")


def compute_square(request, number):
    square = number * number
    context = {"square": square, "number": number}
    return render(request, "compute_square.html", context=context)


def compute_squares(request, number):
    numbers = list(range(number))
    squares = [n**2 for n in numbers]
    context = {
        "number_and_square": [
            {"number": number, "square": square}
            for number, square in zip(numbers, squares)
        ]
    }
    return render(request, "compute_squares.html", context=context)


def random_wiki(request):
    url = "https://en.wikipedia.org/wiki/Special:RandomInCategory/Featured_articles"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    language_list = soup.find_all("a", class_="interlanguage-link-target")
    language_list = [language.span.text for language in language_list]

    page_title = soup.find(id="firstHeading").text
    context = {"page_title": page_title, "languages": language_list}
    return render(request, "random_wiki.html", context=context)
