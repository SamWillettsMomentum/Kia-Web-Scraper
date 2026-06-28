// Wix Velo — paste this into your page code or a public file
// Replace YOUR_GITHUB_USERNAME and YOUR_REPO_NAME below

import { fetch } from 'wix-fetch';

const PRICES_URL =
  "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/main/data/vehicles.json";

export async function getKiaPrices() {
  const response = await fetch(PRICES_URL);
  if (!response.ok) throw new Error("Failed to fetch Kia prices");
  const data = await response.json();
  return data.vehicles; // { "EV3": { from_price: "$55,520", url: "..." }, ... }
}

// Example: call this in your $w.onReady() to populate your page
// import { getKiaPrices } from 'public/kiaPrices.js';
//
// $w.onReady(async () => {
//   const vehicles = await getKiaPrices();
//   const sportage = vehicles["Sportage"];
//   $w("#sportagePrice").text = `From ${sportage.from_price}`;
// });
