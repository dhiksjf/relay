"""
Relay Drive — single-file edition
FastAPI backend + React SPA frontend embedded as HTML string.
No MongoDB. No Node. No build step. Just Python.
"""

# ─────────────────────────────────────────────────────────
# EMBEDDED FRONTEND
# ─────────────────────────────────────────────────────────
HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Relay Drive</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:         #04040e;
  --bg2:        #070714;
  --surface:    #0b0b1f;
  --surface2:   #111128;
  --surface3:   #18183a;
  --border:     rgba(139,92,246,0.1);
  --border2:    rgba(139,92,246,0.2);
  --border3:    rgba(255,255,255,0.06);
  --text:       #eeeeff;
  --text2:      #c4c4e0;
  --muted:      #5a5a80;
  --muted2:     #8888b0;
  --primary:    #818cf8;
  --primary2:   #a5b4fc;
  --primary3:   #6366f1;
  --primary-bg: rgba(99,102,241,0.1);
  --primary-border: rgba(99,102,241,0.3);
  --green:      #34d399;
  --green-bg:   rgba(52,211,153,0.1);
  --green-border:rgba(52,211,153,0.25);
  --red:        #f87171;
  --red-bg:     rgba(248,113,113,0.1);
  --red-border: rgba(248,113,113,0.25);
  --amber:      #fbbf24;
  --amber-bg:   rgba(251,191,36,0.1);
  --amber-border:rgba(251,191,36,0.25);
  --blue:       #60a5fa;
  --blue-bg:    rgba(96,165,250,0.1);
  --blue-border:rgba(96,165,250,0.25);
  --cyan:       #22d3ee;
  --sidebar-w:  240px;
  --radius:     10px;
  --radius-lg:  14px;
  --radius-xl:  18px;
}
html,body{height:100%;background:var(--bg);color:var(--text);font-family:'Outfit',sans-serif;font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased}
::selection{background:rgba(99,102,241,0.35)}
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(139,92,246,0.2);border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:rgba(139,92,246,0.4)}

/* ── Background orbs ── */
.bg-orb{position:fixed;pointer-events:none;z-index:0;border-radius:50%;filter:blur(80px);opacity:0.35}
.bg-orb-1{width:500px;height:500px;background:radial-gradient(circle,rgba(99,102,241,0.15),transparent 70%);top:-150px;left:-100px}
.bg-orb-2{width:400px;height:400px;background:radial-gradient(circle,rgba(139,92,246,0.1),transparent 70%);bottom:-100px;right:-80px}

/* ── Layout ── */
.app-shell{display:flex;min-height:100vh;position:relative}
.sidebar{
  width:var(--sidebar-w);flex-shrink:0;
  background:rgba(11,11,31,0.8);
  backdrop-filter:blur(20px);
  border-right:1px solid var(--border);
  display:flex;flex-direction:column;
  position:fixed;top:0;left:0;height:100vh;z-index:40;
  padding:0 10px;
}
.main-content{margin-left:var(--sidebar-w);flex:1;min-height:100vh;display:flex;flex-direction:column;position:relative;z-index:1}
.page-body{max-width:1080px;width:100%;margin:0 auto;padding:28px 24px 80px}

/* ── Sidebar internals ── */
.sidebar-logo{display:flex;align-items:center;gap:11px;padding:20px 8px 16px}
.logo-icon{
  width:36px;height:36px;border-radius:10px;
  background:linear-gradient(135deg,#6366f1,#8b5cf6);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 20px rgba(99,102,241,0.4);
  flex-shrink:0;
}
.logo-text{font-size:15px;font-weight:800;letter-spacing:-0.3px;color:var(--text)}
.logo-sub{font-size:10px;color:var(--muted);letter-spacing:0.4px;font-weight:500}
.sidebar-nav{display:flex;flex-direction:column;gap:1px;flex:1;padding-bottom:10px}
.nav-section-label{font-size:10px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1.2px;padding:12px 12px 5px}
.nav-item{
  display:flex;align-items:center;gap:10px;
  padding:9px 11px;border-radius:9px;
  color:var(--muted2);font-weight:500;font-size:13px;
  cursor:pointer;transition:all 0.14s;text-decoration:none;
  border:1px solid transparent;position:relative;
}
.nav-item:hover{background:var(--surface2);color:var(--text);border-color:var(--border3)}
.nav-item.active{
  background:var(--primary-bg);color:var(--primary2);
  border-color:var(--primary-border);
}
.nav-item.active::before{content:'';position:absolute;left:-10px;top:50%;transform:translateY(-50%);width:3px;height:20px;background:linear-gradient(180deg,var(--primary),var(--primary3));border-radius:0 2px 2px 0}
.nav-item svg{opacity:0.65;flex-shrink:0;transition:opacity 0.14s}
.nav-item.active svg,.nav-item:hover svg{opacity:1}
.sidebar-footer{border-top:1px solid var(--border);padding:12px 4px 10px}
.user-card{display:flex;align-items:center;gap:10px;padding:10px;border-radius:10px;background:var(--surface2);border:1px solid var(--border3);margin-bottom:8px}
.user-avatar{
  width:32px;height:32px;border-radius:8px;
  background:linear-gradient(135deg,var(--primary3),#8b5cf6);
  display:flex;align-items:center;justify-content:center;
  font-weight:800;font-size:13px;flex-shrink:0;color:#fff;
  box-shadow:0 0 10px rgba(99,102,241,0.3);
}
.user-name{font-size:13px;font-weight:700;line-height:1.2;color:var(--text)}
.user-email{font-size:10px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:130px;margin-top:1px}

/* ── Mobile header & bottom nav ── */
.mobile-header{display:none;position:sticky;top:0;z-index:30;
  background:rgba(7,7,20,0.9);backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  padding:0 16px;height:56px;align-items:center;justify-content:space-between}
.mobile-bottom-nav{
  display:none;position:fixed;bottom:0;left:0;right:0;z-index:40;
  background:rgba(11,11,31,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  padding:8px 4px calc(8px + env(safe-area-inset-bottom));
  flex-direction:row;justify-content:space-around;align-items:center;
}
.mob-nav-item{display:flex;flex-direction:column;align-items:center;gap:3px;padding:6px 12px;border-radius:10px;color:var(--muted);cursor:pointer;transition:all 0.14s;min-width:52px;border:none;background:transparent}
.mob-nav-item.active{color:var(--primary2);background:var(--primary-bg)}
.mob-nav-label{font-size:10px;font-weight:600;letter-spacing:0.2px}

/* ── Page ── */
.page-header{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:24px;flex-wrap:wrap}
.page-title{font-size:22px;font-weight:800;letter-spacing:-0.5px;color:var(--text)}
.page-sub{font-size:13px;color:var(--muted);margin-top:3px;font-weight:400}

/* ── Cards ── */
.card{
  background:var(--surface);
  border:1px solid var(--border3);
  border-radius:var(--radius-lg);
  transition:border-color 0.2s,box-shadow 0.2s;
}
.card:hover{border-color:var(--border)}
.card-p{padding:20px}
.card-glow{border-color:var(--primary-border);box-shadow:0 0 30px rgba(99,102,241,0.08),0 4px 24px rgba(0,0,0,0.4)}

/* ── Stat cards ── */
.stat-card{
  background:var(--surface);border:1px solid var(--border3);border-radius:var(--radius-lg);
  padding:20px;transition:all 0.2s;cursor:pointer;position:relative;overflow:hidden;
}
.stat-card::before{content:'';position:absolute;inset:0;opacity:0;transition:opacity 0.2s;
  background:radial-gradient(circle at 0% 0%,rgba(99,102,241,0.06),transparent 60%)}
.stat-card:hover{border-color:var(--border2);transform:translateY(-2px);box-shadow:0 12px 40px rgba(0,0,0,0.35)}
.stat-card:hover::before{opacity:1}
.stat-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:14px;flex-shrink:0}
.stat-num{font-size:30px;font-weight:800;letter-spacing:-1px;margin-bottom:4px}
.stat-label{font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px}
.stat-sub{font-size:12px;color:var(--muted);margin-top:4px}
.stat-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:600;margin-top:12px;padding:3px 8px;border-radius:99px}

/* ── Buttons ── */
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 15px;border-radius:9px;font-size:13px;font-weight:600;cursor:pointer;border:none;transition:all 0.14s;white-space:nowrap;letter-spacing:0.1px;font-family:'Outfit',sans-serif}
.btn:disabled{opacity:0.4;cursor:not-allowed;pointer-events:none}
.btn:active{transform:scale(0.97)}
.btn-primary{background:linear-gradient(135deg,var(--primary3),#7c3aed);color:#fff;box-shadow:0 2px 16px rgba(99,102,241,0.3)}
.btn-primary:hover{box-shadow:0 4px 24px rgba(99,102,241,0.5);transform:translateY(-1px)}
.btn-secondary{background:var(--surface2);color:var(--text2);border:1px solid var(--border3)}
.btn-secondary:hover{background:var(--surface3);border-color:var(--border);color:var(--text)}
.btn-ghost{background:transparent;color:var(--muted2)}
.btn-ghost:hover{background:var(--surface2);color:var(--text)}
.btn-danger{background:var(--red-bg);color:var(--red);border:1px solid var(--red-border)}
.btn-danger:hover{background:rgba(248,113,113,0.18)}
.btn-sm{padding:5px 11px;font-size:12px;border-radius:7px}
.btn-icon{padding:7px;border-radius:8px}
.btn-xs{padding:3px 8px;font-size:11px;border-radius:6px}

/* ── Forms ── */
.form-group{margin-bottom:14px}
.form-label{display:block;font-size:11px;font-weight:700;color:var(--muted2);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:6px}
.input{
  width:100%;background:var(--surface2);
  border:1px solid var(--border3);
  color:var(--text);border-radius:9px;
  padding:9px 12px;font-size:13px;outline:none;
  transition:border-color 0.14s,box-shadow 0.14s;
  font-family:'Outfit',sans-serif;
}
.input:focus{border-color:var(--primary3);box-shadow:0 0 0 3px rgba(99,102,241,0.12)}
.input::placeholder{color:var(--muted)}
textarea.input{resize:vertical;min-height:80px}
select.input{cursor:pointer;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%235a5a80' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 11px center}

/* ── Badges ── */
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 8px;border-radius:99px;font-size:11px;font-weight:700;border:1px solid;letter-spacing:0.2px}
.badge-green{background:var(--green-bg);color:var(--green);border-color:var(--green-border)}
.badge-red{background:var(--red-bg);color:var(--red);border-color:var(--red-border)}
.badge-amber{background:var(--amber-bg);color:var(--amber);border-color:var(--amber-border)}
.badge-blue{background:var(--blue-bg);color:var(--blue);border-color:var(--blue-border)}
.badge-purple{background:var(--primary-bg);color:var(--primary2);border-color:var(--primary-border)}
.badge-muted{background:rgba(255,255,255,0.04);color:var(--muted2);border-color:var(--border3)}
.proto{display:inline-flex;padding:2px 7px;border-radius:5px;font-size:10px;font-weight:800;font-family:'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:0.5px}
.proto-sftp{background:var(--green-bg);color:var(--green);border:1px solid var(--green-border)}
.proto-ftp{background:var(--amber-bg);color:var(--amber);border:1px solid var(--amber-border)}

/* ── Modal ── */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.75);z-index:100;display:flex;align-items:center;justify-content:center;padding:16px;backdrop-filter:blur(6px);animation:fadeIn 0.15s ease}
.modal{background:var(--surface);border:1px solid var(--border2);border-radius:var(--radius-xl);padding:26px;width:100%;max-width:480px;max-height:92vh;overflow-y:auto;animation:slideUp 0.2s cubic-bezier(0.16,1,0.3,1);box-shadow:0 32px 80px rgba(0,0,0,0.7),0 0 0 1px rgba(99,102,241,0.08)}
.modal-title{font-size:17px;font-weight:800;letter-spacing:-0.3px;margin-bottom:4px;color:var(--text)}
.modal-desc{font-size:13px;color:var(--muted);margin-bottom:20px;line-height:1.6}
.modal-footer{display:flex;gap:8px;justify-content:flex-end;margin-top:22px;padding-top:18px;border-top:1px solid var(--border3)}

/* ── Toast ── */
#toast-root{position:fixed;top:16px;right:16px;z-index:999;display:flex;flex-direction:column;gap:8px;pointer-events:none}
.toast{
  background:rgba(11,11,31,0.97);border:1px solid var(--border2);
  border-radius:11px;padding:11px 15px;font-size:13px;font-weight:600;
  display:flex;align-items:center;gap:9px;min-width:240px;max-width:320px;
  box-shadow:0 8px 40px rgba(0,0,0,0.6);
  backdrop-filter:blur(20px);
  animation:slideInRight 0.28s cubic-bezier(0.16,1,0.3,1);
  pointer-events:all;font-family:'Outfit',sans-serif;
}
.toast-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.toast.success .toast-dot{background:var(--green);box-shadow:0 0 8px var(--green)}
.toast.error .toast-dot{background:var(--red);box-shadow:0 0 8px var(--red)}

/* ── File list ── */
.file-row{display:flex;align-items:center;gap:12px;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.03);transition:background 0.1s}
.file-row:hover{background:rgba(99,102,241,0.04)}
.file-row:last-child{border-bottom:none}
.file-icon-wrap{width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.file-actions{display:flex;gap:5px;opacity:0;transition:opacity 0.12s}
.file-row:hover .file-actions{opacity:1}

/* ── Activity ── */
.activity-row{display:flex;align-items:center;gap:12px;padding:10px 6px;border-radius:9px;transition:background 0.1s}
.activity-row:hover{background:rgba(255,255,255,0.025)}
.activity-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}

/* ── Code ── */
.code-block{background:rgba(0,0,0,0.5);border:1px solid var(--border3);border-radius:9px;padding:13px 15px;font-family:'JetBrains Mono',monospace;font-size:11.5px;overflow-x:auto;white-space:pre;color:#94a3b8;line-height:1.7}

/* ── Connection card ── */
.conn-card{background:var(--surface);border:1px solid var(--border3);border-radius:var(--radius-lg);padding:18px 20px;transition:all 0.18s}
.conn-card:hover{border-color:var(--border2);box-shadow:0 4px 24px rgba(0,0,0,0.3)}

/* ── Empty states ── */
.empty-state{text-align:center;padding:52px 24px}
.empty-icon{font-size:40px;margin-bottom:12px;display:block;opacity:0.55}
.empty-title{font-size:16px;font-weight:700;margin-bottom:6px;color:var(--text)}
.empty-sub{font-size:13px;color:var(--muted);margin-bottom:20px;max-width:280px;margin-left:auto;margin-right:auto;line-height:1.65}

/* ── Auth pages ── */
.auth-page{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;background:var(--bg);overflow:hidden;position:relative}
.auth-glow{position:fixed;top:-10%;left:50%;transform:translateX(-50%);width:700px;height:500px;background:radial-gradient(ellipse,rgba(99,102,241,0.14),transparent 65%);pointer-events:none;z-index:0}
.auth-glow2{position:fixed;bottom:-5%;right:10%;width:400px;height:400px;background:radial-gradient(ellipse,rgba(139,92,246,0.08),transparent 65%);pointer-events:none;z-index:0}
.auth-card{background:var(--surface);border:1px solid var(--border2);border-radius:22px;padding:34px;width:100%;max-width:400px;position:relative;z-index:1;box-shadow:0 32px 80px rgba(0,0,0,0.5),0 0 0 1px rgba(99,102,241,0.06)}
.auth-logo{display:flex;align-items:center;gap:12px;margin-bottom:26px}
.auth-logo-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--primary3),#8b5cf6);display:flex;align-items:center;justify-content:center;box-shadow:0 0 24px rgba(99,102,241,0.4)}

/* ── Spinner ── */
.spin{animation:spin 0.75s linear infinite;display:inline-block}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes slideUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideInRight{from{opacity:0;transform:translateX(24px)}to{opacity:1;transform:translateX(0)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}

/* ── Skeleton loader ── */
.skeleton{background:linear-gradient(90deg,var(--surface2) 25%,var(--surface3) 50%,var(--surface2) 75%);background-size:200% 100%;animation:shimmer 1.6s infinite;border-radius:6px}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}

/* ── Tabs ── */
.tabs{display:flex;gap:2px;background:rgba(255,255,255,0.03);border:1px solid var(--border3);border-radius:10px;padding:3px}
.tab{padding:7px 15px;border-radius:8px;font-size:13px;font-weight:600;color:var(--muted2);cursor:pointer;transition:all 0.14s;border:none;background:transparent;font-family:'Outfit',sans-serif}
.tab.active{background:var(--surface2);color:var(--text);box-shadow:0 1px 6px rgba(0,0,0,0.3)}
.tab:hover:not(.active){color:var(--text)}

/* ── Info box ── */
.info-box{background:var(--primary-bg);border:1px solid var(--primary-border);border-radius:11px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start}
.info-box-icon{width:30px;height:30px;border-radius:8px;background:rgba(99,102,241,0.18);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}

/* ── Divider ── */
.sep{height:1px;background:var(--border3);margin:18px 0}
code{background:rgba(99,102,241,0.1);padding:1px 6px;border-radius:5px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--primary2)}

/* ── Live indicator ── */
.live-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--green);animation:livePulse 2s ease-in-out infinite;box-shadow:0 0 6px var(--green)}
@keyframes livePulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.6;transform:scale(0.85)}}
.last-updated{font-size:11px;color:var(--muted);display:flex;align-items:center;gap:5px}

/* ── Search ── */
.search-input{position:relative;flex:1;min-width:140px}
.search-input input{padding-left:32px}
.search-input .search-icon{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--muted);pointer-events:none}

/* ── Responsive ── */
@media(max-width:860px){
  .sidebar{display:none}
  .main-content{margin-left:0}
  .mobile-header{display:flex}
  .mobile-bottom-nav{display:flex}
  .page-body{padding:16px 14px 80px}
  .page-title{font-size:19px}
  .stat-num{font-size:24px}
}
@media(max-width:540px){
  .page-header{flex-direction:column;align-items:flex-start;gap:10px}
  .page-header .btn{width:100%;justify-content:center}
  .modal{padding:20px}
  .auth-card{padding:26px 22px}
  .tabs{overflow-x:auto}
}
</style>
</head>
<body>
<div class="bg-orb bg-orb-1"></div>
<div class="bg-orb bg-orb-2"></div>
<div id="toast-root"></div>
<div id="root"></div>

<script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.production.min.js" crossorigin></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://cdn.jsdelivr.net/npm/@babel/standalone@7.23.5/babel.min.js"></script>
<script>
  window.addEventListener('load', function() {
    setTimeout(function() {
      if (!window.React || !window.Babel) {
        document.getElementById('root').innerHTML =
          '<div style="min-height:100vh;display:flex;align-items:center;justify-content:center;background:#04040e;font-family:sans-serif">' +
          '<div style="text-align:center;color:#eeeeff;padding:40px">' +
          '<div style="font-size:44px;margin-bottom:16px">⚡</div>' +
          '<h2 style="font-size:20px;font-weight:700;margin-bottom:8px">Failed to load scripts</h2>' +
          '<p style="color:#5a5a80;font-size:14px">Could not reach CDN. Check your network and try refreshing.</p>' +
          '</div></div>';
      }
    }, 6000);
  });
</script>
<script type="text/babel" data-presets="react">
const { useState, useEffect, useCallback, useRef, createContext, useContext, useMemo } = React;

// ─── Toast ────────────────────────────────────────────────
const toast = {
  show(msg, type='success') {
    const el = document.createElement('div');
    el.className = `toast ${type}`;
    el.innerHTML = `<span class="toast-dot"></span><span>${msg}</span>`;
    const root = document.getElementById('toast-root');
    root.appendChild(el);
    setTimeout(() => {
      el.style.transition='opacity 0.3s,transform 0.3s';
      el.style.opacity='0';el.style.transform='translateX(20px)';
      setTimeout(()=>el.remove(),300);
    }, 3000);
  },
  success(m){ this.show(m,'success') },
  error(m){ this.show(m,'error') }
};

// ─── Router ───────────────────────────────────────────────
const RouterCtx = createContext(null);
function Router({ children }) {
  const [path, setPath] = useState(window.location.pathname);
  const navigate = useCallback((to) => {
    window.history.pushState({}, '', to);
    setPath(to);
  }, []);
  useEffect(() => {
    const h = () => setPath(window.location.pathname);
    window.addEventListener('popstate', h);
    return () => window.removeEventListener('popstate', h);
  }, []);
  return <RouterCtx.Provider value={{ path, navigate }}>{children}</RouterCtx.Provider>;
}
function useRouter() { return useContext(RouterCtx); }
function Link({ to, children, className, style, onClick }) {
  const { navigate } = useRouter();
  return (
    <a href={to} className={className} style={style}
       onClick={e => { e.preventDefault(); onClick?.(); navigate(to); }}>
      {children}
    </a>
  );
}

// ─── API ─────────────────────────────────────────────────
async function apiFetch(method, url, body, isFile) {
  const token = localStorage.getItem('token');
  const headers = {};
  if (token) headers['Authorization'] = `Bearer ${token}`;
  if (body && !isFile) headers['Content-Type'] = 'application/json';
  const res = await fetch('/api' + url, { method, headers, body: body ? (isFile ? body : JSON.stringify(body)) : undefined });
  if (res.status === 401) {
    localStorage.removeItem('token');
    window.history.pushState({}, '', '/login');
    window.dispatchEvent(new PopStateEvent('popstate'));
    throw new Error('Session expired');
  }
  const ct = res.headers.get('content-type') || '';
  const data = ct.includes('application/json') ? await res.json() : await res.blob();
  if (!res.ok) throw new Error(data?.detail || `Error ${res.status}`);
  return data;
}
const api = {
  get:     u    => apiFetch('GET', u),
  post:    (u,b)=> apiFetch('POST', u, b),
  put:     (u,b)=> apiFetch('PUT', u, b),
  delete:  u    => apiFetch('DELETE', u),
  postFile:(u,b)=> apiFetch('POST', u, b, true),
};

// ─── Auth Context ─────────────────────────────────────────
const AuthCtx = createContext(null);
function AuthProvider({ children }) {
  const [user, setUser]       = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) { setLoading(false); return; }
    api.get('/auth/me')
      .then(u => setUser(u))
      .catch(() => localStorage.removeItem('token'))
      .finally(() => setLoading(false));
  }, []);
  const login = async (email, password) => {
    const data = await api.post('/auth/login', { email, password });
    localStorage.setItem('token', data.access_token);
    setUser(data.user);
    return data.user;
  };
  const register = async (name, email, password) => {
    const data = await api.post('/auth/register', { name, email, password });
    localStorage.setItem('token', data.access_token);
    setUser(data.user);
    return data.user;
  };
  const logout = () => { localStorage.removeItem('token'); setUser(null); };
  return <AuthCtx.Provider value={{ user, loading, login, register, logout }}>{children}</AuthCtx.Provider>;
}
function useAuth() { return useContext(AuthCtx); }

// ─── Icons ───────────────────────────────────────────────
function Icon({ d, size=16, color='currentColor', sw=1.75 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none"
         stroke={color} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round">
      {[].concat(d).map((p,i) => <path key={i} d={p}/>)}
    </svg>
  );
}
const I = {
  Dashboard: ()=><Icon d={["M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z","M9 22V12h6v10"]}/>,
  Server:    ()=><Icon d={["M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"]}/>,
  Folder:    ()=><Icon d={["M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"]}/>,
  Key:       ()=><Icon d={["m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4","m21 2-9.6 9.6","m3.5 17.5 3 3L13 15l-3-3-6.5 6.5"]}/>,
  Docs:      ()=><Icon d={["M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z","M14 2v6h6","M16 13H8","M16 17H8","M10 9H8"]}/>,
  Settings:  ()=><Icon d={["M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z","M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z"]}/>,
  LogOut:    ()=><Icon d={["M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4","M16 17l5-5-5-5","M21 12H9"]}/>,
  Zap:       ()=><Icon d={["M13 2 3 14h9l-1 8 10-12h-9l1-8z"]} sw={1.5}/>,
  Plus:      ()=><Icon d={["M12 5v14","M5 12h14"]}/>,
  Trash:     ()=><Icon d={["M3 6h18","M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6","M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"]}/>,
  Edit:      ()=><Icon d={["M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7","M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"]}/>,
  Copy:      ()=><Icon d={["M20 9h-9a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2z","M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 0 2 2v1"]}/>,
  Check:     ()=><Icon d={["M20 6 9 17l-5-5"]}/>,
  X:         ()=><Icon d={["M18 6 6 18","M6 6l12 12"]}/>,
  Right:     ()=><Icon d={["M9 18l6-6-6-6"]}/>,
  Up:        ()=><Icon d={["M18 15l-6-6-6 6"]}/>,
  Home:      ()=><Icon d={["M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z","M9 22V12h6v10"]}/>,
  FolderPlus:()=><Icon d={["M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z","M12 11v6","M9 14h6"]}/>,
  Upload:    ()=><Icon d={["M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4","M17 8l-5-5-5 5","M12 3v12"]}/>,
  Download:  ()=><Icon d={["M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4","M7 10l5 5 5-5","M12 15V3"]}/>,
  Refresh:   ()=><Icon d={["M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8","M21 3v5h-5","M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16","M8 16H3v5"]}/>,
  Activity:  ()=><Icon d={["M22 12h-4l-3 9L9 3l-3 9H2"]}/>,
  ArrowRight:()=><Icon d={["M5 12h14","M12 5l7 7-7 7"]}/>,
  Eye:       ()=><Icon d={["M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z","M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"]}/>,
  EyeOff:    ()=><Icon d={["M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94","M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19","M1 1l22 22"]}/>,
  Shield:    ()=><Icon d={["M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"]}/>,
  Clock:     ()=><Icon d={["M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z","M12 6v6l4 2"]}/>,
  Alert:     ()=><Icon d={["M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z","M12 9v4","M12 17h.01"]}/>,
  File:      ()=><Icon d={["M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z","M13 2v7h7"]}/>,
  Code:      ()=><Icon d={["M16 18l6-6-6-6","M8 6l-6 6 6 6"]}/>,
  User:      ()=><Icon d={["M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2","M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"]}/>,
  Hash:      ()=><Icon d={["M4 9h16","M4 15h16","M10 3 8 21","M16 3l-2 18"]}/>,
  Search:    ()=><Icon d={["M21 21l-4.35-4.35","M17 11a6 6 0 1 1-12 0 6 6 0 0 1 12 0z"]}/>,
  MoreV:     ()=><Icon d={["M12 5h.01","M12 12h.01","M12 19h.01"]} sw={2.5}/>,
  Wifi:      ()=><Icon d={["M5 12.55a11 11 0 0 1 14.08 0","M1.42 9a16 16 0 0 1 21.16 0","M8.53 16.11a6 6 0 0 1 6.95 0","M12 20h.01"]}/>,
  Link:      ()=><Icon d={["M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71","M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"]}/>,
  Globe:     ()=><Icon d={["M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z","M2 12h20","M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"]}/>,
};

// ─── Helpers ─────────────────────────────────────────────
function Spinner({ size=15 }) {
  return (
    <svg className="spin" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
      <circle cx="12" cy="12" r="10" strokeOpacity="0.12"/>
      <path d="M12 2a10 10 0 0 1 10 10" strokeLinecap="round"/>
    </svg>
  );
}
function SkeletonLine({ w='100%', h=14, mb=8 }) {
  return <div className="skeleton" style={{width:w,height:h,marginBottom:mb}}/>;
}
function formatBytes(b) {
  if (b == null || b === '') return '—';
  if (b === 0) return '0 B';
  const i = Math.floor(Math.log(b)/Math.log(1024));
  return (b/Math.pow(1024,i)).toFixed(1)+' '+['B','KB','MB','GB','TB'][i];
}
function fmtDate(s) {
  if (!s) return '—';
  return new Date(s).toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric',hour:'2-digit',minute:'2-digit'});
}
function relTime(s) {
  if (!s) return '—';
  const d = (Date.now()-new Date(s))/1000;
  if (d < 60)    return 'just now';
  if (d < 3600)  return `${Math.floor(d/60)}m ago`;
  if (d < 86400) return `${Math.floor(d/3600)}h ago`;
  if (d < 604800)return `${Math.floor(d/86400)}d ago`;
  return fmtDate(s);
}
function fileEmoji(type, name) {
  if (type==='directory') return '📁';
  const e = name?.split('.').pop()?.toLowerCase();
  const m={png:'🖼',jpg:'🖼',jpeg:'🖼',gif:'🖼',svg:'🖼',webp:'🖼',ico:'🖼',
           pdf:'📄',doc:'📄',docx:'📄',txt:'📝',md:'📝',
           js:'💻',ts:'💻',jsx:'💻',tsx:'💻',py:'🐍',java:'☕',rb:'💎',go:'🐹',rs:'🦀',
           html:'🌐',css:'🎨',json:'📋',xml:'📋',yml:'📋',yaml:'📋',
           zip:'📦',tar:'📦',gz:'📦',rar:'📦','7z':'📦',
           mp3:'🎵',wav:'🎵',flac:'🎵',mp4:'🎬',avi:'🎬',mov:'🎬',mkv:'🎬',
           sh:'⚙',bash:'⚙',sql:'🗄',db:'🗄'};
  return m[e] || '📄';
}
function parentPath(p) {
  if(!p||p==='/') return '/';
  const parts=p.split('/').filter(Boolean); parts.pop();
  return '/'+parts.join('/');
}
function joinPath(...parts) {
  return '/'+parts.map(p=>p.replace(/^\/|\/$/g,'')).filter(Boolean).join('/');
}

// ─── Layout ───────────────────────────────────────────────
const MOB_NAV = [
  {path:'/',label:'Home',icon:'Dashboard'},
  {path:'/connections',label:'Servers',icon:'Server'},
  {path:'/browser',label:'Files',icon:'Folder'},
  {path:'/api-keys',label:'Keys',icon:'Key'},
  {path:'/settings',label:'Account',icon:'Settings'},
];
const NAV = [
  {path:'/',label:'Dashboard',icon:'Dashboard'},
  {path:'/connections',label:'Connections',icon:'Server'},
  {path:'/browser',label:'File Browser',icon:'Folder'},
  {path:'/api-keys',label:'API Keys',icon:'Key'},
  {path:'/docs',label:'API Docs',icon:'Docs'},
  {path:'/settings',label:'Settings',icon:'Settings'},
];

function Sidebar() {
  const { path, navigate } = useRouter();
  const { user, logout }   = useAuth();
  const go = p => navigate(p);
  return (
    <div style={{display:'flex',flexDirection:'column',height:'100%'}}>
      <div className="sidebar-logo">
        <div className="logo-icon"><I.Zap/></div>
        <div>
          <div className="logo-text">Relay Drive</div>
          <div className="logo-sub">FTP/SFTP GATEWAY</div>
        </div>
      </div>
      <nav className="sidebar-nav">
        <div className="nav-section-label">Navigation</div>
        {NAV.map(n => {
          const active = n.path==='/' ? path==='/' : path.startsWith(n.path);
          const Icon = I[n.icon];
          return (
            <div key={n.path} className={`nav-item${active?' active':''}`} onClick={()=>go(n.path)}>
              <Icon/> {n.label}
            </div>
          );
        })}
      </nav>
      <div className="sidebar-footer">
        <div className="user-card">
          <div className="user-avatar">{(user?.name||user?.email||'U').charAt(0).toUpperCase()}</div>
          <div style={{flex:1,minWidth:0}}>
            <div className="user-name">{user?.name||'User'}</div>
            <div className="user-email" title={user?.email}>{user?.email||'—'}</div>
          </div>
        </div>
        <div className="nav-item" onClick={()=>{ logout(); navigate('/login'); }} style={{color:'var(--red)',marginTop:2}}>
          <I.LogOut/> Sign Out
        </div>
      </div>
    </div>
  );
}

function Layout({ children }) {
  const { path, navigate } = useRouter();
  return (
    <div className="app-shell" style={{background:'var(--bg)'}}>
      {/* Desktop sidebar */}
      <aside className="sidebar"><Sidebar/></aside>

      {/* Mobile top header */}
      <div className="mobile-header">
        <div style={{display:'flex',alignItems:'center',gap:9}}>
          <div className="logo-icon" style={{width:30,height:30,borderRadius:8}}>
            <I.Zap size={14}/>
          </div>
          <span style={{fontWeight:800,fontSize:14,letterSpacing:'-0.2px'}}>Relay Drive</span>
        </div>
        <div style={{display:'flex',gap:6}}>
          <button className="btn btn-ghost btn-icon btn-sm" onClick={()=>navigate('/settings')} title="Settings">
            <I.Settings size={16}/>
          </button>
        </div>
      </div>

      <div className="main-content">
        <div className="page-body">{children}</div>
      </div>

      {/* Mobile bottom nav */}
      <nav className="mobile-bottom-nav">
        {MOB_NAV.map(n=>{
          const active = n.path==='/' ? path==='/' : path.startsWith(n.path);
          const Icon = I[n.icon];
          return (
            <button key={n.path} className={`mob-nav-item${active?' active':''}`} onClick={()=>navigate(n.path)}>
              <Icon size={18}/>
              <span className="mob-nav-label">{n.label}</span>
            </button>
          );
        })}
      </nav>
    </div>
  );
}

// ─── Guards ───────────────────────────────────────────────
const FullPageSpinner = () => (
  <div style={{minHeight:'100vh',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',background:'var(--bg)',gap:16}}>
    <div className="logo-icon" style={{width:44,height:44,borderRadius:13}}>
      <I.Zap size={20}/>
    </div>
    <Spinner size={20}/>
  </div>
);
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  const { navigate }      = useRouter();
  useEffect(() => { if (!loading && !user) navigate('/login'); }, [user, loading]);
  if (loading || !user) return <FullPageSpinner/>;
  return children;
}
function PublicRoute({ children }) {
  const { user, loading } = useAuth();
  const { navigate }      = useRouter();
  useEffect(() => { if (!loading && user) navigate('/'); }, [user, loading]);
  if (loading || user) return <FullPageSpinner/>;
  return children;
}

// ─── Page: Login ─────────────────────────────────────────
function Login() {
  const { login }    = useAuth();
  const { navigate } = useRouter();
  const [email, setEmail]   = useState('');
  const [pass, setPass]     = useState('');
  const [show, setShow]     = useState(false);
  const [loading, setLoading] = useState(false);
  const submit = async e => {
    e.preventDefault(); setLoading(true);
    try { await login(email, pass); toast.success('Welcome back!'); navigate('/'); }
    catch(err) { toast.error(err.message||'Login failed'); }
    finally { setLoading(false); }
  };
  return (
    <div className="auth-page">
      <div className="auth-glow"/><div className="auth-glow2"/>
      <div className="auth-card">
        <div className="auth-logo">
          <div className="auth-logo-icon"><I.Zap size={20}/></div>
          <div>
            <div style={{fontWeight:800,fontSize:19,letterSpacing:'-0.3px'}}>Relay Drive</div>
            <div style={{fontSize:11,color:'var(--muted)',letterSpacing:'0.5px',textTransform:'uppercase',fontWeight:600}}>FTP/SFTP Gateway</div>
          </div>
        </div>
        <h1 style={{fontSize:21,fontWeight:800,letterSpacing:'-0.5px',marginBottom:6}}>Sign in</h1>
        <p style={{fontSize:13,color:'var(--muted)',marginBottom:24}}>Enter your credentials to continue</p>
        <div onKeyDown={e=>e.key==='Enter'&&submit(e)}>
          <div className="form-group">
            <label className="form-label">Email</label>
            <input className="input" type="email" placeholder="you@example.com" value={email} onChange={e=>setEmail(e.target.value)} autoFocus/>
          </div>
          <div className="form-group" style={{marginBottom:22,position:'relative'}}>
            <label className="form-label">Password</label>
            <input className="input" type={show?'text':'password'} placeholder="••••••••" value={pass} onChange={e=>setPass(e.target.value)} style={{paddingRight:40}}/>
            <button type="button" onClick={()=>setShow(v=>!v)} style={{position:'absolute',right:10,top:32,background:'none',border:'none',cursor:'pointer',color:'var(--muted)',padding:4}}>
              {show?<I.EyeOff size={14}/>:<I.Eye size={14}/>}
            </button>
          </div>
          <button className="btn btn-primary" style={{width:'100%',justifyContent:'center',padding:'11px'}} disabled={loading} onClick={submit}>
            {loading ? <Spinner/> : <I.ArrowRight size={14}/>} Sign in
          </button>
        </div>
        <div style={{textAlign:'center',marginTop:20,fontSize:13,color:'var(--muted)'}}>
          No account?{' '}
          <Link to="/register" style={{color:'var(--primary)',fontWeight:700,textDecoration:'none'}}>Create one →</Link>
        </div>
      </div>
    </div>
  );
}

// ─── Page: Register ───────────────────────────────────────
function Register() {
  const { register } = useAuth();
  const { navigate } = useRouter();
  const [name,  setName]  = useState('');
  const [email, setEmail] = useState('');
  const [pass,  setPass]  = useState('');
  const [show,  setShow]  = useState(false);
  const [loading, setLoading] = useState(false);
  const submit = async e => {
    e.preventDefault();
    if (pass.length < 6) { toast.error('Password must be at least 6 characters'); return; }
    setLoading(true);
    try { await register(name, email, pass); toast.success('Account created!'); navigate('/'); }
    catch(err) { toast.error(err.message||'Registration failed'); }
    finally { setLoading(false); }
  };
  return (
    <div className="auth-page">
      <div className="auth-glow"/><div className="auth-glow2"/>
      <div className="auth-card">
        <div className="auth-logo">
          <div className="auth-logo-icon"><I.Zap size={20}/></div>
          <div>
            <div style={{fontWeight:800,fontSize:19,letterSpacing:'-0.3px'}}>Relay Drive</div>
            <div style={{fontSize:11,color:'var(--muted)',letterSpacing:'0.5px',textTransform:'uppercase',fontWeight:600}}>FTP/SFTP Gateway</div>
          </div>
        </div>
        <h1 style={{fontSize:21,fontWeight:800,letterSpacing:'-0.5px',marginBottom:6}}>Create account</h1>
        <p style={{fontSize:13,color:'var(--muted)',marginBottom:24}}>Get started in seconds</p>
        <div>
          <div className="form-group">
            <label className="form-label">Full Name</label>
            <input className="input" type="text" placeholder="Your name" value={name} onChange={e=>setName(e.target.value)} autoFocus/>
          </div>
          <div className="form-group">
            <label className="form-label">Email</label>
            <input className="input" type="email" placeholder="you@example.com" value={email} onChange={e=>setEmail(e.target.value)}/>
          </div>
          <div className="form-group" style={{marginBottom:22,position:'relative'}}>
            <label className="form-label">Password</label>
            <input className="input" type={show?'text':'password'} placeholder="At least 6 characters" value={pass} onChange={e=>setPass(e.target.value)} style={{paddingRight:40}}/>
            <button type="button" onClick={()=>setShow(v=>!v)} style={{position:'absolute',right:10,top:32,background:'none',border:'none',cursor:'pointer',color:'var(--muted)',padding:4}}>
              {show?<I.EyeOff size={14}/>:<I.Eye size={14}/>}
            </button>
          </div>
          <button className="btn btn-primary" style={{width:'100%',justifyContent:'center',padding:'11px'}} disabled={loading}
            onClick={submit}>
            {loading ? <Spinner/> : <I.ArrowRight size={14}/>} Create account
          </button>
        </div>
        <div style={{textAlign:'center',marginTop:20,fontSize:13,color:'var(--muted)'}}>
          Have an account?{' '}
          <Link to="/login" style={{color:'var(--primary)',fontWeight:700,textDecoration:'none'}}>Sign in →</Link>
        </div>
      </div>
    </div>
  );
}

// ─── Page: Dashboard ─────────────────────────────────────
const ACTION_LABELS = {
  list_directory:'Listed directory',upload_file:'Uploaded file',download_file:'Downloaded file',
  delete_file:'Deleted file',delete_directory:'Deleted directory',create_directory:'Created directory',
  rename_file:'Renamed file',test_connection:'Tested connection',create_connection:'Added connection',
  update_connection:'Updated connection',delete_connection:'Removed connection',
  create_api_key:'Created API key',revoke_api_key:'Revoked API key',
};
const ACTION_ICONS = {
  upload_file:'Upload',download_file:'Download',delete_file:'Trash',delete_directory:'Trash',
  create_directory:'FolderPlus',rename_file:'Edit',test_connection:'Wifi',
  create_connection:'Link',update_connection:'Edit',delete_connection:'Trash',
  create_api_key:'Key',revoke_api_key:'Key',list_directory:'Folder',
};

function Dashboard() {
  const [stats,       setStats]      = useState(null);
  const [lastRefresh, setLastRefresh]= useState(null);
  const [refreshing,  setRefreshing] = useState(false);
  const { navigate }                 = useRouter();

  const fetchStats = useCallback(async (silent=false) => {
    if (!silent) setRefreshing(true);
    try {
      const s = await api.get('/dashboard/stats');
      setStats(s);
      setLastRefresh(new Date());
    } catch(e) {
      if (!silent) toast.error('Failed to load stats');
    } finally {
      setRefreshing(false);
    }
  }, []);

  useEffect(() => {
    fetchStats();
    // Real-time polling every 30 seconds
    const id = setInterval(() => fetchStats(true), 30000);
    return () => clearInterval(id);
  }, [fetchStats]);

  const loaded = stats != null && typeof stats === 'object' && 'total_connections' in stats;
  const STAT_CARDS = [
    {
      label:'Server Connections',
      val: loaded ? (stats.total_connections ?? 0) : null,
      sub:'FTP & SFTP servers',
      link:'/connections',
      color:'var(--primary)',
      bgColor:'var(--primary-bg)',
      borderColor:'var(--primary-border)',
      icon:'Server',
    },
    {
      label:'Active API Keys',
      val: loaded ? `${stats.active_api_keys ?? 0} / ${stats.total_api_keys ?? 0}` : null,
      sub:'Programmatic access keys',
      link:'/api-keys',
      color:'var(--green)',
      bgColor:'var(--green-bg)',
      borderColor:'var(--green-border)',
      icon:'Key',
    },
    {
      label:'Operations Today',
      val: loaded ? (stats.operations_today ?? 0) : null,
      sub:'File ops in last 24h',
      link:'/browser',
      color:'var(--amber)',
      bgColor:'var(--amber-bg)',
      borderColor:'var(--amber-border)',
      icon:'Activity',
    },
  ];

  return (
    <>
      <div className="page-header">
        <div>
          <div className="page-title">Dashboard</div>
          <div className="page-sub">Overview of your relay service</div>
        </div>
        <div style={{display:'flex',gap:8,alignItems:'center'}}>
          {lastRefresh && (
            <span className="last-updated">
              <span className="live-dot"/>
              Updated {relTime(lastRefresh)}
            </span>
          )}
          <button className="btn btn-secondary btn-sm" onClick={()=>fetchStats()} disabled={refreshing} title="Refresh">
            {refreshing ? <Spinner size={12}/> : <I.Refresh size={13}/>}
            {!refreshing && <span style={{display:'none'}}>Refresh</span>}
          </button>
          <button className="btn btn-primary btn-sm" onClick={()=>navigate('/connections')}><I.Plus size={13}/> Add Connection</button>
        </div>
      </div>

      {/* Stat cards */}
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(200px,1fr))',gap:12,marginBottom:20}}>
        {STAT_CARDS.map(s=>{
          const Icon = I[s.icon];
          return (
            <div key={s.label} className="stat-card" onClick={()=>navigate(s.link)}>
              <div className="stat-icon" style={{background:s.bgColor,border:`1px solid ${s.borderColor}`,color:s.color}}>
                <Icon size={18}/>
              </div>
              <div className="stat-label">{s.label}</div>
              {s.val==null ? (
                <><SkeletonLine w="60%" h={30} mb={4}/><SkeletonLine w="80%" h={12}/></>
              ) : (
                <>
                  <div className="stat-num" style={{color:s.color}}>{s.val}</div>
                  <div className="stat-sub">{s.sub}</div>
                </>
              )}
              <div style={{display:'flex',alignItems:'center',gap:4,fontSize:11,color:s.color,marginTop:14,fontWeight:600}}>
                Manage <I.ArrowRight size={11}/>
              </div>
            </div>
          );
        })}
      </div>

      {/* Activity feed */}
      <div className="card card-p">
        <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',marginBottom:18}}>
          <div style={{display:'flex',alignItems:'center',gap:8,fontSize:14,fontWeight:700}}>
            <I.Activity size={15}/> Recent Activity
          </div>
          <button className="btn btn-ghost btn-sm" onClick={()=>navigate('/connections')} style={{fontSize:12}}>
            View all <I.ArrowRight size={11}/>
          </button>
        </div>
        {!loaded ? (
          <div style={{display:'flex',flexDirection:'column',gap:10}}>
            {[1,2,3,4].map(i=>(
              <div key={i} style={{display:'flex',alignItems:'center',gap:12,padding:'8px 4px'}}>
                <div className="skeleton" style={{width:32,height:32,borderRadius:8,flexShrink:0}}/>
                <div style={{flex:1}}><SkeletonLine w="55%" h={13} mb={4}/><SkeletonLine w="40%" h={11} mb={0}/></div>
                <SkeletonLine w={50} h={20} mb={0}/>
              </div>
            ))}
          </div>
        ) : (stats.recent_activities||[]).length > 0 ? (
          <div>
            {(stats.recent_activities||[]).map(a=>{
              const iconKey = ACTION_ICONS[a.action] || 'Activity';
              const AIcon   = I[iconKey];
              const ok      = a.status==='success';
              return (
                <div key={a.id} className="activity-row">
                  <div style={{width:32,height:32,borderRadius:8,display:'flex',alignItems:'center',justifyContent:'center',flexShrink:0,
                    background:ok?'var(--green-bg)':'var(--red-bg)',color:ok?'var(--green)':'var(--red)'}}>
                    <AIcon size={14}/>
                  </div>
                  <div style={{flex:1,minWidth:0}}>
                    <div style={{fontSize:13,fontWeight:600,color:'var(--text)'}}>
                      {ACTION_LABELS[a.action]||a.action}
                      {a.connection_name && <span style={{color:'var(--muted)',fontWeight:400}}> · <span style={{color:'var(--muted2)',fontWeight:500}}>{a.connection_name}</span></span>}
                    </div>
                    {a.path && <div style={{fontSize:11,color:'var(--muted)',fontFamily:'JetBrains Mono,monospace',overflow:'hidden',textOverflow:'ellipsis',whiteSpace:'nowrap',marginTop:1}}>{a.path}</div>}
                  </div>
                  <div style={{display:'flex',alignItems:'center',gap:8,flexShrink:0}}>
                    <span className={`badge ${ok?'badge-green':'badge-red'}`}>{a.status}</span>
                    <span style={{fontSize:11,color:'var(--muted)',whiteSpace:'nowrap'}}>{relTime(a.timestamp)}</span>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div className="empty-state" style={{padding:'32px 24px'}}>
            <span className="empty-icon">📋</span>
            <div className="empty-title">No activity yet</div>
            <div className="empty-sub">Start by adding a connection and browsing files</div>
          </div>
        )}
      </div>
    </>
  );
}

// ─── Page: Connections ────────────────────────────────────
function Connections() {
  const [conns,   setConns]   = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal,   setModal]   = useState(null);
  const [testing, setTesting] = useState(null);
  const [saving,  setSaving]  = useState(false);
  const [search,  setSearch]  = useState('');
  const [form, setForm]       = useState({name:'',protocol:'sftp',host:'',port:22,username:'',password:'',private_key:''});

  const load = useCallback(()=>{
    return api.get('/connections')
      .then(d=>setConns(Array.isArray(d)?d:[]))
      .catch(()=>toast.error('Failed to load connections'))
      .finally(()=>setLoading(false));
  },[]);
  useEffect(()=>{ load(); },[]);

  const openNew  = ()=>{ setForm({name:'',protocol:'sftp',host:'',port:22,username:'',password:'',private_key:''}); setModal('new'); };
  const openEdit = c=>{ setForm({name:c.name,protocol:c.protocol,host:c.host,port:c.port,username:c.username,password:'',private_key:''}); setModal(c); };
  const F = (k,v) => setForm(f=>({...f,[k]:v}));

  const save = async () => {
    if (!form.name || !form.host || !form.username) { toast.error('Name, host and username are required'); return; }
    setSaving(true);
    const d={...form,port:parseInt(form.port)||22};
    if(!d.password) delete d.password;
    if(!d.private_key) delete d.private_key;
    try {
      if(modal==='new'){ await api.post('/connections',d); toast.success('Connection created!'); }
      else { await api.put(`/connections/${modal.id}`,d); toast.success('Connection updated!'); }
      setModal(null); await load();
    } catch(err){ toast.error(err.message||'Failed to save — check your details'); }
    finally{ setSaving(false); }
  };
  const del = async id=>{
    if(!confirm('Delete this connection?')) return;
    try{ await api.delete(`/connections/${id}`); toast.success('Deleted'); load(); }
    catch(err){ toast.error(err.message); }
  };
  const test = async id=>{
    setTesting(id);
    try{ await api.post(`/connections/${id}/test`); toast.success('Connection successful!'); }
    catch(err){ toast.error(err.message||'Connection failed'); }
    finally{ setTesting(null); }
  };

  const filtered = conns.filter(c=>
    c.name.toLowerCase().includes(search.toLowerCase()) ||
    c.host.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <div className="page-header">
        <div>
          <div className="page-title">Connections</div>
          <div className="page-sub">Manage your FTP and SFTP servers</div>
        </div>
        <button className="btn btn-primary" onClick={openNew}><I.Plus size={14}/> New Connection</button>
      </div>

      {conns.length > 2 && (
        <div className="search-input" style={{marginBottom:14,maxWidth:320,position:'relative'}}>
          <span className="search-icon" style={{position:'absolute',left:10,top:'50%',transform:'translateY(-50%)',color:'var(--muted)',pointerEvents:'none'}}>
            <I.Search size={13}/>
          </span>
          <input className="input" placeholder="Search connections…" value={search} onChange={e=>setSearch(e.target.value)}
            style={{paddingLeft:32,height:38}}/>
        </div>
      )}

      {loading ? (
        <div style={{display:'flex',flexDirection:'column',gap:10}}>
          {[1,2].map(i=>(
            <div key={i} className="conn-card"><SkeletonLine w="40%" h={18} mb={8}/><SkeletonLine w="60%" h={13} mb={0}/></div>
          ))}
        </div>
      ) : conns.length===0 ? (
        <div className="card"><div className="empty-state">
          <span className="empty-icon">🖥️</span>
          <div className="empty-title">No connections yet</div>
          <div className="empty-sub">Add your first FTP or SFTP server to start managing files remotely</div>
          <button className="btn btn-primary" onClick={openNew}><I.Plus size={14}/> Add Connection</button>
        </div></div>
      ) : (
        <div style={{display:'flex',flexDirection:'column',gap:10}}>
          {filtered.map(c=>(
            <div key={c.id} className="conn-card">
              <div style={{display:'flex',alignItems:'flex-start',justifyContent:'space-between',gap:12,flexWrap:'wrap'}}>
                <div style={{display:'flex',gap:13,alignItems:'flex-start',flex:1,minWidth:0}}>
                  <div style={{width:44,height:44,borderRadius:11,flexShrink:0,display:'flex',alignItems:'center',justifyContent:'center',
                    background:'var(--primary-bg)',border:'1px solid var(--primary-border)',color:'var(--primary)'}}>
                    <I.Server size={18}/>
                  </div>
                  <div style={{flex:1,minWidth:0}}>
                    <div style={{display:'flex',alignItems:'center',gap:8,flexWrap:'wrap',marginBottom:5}}>
                      <span style={{fontSize:15,fontWeight:700}}>{c.name}</span>
                      <span className={`proto proto-${c.protocol}`}>{c.protocol}</span>
                    </div>
                    <div style={{fontSize:12,color:'var(--muted)',fontFamily:'JetBrains Mono,monospace',marginBottom:6}}>
                      {c.username}@{c.host}:{c.port}
                    </div>
                    <div style={{display:'flex',gap:12,fontSize:11,color:'var(--muted)',flexWrap:'wrap',alignItems:'center'}}>
                      {c.has_password && <span className="badge badge-muted" style={{fontSize:10}}>🔒 Password</span>}
                      {c.has_private_key && <span className="badge badge-muted" style={{fontSize:10}}>🔑 SSH Key</span>}
                      {c.last_used && <span>Last used {relTime(c.last_used)}</span>}
                    </div>
                  </div>
                </div>
                <div style={{display:'flex',gap:6,flexWrap:'wrap',flexShrink:0}}>
                  <button className="btn btn-secondary btn-sm" onClick={()=>test(c.id)} disabled={testing===c.id}>
                    {testing===c.id ? <Spinner size={12}/> : <I.Wifi size={13}/>}
                    {testing===c.id ? 'Testing…' : 'Test'}
                  </button>
                  <button className="btn btn-secondary btn-sm" onClick={()=>openEdit(c)}><I.Edit size={13}/> Edit</button>
                  <button className="btn btn-danger btn-sm" onClick={()=>del(c.id)}><I.Trash size={13}/></button>
                </div>
              </div>
            </div>
          ))}
          {filtered.length===0&&search&&(
            <div style={{textAlign:'center',padding:32,color:'var(--muted)',fontSize:13}}>No connections match "{search}"</div>
          )}
        </div>
      )}

      {modal && (
        <div className="modal-overlay" onClick={()=>setModal(null)}>
          <div className="modal" onClick={e=>e.stopPropagation()}>
            <div className="modal-title">{modal==='new'?'New Connection':'Edit Connection'}</div>
            <div className="modal-desc">{modal==='new'?'Configure your FTP or SFTP server':'Update server details'}</div>
            <div>
              <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'0 12px'}}>
                <div className="form-group" style={{gridColumn:'1 / -1'}}>
                  <label className="form-label">Name</label>
                  <input className="input" placeholder="My Production Server" value={form.name} onChange={e=>F('name',e.target.value)} autoFocus required/>
                </div>
                <div className="form-group">
                  <label className="form-label">Protocol</label>
                  <select className="input" value={form.protocol} onChange={e=>F('protocol',e.target.value)}>
                    <option value="sftp">SFTP</option>
                    <option value="ftp">FTP</option>
                  </select>
                </div>
                <div className="form-group">
                  <label className="form-label">Port</label>
                  <input className="input" type="number" placeholder={form.protocol==='sftp'?'22':'21'} value={form.port} onChange={e=>F('port',parseInt(e.target.value)||22)}/>
                </div>
                <div className="form-group" style={{gridColumn:'1 / -1'}}>
                  <label className="form-label">Host</label>
                  <input className="input" placeholder="server.example.com or 192.168.1.1" value={form.host} onChange={e=>F('host',e.target.value)} required/>
                </div>
                <div className="form-group" style={{gridColumn:'1 / -1'}}>
                  <label className="form-label">Username</label>
                  <input className="input" placeholder="user" value={form.username} onChange={e=>F('username',e.target.value)} required/>
                </div>
                <div className="form-group" style={{gridColumn:'1 / -1'}}>
                  <label className="form-label">Password {modal!=='new'&&<span style={{color:'var(--muted)',fontSize:10,textTransform:'none'}}>(leave blank to keep current)</span>}</label>
                  <input className="input" type="password" placeholder={modal!=='new'?'Leave blank to keep existing':'password'} value={form.password} onChange={e=>F('password',e.target.value)}/>
                </div>
                {form.protocol==='sftp'&&(
                  <div className="form-group" style={{gridColumn:'1 / -1'}}>
                    <label className="form-label">Private Key (optional)</label>
                    <textarea className="input" placeholder="-----BEGIN RSA PRIVATE KEY-----" value={form.private_key} onChange={e=>F('private_key',e.target.value)} style={{minHeight:70}}/>
                  </div>
                )}
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-ghost" onClick={()=>setModal(null)}>Cancel</button>
                <button className="btn btn-primary" onClick={()=>save()} disabled={saving}>
                  {saving?<Spinner/>:<I.Check size={13}/>} {modal==='new'?'Create Connection':'Save Changes'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

// ─── Page: File Browser ───────────────────────────────────
function FileBrowser() {
  const [conns,  setConns]  = useState([]);
  const [conn,   setConn]   = useState(null);
  const [path,   setPath]   = useState('/');
  const [files,  setFiles]  = useState([]);
  const [loading,setLoading]= useState(true);
  const [busy,   setBusy]   = useState(false);
  const [renaming,setRenaming]=useState(null);
  const [mkdir,  setMkdir]  = useState(false);
  const [newName,setNewName]= useState('');
  const [newDir, setNewDir] = useState('');
  const [saving, setSaving] = useState(false);
  const [search, setSearch] = useState('');
  const fileRef = useRef();
  const { navigate } = useRouter();

  useEffect(()=>{
    api.get('/connections')
      .then(cs=>{ const arr=Array.isArray(cs)?cs:[]; setConns(arr); if(arr.length>0) setConn(arr[0]); })
      .catch(()=>toast.error('Failed to load connections'))
      .finally(()=>setLoading(false));
  },[]);

  const browse = useCallback(async(connId,p)=>{
    setBusy(true); setSearch('');
    try{
      const r=await api.get(`/files/${connId}/list?path=${encodeURIComponent(p)}`);
      setFiles(Array.isArray(r.items)?r.items:[]);
      setPath(r.path);
    }
    catch(err){ toast.error(err.message||'Failed to list directory'); }
    finally{ setBusy(false); }
  },[]);

  useEffect(()=>{ if(conn) browse(conn.id,'/'); },[conn]);

  const nav = p => conn && browse(conn.id, p);

  const doDownload = async item=>{
    try{
      const blob = await apiFetch('GET',`/files/${conn.id}/download?path=${encodeURIComponent(item.path)}`);
      const url=URL.createObjectURL(blob); const a=document.createElement('a');
      a.href=url; a.download=item.name; document.body.appendChild(a); a.click();
      URL.revokeObjectURL(url); a.remove(); toast.success('Download started');
    } catch(e){ toast.error('Download failed'); }
  };

  const doDelete = async item=>{
    if(!confirm(`Delete "${item.name}"?`)) return;
    try{
      if(item.type==='directory') await api.delete(`/files/${conn.id}/rmdir?path=${encodeURIComponent(item.path)}`);
      else await api.delete(`/files/${conn.id}/delete?path=${encodeURIComponent(item.path)}`);
      toast.success('Deleted'); browse(conn.id, path);
    }catch(err){ toast.error(err.message); }
  };

  const doRename = async e=>{
    e.preventDefault(); if(!renaming||!newName) return; setSaving(true);
    const np = joinPath(parentPath(renaming.path), newName);
    try{
      await api.post(`/files/${conn.id}/rename?old_path=${encodeURIComponent(renaming.path)}&new_path=${encodeURIComponent(np)}`);
      toast.success('Renamed'); setRenaming(null); browse(conn.id, path);
    }catch(err){ toast.error(err.message); }
    finally{ setSaving(false); }
  };

  const doMkdir = async e=>{
    e.preventDefault(); if(!newDir) return; setSaving(true);
    try{
      await api.post(`/files/${conn.id}/mkdir?path=${encodeURIComponent(joinPath(path,newDir))}`);
      toast.success('Directory created'); setMkdir(false); setNewDir(''); browse(conn.id, path);
    }catch(err){ toast.error(err.message); }
    finally{ setSaving(false); }
  };

  const doUpload = async e=>{
    const file=e.target.files?.[0]; if(!file) return;
    const fd=new FormData(); fd.append('file',file);
    try{
      await api.postFile(`/files/${conn.id}/upload?path=${encodeURIComponent(path)}`,fd);
      toast.success(`Uploaded ${file.name}`); browse(conn.id, path);
    }catch(err){ toast.error(err.message); }
    if(fileRef.current) fileRef.current.value='';
  };

  const pathParts  = path.split('/').filter(Boolean);
  const allSorted  = [...files].sort((a,b)=>{ if(a.type!==b.type) return a.type==='directory'?-1:1; return a.name.localeCompare(b.name); });
  const sorted     = search ? allSorted.filter(f=>f.name.toLowerCase().includes(search.toLowerCase())) : allSorted;

  return (
    <>
      <div className="page-header">
        <div>
          <div className="page-title">File Browser</div>
          <div className="page-sub">Browse and manage remote files</div>
        </div>
      </div>

      {loading ? (
        <div style={{textAlign:'center',padding:48}}><Spinner size={28}/></div>
      ) : conns.length===0 ? (
        <div className="card"><div className="empty-state">
          <span className="empty-icon">🖥️</span>
          <div className="empty-title">No connections available</div>
          <div className="empty-sub">Add a connection first to browse files</div>
          <button className="btn btn-primary" onClick={()=>navigate('/connections')}><I.Plus size={14}/> Add Connection</button>
        </div></div>
      ) : (
        <>
          {/* Toolbar */}
          <div className="card card-p" style={{marginBottom:12}}>
            <div style={{display:'flex',gap:8,flexWrap:'wrap',alignItems:'center'}}>
              <div style={{display:'flex',alignItems:'center',gap:7,flex:'1 1 180px',minWidth:0}}>
                <I.Server size={14} color="var(--muted)"/>
                <select className="input" style={{flex:1,height:36,padding:'5px 30px 5px 10px',fontSize:13}} value={conn?.id||''}
                  onChange={e=>{ const c=conns.find(x=>x.id===e.target.value); if(c) setConn(c); }}>
                  {conns.map(c=><option key={c.id} value={c.id}>{c.name} ({c.protocol.toUpperCase()})</option>)}
                </select>
              </div>
              <div style={{display:'flex',gap:6,flexWrap:'wrap'}}>
                <button className="btn btn-secondary btn-sm" onClick={()=>browse(conn.id,path)} disabled={busy} title="Refresh">
                  {busy?<Spinner size={12}/>:<I.Refresh size={13}/>}
                </button>
                <button className="btn btn-secondary btn-sm" onClick={()=>setMkdir(true)}><I.FolderPlus size={13}/> Folder</button>
                <button className="btn btn-primary btn-sm" onClick={()=>fileRef.current?.click()}><I.Upload size={13}/> Upload</button>
                <input ref={fileRef} type="file" style={{display:'none'}} onChange={doUpload}/>
              </div>
            </div>
          </div>

          {/* Breadcrumb + search row */}
          <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:10,flexWrap:'wrap'}}>
            <div style={{display:'flex',alignItems:'center',gap:2,flex:1,overflowX:'auto',fontSize:12,minWidth:0}}>
              <button className="btn btn-ghost btn-sm" style={{padding:'4px 7px'}} onClick={()=>nav('/')}><I.Home size={12}/></button>
              {pathParts.map((p,i)=>(
                <React.Fragment key={i}>
                  <span style={{color:'var(--muted)',flexShrink:0}}><I.Right size={12}/></span>
                  <button className="btn btn-ghost btn-sm" style={{padding:'4px 8px',color:i===pathParts.length-1?'var(--text)':'var(--muted2)',fontWeight:i===pathParts.length-1?700:400,whiteSpace:'nowrap'}}
                    onClick={()=>nav('/'+pathParts.slice(0,i+1).join('/'))}>
                    {p}
                  </button>
                </React.Fragment>
              ))}
            </div>
            {files.length>5&&(
              <div style={{position:'relative',flexShrink:0}}>
                <span style={{position:'absolute',left:8,top:'50%',transform:'translateY(-50%)',color:'var(--muted)',pointerEvents:'none'}}>
                  <I.Search size={12}/>
                </span>
                <input className="input" placeholder="Filter files…" value={search} onChange={e=>setSearch(e.target.value)}
                  style={{paddingLeft:26,height:32,fontSize:12,width:150}}/>
              </div>
            )}
          </div>

          {/* File list */}
          <div className="card" style={{overflow:'hidden'}}>
            {path!=='/'&&(
              <div className="file-row" style={{cursor:'pointer'}} onClick={()=>nav(parentPath(path))}>
                <div className="file-icon-wrap" style={{background:'rgba(255,255,255,0.04)'}}><I.Up size={14}/></div>
                <span style={{color:'var(--muted)',fontStyle:'italic',fontSize:13}}>.. Parent directory</span>
              </div>
            )}
            {busy ? (
              <div style={{textAlign:'center',padding:40}}><Spinner size={22}/></div>
            ) : sorted.length===0&&search ? (
              <div style={{textAlign:'center',padding:32,color:'var(--muted)',fontSize:13}}>No files match "{search}"</div>
            ) : sorted.length===0 ? (
              <div className="empty-state" style={{padding:'36px 24px'}}>
                <span className="empty-icon" style={{fontSize:32}}>📂</span>
                <div className="empty-title" style={{fontSize:14}}>Empty directory</div>
              </div>
            ) : sorted.map(item=>(
              <div key={item.path} className="file-row" style={{cursor:item.type==='directory'?'pointer':'default'}}
                   onClick={()=>item.type==='directory'&&nav(item.path)}>
                <div className="file-icon-wrap" style={{background:item.type==='directory'?'var(--amber-bg)':'rgba(255,255,255,0.04)',fontSize:15}}>
                  {fileEmoji(item.type,item.name)}
                </div>
                <div style={{flex:1,minWidth:0}}>
                  <div style={{fontSize:13,fontWeight:500,overflow:'hidden',textOverflow:'ellipsis',whiteSpace:'nowrap'}}>{item.name}</div>
                  <div style={{fontSize:11,color:'var(--muted)',display:'flex',gap:10,marginTop:2,flexWrap:'wrap'}}>
                    {item.size!=null&&<span>{formatBytes(item.size)}</span>}
                    {item.modified&&<span>{relTime(item.modified)}</span>}
                    {item.permissions&&<span style={{fontFamily:'JetBrains Mono,monospace'}}>{item.permissions}</span>}
                  </div>
                </div>
                <div className="file-actions">
                  {item.type==='file'&&<button className="btn btn-secondary btn-icon btn-sm" onClick={e=>{e.stopPropagation();doDownload(item);}} title="Download"><I.Download size={13}/></button>}
                  <button className="btn btn-secondary btn-icon btn-sm" onClick={e=>{e.stopPropagation();setRenaming(item);setNewName(item.name);}} title="Rename"><I.Edit size={13}/></button>
                  <button className="btn btn-danger btn-icon btn-sm" onClick={e=>{e.stopPropagation();doDelete(item);}} title="Delete"><I.Trash size={13}/></button>
                </div>
              </div>
            ))}
            {!busy&&sorted.length>0&&(
              <div style={{padding:'8px 16px',borderTop:'1px solid rgba(255,255,255,0.03)',fontSize:11,color:'var(--muted)',display:'flex',gap:12}}>
                <span>{sorted.filter(f=>f.type==='directory').length} folders</span>
                <span>{sorted.filter(f=>f.type==='file').length} files</span>
              </div>
            )}
          </div>
        </>
      )}

      {renaming&&(
        <div className="modal-overlay" onClick={()=>setRenaming(null)}>
          <div className="modal" onClick={e=>e.stopPropagation()} style={{maxWidth:380}}>
            <div className="modal-title">Rename</div>
            <div className="modal-desc">Enter a new name for <strong>"{renaming.name}"</strong></div>
            <div className="form-group">
              <label className="form-label">New Name</label>
              <input className="input" value={newName} onChange={e=>setNewName(e.target.value)} autoFocus
                onKeyDown={e=>e.key==='Enter'&&doRename(e)}/>
            </div>
            <div className="modal-footer">
              <button className="btn btn-ghost" onClick={()=>setRenaming(null)}>Cancel</button>
              <button className="btn btn-primary" onClick={doRename} disabled={saving}>{saving?<Spinner/>:<I.Check size={13}/>} Rename</button>
            </div>
          </div>
        </div>
      )}

      {mkdir&&(
        <div className="modal-overlay" onClick={()=>setMkdir(false)}>
          <div className="modal" onClick={e=>e.stopPropagation()} style={{maxWidth:380}}>
            <div className="modal-title">Create Folder</div>
            <div className="modal-desc">Enter a name for the new directory</div>
            <div className="form-group">
              <label className="form-label">Folder Name</label>
              <input className="input" placeholder="new-folder" value={newDir} onChange={e=>setNewDir(e.target.value)} autoFocus
                onKeyDown={e=>e.key==='Enter'&&doMkdir(e)}/>
            </div>
            <div className="modal-footer">
              <button className="btn btn-ghost" onClick={()=>setMkdir(false)}>Cancel</button>
              <button className="btn btn-primary" onClick={doMkdir} disabled={saving}>{saving?<Spinner/>:<I.FolderPlus size={13}/>} Create</button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

// ─── Page: API Keys ───────────────────────────────────────
function APIKeys() {
  const [keys,   setKeys]   = useState([]);
  const [loading,setLoading]= useState(true);
  const [modal,  setModal]  = useState(false);
  const [newKey, setNewKey] = useState(null);
  const [copied, setCopied] = useState(false);
  const [form,   setForm]   = useState({name:'',expires_in_days:'30'});
  const [saving, setSaving] = useState(false);

  const load = useCallback(()=>
    api.get('/api-keys')
      .then(d=>setKeys(Array.isArray(d)?d:[]))
      .catch(()=>toast.error('Failed to load keys'))
      .finally(()=>setLoading(false))
  ,[]);
  useEffect(()=>{ load(); },[]);

  const create = async e=>{
    e.preventDefault(); setSaving(true);
    try{
      const d = await api.post('/api-keys',{name:form.name,expires_in_days:form.expires_in_days==='never'?null:parseInt(form.expires_in_days)});
      setModal(false); setNewKey(d); setCopied(false); setForm({name:'',expires_in_days:'30'}); load();
    }catch(err){ toast.error(err.message||'Failed to create key'); }
    finally{ setSaving(false); }
  };

  const revoke = async id=>{
    if(!confirm('Revoke this API key? This cannot be undone.')) return;
    try{ await api.delete(`/api-keys/${id}`); toast.success('API key revoked'); load(); }
    catch(err){ toast.error(err.message); }
  };

  const copyKey = () => {
    navigator.clipboard.writeText(newKey.api_key);
    setCopied(true); toast.success('Copied to clipboard!');
    setTimeout(()=>setCopied(false),2000);
  };

  const isExpired = d => d && new Date(d)<new Date();

  return (
    <>
      <div className="page-header">
        <div>
          <div className="page-title">API Keys</div>
          <div className="page-sub">Programmatic access to your files</div>
        </div>
        <button className="btn btn-primary" onClick={()=>setModal(true)}><I.Plus size={14}/> Generate Key</button>
      </div>

      <div className="info-box" style={{marginBottom:16}}>
        <div className="info-box-icon"><I.Code size={14}/></div>
        <div>
          <div style={{fontSize:13,fontWeight:700,marginBottom:2}}>How to use API Keys</div>
          <div style={{fontSize:12,color:'var(--muted2)',lineHeight:1.6}}>
            Send your key in the <code>X-API-Key</code> header to authenticate requests without exposing your password.
          </div>
        </div>
      </div>

      {loading ? (
        <div style={{display:'flex',flexDirection:'column',gap:10}}>
          {[1,2].map(i=>(<div key={i} className="card card-p"><SkeletonLine w="40%" h={18} mb={8}/><SkeletonLine w="60%" h={13} mb={0}/></div>))}
        </div>
      ) : keys.length===0 ? (
        <div className="card"><div className="empty-state">
          <span className="empty-icon">🔑</span>
          <div className="empty-title">No API keys yet</div>
          <div className="empty-sub">Generate a key to access your files programmatically from any app or script</div>
          <button className="btn btn-primary" onClick={()=>setModal(true)}><I.Plus size={14}/> Generate Key</button>
        </div></div>
      ) : (
        <div style={{display:'flex',flexDirection:'column',gap:10}}>
          {keys.map(k=>{
            const expired = isExpired(k.expires_at);
            const active  = k.is_active && !expired;
            return (
              <div key={k.id} className="card card-p">
                <div style={{display:'flex',alignItems:'flex-start',justifyContent:'space-between',gap:12,flexWrap:'wrap'}}>
                  <div style={{display:'flex',gap:13}}>
                    <div style={{width:44,height:44,borderRadius:11,flexShrink:0,display:'flex',alignItems:'center',justifyContent:'center',
                      background:active?'var(--green-bg)':'rgba(255,255,255,0.04)',
                      border:`1px solid ${active?'var(--green-border)':'var(--border3)'}`,
                      color:active?'var(--green)':'var(--muted)'}}>
                      <I.Key size={18}/>
                    </div>
                    <div>
                      <div style={{display:'flex',alignItems:'center',gap:8,flexWrap:'wrap',marginBottom:5}}>
                        <span style={{fontSize:15,fontWeight:700}}>{k.name}</span>
                        {k.is_active ? (expired ? <span className="badge badge-amber">⚠ Expired</span> : <span className="badge badge-green">● Active</span>) : <span className="badge badge-red">Revoked</span>}
                      </div>
                      <div style={{fontSize:12,fontFamily:'JetBrains Mono,monospace',color:'var(--muted)',marginBottom:8,letterSpacing:'0.5px'}}>
                        {k.key_prefix}<span style={{opacity:0.35}}>{'•'.repeat(22)}</span>
                      </div>
                      <div style={{display:'flex',gap:14,fontSize:11,color:'var(--muted)',flexWrap:'wrap',alignItems:'center'}}>
                        <span><I.Clock size={10}/> Created {fmtDate(k.created_at)}</span>
                        {k.expires_at && <span style={{color:expired?'var(--red)':'var(--muted)'}}>Expires {fmtDate(k.expires_at)}</span>}
                        {k.last_used  && <span>Last used {relTime(k.last_used)}</span>}
                      </div>
                    </div>
                  </div>
                  {k.is_active && <button className="btn btn-danger btn-sm" onClick={()=>revoke(k.id)}><I.Trash size={13}/> Revoke</button>}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {modal&&(
        <div className="modal-overlay" onClick={()=>setModal(false)}>
          <div className="modal" onClick={e=>e.stopPropagation()} style={{maxWidth:400}}>
            <div className="modal-title">Generate API Key</div>
            <div className="modal-desc">Create a new key for programmatic access</div>
            <div className="form-group">
              <label className="form-label">Key Name</label>
              <input className="input" placeholder="e.g. My App, CI/CD Pipeline" value={form.name} onChange={e=>setForm(f=>({...f,name:e.target.value}))} autoFocus/>
            </div>
            <div className="form-group">
              <label className="form-label">Expiration</label>
              <select className="input" value={form.expires_in_days} onChange={e=>setForm(f=>({...f,expires_in_days:e.target.value}))}>
                <option value="7">7 days</option>
                <option value="30">30 days</option>
                <option value="90">90 days</option>
                <option value="365">1 year</option>
                <option value="never">Never expires</option>
              </select>
            </div>
            <div className="modal-footer">
              <button className="btn btn-ghost" onClick={()=>setModal(false)}>Cancel</button>
              <button className="btn btn-primary" onClick={create} disabled={saving||!form.name}>
                {saving?<Spinner/>:<I.Key size={13}/>} Generate Key
              </button>
            </div>
          </div>
        </div>
      )}

      {newKey&&(
        <div className="modal-overlay">
          <div className="modal" style={{maxWidth:430}}>
            <div style={{display:'flex',alignItems:'center',gap:10,marginBottom:16}}>
              <div style={{width:36,height:36,borderRadius:9,background:'var(--green-bg)',border:'1px solid var(--green-border)',display:'flex',alignItems:'center',justifyContent:'center',color:'var(--green)',flexShrink:0}}>
                <I.Check size={16}/>
              </div>
              <div>
                <div className="modal-title" style={{margin:0}}>Key Generated!</div>
                <div style={{fontSize:12,color:'var(--red)',marginTop:2,fontWeight:600}}>⚠ Copy now — this key won't be shown again</div>
              </div>
            </div>
            <div style={{background:'rgba(0,0,0,0.5)',border:'1px solid var(--border2)',borderRadius:10,padding:14,fontFamily:'JetBrains Mono,monospace',fontSize:12,wordBreak:'break-all',marginBottom:12,color:'#94a3b8',letterSpacing:'0.3px',lineHeight:1.7}}>
              {newKey.api_key}
            </div>
            <button className="btn btn-primary" style={{width:'100%',justifyContent:'center',marginBottom:8}} onClick={copyKey}>
              {copied ? <><I.Check size={13}/> Copied!</> : <><I.Copy size={13}/> Copy to Clipboard</>}
            </button>
            <button className="btn btn-secondary" style={{width:'100%',justifyContent:'center'}} onClick={()=>setNewKey(null)}>Done</button>
          </div>
        </div>
      )}
    </>
  );
}

// ─── Page: API Docs ───────────────────────────────────────
function APIDocs() {
  const [tab, setTab]     = useState('files');
  const [copied, setCopied]= useState(null);
  const base = window.location.origin + '/api';

  const copyCode = (code, id) => {
    navigator.clipboard.writeText(code);
    setCopied(id); toast.success('Copied!');
    setTimeout(()=>setCopied(null),2000);
  };

  const methodStyle = {
    GET:   {color:'var(--green)',bg:'var(--green-bg)',border:'var(--green-border)'},
    POST:  {color:'var(--blue)',bg:'var(--blue-bg)',border:'var(--blue-border)'},
    PUT:   {color:'var(--amber)',bg:'var(--amber-bg)',border:'var(--amber-border)'},
    DELETE:{color:'var(--red)',bg:'var(--red-bg)',border:'var(--red-border)'},
  };

  const EP = ({method,path:p,desc,code,params,id}) => {
    const s = methodStyle[method];
    return (
      <div className="card card-p" style={{marginBottom:10}}>
        <div style={{display:'flex',alignItems:'flex-start',gap:10,marginBottom:code?12:0}}>
          <span style={{padding:'3px 8px',borderRadius:6,fontSize:11,fontWeight:800,fontFamily:'JetBrains Mono,monospace',
            background:s.bg,color:s.color,border:`1px solid ${s.border}`,flexShrink:0,letterSpacing:'0.5px'}}>
            {method}
          </span>
          <div style={{flex:1,minWidth:0}}>
            <code style={{fontSize:13,background:'transparent',padding:0,color:'var(--text)',fontFamily:'JetBrains Mono,monospace',fontWeight:500}}>{p}</code>
            <div style={{fontSize:12,color:'var(--muted)',marginTop:4,lineHeight:1.55}}>{desc}</div>
            {params&&<div style={{marginTop:6,fontSize:12}}><span style={{color:'var(--muted)',fontWeight:600}}>Params: </span><span style={{color:'var(--muted2)'}}>{params}</span></div>}
          </div>
          {code&&(
            <button className="btn btn-ghost btn-icon btn-sm" style={{flexShrink:0}} onClick={()=>copyCode(code,id||p)} title="Copy">
              {copied===id||copied===p ? <I.Check size={13} color="var(--green)"/> : <I.Copy size={13}/>}
            </button>
          )}
        </div>
        {code&&<pre className="code-block">{code}</pre>}
      </div>
    );
  };

  return (
    <>
      <div className="page-header">
        <div>
          <div className="page-title">API Documentation</div>
          <div className="page-sub">Interact with your files programmatically</div>
        </div>
      </div>

      <div className="card card-p" style={{marginBottom:12}}>
        <div style={{display:'flex',gap:10,alignItems:'flex-start',marginBottom:14}}>
          <div style={{width:34,height:34,borderRadius:8,background:'var(--primary-bg)',border:'1px solid var(--primary-border)',display:'flex',alignItems:'center',justifyContent:'center',flexShrink:0,color:'var(--primary)'}}>
            <I.Shield size={14}/>
          </div>
          <div>
            <div style={{fontSize:14,fontWeight:700,marginBottom:3}}>Authentication</div>
            <div style={{fontSize:12,color:'var(--muted2)',lineHeight:1.6}}>
              Use an API key via <code>X-API-Key</code> header, or a JWT token via <code>Authorization: Bearer</code>
            </div>
          </div>
        </div>
        <pre className="code-block">{`curl "${base}/files/{id}/list?path=/" \\\n  -H "X-API-Key: your_api_key"`}</pre>
      </div>

      <div className="info-box" style={{marginBottom:16}}>
        <div className="info-box-icon"><I.Globe size={14}/></div>
        <div>
          <div style={{fontSize:11,fontWeight:700,color:'var(--muted2)',textTransform:'uppercase',letterSpacing:'0.6px',marginBottom:2}}>Base URL</div>
          <code style={{fontSize:13,background:'transparent',padding:0,color:'var(--primary2)',fontFamily:'JetBrains Mono,monospace'}}>{base}</code>
        </div>
      </div>

      <div className="tabs" style={{marginBottom:16}}>
        {[['files','📁 Files'],['connections','🖥️ Connections'],['keys','🔑 API Keys']].map(([k,l])=>(
          <button key={k} className={`tab${tab===k?' active':''}`} onClick={()=>setTab(k)}>{l}</button>
        ))}
      </div>

      {tab==='files'&&<>
        <EP method="GET"    path="/files/{id}/list"     desc="List directory contents" params="path (default: /)" id="list" code={`curl "${base}/files/{id}/list?path=/home/user" \\\n  -H "X-API-Key: your_key"`}/>
        <EP method="GET"    path="/files/{id}/download" desc="Download a file" params="path (required)" id="dl" code={`curl "${base}/files/{id}/download?path=/file.txt" \\\n  -H "X-API-Key: your_key" -o file.txt`}/>
        <EP method="POST"   path="/files/{id}/upload"   desc="Upload a file (multipart/form-data)" params="path, file (form)" id="ul" code={`curl -X POST "${base}/files/{id}/upload?path=/home/user" \\\n  -H "X-API-Key: your_key" \\\n  -F "file=@local_file.txt"`}/>
        <EP method="POST"   path="/files/{id}/mkdir"    desc="Create a directory" params="path (required)" id="mkdir" code={`curl -X POST "${base}/files/{id}/mkdir?path=/newdir" \\\n  -H "X-API-Key: your_key"`}/>
        <EP method="POST"   path="/files/{id}/rename"   desc="Rename a file or directory" params="old_path, new_path" id="rename" code={`curl -X POST "${base}/files/{id}/rename?old_path=/old.txt&new_path=/new.txt" \\\n  -H "X-API-Key: your_key"`}/>
        <EP method="DELETE" path="/files/{id}/delete"   desc="Delete a file" params="path (required)" id="delfile" code={`curl -X DELETE "${base}/files/{id}/delete?path=/file.txt" \\\n  -H "X-API-Key: your_key"`}/>
        <EP method="DELETE" path="/files/{id}/rmdir"    desc="Delete a directory" params="path (required)" id="rmdir" code={`curl -X DELETE "${base}/files/{id}/rmdir?path=/dir" \\\n  -H "X-API-Key: your_key"`}/>
      </>}
      {tab==='connections'&&<>
        <EP method="GET"    path="/connections"           desc="List all server connections" id="lconns" code={`curl "${base}/connections" -H "Authorization: Bearer jwt"`}/>
        <EP method="POST"   path="/connections"           desc="Create a new server connection" id="cconn" code={`curl -X POST "${base}/connections" \\\n  -H "Authorization: Bearer jwt" \\\n  -H "Content-Type: application/json" \\\n  -d '{"name":"Server","protocol":"sftp","host":"host","port":22,"username":"user","password":"pass"}'`}/>
        <EP method="POST"   path="/connections/{id}/test" desc="Test a connection" id="tconn" code={`curl -X POST "${base}/connections/{id}/test" -H "Authorization: Bearer jwt"`}/>
        <EP method="PUT"    path="/connections/{id}"      desc="Update a connection" id="uconn" code={`curl -X PUT "${base}/connections/{id}" -H "Authorization: Bearer jwt" -H "Content-Type: application/json" -d '{"name":"New Name"}'`}/>
        <EP method="DELETE" path="/connections/{id}"      desc="Delete a connection" id="dconn" code={`curl -X DELETE "${base}/connections/{id}" -H "Authorization: Bearer jwt"`}/>
      </>}
      {tab==='keys'&&<>
        <EP method="GET"    path="/api-keys"       desc="List all API keys" id="lkeys" code={`curl "${base}/api-keys" -H "Authorization: Bearer jwt"`}/>
        <EP method="POST"   path="/api-keys"       desc="Create an API key" id="ckey" code={`curl -X POST "${base}/api-keys" \\\n  -H "Authorization: Bearer jwt" \\\n  -H "Content-Type: application/json" \\\n  -d '{"name":"My App","expires_in_days":30}'`}/>
        <EP method="DELETE" path="/api-keys/{id}"  desc="Revoke an API key" id="dkey" code={`curl -X DELETE "${base}/api-keys/{id}" -H "Authorization: Bearer jwt"`}/>
      </>}
    </>
  );
}

// ─── Page: Settings ───────────────────────────────────────
function Settings() {
  const { user, logout } = useAuth();
  const { navigate }     = useRouter();
  const [showToken, setShowToken] = useState(false);
  const [copied,    setCopied]    = useState('');
  const token = localStorage.getItem('token');
  let tokenExpiry = null;
  try { const p=JSON.parse(atob(token.split('.')[1])); tokenExpiry=new Date(p.exp*1000); } catch{}

  const copy = (text, key) => {
    navigator.clipboard.writeText(text);
    setCopied(key); toast.success('Copied!');
    setTimeout(()=>setCopied(''),1500);
  };

  const isExpired = tokenExpiry && tokenExpiry < new Date();

  return (
    <>
      <div className="page-header">
        <div>
          <div className="page-title">Settings</div>
          <div className="page-sub">Account and credentials</div>
        </div>
      </div>

      {/* Profile */}
      <div className="card card-p" style={{marginBottom:12}}>
        <div style={{display:'flex',alignItems:'center',gap:10,marginBottom:18}}>
          <I.User size={14} color="var(--primary)"/>
          <span style={{fontSize:14,fontWeight:700}}>Profile</span>
        </div>
        <div style={{display:'flex',gap:12,flexWrap:'wrap'}}>
          <div style={{width:54,height:54,borderRadius:13,background:'linear-gradient(135deg,var(--primary3),#8b5cf6)',display:'flex',alignItems:'center',justifyContent:'center',fontSize:22,fontWeight:800,color:'#fff',flexShrink:0}}>
            {user?.name?.charAt(0).toUpperCase()}
          </div>
          <div style={{flex:1,minWidth:0}}>
            <div style={{fontSize:17,fontWeight:800,marginBottom:2}}>{user?.name}</div>
            <div style={{fontSize:13,color:'var(--muted)',marginBottom:6}}>{user?.email}</div>
            <div style={{display:'flex',gap:6,flexWrap:'wrap'}}>
              <span className="badge badge-muted">Member since {user?.created_at ? new Date(user.created_at).toLocaleDateString('en-US',{month:'short',year:'numeric'}) : '—'}</span>
              <span className="badge badge-purple">
                <button style={{background:'none',border:'none',cursor:'pointer',color:'inherit',font:'inherit',padding:0,display:'flex',alignItems:'center',gap:4}}
                  onClick={()=>copy(user?.id,'uid')}>
                  {copied==='uid'?<I.Check size={10}/>:<I.Copy size={10}/>} Copy User ID
                </button>
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* JWT Token */}
      <div className="card card-p" style={{marginBottom:12}}>
        <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',marginBottom:14}}>
          <div style={{display:'flex',alignItems:'center',gap:8}}>
            <I.Shield size={14} color="var(--primary)"/>
            <span style={{fontSize:14,fontWeight:700}}>JWT Session Token</span>
          </div>
          {tokenExpiry && (
            <span className={`badge ${isExpired?'badge-red':'badge-green'}`}>
              {isExpired ? '⚠ Expired' : '● Active'}
            </span>
          )}
        </div>
        <div style={{fontSize:12,color:'var(--muted)',marginBottom:14,lineHeight:1.6}}>
          Use in <code>Authorization: Bearer &lt;token&gt;</code> for API access.
          {tokenExpiry && <span style={{color:isExpired?'var(--red)':'var(--muted)'}}> Expires {fmtDate(tokenExpiry.toISOString())}.</span>}
        </div>
        <div style={{background:'rgba(0,0,0,0.4)',border:'1px solid var(--border3)',borderRadius:10,padding:14,marginBottom:12}}>
          <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',marginBottom:10}}>
            <span style={{fontSize:11,fontWeight:700,color:'var(--muted2)',textTransform:'uppercase',letterSpacing:'0.6px'}}>Bearer Token</span>
            <div style={{display:'flex',gap:6}}>
              <button className="btn btn-ghost btn-icon btn-sm" onClick={()=>setShowToken(v=>!v)} title={showToken?'Hide':'Show'}>
                {showToken?<I.EyeOff size={13}/>:<I.Eye size={13}/>}
              </button>
              <button className="btn btn-ghost btn-icon btn-sm" onClick={()=>copy(token,'token')} title="Copy">
                {copied==='token'?<I.Check size={13} color="var(--green)"/>:<I.Copy size={13}/>}
              </button>
            </div>
          </div>
          <div style={{fontFamily:'JetBrains Mono,monospace',fontSize:11,wordBreak:'break-all',color:'var(--muted)',maxHeight:68,overflow:'auto',lineHeight:1.7}}>
            {showToken ? token : '•'.repeat(80)}
          </div>
        </div>
        <div className="sep"/>
        <div style={{fontSize:12,fontWeight:700,marginBottom:8,color:'var(--muted2)',textTransform:'uppercase',letterSpacing:'0.6px'}}>Example Usage</div>
        <pre className="code-block">{`curl "${window.location.origin}/api/connections" \\\n  -H "Authorization: Bearer YOUR_TOKEN"`}</pre>
      </div>

      {/* Auth info */}
      <div className="info-box" style={{marginBottom:16}}>
        <div className="info-box-icon"><I.Key size={14}/></div>
        <div>
          <div style={{fontSize:13,fontWeight:700,marginBottom:6}}>Authentication Methods</div>
          <div style={{display:'flex',gap:6,flexWrap:'wrap',marginBottom:8}}>
            <span className="badge badge-blue">JWT → Authorization: Bearer</span>
            <span className="badge badge-purple">API Key → X-API-Key</span>
          </div>
          <div style={{fontSize:12,color:'var(--muted2)',lineHeight:1.6}}>
            Use JWT tokens for dashboard sessions. Use API keys for scripts, CI/CD, and automations.
          </div>
        </div>
      </div>

      {/* Sign out */}
      <div className="card card-p" style={{borderColor:'var(--red-border)'}}>
        <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',flexWrap:'wrap',gap:12}}>
          <div>
            <div style={{fontSize:14,fontWeight:700,marginBottom:2}}>Sign Out</div>
            <div style={{fontSize:12,color:'var(--muted)'}}>Signed in as {user?.email}</div>
          </div>
          <button className="btn btn-danger" onClick={()=>{ logout(); navigate('/login'); }}>
            <I.LogOut size={13}/> Sign Out
          </button>
        </div>
      </div>
    </>
  );
}

// ─── App Root ─────────────────────────────────────────────
function ProtectedPages() {
  const { path } = useRouter();
  const pages = {
    '/':            <Dashboard/>,
    '/connections': <Connections/>,
    '/browser':     <FileBrowser/>,
    '/api-keys':    <APIKeys/>,
    '/docs':        <APIDocs/>,
    '/settings':    <Settings/>,
  };
  const page = pages[path] ?? <Dashboard/>;
  return <Layout>{page}</Layout>;
}

function AppRoutes() {
  const { path } = useRouter();
  const isPublic = path === '/login' || path === '/register';
  return (
    <>
      {path === '/login'    && <PublicRoute><Login/></PublicRoute>}
      {path === '/register' && <PublicRoute><Register/></PublicRoute>}
      {!isPublic            && <ProtectedRoute><ProtectedPages/></ProtectedRoute>}
    </>
  );
}

function App() {
  return (
    <Router>
      <AuthProvider>
        <AppRoutes/>
      </AuthProvider>
    </Router>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App/>);
</script>
</body>
</html>"""

# ─────────────────────────────────────────────────────────
# BACKEND
# ─────────────────────────────────────────────────────────
from fastapi import FastAPI, APIRouter, HTTPException, Depends, UploadFile, File, Query, Header
from fastapi.responses import StreamingResponse, HTMLResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
import aiosqlite
import os, logging, asyncio, io, hashlib, secrets, uuid, base64
from pathlib import Path
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Optional, Literal
from datetime import datetime, timezone, timedelta
import jwt
from passlib.context import CryptContext
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import paramiko, aioftp

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

DB_PATH       = os.environ.get("DB_PATH", str(ROOT_DIR / "relay_drive.db"))
import hashlib as _hl
# Always ensure keys are exactly 64 hex chars (32 bytes) — safe even if user sets a short env var
SECRET_KEY    = _hl.sha256(os.environ.get("SECRET_KEY",    secrets.token_hex(32)).encode()).hexdigest()
ENCRYPTION_KEY= _hl.sha256(os.environ.get("ENCRYPTION_KEY",secrets.token_hex(32)).encode()).hexdigest()
ALGORITHM     = "HS256"
TOKEN_MINUTES = 60 * 24

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _fernet():
    key = ENCRYPTION_KEY.encode()[:32].ljust(32, b"\0")
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"ftp_relay_salt_v1", iterations=100_000)
    return Fernet(base64.urlsafe_b64encode(kdf.derive(key)))

fernet = _fernet()
def enc(v): return fernet.encrypt(v.encode()).decode()
def dec(v): return fernet.decrypt(v.encode()).decode()

# ── DB ────────────────────────────────────────────────────
async def get_db():
    db = await aiosqlite.connect(DB_PATH)
    db.row_factory = aiosqlite.Row
    try: yield db
    finally: await db.close()

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY, email TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
            password_hash TEXT NOT NULL, created_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS connections (
            id TEXT PRIMARY KEY, user_id TEXT NOT NULL, name TEXT NOT NULL,
            protocol TEXT NOT NULL, host TEXT NOT NULL, port INTEGER NOT NULL,
            username TEXT NOT NULL, password TEXT, private_key TEXT,
            created_at TEXT NOT NULL, last_used TEXT);
        CREATE TABLE IF NOT EXISTS api_keys (
            id TEXT PRIMARY KEY, user_id TEXT NOT NULL, name TEXT NOT NULL,
            key_hash TEXT NOT NULL, key_prefix TEXT NOT NULL, created_at TEXT NOT NULL,
            expires_at TEXT, last_used TEXT, is_active INTEGER NOT NULL DEFAULT 1);
        CREATE TABLE IF NOT EXISTS activities (
            id TEXT PRIMARY KEY, user_id TEXT NOT NULL, connection_id TEXT,
            connection_name TEXT, action TEXT NOT NULL, path TEXT,
            status TEXT NOT NULL, error_message TEXT, timestamp TEXT NOT NULL);
        """)
        await db.commit()

def row(r): return dict(r) if r else None

# ── Models ────────────────────────────────────────────────
class UserCreate(BaseModel):
    email: EmailStr; password: str; name: str
class UserLogin(BaseModel):
    email: EmailStr; password: str
class UserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id:str; email:str; name:str; created_at:str
class TokenResponse(BaseModel):
    access_token:str; token_type:str="bearer"; user:UserResponse
class ConnCreate(BaseModel):
    name:str; protocol:Literal["ftp","sftp"]; host:str; port:int=22
    username:str; password:Optional[str]=None; private_key:Optional[str]=None
class ConnResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id:str; name:str; protocol:str; host:str; port:int; username:str
    has_password:bool; has_private_key:bool; created_at:str; last_used:Optional[str]=None
class ConnUpdate(BaseModel):
    name:Optional[str]=None; host:Optional[str]=None; port:Optional[int]=None
    username:Optional[str]=None; password:Optional[str]=None; private_key:Optional[str]=None
class KeyCreate(BaseModel):
    name:str; expires_in_days:Optional[int]=30
class KeyResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id:str; name:str; key_prefix:str; created_at:str
    expires_at:Optional[str]=None; last_used:Optional[str]=None; is_active:bool
class KeyCreated(KeyResponse):
    api_key:str
class FileItem(BaseModel):
    name:str; path:str; type:Literal["file","directory"]
    size:Optional[int]=None; modified:Optional[str]=None; permissions:Optional[str]=None
class DirResponse(BaseModel):
    path:str; items:List[FileItem]
class ActivityLog(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id:str; user_id:str; connection_id:Optional[str]=None; connection_name:Optional[str]=None
    action:str; path:Optional[str]=None; status:str; error_message:Optional[str]=None; timestamp:str
class Stats(BaseModel):
    total_connections:int; total_api_keys:int; active_api_keys:int
    recent_activities:List[ActivityLog]; operations_today:int

# ── Auth helpers ──────────────────────────────────────────
def make_token(uid): 
    return jwt.encode({"sub":uid,"exp":datetime.now(timezone.utc)+timedelta(minutes=TOKEN_MINUTES)}, SECRET_KEY, algorithm=ALGORITHM)

async def current_user(authorization:str=Header(None), db:aiosqlite.Connection=Depends(get_db)):
    if not authorization: raise HTTPException(401,"Not authenticated")
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer": raise HTTPException(401,"Bad scheme")
        uid = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        async with db.execute("SELECT id,email,name,created_at FROM users WHERE id=?",(uid,)) as c:
            u = row(await c.fetchone())
        if not u: raise HTTPException(401,"User not found")
        return u
    except jwt.ExpiredSignatureError: raise HTTPException(401,"Token expired")
    except HTTPException: raise
    except: raise HTTPException(401,"Invalid token")

async def current_user_or_key(authorization:str=Header(None), x_api_key:str=Header(None), db:aiosqlite.Connection=Depends(get_db)):
    if x_api_key:
        h = hashlib.sha256(x_api_key.encode()).hexdigest()
        async with db.execute("SELECT * FROM api_keys WHERE key_hash=? AND is_active=1",(h,)) as c:
            k = row(await c.fetchone())
        if not k: raise HTTPException(401,"Invalid API key")
        if k.get("expires_at") and datetime.now(timezone.utc) > datetime.fromisoformat(k["expires_at"]):
            raise HTTPException(401,"API key expired")
        await db.execute("UPDATE api_keys SET last_used=? WHERE id=?",(datetime.now(timezone.utc).isoformat(),k["id"]))
        await db.commit()
        async with db.execute("SELECT id,email,name,created_at FROM users WHERE id=?",(k["user_id"],)) as c:
            u = row(await c.fetchone())
        if not u: raise HTTPException(401,"User not found")
        return u
    return await current_user(authorization, db)

async def log_act(db, user_id, action, conn_id=None, conn_name=None, path=None, status="success", err=None):
    await db.execute(
        "INSERT INTO activities VALUES(?,?,?,?,?,?,?,?,?)",
        (str(uuid.uuid4()),user_id,conn_id,conn_name,action,path,status,err,datetime.now(timezone.utc).isoformat()))
    await db.commit()

# ── FTP/SFTP clients ──────────────────────────────────────
class SFTP:
    def __init__(self,h,p,u,pw=None,pk=None): self.h,self.p,self.u,self.pw,self.pk=h,p,u,pw,pk; self._c=self._s=None
    async def connect(self):
        def _():
            self._c=paramiko.SSHClient(); self._c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.pk: self._c.connect(self.h,self.p,self.u,pkey=paramiko.RSAKey.from_private_key(io.StringIO(self.pk)),timeout=30)
            else: self._c.connect(self.h,self.p,self.u,self.pw,timeout=30)
            self._s=self._c.open_sftp()
        await asyncio.get_event_loop().run_in_executor(None,_)
    async def list_dir(self,path):
        def _():
            out=[]
            for a in self._s.listdir_attr(path):
                t="directory" if a.st_mode and (a.st_mode&0o40000) else "file"
                out.append(FileItem(name=a.filename,path=f"{path.rstrip('/')}/{a.filename}",type=t,
                    size=a.st_size if t=="file" else None,
                    modified=datetime.fromtimestamp(a.st_mtime,tz=timezone.utc).isoformat() if a.st_mtime else None,
                    permissions=oct(a.st_mode)[-3:] if a.st_mode else None))
            return out
        return await asyncio.get_event_loop().run_in_executor(None,_)
    async def download(self,path):
        def _():
            buf=io.BytesIO(); self._s.getfo(path,buf); return buf.getvalue()
        return await asyncio.get_event_loop().run_in_executor(None,_)
    async def upload(self,path,data):
        await asyncio.get_event_loop().run_in_executor(None,lambda:self._s.putfo(io.BytesIO(data),path))
    async def mkdir(self,path): await asyncio.get_event_loop().run_in_executor(None,self._s.mkdir,path)
    async def rmdir(self,path): await asyncio.get_event_loop().run_in_executor(None,self._s.rmdir,path)
    async def remove(self,path): await asyncio.get_event_loop().run_in_executor(None,self._s.remove,path)
    async def rename(self,o,n): await asyncio.get_event_loop().run_in_executor(None,self._s.rename,o,n)
    async def close(self):
        def _():
            if self._s: self._s.close()
            if self._c: self._c.close()
        await asyncio.get_event_loop().run_in_executor(None,_)

class FTP:
    def __init__(self,h,p,u,pw=None): self.h,self.p,self.u,self.pw=h,p,u,pw; self._c=None
    async def connect(self): self._c=aioftp.Client(); await self._c.connect(self.h,self.p); await self._c.login(self.u,self.pw or "")
    async def list_dir(self,path):
        out=[]
        async for e in self._c.list(path):
            out.append(FileItem(name=e[0],path=f"{path.rstrip('/')}/{e[0]}",
                type="directory" if e[1].get("type")=="dir" else "file",
                size=int(e[1].get("size",0)) if e[1].get("type")!="dir" else None,modified=e[1].get("modify")))
        return out
    async def download(self,path):
        s=await self._c.download_stream(path); d=b""
        async for ch in s.iter_by_block(): d+=ch
        await s.finish(); return d
    async def upload(self,path,data):
        s=await self._c.upload_stream(path); await s.write(data); await s.finish()
    async def mkdir(self,path): await self._c.make_directory(path)
    async def rmdir(self,path): await self._c.remove_directory(path)
    async def remove(self,path): await self._c.remove_file(path)
    async def rename(self,o,n): await self._c.rename(o,n)
    async def close(self):
        if self._c:
            try: await self._c.quit()
            except: pass

async def get_client(c):
    pw  = dec(c["password"])    if c.get("password")    else None
    pk  = dec(c["private_key"]) if c.get("private_key") else None
    cli = SFTP(c["host"],c["port"],c["username"],pw,pk) if c["protocol"]=="sftp" else FTP(c["host"],c["port"],c["username"],pw)
    await cli.connect(); return cli

# ── App ───────────────────────────────────────────────────
app = FastAPI(title="Relay Drive")
r   = APIRouter(prefix="/api")

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

# ── Auth ──────────────────────────────────────────────────
@r.post("/auth/register",response_model=TokenResponse)
async def register(body:UserCreate,db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT id FROM users WHERE email=?",(body.email,)) as c:
        if await c.fetchone(): raise HTTPException(400,"Email already registered")
    uid=str(uuid.uuid4()); now=datetime.now(timezone.utc).isoformat()
    await db.execute("INSERT INTO users VALUES(?,?,?,?,?)",(uid,body.email,body.name,pwd_ctx.hash(body.password),now))
    await db.commit()
    return TokenResponse(access_token=make_token(uid),user=UserResponse(id=uid,email=body.email,name=body.name,created_at=now))

@r.post("/auth/login",response_model=TokenResponse)
async def login(body:UserLogin,db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT * FROM users WHERE email=?",(body.email,)) as c:
        u=row(await c.fetchone())
    if not u or not pwd_ctx.verify(body.password,u["password_hash"]): raise HTTPException(401,"Invalid credentials")
    return TokenResponse(access_token=make_token(u["id"]),user=UserResponse(id=u["id"],email=u["email"],name=u["name"],created_at=u["created_at"]))

@r.get("/auth/me",response_model=UserResponse)
async def me(u=Depends(current_user)): return UserResponse(**u)

# ── Connections ───────────────────────────────────────────
@r.post("/connections",response_model=ConnResponse)
async def create_conn(body:ConnCreate,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    cid=str(uuid.uuid4()); now=datetime.now(timezone.utc).isoformat()
    await db.execute("INSERT INTO connections VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        (cid,u["id"],body.name,body.protocol,body.host,body.port,body.username,
         enc(body.password) if body.password else None,
         enc(body.private_key) if body.private_key else None,now,None))
    await db.commit(); await log_act(db,u["id"],"create_connection",cid,body.name)
    return ConnResponse(id=cid,name=body.name,protocol=body.protocol,host=body.host,port=body.port,
        username=body.username,has_password=bool(body.password),has_private_key=bool(body.private_key),created_at=now)

@r.get("/connections",response_model=List[ConnResponse])
async def list_conns(u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT * FROM connections WHERE user_id=?",(u["id"],)) as c:
        rows=[row(x) for x in await c.fetchall()]
    return [ConnResponse(id=x["id"],name=x["name"],protocol=x["protocol"],host=x["host"],port=x["port"],
        username=x["username"],has_password=bool(x.get("password")),has_private_key=bool(x.get("private_key")),
        created_at=x["created_at"],last_used=x.get("last_used")) for x in rows]

@r.get("/connections/{cid}",response_model=ConnResponse)
async def get_conn(cid:str,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT * FROM connections WHERE id=? AND user_id=?",(cid,u["id"])) as c:
        x=row(await c.fetchone())
    if not x: raise HTTPException(404,"Not found")
    return ConnResponse(id=x["id"],name=x["name"],protocol=x["protocol"],host=x["host"],port=x["port"],
        username=x["username"],has_password=bool(x.get("password")),has_private_key=bool(x.get("private_key")),
        created_at=x["created_at"],last_used=x.get("last_used"))

@r.put("/connections/{cid}",response_model=ConnResponse)
async def update_conn(cid:str,body:ConnUpdate,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT * FROM connections WHERE id=? AND user_id=?",(cid,u["id"])) as c:
        if not await c.fetchone(): raise HTTPException(404,"Not found")
    fields,vals=[],[]
    for f,v in [("name",body.name),("host",body.host),("port",body.port),("username",body.username)]:
        if v is not None: fields.append(f"{f}=?"); vals.append(v)
    if body.password: fields.append("password=?"); vals.append(enc(body.password))
    if body.private_key: fields.append("private_key=?"); vals.append(enc(body.private_key))
    if fields:
        vals.append(cid); await db.execute(f"UPDATE connections SET {','.join(fields)} WHERE id=?",vals); await db.commit()
    async with db.execute("SELECT * FROM connections WHERE id=?",(cid,)) as c:
        x=row(await c.fetchone())
    await log_act(db,u["id"],"update_connection",cid,x["name"])
    return ConnResponse(id=x["id"],name=x["name"],protocol=x["protocol"],host=x["host"],port=x["port"],
        username=x["username"],has_password=bool(x.get("password")),has_private_key=bool(x.get("private_key")),
        created_at=x["created_at"],last_used=x.get("last_used"))

@r.delete("/connections/{cid}")
async def delete_conn(cid:str,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT name FROM connections WHERE id=? AND user_id=?",(cid,u["id"])) as c:
        x=row(await c.fetchone())
    if not x: raise HTTPException(404,"Not found")
    await db.execute("DELETE FROM connections WHERE id=?",(cid,)); await db.commit()
    await log_act(db,u["id"],"delete_connection",cid,x["name"])
    return {"message":"Deleted"}

@r.post("/connections/{cid}/test")
async def test_conn(cid:str,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT * FROM connections WHERE id=? AND user_id=?",(cid,u["id"])) as c:
        x=row(await c.fetchone())
    if not x: raise HTTPException(404,"Not found")
    try:
        cli=await get_client(x); await cli.list_dir("/"); await cli.close()
        await log_act(db,u["id"],"test_connection",cid,x["name"])
        return {"status":"success","message":"Connection successful"}
    except Exception as e:
        await log_act(db,u["id"],"test_connection",cid,x["name"],status="error",err=str(e))
        raise HTTPException(400,f"Connection failed: {e}")

# ── API Keys ──────────────────────────────────────────────
@r.post("/api-keys",response_model=KeyCreated)
async def create_key(body:KeyCreate,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    k=secrets.token_urlsafe(32); kid=str(uuid.uuid4()); now=datetime.now(timezone.utc).isoformat()
    exp=(datetime.now(timezone.utc)+timedelta(days=body.expires_in_days)).isoformat() if body.expires_in_days else None
    await db.execute("INSERT INTO api_keys VALUES(?,?,?,?,?,?,?,?,1)",
        (kid,u["id"],body.name,hashlib.sha256(k.encode()).hexdigest(),k[:8],now,exp,None))
    await db.commit(); await log_act(db,u["id"],"create_api_key")
    return KeyCreated(id=kid,name=body.name,key_prefix=k[:8],created_at=now,expires_at=exp,is_active=True,api_key=k)

@r.get("/api-keys",response_model=List[KeyResponse])
async def list_keys(u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT id,name,key_prefix,created_at,expires_at,last_used,is_active FROM api_keys WHERE user_id=?",(u["id"],)) as c:
        rows=[row(x) for x in await c.fetchall()]
    return [KeyResponse(id=x["id"],name=x["name"],key_prefix=x["key_prefix"],created_at=x["created_at"],
        expires_at=x.get("expires_at"),last_used=x.get("last_used"),is_active=bool(x["is_active"])) for x in rows]

@r.delete("/api-keys/{kid}")
async def revoke_key(kid:str,u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT id FROM api_keys WHERE id=? AND user_id=?",(kid,u["id"])) as c:
        if not await c.fetchone(): raise HTTPException(404,"Not found")
    await db.execute("UPDATE api_keys SET is_active=0 WHERE id=?",(kid,)); await db.commit()
    await log_act(db,u["id"],"revoke_api_key"); return {"message":"Revoked"}

# ── File ops ──────────────────────────────────────────────
async def _get_conn(cid,uid,db):
    async with db.execute("SELECT * FROM connections WHERE id=? AND user_id=?",(cid,uid)) as c:
        x=row(await c.fetchone())
    if not x: raise HTTPException(404,"Connection not found")
    return x

@r.get("/files/{cid}/list",response_model=DirResponse)
async def list_dir(cid:str,path:str=Query("/"),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); items=await cli.list_dir(path); await cli.close()
        await db.execute("UPDATE connections SET last_used=? WHERE id=?",(datetime.now(timezone.utc).isoformat(),cid)); await db.commit()
        await log_act(db,u["id"],"list_directory",cid,x["name"],path)
        return DirResponse(path=path,items=items)
    except Exception as e:
        await log_act(db,u["id"],"list_directory",cid,x["name"],path,"error",str(e)); raise HTTPException(400,f"Failed: {e}")

@r.get("/files/{cid}/download")
async def download(cid:str,path:str=Query(...),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); data=await cli.download(path); await cli.close()
        await db.execute("UPDATE connections SET last_used=? WHERE id=?",(datetime.now(timezone.utc).isoformat(),cid)); await db.commit()
        await log_act(db,u["id"],"download_file",cid,x["name"],path)
        return StreamingResponse(io.BytesIO(data),media_type="application/octet-stream",
            headers={"Content-Disposition":f"attachment; filename={path.split('/')[-1]}"})
    except Exception as e:
        await log_act(db,u["id"],"download_file",cid,x["name"],path,"error",str(e)); raise HTTPException(400,f"Failed: {e}")

@r.post("/files/{cid}/upload")
async def upload(cid:str,path:str=Query(...),file:UploadFile=File(...),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); data=await file.read(); fp=f"{path.rstrip('/')}/{file.filename}"
        await cli.upload(fp,data); await cli.close()
        await db.execute("UPDATE connections SET last_used=? WHERE id=?",(datetime.now(timezone.utc).isoformat(),cid)); await db.commit()
        await log_act(db,u["id"],"upload_file",cid,x["name"],fp)
        return {"message":"Uploaded","path":fp}
    except Exception as e:
        await log_act(db,u["id"],"upload_file",cid,x["name"],path,"error",str(e)); raise HTTPException(400,f"Failed: {e}")

@r.post("/files/{cid}/mkdir")
async def mkdir(cid:str,path:str=Query(...),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); await cli.mkdir(path); await cli.close()
        await log_act(db,u["id"],"create_directory",cid,x["name"],path); return {"message":"Created","path":path}
    except Exception as e: raise HTTPException(400,f"Failed: {e}")

@r.delete("/files/{cid}/rmdir")
async def rmdir(cid:str,path:str=Query(...),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); await cli.rmdir(path); await cli.close()
        await log_act(db,u["id"],"delete_directory",cid,x["name"],path); return {"message":"Deleted"}
    except Exception as e: raise HTTPException(400,f"Failed: {e}")

@r.delete("/files/{cid}/delete")
async def delete_file(cid:str,path:str=Query(...),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); await cli.remove(path); await cli.close()
        await log_act(db,u["id"],"delete_file",cid,x["name"],path); return {"message":"Deleted"}
    except Exception as e: raise HTTPException(400,f"Failed: {e}")

@r.post("/files/{cid}/rename")
async def rename(cid:str,old_path:str=Query(...),new_path:str=Query(...),u=Depends(current_user_or_key),db:aiosqlite.Connection=Depends(get_db)):
    x=await _get_conn(cid,u["id"],db)
    try:
        cli=await get_client(x); await cli.rename(old_path,new_path); await cli.close()
        await log_act(db,u["id"],"rename_file",cid,x["name"],f"{old_path} -> {new_path}"); return {"message":"Renamed"}
    except Exception as e: raise HTTPException(400,f"Failed: {e}")

# ── Dashboard ─────────────────────────────────────────────
@r.get("/dashboard/stats",response_model=Stats)
async def stats(u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT COUNT(*) FROM connections WHERE user_id=?",(u["id"],)) as c: tc=(await c.fetchone())[0]
    async with db.execute("SELECT COUNT(*) FROM api_keys WHERE user_id=?",(u["id"],)) as c: tk=(await c.fetchone())[0]
    async with db.execute("SELECT COUNT(*) FROM api_keys WHERE user_id=? AND is_active=1",(u["id"],)) as c: ak=(await c.fetchone())[0]
    async with db.execute("SELECT * FROM activities WHERE user_id=? ORDER BY timestamp DESC LIMIT 10",(u["id"],)) as c: acts=[row(x) for x in await c.fetchall()]
    today=datetime.now(timezone.utc).replace(hour=0,minute=0,second=0,microsecond=0).isoformat()
    async with db.execute("SELECT COUNT(*) FROM activities WHERE user_id=? AND timestamp>=?",(u["id"],today)) as c: ot=(await c.fetchone())[0]
    return Stats(total_connections=tc,total_api_keys=tk,active_api_keys=ak,recent_activities=[ActivityLog(**a) for a in acts],operations_today=ot)

@r.get("/activities",response_model=List[ActivityLog])
async def activities(limit:int=Query(50,le=100),u=Depends(current_user),db:aiosqlite.Connection=Depends(get_db)):
    async with db.execute("SELECT * FROM activities WHERE user_id=? ORDER BY timestamp DESC LIMIT ?",(u["id"],limit)) as c:
        return [ActivityLog(**row(x)) for x in await c.fetchall()]

@r.get("/health")
async def health(): return {"status":"healthy","timestamp":datetime.now(timezone.utc).isoformat()}

# ── Frontend catch-all ────────────────────────────────────
@app.get("/{full_path:path}", include_in_schema=False)
async def frontend(full_path: str):
    return HTMLResponse(HTML)

app.include_router(r)

# ── Startup ───────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    await init_db()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logging.getLogger(__name__).info(f"DB: {DB_PATH}")
