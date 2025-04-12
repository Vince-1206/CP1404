"""
CP1404 Practical - Enhanced Wikipedia API Program
Search Wikipedia and handle results, saving output to a file.
"""

import wikipedia
import warnings
from bs4 import GuessedAtParserWarning

# Optional: Hide the BeautifulSoup parser warning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

def main():
    print("Wikipedia Search")
    while True:
        title = input("\nEnter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)
            summary = wikipedia.summary(title, auto_suggest=False)

            print(f"\n{page.title}")
            print(summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()

