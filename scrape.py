import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timezone

URL = "https://www.kia.co.nz/kia-new-zealand"

def scrape_vehicles():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Target only the #all section to avoid duplicates (models are repeated per category)
    all_section = soup.find("div", id="all")
    if not all_section:
        raise ValueError("Could not find #all vehicles section in page")

    vehicles = {}
    for li in all_section.select("li.vehicle"):
        name_tag = li.select_one("span.range-name")
        price_tag = li.select_one("span.price")
        link_tag = li.select_one("a[href]")

        if name_tag and price_tag:
            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            href = link_tag["href"] if link_tag else None
            url = f"https://www.kia.co.nz{href}" if href else None

            vehicles[name] = {
                "from_price": price,
                "url": url
            }

    return vehicles

def main():
    vehicles = scrape_vehicles()

    output = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "source": URL,
        "vehicles": vehicles
    }

    with open("data/vehicles.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"✅ Scraped {len(vehicles)} vehicles:")
    for name, data in vehicles.items():
        print(f"   {name}: {data['from_price']}")

if __name__ == "__main__":
    main()
