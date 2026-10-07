# AirLine Pop – Policy site

The public website for **AirLine Pop**, the cat airline one-line puzzle game by **Biexce**:
the game's introduction, its Privacy Policy and its Terms of Service, in English and
Vietnamese.

| Page | File |
|---|---|
| Home | `index.html` |
| Privacy Policy | `privacy.html` |
| Terms of Service | `terms.html` |

Plain HTML and CSS with no build step, ready for GitHub Pages: in the repository
settings, under **Pages**, publish the `main` branch from the root. The privacy policy
link for Google Play and the App Store is then
`https://hgkhanhvy.github.io/Airline-Pop-Policy/privacy.html`.

## Languages

Every text is written in both languages in the page itself, as `lang="en"` and
`lang="vi"` elements. `assets/js/lang.js` shows one of them: the visitor's earlier
choice, else their browser language. `?lang=vi` or `?lang=en` in the address forces one,
for example `privacy.html?lang=vi`.

## Updating

- Keep the two languages saying the same thing, and change the "Last updated" date at
  the top of a page whenever its content changes.
- When a service is added to or removed from the game (ads, analytics, measurement),
  update the table in section 3 of `privacy.html`.

The art comes from the game itself (Craftpix.net cat characters used under licence) and
the typeface is Baloo 2 from Google Fonts (SIL Open Font License).
