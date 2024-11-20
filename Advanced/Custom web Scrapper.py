# Custom web scraper to collect data on things that you I am interested in.


import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    """
    Fetch the HTML content from the given URL.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_data(html_content):
    """
    Parse the HTML content and extract the desired data.
    Customize this function based on your requirements.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Scrape titles of articles from a blog or news site
    data = []
    for item in soup.find_all('h2', class_='entry-title'):  # Customize the tag and class
        title = item.get_text(strip=True)
        link = item.find('a')['href'] if item.find('a') else None
        data.append({'title': title, 'link': link})
    
    return data

def save_data(data, file_name='scraped_data.txt'):
    """
    Save the scraped data to a file.
    """
    with open(file_name, 'w') as f:
        for item in data:
            f.write(f"Title: {item['title']}\n")
            f.write(f"Link: {item['link']}\n\n")
    print(f"Data saved to {file_name}")

def main():
    """
    Main function to execute the web scraper.
    """
    url = input("Enter the URL to scrape: ").strip()
    html_content = fetch_data(url)
    if html_content:
        data = parse_data(html_content)
        if data:
            save_data(data)
        else:
            print("No data found to scrape.")
    else:
        print("Failed to retrieve content.")

if __name__ == "__main__":
    main()
