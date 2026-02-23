import requests
from bs4 import BeautifulSoup

def fetch_profile(ticker):
    url = f"https://tw.stock.yahoo.com/quote/{ticker}/profile"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Look for common container for profile text
            # Depending on Yahoo's layout, it might be in a specific section.
            # Let's search for "基本資料" or relevant headings.
            
            # Simple text dump to search for keywords
            text = soup.get_text()
            if "公司基本資料" in text:
                print("Found '公司基本資料'")
                # Try to extract the specific block
                # Often in <section> or <div> blocks
                # Let's just print a snippet around "成立日期" (Founding Date) which is usually there.
                if "成立日期" in text:
                    print("Found '成立日期', profile likely present.")
                    # Find a nearby long paragraph?
                    paragraphs = soup.find_all('p')
                    for p in paragraphs:
                        if len(p.text) > 50:
                            print(f"Sample Content: {p.text[:100]}...")
                            break
            else:
                print("Could not find '公司基本資料' in text.")
        else:
            print("Failed to retrieve page.")
            
    except Exception as e:
        print(f"Error: {e}")

fetch_profile("2330")
