# OMID IRAN v2.5.3 — Vercel Session Hotfix

## What this fixes

The login flow previously stored session tokens only in a process-local Python dictionary. On Vercel, the next request can be handled by a different Function instance, which does not have that dictionary entry. This made the dashboard briefly appear and then redirect back to the login page.

This hotfix changes `gateway_session` to a stateless HMAC-SHA256 signed cookie. Each instance verifies the cookie using the same `SECRET_KEY`, without requiring a session entry in its own memory. Changing the username or password invalidates older cookies through a credential fingerprint.

## Required Vercel settings

In **Project → Settings → Environment Variables**, configure a strong, stable `SECRET_KEY` for every environment where you test the app (Production / Preview as applicable). Use the same value across all Function instances. Do not generate a new value on every startup. Since a previous secret was shared in chat, create a fresh one and do not paste it into public places or conversations.

Keep `ADMIN_USERNAME` and `ADMIN_PASSWORD` consistent with the credentials you actually use. Redeploy after changing environment variables.

## Important limitations

- This fixes the *session lookup across instances*; it does not provide a shared database.
- The Vercel `/tmp` fallback is writable but ephemeral and local to an instance. It is not durable storage for `gateway_state.json`, generated configs, or panel settings.
- If you still see `WS rejected ... (not allowed)` for a config that exists, the app's state is not shared/persisted across instances. Run the complete FastAPI backend on Railway with a persistent Volume mounted at `/data`, or implement a shared external database/store. Do not rely on `/tmp` for production state.
- Logout clears the current browser cookie. With a stateless session there is no per-token server-side revocation list; sessions expire according to `SESSION_TTL`, and changing credentials invalidates older tokens.

## Validation performed

- Python syntax compilation passed.
- Signed session verification passed without any in-memory session dictionary.
- Tampered session tokens were rejected.
- Changing the credential fingerprint invalidated the old token.

These are local code tests. A successful Vercel deployment and end-to-end browser test are still required.
