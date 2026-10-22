# OMID // NEON ARENA — Gaming Skin

A pure visual layer (`gaming_skin.py`). No panel logic, API or database code was changed.

## Files touched
- `gaming_skin.py` (new) — CSS + JS + `inject_gaming_skin(html, mode)`
- `pages.py` — 3 lines at the end: injects the skin into LOGIN_HTML / DASHBOARD_HTML
- `public_page.py` — import + 3 lines: injects into public page, single-config page, admin-all page

## Disable / roll back
- Set env var `OMID_SKIN=off` → every page renders exactly as v2.5.0.
- Or delete `gaming_skin.py` and the injection lines.

## What it adds
- Neon Arena palette (cyan / violet / magenta) on the existing theme tokens; light theme becomes "Daylight HUD"
- Synthwave perspective floor + aurora + live particle network (reacts to mouse, click sparks)
- Asymmetric cyber-panels with HUD corner brackets; rotating neon conic border on hover
- Hex icon badges, chamfered primary buttons, glitch logo, scanlines/vignette
- XP-style segmented progress bars that turn amber (>=60%) and red (>=85%) automatically
- Radar-ping status dots, HUD ribbon with live clock/online state, once-per-session boot screen
- Easter egg: Konami code toggles OVERDRIVE (hue-cycling)
- Respects `prefers-reduced-motion`; pauses animation when the tab is hidden; lighter on mobile

---

## ☀️ Daylight HUD — premium light theme (new)

New file: `daylight_skin.py` (pure CSS layer, loaded after the dark skin). `gaming_skin.py` only got an import,
one extra line in `inject_gaming_skin`, and new particle colours for light mode.
It activates **only** when `data-theme="light"` / `data-login-theme="light"`, so the dark Neon Arena theme is untouched.

### What it adds
- New palette: porcelain white + indigo / sky / orchid (WCAG-friendly dark text, status colours re-tuned)
- Crystal-glass panels: frosted blur, inner highlight, layered soft shadows, indigo HUD corner brackets
- Sunrise horizon glow, animated soft perspective floor, richer aurora mesh, subtle paper grain
- Glossy chamfered primary buttons, clean focus rings on inputs, frosted sidebar with soft active pill
- Light-native segmented progress bars (cyan→indigo→orchid, amber ≥60%, red ≥85%) with proper gap colour
- Light boot screen, light modals / toasts, readable badge colours, softened glitch + logo ring

### Disable / roll back
- `OMID_SKIN_LIGHT=off` → light theme falls back to the previous "Daylight HUD" (dark skin untouched)
- `OMID_SKIN=off` → everything renders exactly as v2.5.0
- Or delete `daylight_skin.py` (the import is wrapped in try/except, nothing breaks)

---

## Menu redesign (13 → 8 items) + Server Resources + Effects switch

Sidebar: Dashboard · Configurations · Groups · Connections · Logs · Telegram · Settings · Support

- **Groups** = tabs *Groups* + *Subscription Links* (old "Subscription Groups" + "Subscriptions")
- **Logs** = tabs *Activity* + *Errors* (error-count badge lives on the tab)
- **Dashboard** = tabs *Overview* + *Traffic Details* (old "Traffic" page; its chart `ch3` is unchanged)
- **Settings** = tabs *Account & Security* (admin account + security info), *Server*, *Appearance* (Effects), *Diagnostics* (WebSocket test)
- **Support** kept, with a new YouTube tile: https://www.youtube.com/@omid_Gaming
- Old page ids still work: `navTo('errors' | 'traffic' | 'subscriptions' | 'security' | 'testws')` open the right tab.

### Server Resources card (dashboard)
New endpoint `GET /api/system` (admin session required). CPU %, RAM, disk, network rate/total, cores, load average.
Reads `/proc` and container cgroup limits, no new dependency (no psutil). Returns `null` fields on non-Linux hosts.
Polled every 4 s only while the Dashboard is visible and the tab is not hidden.

### Effects: Full / Lite / Off
Settings > Appearance. Stored per device in `localStorage['omid_fx']`; with no saved choice it auto-picks **Lite** on
reduced-motion, Data-Saver, ≤4 cores, ≤4 GB RAM or <700 px screens, else **Full**.
- **Lite**: no particle canvas, synthwave floor, cursor glow, scanlines, boot screen, Konami, glitch or looping animations
- **Off**: Lite + no background layers, HUD overlay, transitions or backdrop blur
