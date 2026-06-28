# Kia NZ Price Scraper

Scrapes vehicle "from" prices from kia.co.nz daily and stores them as JSON for use in a Wix Studio site.

## How it works

1. GitHub Actions runs `scrape.py` every day at 8am NZT
2. The script writes prices to `data/vehicles.json`
3. The JSON is committed back to this repo
4. Your Wix site fetches the raw JSON file on page load via Wix Velo

## Setup

### 1. Create a GitHub repo
Push this folder to a **public** GitHub repo (so the raw JSON URL is accessible without auth).

### 2. Enable Actions write permissions
Go to **Settings → Actions → General → Workflow permissions** and set to **Read and write**.

### 3. Run it manually first
Go to **Actions → Scrape Kia NZ Prices → Run workflow** to generate `data/vehicles.json` immediately.

### 4. Wire up Wix Velo
- Copy `wix-velo.js` into a Public file in Wix Studio (e.g. `public/kiaPrices.js`)
- Update `YOUR_GITHUB_USERNAME` and `YOUR_REPO_NAME` in the URL
- Import and call `getKiaPrices()` in your page's `$w.onReady()`

## Output format

```json
{
  "last_updated": "2025-06-29T08:00:00+00:00",
  "source": "https://www.kia.co.nz/kia-new-zealand",
  "vehicles": {
    "EV3": { "from_price": "$55,520", "url": "https://www.kia.co.nz/vehicles/ev3" },
    "EV4": { "from_price": "$63,990", "url": "https://www.kia.co.nz/vehicles/ev4" },
    "Sportage": { "from_price": "$39,990", "url": "https://www.kia.co.nz/vehicles/sportage" }
  }
}
```

## Manual trigger
You can re-run the scraper anytime from the **Actions** tab in GitHub — useful after a Kia NZ price update.
