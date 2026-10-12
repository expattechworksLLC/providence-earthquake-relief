# Providence Church — Earthquake Relief: public website

## Links to share
- **English:** https://providenceearthquakerelief.netlify.app/en/ — always opens in English (best for expats)
- **Spanish:** https://providenceearthquakerelief.netlify.app/es/ — always opens in Spanish
- **Main:** https://providenceearthquakerelief.netlify.app/ — follows the phone's language

To update: Netlify → your site → **Deploys** tab → drag the new unzipped folder into the box at the bottom.
Every page has the ES/EN switch at the top.

This folder is the complete public site (`index.html`, `en/`, `es/`). Each page is self-contained (logo embedded, no build step).
Visitors never need an account.

## 1. Put it online (about 5 minutes, free)

**Netlify Drop (fastest)**
1. Go to https://app.netlify.com/drop and sign in (free account, only for you).
2. Drag this whole `deploy` folder onto the page.
3. Netlify gives you an address like `https://something.netlify.app`. Open it on your phone to check.
4. Site settings → change the site name to something readable, e.g. `ayuda-sismo-providence`.

**Cloudflare Pages (alternative)**
Workers & Pages → Create → Pages → Upload assets → upload this folder.

**Using relief.providencechurchpa.org**
Whoever manages the providencechurchpa.org DNS adds a CNAME record `relief` pointing at the
Netlify/Cloudflare address, then adds the custom domain in the hosting dashboard (HTTPS is automatic).
Nothing about this subdomain has been configured yet.

## 2. After it's live

- In `index.html`, set `publicUrl` in CONFIG to the final address (sharing works without it on the
  live host, but setting it keeps the WhatsApp/Facebook links consistent if you later change domains).
- In the `<head>`, uncomment/add `<meta property="og:url" content="https://YOUR-ADDRESS/">`.
- Re-upload the folder. Test the preview by pasting the link into a WhatsApp chat with yourself.
  (Facebook caches previews; refresh with https://developers.facebook.com/tools/debug/.)

## 3. Updating information

Everything editable is in the `CONFIG` block at the top of the `<script>` in `index.html`.
**Everything in CONFIG is public** — anyone can view the page source.

| What | Where in CONFIG |
|---|---|
| Add/edit a drop-off point | `locations` (set `approved: true` to show it) |
| Point status | `status`: `accepting`, `full`, `closed`, `awaiting` |
| Tower/unit numbers | fill `tower` / `unit` **and** set `publishUnitDetails: true` — only after each resident agrees |
| Map links / nearest-point finder | `lat`, `lng`, `mapsUrl`, `wazeUrl` — verified values only |
| Supply priorities | each item's `priority`: `urgent`, `needed`, `sufficient`, `notAccepting`; set `suppliesLastUpdated` |
| Yappy | `yappy.recipientName`, `yappy.handle`, optional `yappy.qrImage` |
| Bank transfer | `bank.bankName`, `accountHolder`, `accountType`, `accountNumber`, optional `extra` |
| Forms | `coordinatorWhatsApp` (forms open WhatsApp to this number) and/or `formEndpoint` |
| Financial totals | `finance` — set `published: true` only with verified figures |
| Mission updates | `updates` — newest first; photos only with consent |
| Banner message | `announcement` |

## 4. Optional: manage from Google Sheets (Phase 2)

Make a sheet per list, then **File → Share → Publish to web → (that tab) → CSV**, and paste the CSV
link into `CONFIG.sheets`. The site loads these on each visit and falls back to CONFIG if loading fails.
Keep volunteer contacts, bank records and unapproved addresses in a **separate, unpublished** sheet.

- **Locations**: `id, name, area, status, approved, frontGate, publishDetails, tower, unit, lat, lng, mapsUrl, wazeUrl, instructions_es, instructions_en`
  (`area` = coronado / nueva-gorgona / san-carlos / other; yes/no columns accept yes, sí, x)
- **Supplies**: `category, item_es, item_en, priority, last_updated` (`category` = food / shelter / hygiene / kids)
- **Updates**: `date, area_es, area_en, description_es, description_en, quantities_es, quantities_en, photo_url, photo_alt_es, photo_alt_en, confirmed_by_es, confirmed_by_en, notes_es, notes_en`
  (separate multiple quantities with `;`)

## 5. Receiving form submissions privately

Easiest: set `coordinatorWhatsApp`. Each form then opens WhatsApp with the details pre-filled, addressed
to the coordinator; nothing is stored on the website.

For a spreadsheet inbox: create a Google Apps Script web app bound to a **private** sheet whose
`doPost(e)` appends `JSON.parse(e.postData.contents)` as a row, deploy it ("Anyone" can access), and paste
its URL into `formEndpoint`. Test it before announcing.

## 6. Map stars

Each location with `lat` and `lng` gets a gold star on the map, and the "find nearest" button uses them.
Get them from Google Maps: long-press the exact building entrance → the coordinates appear at the top
(e.g. `8.53412, -79.88765`). The map image covers Nueva Gorgona to Coronado; a point outside that area
still works for "nearest" but won't show a star. Map data © OpenStreetMap contributors.

## 7. Donations received & deliveries

- `received`: one row per drop-off collected — date, time, location id, items, donor name (only with
  permission; blank shows "Anonymous donor"), optional photo.
- `distributions`: one card per delivery trip — date, place, description, verified items, photos, who confirmed.
- Photos: put image files in a `photos/` folder next to index.html and use `photos/name.jpg`, or paste a
  public Google Drive share link (converted automatically). Only publish photos with consent.
- Google Sheets columns — **received**: `date, time, location, items_es, items_en, donor, photo_url, publish`
  · **distributions**: `date, place_es, place_en, description_es, description_en, items_es, items_en,
  photo_urls, photo_alt_es, photo_alt_en, confirmed_by_es, confirmed_by_en, notes_es, notes_en`
  (separate multiple items or photo links with `;`).

## 8. Recent cash donations

`cashDonations` in CONFIG (or a sheet linked as `cashCsv` with columns `date, name, amount, method, note, publish`).
Post a gift only after the money is confirmed received, and show a name only with the donor's permission
(blank name shows "Anonymous donor"). `method` = yappy, transfer or cash. The total shown is the sum of the
gifts posted there.
