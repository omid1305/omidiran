# -*- coding: utf-8 -*-
"""
OMID // DAYLIGHT HUD  ·  premium light theme for the NEON ARENA skin
─────────────────────────────────────────────────────────────────────
Pure visual layer, loaded AFTER gaming_skin's CSS. It only activates when
<html data-theme="light"> (dashboard / public pages) or
<html data-login-theme="light"> (login page) is set, so the dark
Neon Arena theme is byte-for-byte untouched.

Disable only the light layer:  OMID_SKIN_LIGHT=off
Disable the whole skin:        OMID_SKIN=off
"""
import os
import re

# ── Light design tokens (crisp porcelain + indigo / sky / orchid) ───────────
_LIGHT_TOKENS = r"""
html[data-theme="light"],html[data-login-theme="light"]{
  color-scheme:light;
  --bg:#f3f5fc; --bg-2:#e9edf9;
  --bg-gradient:
    radial-gradient(ellipse 60% 50% at 10% 6%,rgba(99,102,241,.20),transparent 62%),
    radial-gradient(ellipse 56% 46% at 92% 12%,rgba(14,165,233,.17),transparent 62%),
    radial-gradient(ellipse 62% 50% at 50% 104%,rgba(244,114,182,.20),transparent 66%),
    linear-gradient(160deg,#f8f9ff 0%,#eff2fb 55%,#f6f1fb 100%);
  --grid:rgba(79,70,229,.05);

  --surface:rgba(255,255,255,.74); --surface-2:rgba(255,255,255,.55);
  --surface-3:rgba(99,102,241,.06); --surface-solid:#ffffff;
  --glass:rgba(255,255,255,.80); --glass-strong:rgba(255,255,255,.94);
  --overlay:rgba(30,35,80,.36);
  --card-b:rgba(79,70,229,.14); --card-bh:rgba(79,70,229,.46); --hairline:rgba(79,70,229,.09);

  --accent:#4f46e5; --accent-2:#c026d3; --accent-3:#0891b2;
  --accent-soft:rgba(79,70,229,.10); --accent-soft-2:rgba(192,38,211,.08);
  --accent-grad:linear-gradient(135deg,#0ea5e9 0%,#6366f1 52%,#c026d3 100%);
  --accent-grad-reverse:linear-gradient(135deg,#c026d3 0%,#6366f1 48%,#0ea5e9 100%);
  --accent-shadow:0 12px 30px -8px rgba(79,70,229,.45);
  --accent-glow:0 0 12px rgba(99,102,241,.40);
  --info:#0284c7; --info-2:#0369a1;
  --info-grad:linear-gradient(135deg,#38bdf8,#0284c7); --info-soft:rgba(2,132,199,.10);

  --green:#059669; --green-bg:rgba(5,150,105,.11); --green-t:#047857;
  --red:#e11d48;   --red-bg:rgba(225,29,72,.09);   --red-t:#be123c;
  --amber:#d97706; --amber-bg:rgba(217,119,6,.11); --amber-t:#b45309;
  --purple:#7c3aed; --purple-bg:rgba(124,58,237,.10);

  --t1:#141a3a; --t2:#4a5272; --t3:#7b83a3; --muted:#8a92ae;

  --shadow:0 24px 60px -16px rgba(40,50,130,.28),0 0 0 1px rgba(79,70,229,.06);
  --shadow-sm:0 8px 22px -8px rgba(40,50,130,.18);
  --glass-shadow:0 22px 60px -18px rgba(40,50,130,.25),inset 0 1px 0 rgba(255,255,255,.95);
  --focus-ring:0 0 0 3px rgba(99,102,241,.18);

  --login-card:rgba(255,255,255,.88);
  --login-input:rgba(255,255,255,.92);
  --login-textarea:rgba(255,255,255,.86);

  /* skin variables (override the Neon Arena ones) */
  --gx-panel:rgba(255,255,255,.96);
  --gx-cyan:#0891b2; --gx-mag:#c026d3; --gx-vio:#6366f1;
  --gx-lime:#65a30d; --gx-amber:#f59e0b; --gx-red:#e11d48;
  --gx-glow:rgba(99,102,241,.32);
}
"""

# ── Keyframes (global names, not scoped) ────────────────────────────────────
_LIGHT_KEYFRAMES = r"""
@keyframes gxl-glitch{
  0%,92%,100%{text-shadow:none;transform:none}
  93%{text-shadow:2px 0 rgba(192,38,211,.45),-2px 0 rgba(8,145,178,.45);transform:translateX(1px)}
  95%{text-shadow:-2px 0 rgba(192,38,211,.45),2px 0 rgba(8,145,178,.45);transform:translateX(-1px)}
  97%{text-shadow:none;transform:none}
}
@keyframes gxl-ring{
  0%{box-shadow:0 0 0 0 rgba(99,102,241,.45),0 8px 20px -6px rgba(79,70,229,.40)}
  100%{box-shadow:0 0 0 14px rgba(99,102,241,0),0 8px 20px -6px rgba(79,70,229,.40)}
}
@keyframes gxl-sheen{
  0%{background-position:-160% 0}
  100%{background-position:260% 0}
}
@keyframes gxl-float{
  0%,100%{transform:translate3d(0,0,0)}
  50%{transform:translate3d(0,-14px,0)}
}
"""

# ── Light rules (each selector is auto-prefixed with the light-theme scope) ─
_LIGHT_RULES = r"""
/* ═══ Background stack ═══ */
#gx-aurora{
  opacity:1;
  background:
    radial-gradient(38% 34% at 18% 26%,rgba(99,102,241,.22),transparent 70%),
    radial-gradient(36% 32% at 82% 20%,rgba(14,165,233,.20),transparent 70%),
    radial-gradient(44% 38% at 62% 82%,rgba(244,114,182,.22),transparent 72%),
    radial-gradient(30% 28% at 8% 86%,rgba(251,191,36,.14),transparent 70%)}
#gx-floor{
  display:block;opacity:.42;height:50vh;
  background-image:
    linear-gradient(rgba(79,70,229,.34) 1px,transparent 1px),
    linear-gradient(90deg,rgba(14,165,233,.30) 1px,transparent 1px)}
#gx-horizon{
  display:block;
  background:radial-gradient(60% 100% at 50% 100%,rgba(255,170,120,.34),rgba(167,139,250,.20) 46%,transparent 74%)}
#gx-fx{
  display:block;opacity:1;animation:none;mix-blend-mode:normal;
  background:
    radial-gradient(ellipse 80% 40% at 50% -8%,rgba(255,255,255,.85),transparent 70%),
    radial-gradient(ellipse at center,transparent 64%,rgba(79,70,229,.07) 100%)}
#gx-fx::after{
  content:"";position:absolute;inset:0;opacity:.05;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
#gx-cursor{background:radial-gradient(circle,rgba(99,102,241,.14),rgba(14,165,233,.07) 42%,transparent 70%)}
#gx-hud i{opacity:.85;filter:drop-shadow(0 0 4px rgba(79,70,229,.30))}
#gx-ribbon{color:var(--t3)}
#gx-ribbon b{color:var(--accent);text-shadow:none}

/* ═══ Panels: frosted crystal glass ═══ */
.metric,.vless-box,.card,.create-panel,.srv-panel,.pw-panel,.tg-panel,.traf-main-stat,.traf-mini,
.traf-chart-card,.conn-hero-tile,.conn-card-v2,.cfg-card,.sub-card,.conn-empty-v2,.subs-empty-v2,
.settings-card,.hero,.lock-card,.sheet,.cp-block,.sub-box,.cl{
  background-color:var(--surface)!important;
  border:1px solid var(--card-b)!important;
  -webkit-backdrop-filter:blur(18px) saturate(1.5);backdrop-filter:blur(18px) saturate(1.5);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.95),
    0 1px 2px rgba(30,41,110,.06),
    0 14px 34px -12px rgba(60,70,170,.22)!important}
.metric:hover,.cfg-card:hover,.sub-card:hover,.conn-card-v2:hover,.traf-mini:hover,.conn-hero-tile:hover,
.settings-card:hover,.proto-card.active{
  box-shadow:0 24px 50px -14px rgba(79,70,229,.34),0 0 0 5px rgba(99,102,241,.06)!important}
.metric:hover,.sub-card:hover,.cfg-card:hover,.conn-card-v2:hover{
  box-shadow:0 26px 54px -14px rgba(79,70,229,.38),0 0 30px rgba(99,102,241,.16)!important}

/* login card: permanent rotating frame, light version */
.shell .card{
  background:
    linear-gradient(var(--gx-panel),var(--gx-panel)) padding-box,
    conic-gradient(from var(--gx-ang),#06b6d4,#6366f1,#d946ef,#f59e0b,#06b6d4) border-box!important;
  box-shadow:0 38px 80px -28px rgba(60,60,170,.42),0 0 60px rgba(99,102,241,.14),inset 0 1px 0 rgba(255,255,255,1)!important}

/* ═══ Modals / sheets / toast ═══ */
.modal,.modal-v2,.sheet,.lock-card{
  border:1px solid rgba(99,102,241,.32)!important;
  background-color:rgba(255,255,255,.97)!important;
  box-shadow:0 0 0 6px rgba(99,102,241,.05),0 34px 80px -22px rgba(40,50,130,.42)!important}
.toast{
  background-color:rgba(255,255,255,.96)!important;color:var(--t1)!important;
  box-shadow:0 18px 44px -12px rgba(40,50,130,.34),0 0 0 1px rgba(99,102,241,.10)!important}

/* ═══ Typography (no neon text-glow on light) ═══ */
.m-val,.traf-main-val,.traf-mini-val,.conn-hero-val,.sub-card-stat-val,.hero-stat-val,.conn-ip-v2,.m-unit{
  text-shadow:none!important}
.brand-name,.logo-name,.mob-title{animation:gxl-glitch 9s steps(1) infinite!important}
.vl-code{text-shadow:none!important}

/* ═══ Hex badges ═══ */
.m-icon,.cp-head-icon,.srv-hero-icon,.pw-hero-icon,.tg-hero-icon,.sub-card-icon,.modal-v2-icon,
.lmodal-icon,.conn-hero-icon,.traf-mini-icon,.srv-tile-icon,.conn-empty-v2-icon,.subs-empty-v2-icon,
.cfg-icon,.settings-icon,.lock-icon,.proto-card-icon,.conn-stat-icon,.log-ic{
  filter:drop-shadow(0 5px 8px rgba(79,70,229,.26))}
.m-icon,.conn-hero-icon,.traf-mini-icon,.srv-tile-icon,.settings-icon,.conn-stat-icon{
  background:linear-gradient(145deg,rgba(99,102,241,.18),rgba(14,165,233,.14))}
.logo-img,.brand-img,.brand-logo,.mob-logo,.conn-avatar{animation:gxl-ring 3.4s ease-out infinite!important}

/* ═══ Buttons: glossy glass-gem ═══ */
.btn-p,.cp-submit-btn,.pw-submit,.btn-primary,.shell .btn,.action-btn.primary{
  background:
    linear-gradient(180deg,rgba(255,255,255,.30),rgba(255,255,255,0) 48%),
    var(--accent-grad)!important;
  text-shadow:0 1px 2px rgba(20,20,90,.40);
  box-shadow:
    inset 0 0 0 1px rgba(255,255,255,.40),
    inset 0 1px 0 rgba(255,255,255,.60),
    inset 0 -12px 20px rgba(40,20,140,.22)!important}
.btn-p:hover,.cp-submit-btn:hover,.pw-submit:hover,.btn-primary:hover,.shell .btn:hover{
  filter:brightness(1.07) saturate(1.15)}
.btn-o:hover,.btn-g:hover,.chip:hover,.nav-it:hover,.lang:hover{
  box-shadow:0 10px 24px -8px rgba(79,70,229,.38)!important}
.chip.active{box-shadow:0 8px 20px -6px rgba(79,70,229,.40)!important}

/* ═══ Inputs ═══ */
.cp-input-full,.fi,.fs,.pw-input,.tg-input,.modal-v2-input,.input-shell input,.lock-input,
.subs-search input,.lmodal-search input,.search input,input[type=text],input[type=password],input[type=number],select,textarea{
  background-color:rgba(255,255,255,.88)!important;
  border:1px solid rgba(79,70,229,.18)!important;
  box-shadow:inset 0 1px 2px rgba(30,41,110,.06)!important;
  caret-color:var(--accent)}
.cp-input-full:focus,.fi:focus,.fs:focus,.pw-input:focus,.tg-input:focus,.modal-v2-input:focus,
.input-shell input:focus,.lock-input:focus,.subs-search input:focus,.lmodal-search input:focus,.search input:focus{
  border-color:#6366f1!important;
  box-shadow:0 0 0 3px rgba(99,102,241,.18),0 10px 24px -10px rgba(99,102,241,.45)!important}

/* ═══ Sidebar / nav ═══ */
.sidebar{
  background:linear-gradient(180deg,rgba(255,255,255,.86),rgba(243,245,255,.74))!important;
  -webkit-backdrop-filter:blur(22px) saturate(1.4);backdrop-filter:blur(22px) saturate(1.4);
  box-shadow:0 0 50px rgba(60,70,170,.12)!important}
.nav-it.on{
  background:linear-gradient(90deg,rgba(99,102,241,.15),transparent 88%)!important;
  box-shadow:inset 0 0 0 1px rgba(99,102,241,.24)!important;color:#27237a!important}
body.ui-fa .nav-it.on{background:linear-gradient(270deg,rgba(99,102,241,.15),transparent 88%)!important}
.nav-it.on i{filter:drop-shadow(0 2px 4px rgba(79,70,229,.35))}
.nav-it.on::after{box-shadow:0 0 8px rgba(192,38,211,.55)}
.nav-sec{opacity:.9}

/* ═══ XP-style segmented bars, light ═══ */
.ubar,.spbar,.usage-track,.cfg-usage-track,.conn-duration-track,.pw-strength{
  background:rgba(99,102,241,.08)!important;
  box-shadow:inset 0 0 0 1px rgba(99,102,241,.18),inset 0 1px 2px rgba(30,41,110,.10)}
.ubar::after,.spbar::after,.usage-track::after,.cfg-usage-track::after,.conn-duration-track::after{
  background:repeating-linear-gradient(90deg,transparent 0 8px,rgba(244,246,253,.96) 8px 10px)}
.ubar-f,.spfill,.usage-fill,.cfg-usage-fill,.conn-duration-fill{
  background:linear-gradient(90deg,#06b6d4,#6366f1 60%,#c026d3)!important;
  box-shadow:0 0 12px rgba(99,102,241,.45)}
[data-gx-tier="warn"]{
  background:linear-gradient(90deg,#f59e0b,#f97316)!important;
  box-shadow:0 0 12px rgba(245,158,11,.50)!important}
[data-gx-tier="crit"]{
  background:linear-gradient(90deg,#f97316,#e11d48)!important;
  box-shadow:0 0 14px rgba(225,29,72,.55)!important}

/* ═══ Badges: readable contrast on light ═══ */
.bg-purple{color:#6d28d9!important}
.bg-green{color:var(--green-t)!important}
.bg-amber{color:var(--amber-t)!important}
.bg-red{color:var(--red-t)!important}
.tb-sub,.page-sub{color:var(--t3)}

/* ═══ Boot screen, light ═══ */
#gx-boot{
  background-color:#f5f7fd;
  background-image:
    radial-gradient(60% 50% at 20% 18%,rgba(99,102,241,.20),transparent 70%),
    radial-gradient(50% 50% at 86% 24%,rgba(14,165,233,.18),transparent 70%),
    radial-gradient(60% 50% at 50% 104%,rgba(244,114,182,.22),transparent 70%)}
#gx-boot.out{filter:blur(8px) brightness(1.08)}
#gx-boot h2{
  color:#1e1b4b;
  text-shadow:2px 0 rgba(192,38,211,.35),-2px 0 rgba(8,145,178,.35),0 10px 34px rgba(99,102,241,.28)}
#gx-boot pre{color:#4338ca;text-shadow:none}
#gx-boot .bar{background:rgba(99,102,241,.12);box-shadow:0 0 0 1px rgba(99,102,241,.30)}
#gx-boot .bar i{background:linear-gradient(90deg,#06b6d4,#6366f1,#d946ef);box-shadow:0 0 14px rgba(99,102,241,.60)}
#gx-boot small{color:rgba(30,27,75,.45)}
"""


def _scope_light(css: str) -> str:
    """Prefix every top-level selector with the light-theme scope.
    At-rules (@keyframes / @media) are passed through untouched."""
    prefix = ':is(html[data-theme="light"],html[data-login-theme="light"]) '
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j == -1:
            break
        sel = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        body = css[j + 1:k - 1]
        if sel.startswith("@"):
            out.append(sel + "{" + body + "}")
        else:
            sels = [prefix + s.strip() for s in sel.split(",") if s.strip()]
            out.append(",".join(sels) + "{" + body + "}")
        i = k
    return "\n".join(out)


DAYLIGHT_CSS = (
    re.sub(r"/\*.*?\*/", "", _LIGHT_TOKENS, flags=re.S)
    + _LIGHT_KEYFRAMES
    + _scope_light(_LIGHT_RULES)
)


def daylight_style_tag() -> str:
    """Return the <style> block for the light layer ('' when disabled)."""
    if os.environ.get("OMID_SKIN_LIGHT", "on").lower() in ("off", "0", "false", "no"):
        return ""
    return '<style id="gx-skin-light">' + DAYLIGHT_CSS + "</style>"
