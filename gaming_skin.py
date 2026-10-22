# -*- coding: utf-8 -*-
"""
OMID // NEON ARENA  ·  gaming skin layer for OMID-IRAN PANEL
────────────────────────────────────────────────────────────
A self-contained visual layer. It does NOT touch any panel logic:
it only appends one <style>, one <link> (fonts) and one <script> to the
existing pages (login, dashboard, public page, single-config page, admin-all).

Usage:   html = inject_gaming_skin(html, mode="dash")   # mode: login|dash|public|admin
Disable: set environment variable OMID_SKIN=off  (pages render exactly as before)
"""
import os

try:
    from daylight_skin import daylight_style_tag
except Exception:  # light layer is optional
    def daylight_style_tag():
        return ''

_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700'
    '&family=Orbitron:wght@500;700;900&display=swap" rel="stylesheet">'
)

GAMING_CSS = r"""
/* ═══════════════════════════════════════════════════════════════════════
   OMID // NEON ARENA  ·  GAMING SKIN
   Layered on top of the shared theme tokens. Dark = Neon Arena,
   Light = "Daylight HUD" (same geometry, softer palette).
   ═══════════════════════════════════════════════════════════════════════ */
@property --gx-ang{syntax:'<angle>';inherits:false;initial-value:0deg}
@keyframes gx-spin{to{--gx-ang:360deg}}

:root{
  --gx-cyan:#00f0ff; --gx-mag:#ff2bd6; --gx-vio:#8b5cff;
  --gx-lime:#b6ff3b; --gx-amber:#ffc400; --gx-red:#ff3d6e;
  --gx-display:'Orbitron','Chakra Petch','Vazirmatn',system-ui,sans-serif;
  --gx-hud:'Chakra Petch','Vazirmatn',system-ui,sans-serif;
  --gx-mono:'JetBrains Mono','Share Tech Mono',ui-monospace,monospace;
  --gx-panel:rgba(9,6,24,.94);
  --gx-chamfer:10px;
}

/* ── DARK · NEON ARENA tokens ───────────────────────────────────────── */
html:not([data-theme="light"]):not([data-login-theme="light"]){
  --bg:#04020c; --bg-2:#080418;
  --bg-gradient:
    radial-gradient(ellipse 60% 50% at 12% 8%,rgba(0,240,255,.10),transparent 62%),
    radial-gradient(ellipse 58% 48% at 92% 14%,rgba(255,43,214,.12),transparent 62%),
    radial-gradient(ellipse 70% 55% at 50% 108%,rgba(139,92,255,.20),transparent 66%);
  --grid:rgba(0,240,255,.035);
  --surface:rgba(14,10,36,.66); --surface-2:rgba(255,255,255,.035);
  --surface-3:rgba(2,1,10,.55); --surface-solid:#0a0720;
  --glass:rgba(7,4,20,.84); --glass-strong:rgba(7,4,20,.93); --overlay:rgba(2,0,10,.78);
  --card-b:rgba(0,240,255,.16); --card-bh:rgba(0,240,255,.55); --hairline:rgba(0,240,255,.08);
  --accent:#00f0ff; --accent-2:#ff2bd6; --accent-3:#8b5cff;
  --accent-soft:rgba(0,240,255,.11); --accent-soft-2:rgba(255,43,214,.10);
  --accent-grad:linear-gradient(135deg,#00a8d6 0%,#6a3dff 58%,#d81bb0 100%);
  --accent-grad-reverse:linear-gradient(135deg,#d81bb0 0%,#6a3dff 45%,#00a8d6 100%);
  --accent-shadow:0 0 0 1px rgba(0,240,255,.30),0 10px 34px rgba(0,240,255,.22),0 0 46px rgba(255,43,214,.14);
  --accent-glow:0 0 12px rgba(0,240,255,.85);
  --green:#39ff88; --green-bg:rgba(57,255,136,.12); --green-t:#39ff88;
  --red:#ff4d73; --red-bg:rgba(255,77,115,.13); --red-t:#ff6b8b;
  --amber:#ffc400; --amber-bg:rgba(255,196,0,.13); --amber-t:#ffd24a;
  --purple:#b388ff; --purple-bg:rgba(179,136,255,.14);
  --t1:#f4fbff; --t2:rgba(220,238,255,.74); --t3:rgba(180,205,255,.50); --muted:rgba(180,205,255,.40);
  --shadow:0 24px 70px rgba(0,0,0,.65),0 0 0 1px rgba(0,240,255,.10);
  --glass-shadow:0 22px 60px rgba(0,0,0,.5),inset 0 1px 0 rgba(0,240,255,.18);
  --focus-ring:0 0 0 3px rgba(0,240,255,.16);
  --login-card:rgba(9,6,24,.9); --login-input:rgba(0,0,0,.42);
  --gx-panel:rgba(9,6,24,.94);
  --gx-glow:rgba(0,240,255,.55);
}
html[data-theme="light"],html[data-login-theme="light"]{
  --gx-panel:rgba(236,246,247,.95);
  --gx-cyan:#2a8fa0; --gx-mag:#7188d5; --gx-vio:#5b6fd0;
  --gx-glow:rgba(79,157,168,.45);
}

/* ── Canvas / base ─────────────────────────────────────────────────── */
html{background-color:var(--bg)!important;background-image:var(--bg-gradient)!important;background-attachment:fixed!important}
body{background:transparent!important;font-family:'Chakra Petch','Vazirmatn',system-ui,sans-serif!important}
body.gx-login{background:transparent!important}
::selection{background:var(--gx-mag);color:#fff}
*{scrollbar-width:thin;scrollbar-color:var(--gx-cyan) transparent}
::-webkit-scrollbar{width:7px;height:7px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:linear-gradient(180deg,var(--gx-cyan),var(--gx-mag));border-radius:0;box-shadow:0 0 8px var(--gx-glow)}

/* ── Background stack (z:-1) ───────────────────────────────────────── */
#gx-bg{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden}
#gx-aurora{position:absolute;inset:-20%;
  background:
    radial-gradient(40% 36% at 22% 30%,rgba(0,240,255,.16),transparent 70%),
    radial-gradient(38% 34% at 78% 24%,rgba(255,43,214,.15),transparent 70%),
    radial-gradient(46% 40% at 55% 78%,rgba(139,92,255,.18),transparent 72%);
  animation:gx-aurora 22s ease-in-out infinite alternate}
@keyframes gx-aurora{0%{transform:translate3d(-3%,-2%,0) scale(1)}50%{transform:translate3d(3%,2%,0) scale(1.08)}100%{transform:translate3d(-2%,3%,0) scale(1.03)}}
#gx-floor{position:absolute;left:-60%;right:-60%;bottom:-2%;height:58vh;
  background-image:
    linear-gradient(rgba(0,240,255,.55) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,43,214,.42) 1px,transparent 1px);
  background-size:70px 70px;
  transform:perspective(380px) rotateX(64deg);transform-origin:50% 100%;
  -webkit-mask-image:linear-gradient(to top,#000 0%,rgba(0,0,0,.55) 40%,transparent 92%);
          mask-image:linear-gradient(to top,#000 0%,rgba(0,0,0,.55) 40%,transparent 92%);
  opacity:.5;animation:gx-floor 3.2s linear infinite}
@keyframes gx-floor{to{background-position:0 70px,70px 0}}
#gx-horizon{position:absolute;left:0;right:0;bottom:0;height:34vh;
  background:radial-gradient(60% 100% at 50% 100%,rgba(139,92,255,.30),rgba(255,43,214,.10) 45%,transparent 72%)}
#gx-cv{position:absolute;inset:0;width:100%;height:100%}
#gx-cursor{position:absolute;left:0;top:0;width:460px;height:460px;margin:-230px 0 0 -230px;border-radius:50%;
  background:radial-gradient(circle,rgba(0,240,255,.13),rgba(255,43,214,.06) 42%,transparent 70%);
  opacity:0;transition:opacity .4s;will-change:transform}
#gx-cursor.on{opacity:1}
html[data-theme="light"] #gx-floor,html[data-login-theme="light"] #gx-floor,
html[data-theme="light"] #gx-horizon,html[data-login-theme="light"] #gx-horizon{display:none}
html[data-theme="light"] #gx-aurora,html[data-login-theme="light"] #gx-aurora{opacity:.45}

/* ── Top overlay (scanlines · vignette · HUD) ──────────────────────── */
#gx-top{position:fixed;inset:0;z-index:9990;pointer-events:none}
#gx-fx{position:absolute;inset:0;
  background:
    repeating-linear-gradient(0deg,rgba(0,0,0,.17) 0 1px,transparent 1px 3px),
    radial-gradient(ellipse at center,transparent 58%,rgba(0,0,0,.50) 100%);
  mix-blend-mode:multiply;opacity:.55;animation:gx-flicker 7s steps(1) infinite}
@keyframes gx-flicker{0%,93%,100%{opacity:.55}94%{opacity:.42}95%{opacity:.6}96%{opacity:.46}}
html[data-theme="light"] #gx-fx,html[data-login-theme="light"] #gx-fx{display:none}
#gx-hud i{position:absolute;width:24px;height:24px;border:2px solid var(--gx-cyan);opacity:.75;filter:drop-shadow(0 0 6px var(--gx-glow))}
#gx-hud i:nth-child(1){top:7px;left:7px;border-right:0;border-bottom:0}
#gx-hud i:nth-child(2){top:7px;right:7px;border-left:0;border-bottom:0;border-color:var(--gx-mag)}
#gx-hud i:nth-child(3){bottom:7px;left:7px;border-right:0;border-top:0;border-color:var(--gx-mag)}
#gx-hud i:nth-child(4){bottom:7px;right:7px;border-left:0;border-top:0}
body.gx-public #gx-hud,body.gx-admin #gx-hud{display:none}
#gx-ribbon{position:absolute;top:6px;left:50%;transform:translateX(-50%);white-space:nowrap;
  font:600 9px/1 var(--gx-mono);letter-spacing:.24em;color:var(--t3);text-transform:uppercase}
#gx-ribbon b{color:var(--gx-cyan);font-weight:700;text-shadow:0 0 10px var(--gx-glow)}
body.gx-login #gx-ribbon{top:auto;bottom:8px}
@media(max-width:1050px){#gx-ribbon{display:none}}
@media(max-width:1050px){body.gx-login #gx-ribbon{display:block}}
@media(max-width:600px){#gx-hud i{width:16px;height:16px}}

/* ── Panels: asymmetric cyber-shape + HUD corner brackets ──────────── */
.metric,.vless-box,.card,.create-panel,.srv-panel,.pw-panel,.tg-panel,.traf-main-stat,.traf-mini,
.traf-chart-card,.conn-hero-tile,.conn-card-v2,.cfg-card,.sub-card,.conn-empty-v2,.subs-empty-v2,
.settings-card,.hero,.lock-card,.sheet,.cp-block,.sub-box,.cl{
  border-radius:4px 22px 4px 22px!important;
  background-image:
    linear-gradient(var(--gx-cyan),var(--gx-cyan)),linear-gradient(var(--gx-cyan),var(--gx-cyan)),
    linear-gradient(var(--gx-mag),var(--gx-mag)),linear-gradient(var(--gx-mag),var(--gx-mag));
  background-size:16px 2px,2px 16px,16px 2px,2px 16px;
  background-position:0 0,0 0,100% 100%,100% 100%;
  background-repeat:no-repeat;
}
.cp-block,.sub-box,.cl{border-radius:3px 14px 3px 14px!important;background-size:10px 1px,1px 10px,10px 1px,1px 10px}
.cfg-card,.conn-card-v2{border-radius:4px 18px 4px 18px!important}

/* animated neon conic border on hover (interactive tiles only) */
.metric:hover,.cfg-card:hover,.sub-card:hover,.conn-card-v2:hover,.traf-mini:hover,.conn-hero-tile:hover,
.settings-card:hover,.proto-card.active{
  border-color:transparent!important;
  background-image:
    linear-gradient(var(--gx-cyan),var(--gx-cyan)),linear-gradient(var(--gx-cyan),var(--gx-cyan)),
    linear-gradient(var(--gx-mag),var(--gx-mag)),linear-gradient(var(--gx-mag),var(--gx-mag)),
    linear-gradient(var(--surface-solid),var(--surface-solid)),
    conic-gradient(from var(--gx-ang),var(--gx-cyan),var(--gx-vio),var(--gx-mag),var(--gx-amber),var(--gx-cyan))!important;
  background-size:16px 2px,2px 16px,16px 2px,2px 16px,auto,auto!important;
  background-position:0 0,0 0,100% 100%,100% 100%,0 0,0 0!important;
  background-origin:border-box!important;
  background-repeat:no-repeat!important;
  background-clip:padding-box,padding-box,padding-box,padding-box,padding-box,border-box!important;
  animation:gx-spin 4.5s linear infinite;
}
.metric:hover,.sub-card:hover,.cfg-card:hover,.conn-card-v2:hover{box-shadow:0 18px 50px rgba(0,0,0,.45),0 0 34px var(--gx-glow)!important}

/* Login card — permanent rotating frame */
.shell .card{
  border:1px solid transparent!important;border-radius:6px 32px 6px 32px!important;
  background:
    linear-gradient(var(--gx-panel),var(--gx-panel)) padding-box,
    conic-gradient(from var(--gx-ang),var(--gx-cyan),var(--gx-vio),var(--gx-mag),var(--gx-cyan)) border-box!important;
  animation:gx-spin 7s linear infinite;
  box-shadow:0 30px 90px rgba(0,0,0,.6),0 0 60px var(--gx-glow)!important;
}
.shell .card::after{opacity:.9}
.shell{animation:gx-rise .7s cubic-bezier(.2,.8,.2,1) both}
@keyframes gx-rise{from{opacity:0;transform:translateY(24px) scale(.97)}to{opacity:1;transform:none}}

/* Modals / sheets */
.modal,.modal-v2,.sheet,.lock-card{
  border:1px solid var(--gx-cyan)!important;border-radius:4px 26px 4px 26px!important;
  background-color:var(--gx-panel)!important;
  box-shadow:0 0 0 1px rgba(0,240,255,.12),0 30px 90px rgba(0,0,0,.7),0 0 60px var(--gx-glow)!important;
  animation:gx-pop .3s cubic-bezier(.2,1.2,.3,1) both!important;
}
@keyframes gx-pop{0%{opacity:0;transform:scale(.94) translateY(10px);filter:brightness(2)}60%{filter:brightness(1.2)}100%{opacity:1;transform:none;filter:none}}

/* ── Typography ────────────────────────────────────────────────────── */
.m-val,.traf-main-val,.traf-mini-val,.conn-hero-val,.sub-card-stat-val,.hero-stat-val,.conn-ip-v2,.m-unit{
  font-family:var(--gx-display)!important;letter-spacing:.02em;
  text-shadow:0 0 18px var(--gx-glow)}
.m-val{font-size:24px!important}
.traf-main-val{font-size:30px!important}
.brand-name,.logo-name,.mob-title,.cp-head-title,.srv-hero-domain,.pw-hero-title,.tg-hero-title,
.sub-card-name-v2,.tb-title,.kicker,.modal-title,.modal-v2-title,.lock-title,.card-title,.section-title,.cfg-label{
  font-family:var(--gx-display)!important;letter-spacing:.06em}
.tb-title{font-size:17px!important}
.cfg-label,.sub-card-name-v2,.card-title,.section-title{font-size:12.5px!important}
.m-label,.nav-sec,.m-sub,.traf-main-label,.traf-mini-label,.conn-hero-label,.cp-block-label,.fg label,
.pw-field label,.tg-field label,.modal-v2-field label,.srv-tile-label,.hero-stat-label,.sub-card-stat-label{
  font-family:var(--gx-hud)!important;letter-spacing:.14em!important;font-weight:700}
.nav-it,.btn,.chip,.badge,.exp-chip,.proto-chip,.nav-item{font-family:var(--gx-hud)!important;letter-spacing:.04em}
h1{font-family:var(--gx-display)!important;letter-spacing:.03em}
h1 .accent,.accent{
  background:var(--accent-grad);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent;
  filter:drop-shadow(0 0 14px var(--gx-glow))}
html[data-theme="light"] h1 .accent,html[data-login-theme="light"] h1 .accent{filter:none}

/* chromatic glitch burst */
.brand-name,.logo-name,.mob-title{animation:gx-glitch 7s steps(1) infinite}
@keyframes gx-glitch{
  0%,90%,100%{text-shadow:0 0 14px var(--gx-glow)}
  91%{text-shadow:3px 0 var(--gx-mag),-3px 0 var(--gx-cyan);transform:translateX(1px)}
  93%{text-shadow:-3px 0 var(--gx-mag),3px 0 var(--gx-cyan);transform:translateX(-1px) skewX(-4deg)}
  95%{text-shadow:2px 1px var(--gx-mag),-2px -1px var(--gx-cyan);transform:none}
}

/* ── Hex badges for icon tiles ─────────────────────────────────────── */
.m-icon,.cp-head-icon,.srv-hero-icon,.pw-hero-icon,.tg-hero-icon,.sub-card-icon,.modal-v2-icon,
.lmodal-icon,.conn-hero-icon,.traf-mini-icon,.srv-tile-icon,.conn-empty-v2-icon,.subs-empty-v2-icon,
.cfg-icon,.settings-icon,.lock-icon,.proto-card-icon,.conn-stat-icon,.log-ic{
  clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);
  border-radius:0!important;box-shadow:none!important;
  filter:drop-shadow(0 0 7px var(--gx-glow))}
.m-icon,.conn-hero-icon,.traf-mini-icon,.srv-tile-icon,.settings-icon,.conn-stat-icon{background:var(--accent-soft)}
.logo-img,.brand-img,.brand-logo,.mob-logo,.conn-avatar{
  border-radius:4px 14px 4px 14px!important;position:relative;
  animation:gx-ring 3.2s ease-out infinite}
@keyframes gx-ring{0%{box-shadow:0 0 0 0 rgba(0,240,255,.55),0 0 18px rgba(0,240,255,.35)}100%{box-shadow:0 0 0 14px rgba(0,240,255,0),0 0 18px rgba(0,240,255,.35)}}

/* ── Buttons ───────────────────────────────────────────────────────── */
.btn,.chip,.badge,.exp-chip,.proto-chip,.lmodal-qbtn,.traf-range-tab,.lang,.theme-btn,.side-lang,.logout-btn,
.menu-btn,.theme-mob,.icon-btn,.cfg-btn,.action-btn,.segment{border-radius:3px 11px 3px 11px!important}
.btn-p,.cp-submit-btn,.pw-submit,.btn-primary,.shell .btn,.action-btn.primary{
  border-radius:0!important;border:none!important;color:#fff!important;font-weight:800!important;
  text-shadow:0 1px 3px rgba(0,0,0,.55);letter-spacing:.08em!important;
  clip-path:polygon(var(--gx-chamfer) 0,100% 0,100% calc(100% - var(--gx-chamfer)),calc(100% - var(--gx-chamfer)) 100%,0 100%,0 var(--gx-chamfer));
  background:var(--accent-grad)!important;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.28),inset 0 -12px 22px rgba(0,0,0,.28),inset 0 12px 20px rgba(255,255,255,.10)!important;
  transition:filter .18s,transform .18s!important}
.btn-p:hover,.cp-submit-btn:hover,.pw-submit:hover,.btn-primary:hover,.shell .btn:hover{filter:brightness(1.18) saturate(1.2);transform:translateY(-2px)}
.btn-p:active,.cp-submit-btn:active,.pw-submit:active,.btn-primary:active{transform:translateY(0) scale(.97)}
.btn-o:hover,.btn-g:hover,.chip:hover,.nav-it:hover,.lang:hover{box-shadow:0 0 18px var(--gx-glow)}
.chip.active{box-shadow:0 0 18px var(--gx-glow)!important}

/* ── Inputs ────────────────────────────────────────────────────────── */
.cp-input-full,.fi,.fs,.pw-input,.tg-input,.modal-v2-input,.input-shell input,.lock-input,
.subs-search input,.lmodal-search input,.search input,input[type=text],input[type=password],input[type=number],select,textarea{
  border-radius:3px 12px 3px 12px!important;caret-color:var(--gx-cyan)}
.cp-input-full:focus,.fi:focus,.fs:focus,.pw-input:focus,.tg-input:focus,.modal-v2-input:focus,
.input-shell input:focus,.lock-input:focus,.subs-search input:focus,.lmodal-search input:focus,.search input:focus{
  border-color:var(--gx-cyan)!important;
  box-shadow:0 0 0 1px var(--gx-cyan),0 0 22px var(--gx-glow),inset 0 0 14px rgba(0,240,255,.07)!important}

/* ── Sidebar / nav ─────────────────────────────────────────────────── */
.sidebar{border-inline-end:1px solid transparent!important;
  border-image:linear-gradient(180deg,transparent,var(--gx-cyan) 22%,var(--gx-mag) 78%,transparent) 1;
  box-shadow:0 0 50px rgba(0,0,0,.5)}
.side-telemetry{border-radius:3px 14px 3px 14px!important}
.nav-it{border-radius:3px 12px 3px 12px!important}
.nav-it.on{
  background:linear-gradient(90deg,var(--accent-soft),transparent 85%)!important;
  box-shadow:inset 0 0 30px var(--accent-soft),0 0 0 1px var(--card-b)!important;color:var(--t1)!important}
body.ui-fa .nav-it.on{background:linear-gradient(270deg,var(--accent-soft),transparent 85%)!important}
.nav-it.on i{color:var(--gx-cyan)!important;filter:drop-shadow(0 0 6px var(--gx-glow))}
.nav-it.on::after{content:"";position:absolute;inset-inline-end:10px;top:50%;width:7px;height:7px;margin-top:-3.5px;
  background:var(--gx-mag);transform:rotate(45deg);box-shadow:0 0 12px var(--gx-mag);animation:gx-blink 1.4s steps(2) infinite}
@keyframes gx-blink{50%{opacity:.25}}
.nav-sec{position:relative;padding-inline-start:22px!important;color:var(--gx-cyan)!important;opacity:.75}
.nav-sec::before{content:"//";position:absolute;inset-inline-start:8px;color:var(--gx-mag)}
.nav-item.active{box-shadow:0 0 18px var(--gx-glow)}

/* ── XP-style segmented progress bars ──────────────────────────────── */
.ubar,.spbar,.usage-track,.cfg-usage-track,.conn-duration-track,.pw-strength{
  height:9px!important;border-radius:2px!important;position:relative;
  background:var(--surface-3)!important;box-shadow:inset 0 0 0 1px var(--card-b)}
.ubar::after,.spbar::after,.usage-track::after,.cfg-usage-track::after,.conn-duration-track::after{
  content:"";position:absolute;inset:0;pointer-events:none;z-index:2;
  background:repeating-linear-gradient(90deg,transparent 0 8px,rgba(4,2,12,.88) 8px 10px)}
.ubar-f,.spfill,.usage-fill,.cfg-usage-fill,.conn-duration-fill{
  border-radius:1px!important;
  background:linear-gradient(90deg,var(--gx-cyan),var(--gx-vio))!important;
  box-shadow:0 0 14px var(--gx-glow)}
[data-gx-tier="warn"]{background:linear-gradient(90deg,#ffc400,#ff8a00)!important;box-shadow:0 0 14px rgba(255,196,0,.6)!important}
[data-gx-tier="crit"]{background:linear-gradient(90deg,#ff8a00,#ff2b5e)!important;box-shadow:0 0 16px rgba(255,43,94,.75)!important;animation:gx-crit 1s ease-in-out infinite}
@keyframes gx-crit{50%{filter:brightness(1.4)}}
.traf-legend-dot{border-radius:0!important;transform:rotate(45deg)}

/* ── Status radar dots ─────────────────────────────────────────────── */
.cfg-status-dot,.status-dot,.telemetry-led,.conn-live-dot{--gx-dot:var(--green);animation:gx-ping 1.8s ease-out infinite!important}
.cfg-card.is-off .cfg-status-dot{--gx-dot:var(--red)}
.cfg-card.is-exp .cfg-status-dot{--gx-dot:var(--amber)}
@keyframes gx-ping{0%{box-shadow:0 0 0 0 var(--gx-dot),0 0 8px var(--gx-dot)}80%,100%{box-shadow:0 0 0 10px transparent,0 0 8px var(--gx-dot)}}
.tog.on{box-shadow:0 0 14px var(--gx-glow)}

/* ── Toast ─────────────────────────────────────────────────────────── */
.toast{border-radius:3px 14px 3px 14px!important;border-inline-start:4px solid var(--gx-cyan)!important;
  font-family:var(--gx-hud)!important;letter-spacing:.05em;box-shadow:0 14px 50px rgba(0,0,0,.6),0 0 30px var(--gx-glow)!important}
.toast.ok{border-inline-start-color:var(--green)!important}
.toast.err{border-inline-start-color:var(--red)!important}

/* ── Misc ──────────────────────────────────────────────────────────── */
.vl-code,.sub-url,.cfg-uuid-mini,.emsg{font-family:var(--gx-mono)!important}
.vl-code{border-inline-start:3px solid var(--gx-mag)!important;border-radius:3px 12px 3px 12px!important;
  text-shadow:0 0 12px rgba(255,43,214,.35)}
.pg.on{animation:gx-page .35s cubic-bezier(.2,.9,.3,1)}
@keyframes gx-page{from{opacity:0;transform:translateY(14px);filter:blur(4px)}to{opacity:1;transform:none;filter:none}}
.metric{animation:gx-rise .6s cubic-bezier(.2,.8,.2,1) both}
.metric:nth-child(2){animation-delay:.07s}.metric:nth-child(3){animation-delay:.14s}.metric:nth-child(4){animation-delay:.21s}
.cfg-card,.sub-card,.conn-card-v2{animation:gx-rise .5s cubic-bezier(.2,.8,.2,1) both}
.top-status{border-radius:3px 10px 3px 10px!important}
.meta{border-radius:3px 12px 3px 12px!important;font-family:var(--gx-hud)}
.scan{height:2px!important;background:linear-gradient(90deg,transparent,var(--gx-cyan),var(--gx-mag),transparent)!important;
  box-shadow:0 0 28px var(--gx-cyan),0 0 60px var(--gx-mag)!important;opacity:.7!important}

/* ── Boot screen ───────────────────────────────────────────────────── */
#gx-boot{position:fixed;inset:0;z-index:99999;background:#04020c;display:flex;align-items:center;justify-content:center;
  flex-direction:column;gap:18px;cursor:pointer;transition:opacity .45s,filter .45s;
  background-image:repeating-linear-gradient(0deg,rgba(0,240,255,.05) 0 1px,transparent 1px 3px)}
#gx-boot.out{opacity:0;filter:blur(8px) brightness(2);pointer-events:none}
#gx-boot h2{font:900 clamp(26px,7vw,54px)/1 'Orbitron',sans-serif;letter-spacing:.18em;color:#fff;
  text-shadow:3px 0 var(--gx-mag),-3px 0 var(--gx-cyan),0 0 40px rgba(0,240,255,.6);animation:gx-glitch 1.1s steps(1) infinite}
#gx-boot pre{font:600 11px/1.9 var(--gx-mono);color:var(--gx-cyan);letter-spacing:.12em;min-height:76px;text-align:start;margin:0;text-shadow:0 0 10px var(--gx-glow)}
#gx-boot .bar{width:min(320px,70vw);height:6px;background:rgba(255,255,255,.08);box-shadow:0 0 0 1px rgba(0,240,255,.3);position:relative;overflow:hidden}
#gx-boot .bar i{position:absolute;inset:0;width:0;background:linear-gradient(90deg,var(--gx-cyan),var(--gx-mag));box-shadow:0 0 20px var(--gx-cyan);animation:gx-load 1.35s cubic-bezier(.6,0,.2,1) forwards}
@keyframes gx-load{to{width:100%}}
#gx-boot small{font:600 9px var(--gx-mono);letter-spacing:.3em;color:rgba(255,255,255,.35)}

/* ── Overdrive (konami) ────────────────────────────────────────────── */
body.gx-overdrive{animation:gx-hue 2.4s linear infinite}
@keyframes gx-hue{to{filter:hue-rotate(360deg)}}
body.gx-overdrive #gx-floor{animation-duration:.8s;opacity:.6}

/* ── Responsive / accessibility ────────────────────────────────────── */
@media(max-width:700px){
  #gx-floor{opacity:.22}
  .m-val{font-size:21px!important}
  .metric,.cfg-card,.sub-card,.conn-card-v2{border-radius:4px 16px 4px 16px!important}
  #gx-cursor{display:none}
}
@media(hover:none){#gx-cursor{display:none}}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}
  #gx-boot{display:none}
}
/* ── Effects switch · html[data-fx="full|lite|off"] (Settings > Appearance) ── */
html[data-fx="lite"] body.gx #gx-floor,
html[data-fx="lite"] body.gx #gx-cv,
html[data-fx="lite"] body.gx #gx-cursor,
html[data-fx="lite"] body.gx #gx-fx,
html[data-fx="lite"] body.gx #gx-boot{display:none!important}
html[data-fx="lite"] body.gx *,
html[data-fx="lite"] body.gx *::before,
html[data-fx="lite"] body.gx *::after{animation-duration:.001ms!important;animation-iteration-count:1!important}
html[data-fx="off"] body.gx #gx-bg,
html[data-fx="off"] body.gx #gx-top,
html[data-fx="off"] body.gx #gx-boot{display:none!important}
html[data-fx="off"] body.gx *,
html[data-fx="off"] body.gx *::before,
html[data-fx="off"] body.gx *::after{
  animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;
  backdrop-filter:none!important;-webkit-backdrop-filter:none!important;text-shadow:none!important}

"""

GAMING_JS = r"""
(function(){
  if(window.__GX__)return;window.__GX__=1;
  var MODE=window.__GX_MODE__||'dash';
  var doc=document,root=doc.documentElement;
  var reduce=false,fine=false;
  try{reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;fine=matchMedia('(pointer:fine)').matches}catch(e){}

  /* ── Effects mode: full | lite | off  (saved in localStorage 'omid_fx') ──
     No saved choice → auto: lite on weak / small / reduced-motion devices, full otherwise. */
  function autoFx(){
    try{
      var n=navigator,c=n.connection||{};
      if(reduce||c.saveData||(n.hardwareConcurrency&&n.hardwareConcurrency<=4)||(n.deviceMemory&&n.deviceMemory<=4)||Math.min(screen.width,window.innerWidth)<700)return 'lite';
    }catch(e){}
    return 'full';
  }
  function readFx(){var v=null;try{v=localStorage.getItem('omid_fx')}catch(e){}return(v==='full'||v==='lite'||v==='off')?v:autoFx()}
  function fxMode(){return root.getAttribute('data-fx')||'full'}
  root.setAttribute('data-fx',readFx());
  var fxApply=function(){};
  window.omidSetFx=function(m){
    if(m!=='full'&&m!=='lite'&&m!=='off')return;
    try{localStorage.setItem('omid_fx',m)}catch(e){}
    root.setAttribute('data-fx',m);
    if(doc.body&&m!=='full')doc.body.classList.remove('gx-overdrive');
    fxApply();
  };

  function init(){
    var body=doc.body;if(!body)return;
    body.classList.add('gx','gx-'+MODE);

    /* ── layers ── */
    var bg=doc.createElement('div');bg.id='gx-bg';bg.setAttribute('aria-hidden','true');bg.setAttribute('translate','no');
    bg.innerHTML='<div id="gx-aurora"></div><div id="gx-floor"></div><div id="gx-horizon"></div><canvas id="gx-cv"></canvas><div id="gx-cursor"></div>';
    var top=doc.createElement('div');top.id='gx-top';top.setAttribute('aria-hidden','true');top.setAttribute('translate','no');
    top.innerHTML='<div id="gx-fx"></div><div id="gx-hud"><i></i><i></i><i></i><i></i><div id="gx-ribbon"></div></div>';
    body.insertBefore(bg,body.firstChild);body.appendChild(top);

    /* ── theme-aware colours ── */
    function isLight(){return root.getAttribute('data-theme')==='light'||root.getAttribute('data-login-theme')==='light'}
    var C1=[0,240,255],C2=[255,43,214];
    function readTheme(){ if(isLight()){C1=[79,70,229];C2=[8,145,178]}else{C1=[0,240,255];C2=[255,43,214]} }
    readTheme();
    try{new MutationObserver(readTheme).observe(root,{attributes:true,attributeFilter:['data-theme','data-login-theme']})}catch(e){}

    /* ── particle network canvas ── */
    var cv=doc.getElementById('gx-cv'),cx=cv.getContext('2d'),cur=doc.getElementById('gx-cursor');
    var W=0,H=0,DPR=Math.min(window.devicePixelRatio||1,1.5),P=[],S=[],mx=-9999,my=-9999,tx=0,ty=0,gx=0,gy=0,run=true,last=0;
    function size(){
      W=window.innerWidth;H=window.innerHeight;cv.width=W*DPR;cv.height=H*DPR;cx.setTransform(DPR,0,0,DPR,0,0);
      var n=(reduce||fxMode()!=='full')?0:Math.min(W<700?34:84,Math.round(W*H/16000));
      while(P.length<n)P.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.35,vy:(Math.random()-.5)*.35,r:Math.random()*1.6+.6,m:Math.random()<.35});
      P.length=n;
    }
    size();window.addEventListener('resize',size);
    function rgba(c,a){return 'rgba('+c[0]+','+c[1]+','+c[2]+','+a+')'}
    var LINK=130,LINK2=LINK*LINK;
    function frame(t){
      if(!run){return}
      requestAnimationFrame(frame);
      if(t-last<20)return;last=t;
      cx.clearRect(0,0,W,H);
      var light=isLight(),aMul=light?.7:1,i,j,p,q,dx,dy,d;
      for(i=0;i<P.length;i++){
        p=P[i];p.x+=p.vx;p.y+=p.vy;
        if(p.x<-10)p.x=W+10;else if(p.x>W+10)p.x=-10;
        if(p.y<-10)p.y=H+10;else if(p.y>H+10)p.y=-10;
        dx=p.x-mx;dy=p.y-my;d=dx*dx+dy*dy;
        if(d<22000&&d>1){var f=(1-d/22000)*.02;p.vx+=dx*f*.02;p.vy+=dy*f*.02}
        p.vx*=.999;p.vy*=.999;
        cx.beginPath();cx.fillStyle=rgba(p.m?C2:C1,.85*aMul);cx.arc(p.x,p.y,p.r,0,6.2832);cx.fill();
        for(j=i+1;j<P.length;j++){
          q=P[j];dx=p.x-q.x;dy=p.y-q.y;d=dx*dx+dy*dy;
          if(d<LINK2){cx.strokeStyle=rgba(p.m?C2:C1,(1-d/LINK2)*.28*aMul);cx.lineWidth=.7;cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(q.x,q.y);cx.stroke()}
        }
        dx=p.x-mx;dy=p.y-my;d=dx*dx+dy*dy;
        if(d<30000){cx.strokeStyle=rgba(C1,(1-d/30000)*.55*aMul);cx.lineWidth=.9;cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(mx,my);cx.stroke()}
      }
      /* click sparks */
      for(i=S.length-1;i>=0;i--){
        p=S[i];p.x+=p.vx;p.y+=p.vy;p.vy+=.06;p.l-=.025;
        if(p.l<=0){S.splice(i,1);continue}
        cx.fillStyle=rgba(p.c,p.l);cx.fillRect(p.x,p.y,2.2,2.2);
      }
      /* cursor glow easing */
      if(fine){gx+=(tx-gx)*.12;gy+=(ty-gy)*.12;cur.style.transform='translate3d('+gx+'px,'+gy+'px,0)'}
    }
    if(reduce||fxMode()!=='full'){frame(100);run=false}else{requestAnimationFrame(frame)}
    doc.addEventListener('visibilitychange',function(){
      if(reduce||fxMode()!=='full')return;
      if(doc.hidden){run=false}else if(!run){run=true;requestAnimationFrame(frame)}
    });
    fxApply=function(){
      size();                                   /* rebuilds / empties the particle set */
      if(fxMode()==='full'&&!reduce){if(!run){run=true;requestAnimationFrame(frame)}}
      else{run=false;cx.clearRect(0,0,W,H);untilt()}
    };

    /* ── pointer effects ── */
    var tilted=null;
    function untilt(){if(tilted){tilted.style.transform='';tilted.style.transition='';tilted=null}}
    doc.addEventListener('pointermove',function(e){
      mx=e.clientX;my=e.clientY;tx=mx;ty=my;
      if(fine&&!reduce&&fxMode()==='full'){
        cur.classList.add('on');
        var el=e.target&&e.target.closest?e.target.closest('.metric,.sub-card,.hero-stat,.traf-mini,.conn-hero-tile'):null;
        if(el!==tilted)untilt();
        if(el){
          var r=el.getBoundingClientRect(),px=(e.clientX-r.left)/r.width-.5,py=(e.clientY-r.top)/r.height-.5;
          el.style.transition='transform .08s linear';
          el.style.transform='perspective(800px) rotateX('+(-py*7).toFixed(2)+'deg) rotateY('+(px*9).toFixed(2)+'deg) translateY(-4px)';
          tilted=el;
        }
      }
    },{passive:true});
    doc.addEventListener('pointerleave',function(){mx=my=-9999;cur.classList.remove('on');untilt()});
    doc.addEventListener('pointerdown',function(e){
      if(reduce||fxMode()!=='full')return;
      var t=e.target&&e.target.closest?e.target.closest('button,.btn,.nav-it,.nav-item,.chip,.proto-card,a,.tog'):null;
      if(!t)return;
      for(var k=0;k<16;k++){var a=Math.random()*6.2832,s=Math.random()*3+1;
        S.push({x:e.clientX,y:e.clientY,vx:Math.cos(a)*s,vy:Math.sin(a)*s-1.2,l:1,c:Math.random()<.5?C1:C2})}
    },{passive:true});

    /* ── XP-bar tier tagging (reads the width the panel already sets) ── */
    var FILL='.ubar-f,.spfill,.usage-fill,.cfg-usage-fill';
    function tier(el){
      var w=parseFloat(el.style.width);if(isNaN(w))return;
      var t=w>=85?'crit':(w>=60?'warn':'');
      if(t){if(el.getAttribute('data-gx-tier')!==t)el.setAttribute('data-gx-tier',t)}else if(el.hasAttribute('data-gx-tier'))el.removeAttribute('data-gx-tier');
    }
    function scan(scope){try{(scope||doc).querySelectorAll(FILL).forEach(tier)}catch(e){}}
    scan();
    var tmr=0;
    function sched(){clearTimeout(tmr);tmr=setTimeout(scan,120)}
    try{new MutationObserver(sched).observe(body,{subtree:true,childList:true,attributes:true,attributeFilter:['style']})}catch(e){}

    /* ── HUD ribbon clock (text node mutated in place: no childList churn) ── */
    if(MODE==='login'||MODE==='dash'){
      var rb=doc.getElementById('gx-ribbon'),tn=doc.createTextNode('');rb.appendChild(tn);
      var pad=function(n){return n<10?'0'+n:n};
      var tick=function(){var d=new Date();tn.nodeValue='\u25E2 OMID//ARENA \u25AA '+(navigator.onLine?'LINK ONLINE':'LINK OFFLINE')+' \u25AA '+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds())+' \u25E3'};
      tick();setInterval(tick,1000);
    }

    /* ── Boot screen (once per session; click / key to skip) ── */
    var seen=false;try{seen=sessionStorage.getItem('gx_boot')==='1'}catch(e){}
    if(!reduce&&fxMode()==='full'&&!seen&&(MODE==='login'||MODE==='dash')){
      try{sessionStorage.setItem('gx_boot','1')}catch(e){}
      var b=doc.createElement('div');b.id='gx-boot';b.setAttribute('translate','no');
      b.innerHTML='<h2>OMID//ARENA</h2><pre id="gx-boot-t"></pre><div class="bar"><i></i></div><small>CLICK TO SKIP</small>';
      body.appendChild(b);
      var lines=['> INITIALIZING NEON CORE ........ OK','> LINKING RELAY NODES .......... OK','> SYNCING TELEMETRY ............ OK','> ARENA READY'],li=0,pre=doc.getElementById('gx-boot-t');
      var tt=doc.createTextNode('');pre.appendChild(tt);
      var typer=setInterval(function(){if(li>=lines.length){clearInterval(typer);return}tt.nodeValue+=lines[li++]+'\n'},300);
      var done=false;
      function kill(){if(done)return;done=true;clearInterval(typer);b.classList.add('out');setTimeout(function(){if(b.parentNode)b.parentNode.removeChild(b)},480)}
      b.addEventListener('click',kill);doc.addEventListener('keydown',kill,{once:true});
      setTimeout(kill,1600);
    }

    /* ── Konami → OVERDRIVE ── */
    var seq=[38,38,40,40,37,39,37,39,66,65],pos=0;
    doc.addEventListener('keydown',function(e){
      pos=(e.keyCode===seq[pos])?pos+1:(e.keyCode===seq[0]?1:0);
      if(pos===seq.length){pos=0;if(fxMode()==='full')body.classList.toggle('gx-overdrive')}
    });
  }
  if(doc.readyState==='loading')doc.addEventListener('DOMContentLoaded',init);else init();
})();
"""


def inject_gaming_skin(html: str, mode: str = "dash") -> str:
    """Append the skin to a complete HTML document. Idempotent and failure-safe."""
    if os.environ.get("OMID_SKIN", "on").lower() in ("off", "0", "false", "no"):
        return html
    if not isinstance(html, str) or "id=\"gx-skin\"" in html:
        return html
    head_block = (
        _FONTS
        + '<style id="gx-skin">' + GAMING_CSS + "</style>"
        + daylight_style_tag()
    )
    body_block = (
        '<script id="gx-skin-js">window.__GX_MODE__="%s";</script>' % mode
        + "<script>" + GAMING_JS + "</script>"
    )
    low = html.lower()
    h = low.rfind("</head>")
    html = (html[:h] + head_block + html[h:]) if h != -1 else (head_block + html)
    low = html.lower()
    b = low.rfind("</body>")
    html = (html[:b] + body_block + html[b:]) if b != -1 else (html + body_block)
    return html
