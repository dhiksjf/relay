"""
Relay Drive — single-file edition
FastAPI backend + React SPA frontend embedded as HTML string.
No MongoDB. No Node. No build step. Just Python.
"""

# ─────────────────────────────────────────────────────────
# EMBEDDED FRONTEND (served at every non-/api path)
# ─────────────────────────────────────────────────────────
HTML = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Relay Drive</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        background: 'hsl(240,10%,4%)',
        foreground: 'hsl(0,0%,98%)',
        card: 'hsl(240,10%,7%)',
        border: 'hsl(240,5%,16%)',
        primary: { DEFAULT:'hsl(258,89%,66%)', foreground:'hsl(0,0%,100%)' },
        secondary: { DEFAULT:'hsl(240,5%,14%)', foreground:'hsl(0,0%,98%)' },
        muted: { DEFAULT:'hsl(240,5%,14%)', foreground:'hsl(240,5%,55%)' },
        destructive: { DEFAULT:'hsl(0,63%,47%)', foreground:'hsl(0,0%,98%)' },
        input: 'hsl(240,5%,16%)',
        ring: 'hsl(258,89%,66%)',
      }
    }
  }
};
</script>
<style>
*, *::before, *::after { box-sizing: border-box; }
body { background: hsl(240,10%,4%); color: hsl(0,0%,98%); font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; margin:0; }
:root {
  --bg: hsl(240,10%,4%);
  --card: hsl(240,10%,7%);
  --border: hsl(240,5%,16%);
  --muted: hsl(240,5%,55%);
  --primary: hsl(258,89%,66%);
  --secondary: hsl(240,5%,14%);
  --destructive: hsl(0,63%,47%);
}
.grid-bg {
  background-image: linear-gradient(var(--border) 1px, transparent 1px),
    linear-gradient(90deg, var(--border) 1px, transparent 1px);
  background-size: 40px 40px;
  background-color: var(--bg);
}
.bento-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.bento-card:hover { border-color: rgba(124,58,237,0.3); box-shadow: 0 4px 20px rgba(0,0,0,0.4); }
.nav-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 16px; border-radius: 8px;
  color: var(--muted); text-decoration: none; font-weight: 500;
  transition: background 0.2s, color 0.2s; cursor: pointer;
}
.nav-item:hover { background: var(--secondary); color: hsl(0,0%,98%); }
.nav-item.active { background: var(--secondary); color: hsl(0,0%,98%); }
.file-row {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 16px; border-bottom: 1px solid rgba(255,255,255,0.06);
  cursor: pointer; transition: background 0.15s;
}
.file-row:hover { background: rgba(255,255,255,0.04); }
.badge { display:inline-flex; align-items:center; gap:4px; padding:2px 8px; border-radius:9999px; font-size:11px; font-weight:600; border:1px solid; }
.badge-green { background:rgba(16,185,129,0.15); color:#34d399; border-color:rgba(16,185,129,0.3); }
.badge-red   { background:rgba(239,68,68,0.15);  color:#f87171; border-color:rgba(239,68,68,0.3); }
.badge-amber { background:rgba(245,158,11,0.15); color:#fbbf24; border-color:rgba(245,158,11,0.3); }
.badge-blue  { background:rgba(99,102,241,0.15); color:#a5b4fc; border-color:rgba(99,102,241,0.3); }
.badge-purple{ background:rgba(124,58,237,0.15); color:#c4b5fd; border-color:rgba(124,58,237,0.3); }
.code-block  { background:var(--secondary); border:1px solid var(--border); border-radius:8px; padding:16px; font-family:monospace; font-size:12px; overflow-x:auto; white-space:pre; }
.proto-sftp  { background:rgba(16,185,129,0.15); color:#34d399; border:1px solid rgba(16,185,129,0.3); padding:1px 8px; border-radius:4px; font-size:11px; font-family:monospace; text-transform:uppercase; }
.proto-ftp   { background:rgba(245,158,11,0.15);  color:#fbbf24; border:1px solid rgba(245,158,11,0.3); padding:1px 8px; border-radius:4px; font-size:11px; font-family:monospace; text-transform:uppercase; }
/* Inputs */
input, textarea, select {
  background: var(--secondary); border: 1px solid var(--border); color: hsl(0,0%,98%);
  border-radius: 8px; padding: 8px 12px; width: 100%; font-size: 14px; outline: none;
}
input:focus, textarea:focus, select:focus { border-color: var(--primary); box-shadow: 0 0 0 2px rgba(124,58,237,0.2); }
label { font-size:13px; font-weight:500; color:var(--muted); margin-bottom:4px; display:block; }
/* Buttons */
.btn { display:inline-flex; align-items:center; gap:8px; padding:8px 16px; border-radius:8px; font-size:14px; font-weight:500; cursor:pointer; border:none; transition:opacity 0.2s,background 0.2s; }
.btn:disabled { opacity:0.5; cursor:not-allowed; }
.btn-primary   { background:var(--primary); color:#fff; }
.btn-primary:hover:not(:disabled)   { opacity:0.9; }
.btn-secondary { background:var(--secondary); color:hsl(0,0%,98%); border:1px solid var(--border); }
.btn-secondary:hover:not(:disabled) { background:hsl(240,5%,20%); }
.btn-ghost     { background:transparent; color:var(--muted); }
.btn-ghost:hover:not(:disabled)     { background:var(--secondary); color:hsl(0,0%,98%); }
.btn-danger    { background:rgba(239,68,68,0.15); color:#f87171; border:1px solid rgba(239,68,68,0.3); }
.btn-danger:hover:not(:disabled)    { background:rgba(239,68,68,0.25); }
.btn-sm  { padding:5px 10px; font-size:12px; }
.btn-icon{ padding:6px; border-radius:8px; }
/* Modal */
.modal-bg    { position:fixed; inset:0; background:rgba(0,0,0,0.7); z-index:100; display:flex; align-items:center; justify-content:center; padding:16px; }
.modal-box   { background:var(--card); border:1px solid var(--border); border-radius:16px; padding:24px; width:100%; max-width:480px; max-height:90vh; overflow-y:auto; }
.modal-title { font-size:18px; font-weight:700; margin-bottom:4px; }
.modal-desc  { font-size:13px; color:var(--muted); margin-bottom:20px; }
/* Toast */
#toast-root { position:fixed; top:16px; right:16px; z-index:999; display:flex; flex-direction:column; gap:8px; }
.toast { background:var(--card); border:1px solid var(--border); border-radius:10px; padding:12px 16px; font-size:13px; font-weight:500; display:flex; align-items:center; gap:8px; min-width:240px; box-shadow:0 8px 24px rgba(0,0,0,0.4); animation:slideIn 0.2s ease; }
@keyframes slideIn { from{transform:translateX(100%);opacity:0} to{transform:translateX(0);opacity:1} }
.toast.success { border-color:rgba(16,185,129,0.4); }
.toast.error   { border-color:rgba(239,68,68,0.4); }
/* Spinner */
.spin { animation: spin 0.8s linear infinite; display:inline-block; }
@keyframes spin { to { transform: rotate(360deg); } }
/* Scrollbar */
::-webkit-scrollbar { width:6px; height:6px; }
::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:var(--border); border-radius:3px; }
</style>
</head>
<body>
<div id="toast-root"></div>
<div id="root"></div>

<script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script type="text/babel" data-presets="react">
const { useState, useEffect, useCallback, useRef, createContext, useContext } = React;

// ─── Toast ───────────────────────────────────────────────
const toast = {
  _id: 0,
  show(msg, type = 'success') {
    const el = document.createElement('div');
    el.className = `toast ${type}`;
    el.innerHTML = `<span>${type === 'success' ? '✓' : '✕'}</span><span>${msg}</span>`;
    document.getElementById('toast-root').appendChild(el);
    setTimeout(() => el.remove(), 3500);
  },
  success(m) { this.show(m,'success'); },
  error(m)   { this.show(m,'error'); }
};

// ─── Router ───────────────────────────────────────────────
const RouterCtx = createContext();
function Router({ children }) {
  const [path, setPath] = useState(window.location.pathname);
  useEffect(() => {
    const onPop = () => setPath(window.location.pathname);
    window.addEventListener('popstate', onPop);
    return () => window.removeEventListener('popstate', onPop);
  }, []);
  const navigate = useCallback((to) => {
    window.history.pushState({}, '', to);
    setPath(to);
  }, []);
  return <RouterCtx.Provider value={{ path, navigate }}>{children}</RouterCtx.Provider>;
}
function useRouter() { return useContext(RouterCtx); }
function Link({ to, children, className, onClick, style }) {
  const { navigate } = useRouter();
  return (
    <a href={to} className={className} style={style}
       onClick={e => { e.preventDefault(); if(onClick) onClick(); navigate(to); }}>
      {children}
    </a>
  );
}
function Route({ path: p, exact, children }) {
  const { path } = useRouter();
  const match = exact ? path === p : path.startsWith(p);
  return match ? children : null;
}

// ─── API ──────────────────────────────────────────────────
const API = '/api';
async function apiFetch(method, url, body, isFile) {
  const token = localStorage.getItem('token');
  const headers = {};
  if (token) headers['Authorization'] = `Bearer ${token}`;
  if (body && !isFile) headers['Content-Type'] = 'application/json';

  const opts = { method, headers };
  if (body) opts.body = isFile ? body : JSON.stringify(body);

  const res = await fetch(API + url, opts);
  if (res.status === 401) {
    localStorage.removeItem('token');
    window.history.pushState({}, '', '/login');
    window.dispatchEvent(new PopStateEvent('popstate'));
    throw new Error('Unauthorized');
  }
  const data = res.headers.get('content-type')?.includes('application/json')
    ? await res.json() : await res.blob();
  if (!res.ok) throw new Error(data?.detail || `Error ${res.status}`);
  return data;
}
const api = {
  get:    (u)    => apiFetch('GET', u),
  post:   (u,b)  => apiFetch('POST', u, b),
  put:    (u,b)  => apiFetch('PUT', u, b),
  delete: (u)    => apiFetch('DELETE', u),
  postFile:(u,b) => apiFetch('POST', u, b, true),
};

// ─── Auth Context ─────────────────────────────────────────
const AuthCtx = createContext();
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const { navigate } = useRouter();
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) { setLoading(false); return; }
    api.get('/auth/me').then(u => setUser(u)).catch(() => localStorage.removeItem('token')).finally(() => setLoading(false));
  }, []);
  const login = async (email, password) => {
    const data = await api.post('/auth/login', { email, password });
    localStorage.setItem('token', data.access_token);
    setUser(data.user); return data.user;
  };
  const register = async (name, email, password) => {
    const data = await api.post('/auth/register', { name, email, password });
    localStorage.setItem('token', data.access_token);
    setUser(data.user); return data.user;
  };
  const logout = () => {
    localStorage.removeItem('token'); setUser(null); navigate('/login');
  };
  return <AuthCtx.Provider value={{ user, loading, login, register, logout }}>{children}</AuthCtx.Provider>;
}
function useAuth() { return useContext(AuthCtx); }

// ─── Icons ────────────────────────────────────────────────
const Ico = ({ d, size=18, color='currentColor' }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    {d.map((p,i) => <path key={i} d={p}/>)}
  </svg>
);
const Icons = {
  Dashboard:  () => <Ico d={["M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z","M9 22V12h6v10"]}/>,
  Server:     () => <Ico d={["M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"]}/>,
  Folder:     () => <Ico d={["M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"]}/>,
  Key:        () => <Ico d={["m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4","m21 2-9.6 9.6","m3.5 17.5 3 3L13 15l-3-3-6.5 6.5"]}/>,
  FileText:   () => <Ico d={["M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z","M14 2v6h6","M16 13H8","M16 17H8","M10 9H8"]}/>,
  Settings:   () => <Ico d={["M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z","M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z"]}/>,
  LogOut:     () => <Ico d={["M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4","M16 17l5-5-5-5","M21 12H9"]}/>,
  Zap:        () => <Ico d={["M13 2 3 14h9l-1 8 10-12h-9l1-8z"]}/>,
  Plus:       () => <Ico d={["M12 5v14","M5 12h14"]}/>,
  Trash:      () => <Ico d={["M3 6h18","M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6","M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"]}/>,
  Edit:       () => <Ico d={["M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7","M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"]}/>,
  Copy:       () => <Ico d={["M20 9h-9a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2z","M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 0 2 2v1"]}/>,
  Check:      () => <Ico d={["M20 6 9 17l-5-5"]}/>,
  X:          () => <Ico d={["M18 6 6 18","M6 6l12 12"]}/>,
  ChevronRight:()=> <Ico d={["M9 18l6-6-6-6"]}/>,
  ChevronUp:  () => <Ico d={["M18 15l-6-6-6 6"]}/>,
  Home:       () => <Ico d={["M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z","M9 22V12h6v10"]}/>,
  FolderPlus: () => <Ico d={["M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z","M12 11v6","M9 14h6"]}/>,
  Upload:     () => <Ico d={["M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4","M17 8l-5-5-5 5","M12 3v12"]}/>,
  Download:   () => <Ico d={["M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4","M7 10l5 5 5-5","M12 15V3"]}/>,
  RefreshCw:  () => <Ico d={["M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8","M21 3v5h-5","M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16","M8 16H3v5"]}/>,
  Activity:   () => <Ico d={["M22 12h-4l-3 9L9 3l-3 9H2"]}/>,
  ArrowRight: () => <Ico d={["M5 12h14","M12 5l7 7-7 7"]}/>,
  Eye:        () => <Ico d={["M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z","M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"]}/>,
  EyeOff:     () => <Ico d={["M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94","M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19","M1 1l22 22"]}/>,
  Shield:     () => <Ico d={["M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"]}/>,
  Clock:      () => <Ico d={["M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20z","M12 6v6l4 2"]}/>,
  Alert:      () => <Ico d={["M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z","M12 9v4","M12 17h.01"]}/>,
  File:       () => <Ico d={["M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z","M13 2v7h7"]}/>,
  MoreVert:   () => <Ico d={["M12 5a1 1 0 1 0 0-2 1 1 0 0 0 0 2z","M12 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2z","M12 21a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"]}/>,
  Code:       () => <Ico d={["M16 18l6-6-6-6","M8 6l-6 6 6 6"]}/>,
  User:       () => <Ico d={["M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2","M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"]}/>,
  Zap2:       () => <Ico d={["M13 2 3 14h9l-1 8 10-12h-9l1-8z"]}/>,
};

// ─── Helpers ──────────────────────────────────────────────
function formatBytes(b) {
  if (!b && b !== 0) return '-';
  if (b === 0) return '0 B';
  const i = Math.floor(Math.log(b) / Math.log(1024));
  return (b / Math.pow(1024, i)).toFixed(1) + ' ' + ['B','KB','MB','GB'][i];
}
function formatDate(s) {
  if (!s) return '-';
  return new Date(s).toLocaleDateString('en-US', { year:'numeric', month:'short', day:'numeric', hour:'2-digit', minute:'2-digit' });
}
function relTime(s) {
  if (!s) return '-';
  const d = (Date.now() - new Date(s)) / 1000;
  if (d < 60) return 'Just now';
  if (d < 3600) return `${Math.floor(d/60)}m ago`;
  if (d < 86400) return `${Math.floor(d/3600)}h ago`;
  if (d < 604800) return `${Math.floor(d/86400)}d ago`;
  return formatDate(s);
}
function fileIcon(type, name) {
  if (type === 'directory') return '📁';
  const ext = name?.split('.').pop()?.toLowerCase();
  const m = { png:'🖼️',jpg:'🖼️',jpeg:'🖼️',gif:'🖼️',svg:'🖼️',webp:'🖼️',
              pdf:'📄',doc:'📄',docx:'📄',txt:'📄',md:'📄',
              js:'💻',ts:'💻',jsx:'💻',tsx:'💻',py:'💻',html:'💻',css:'💻',json:'💻',
              zip:'📦',tar:'📦',gz:'📦',rar:'📦',
              mp3:'🎵',wav:'🎵',mp4:'🎬',avi:'🎬',mov:'🎬' };
  return m[ext] || '📄';
}
function parentPath(p) {
  if (!p || p === '/') return '/';
  const parts = p.split('/').filter(Boolean); parts.pop();
  return '/' + parts.join('/');
}
function joinPath(...parts) {
  return '/' + parts.map(p => p.replace(/^\/|\/$/g,'')).filter(Boolean).join('/');
}
function Spinner({ size = 16 }) {
  return <svg className="spin" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10" strokeOpacity="0.2"/><path d="M12 2a10 10 0 0 1 10 10" strokeLinecap="round"/></svg>;
}

// ─── Layout ───────────────────────────────────────────────
const NAV = [
  { path:'/',            label:'Dashboard',   icon:'Dashboard' },
  { path:'/connections', label:'Connections', icon:'Server' },
  { path:'/browser',     label:'File Browser',icon:'Folder' },
  { path:'/api-keys',    label:'API Keys',    icon:'Key' },
  { path:'/docs',        label:'API Docs',    icon:'FileText' },
  { path:'/settings',    label:'Settings',    icon:'Settings' },
];
function Layout({ children }) {
  const { user, logout } = useAuth();
  const { path, navigate } = useRouter();
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <div style={{ minHeight:'100vh', background:'var(--bg)' }} className="grid-bg">
      {/* Desktop sidebar */}
      <aside style={{ position:'fixed', top:0, left:0, width:256, height:'100vh', background:'var(--card)', borderRight:'1px solid var(--border)', display:'flex', flexDirection:'column', padding:'24px 16px', zIndex:40 }} className="hidden lg:flex">
        <div style={{ display:'flex', alignItems:'center', gap:12, marginBottom:32 }}>
          <div style={{ width:40, height:40, borderRadius:12, background:'var(--primary)', display:'flex', alignItems:'center', justifyContent:'center' }}>
            <Icons.Zap/>
          </div>
          <div>
            <div style={{ fontWeight:700, fontSize:17 }}>Relay Drive</div>
            <div style={{ fontSize:11, color:'var(--muted)' }}>FTP/SFTP Gateway</div>
          </div>
        </div>
        <nav style={{ flex:1, display:'flex', flexDirection:'column', gap:4 }}>
          {NAV.map(n => {
            const Icon = Icons[n.icon];
            const active = n.path === '/' ? path === '/' : path.startsWith(n.path);
            return (
              <div key={n.path} className={`nav-item${active?' active':''}`} onClick={() => navigate(n.path)}>
                <Icon/> <span>{n.label}</span>
              </div>
            );
          })}
        </nav>
        <div style={{ borderTop:'1px solid var(--border)', paddingTop:16 }}>
          <div style={{ display:'flex', alignItems:'center', gap:10, padding:'8px 8px 12px' }}>
            <div style={{ width:34, height:34, borderRadius:'50%', background:'var(--secondary)', display:'flex', alignItems:'center', justifyContent:'center', fontWeight:700, fontSize:14 }}>
              {user?.name?.charAt(0).toUpperCase()}
            </div>
            <div style={{ flex:1, minWidth:0 }}>
              <div style={{ fontSize:13, fontWeight:500, overflow:'hidden', textOverflow:'ellipsis', whiteSpace:'nowrap' }}>{user?.name}</div>
              <div style={{ fontSize:11, color:'var(--muted)', overflow:'hidden', textOverflow:'ellipsis', whiteSpace:'nowrap' }}>{user?.email}</div>
            </div>
          </div>
          <div className="nav-item" onClick={logout} style={{ color:'var(--muted)' }}>
            <Icons.LogOut/> <span>Sign Out</span>
          </div>
        </div>
      </aside>

      {/* Mobile top bar */}
      <div style={{ position:'sticky', top:0, zIndex:30, background:'var(--card)', borderBottom:'1px solid var(--border)', padding:'12px 16px', display:'flex', alignItems:'center', justifyContent:'space-between' }} className="lg:hidden">
        <div style={{ display:'flex', alignItems:'center', gap:10 }}>
          <div style={{ width:32, height:32, borderRadius:8, background:'var(--primary)', display:'flex', alignItems:'center', justifyContent:'center' }}>
            <Icons.Zap/>
          </div>
          <span style={{ fontWeight:700 }}>Relay Drive</span>
        </div>
        <button className="btn btn-ghost btn-icon" onClick={() => setMobileOpen(!mobileOpen)}>
          {mobileOpen ? <Icons.X/> : <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg>}
        </button>
      </div>

      {/* Mobile menu */}
      {mobileOpen && (
        <div style={{ position:'fixed', inset:0, background:'rgba(0,0,0,0.8)', zIndex:50 }} onClick={() => setMobileOpen(false)}>
          <div style={{ position:'absolute', top:0, right:0, width:260, height:'100%', background:'var(--card)', padding:'24px 16px' }} onClick={e => e.stopPropagation()}>
            <nav style={{ display:'flex', flexDirection:'column', gap:4, marginTop:16 }}>
              {NAV.map(n => {
                const Icon = Icons[n.icon];
                const active = n.path === '/' ? path === '/' : path.startsWith(n.path);
                return (
                  <div key={n.path} className={`nav-item${active?' active':''}`} onClick={() => { navigate(n.path); setMobileOpen(false); }}>
                    <Icon/> <span>{n.label}</span>
                  </div>
                );
              })}
            </nav>
            <div style={{ marginTop:24, borderTop:'1px solid var(--border)', paddingTop:16 }}>
              <div className="nav-item" onClick={() => { logout(); setMobileOpen(false); }}>
                <Icons.LogOut/> <span>Sign Out</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Main */}
      <main style={{ marginLeft:0, paddingBottom:32 }} className="lg:ml-64">
        <div style={{ maxWidth:1100, margin:'0 auto', padding:'24px 16px' }}>
          {children}
        </div>
      </main>
    </div>
  );
}

// ─── Page: Login ──────────────────────────────────────────
function Login() {
  const { login } = useAuth();
  const { navigate } = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const submit = async e => {
    e.preventDefault(); setLoading(true);
    try { await login(email, password); toast.success('Welcome back!'); navigate('/'); }
    catch(err) { toast.error(err.message || 'Login failed'); }
    finally { setLoading(false); }
  };
  return (
    <div style={{ minHeight:'100vh', display:'flex', alignItems:'center', justifyContent:'center', padding:16 }} className="grid-bg">
      <div style={{ width:'100%', maxWidth:420 }}>
        <div style={{ display:'flex', alignItems:'center', gap:12, marginBottom:32, justifyContent:'center' }}>
          <div style={{ width:44, height:44, borderRadius:12, background:'var(--primary)', display:'flex', alignItems:'center', justifyContent:'center' }}>
            <Icons.Zap/>
          </div>
          <div>
            <div style={{ fontWeight:800, fontSize:22 }}>Relay Drive</div>
            <div style={{ fontSize:12, color:'var(--muted)' }}>FTP/SFTP Gateway</div>
          </div>
        </div>
        <div className="bento-card" style={{ padding:28 }}>
          <h2 style={{ fontSize:22, fontWeight:700, marginBottom:4 }}>Sign in</h2>
          <p style={{ color:'var(--muted)', fontSize:13, marginBottom:20 }}>Enter your credentials to continue</p>
          <form onSubmit={submit}>
            <div style={{ marginBottom:14 }}>
              <label>Email</label>
              <input type="email" placeholder="you@example.com" value={email} onChange={e=>setEmail(e.target.value)} required/>
            </div>
            <div style={{ marginBottom:20 }}>
              <label>Password</label>
              <input type="password" placeholder="••••••••" value={password} onChange={e=>setPassword(e.target.value)} required/>
            </div>
            <button className="btn btn-primary" style={{ width:'100%', justifyContent:'center' }} disabled={loading}>
              {loading ? <Spinner/> : <Icons.ArrowRight/>} Sign in
            </button>
          </form>
          <p style={{ textAlign:'center', marginTop:16, fontSize:13, color:'var(--muted)' }}>
            No account? <Link to="/register" style={{ color:'var(--primary)', fontWeight:600 }}>Create one</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

// ─── Page: Register ───────────────────────────────────────
function Register() {
  const { register } = useAuth();
  const { navigate } = useRouter();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const submit = async e => {
    e.preventDefault();
    if (password.length < 6) { toast.error('Password must be at least 6 characters'); return; }
    setLoading(true);
    try { await register(name, email, password); toast.success('Account created!'); navigate('/'); }
    catch(err) { toast.error(err.message || 'Registration failed'); }
    finally { setLoading(false); }
  };
  return (
    <div style={{ minHeight:'100vh', display:'flex', alignItems:'center', justifyContent:'center', padding:16 }} className="grid-bg">
      <div style={{ width:'100%', maxWidth:420 }}>
        <div style={{ display:'flex', alignItems:'center', gap:12, marginBottom:32, justifyContent:'center' }}>
          <div style={{ width:44, height:44, borderRadius:12, background:'var(--primary)', display:'flex', alignItems:'center', justifyContent:'center' }}>
            <Icons.Zap/>
          </div>
          <div>
            <div style={{ fontWeight:800, fontSize:22 }}>Relay Drive</div>
            <div style={{ fontSize:12, color:'var(--muted)' }}>FTP/SFTP Gateway</div>
          </div>
        </div>
        <div className="bento-card" style={{ padding:28 }}>
          <h2 style={{ fontSize:22, fontWeight:700, marginBottom:4 }}>Create account</h2>
          <p style={{ color:'var(--muted)', fontSize:13, marginBottom:20 }}>Enter your details to get started</p>
          <form onSubmit={submit}>
            <div style={{ marginBottom:14 }}>
              <label>Name</label>
              <input type="text" placeholder="Your name" value={name} onChange={e=>setName(e.target.value)} required/>
            </div>
            <div style={{ marginBottom:14 }}>
              <label>Email</label>
              <input type="email" placeholder="you@example.com" value={email} onChange={e=>setEmail(e.target.value)} required/>
            </div>
            <div style={{ marginBottom:20 }}>
              <label>Password</label>
              <input type="password" placeholder="At least 6 characters" value={password} onChange={e=>setPassword(e.target.value)} required/>
            </div>
            <button className="btn btn-primary" style={{ width:'100%', justifyContent:'center' }} disabled={loading}>
              {loading ? <Spinner/> : <Icons.ArrowRight/>} Create account
            </button>
          </form>
          <p style={{ textAlign:'center', marginTop:16, fontSize:13, color:'var(--muted)' }}>
            Already have an account? <Link to="/login" style={{ color:'var(--primary)', fontWeight:600 }}>Sign in</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

// ─── Page: Dashboard ─────────────────────────────────────
function Dashboard() {
  const [stats, setStats] = useState(null);
  const { navigate } = useRouter();
  useEffect(() => {
    api.get('/dashboard/stats').then(setStats).catch(() => toast.error('Failed to load stats'));
  }, []);
  const actionLabel = a => ({
    list_directory:'Listed directory', upload_file:'Uploaded file', download_file:'Downloaded file',
    delete_file:'Deleted file', delete_directory:'Deleted directory', create_directory:'Created directory',
    rename_file:'Renamed file', test_connection:'Tested connection', create_connection:'Created connection',
    update_connection:'Updated connection', delete_connection:'Deleted connection',
    create_api_key:'Created API key', revoke_api_key:'Revoked API key',
  }[a] || a);

  return (
    <Layout>
      <div style={{ display:'flex', flexDirection:'column', gap:24 }}>
        <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', flexWrap:'wrap', gap:12 }}>
          <div>
            <h1 style={{ fontSize:26, fontWeight:700, margin:0 }}>Dashboard</h1>
            <p style={{ color:'var(--muted)', fontSize:13, marginTop:4 }}>Overview of your FTP/SFTP relay service</p>
          </div>
          <button className="btn btn-primary" onClick={() => navigate('/connections')}>
            <Icons.Plus/> Add Connection
          </button>
        </div>

        {/* Stats */}
        <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(200px,1fr))', gap:16 }}>
          {[
            { label:'Server Connections', val:stats?.total_connections??'—', sub:'FTP & SFTP servers', link:'/connections', Icon:Icons.Server },
            { label:'Active API Keys', val:`${stats?.active_api_keys??'—'} / ${stats?.total_api_keys??'—'}`, sub:'Keys for API access', link:'/api-keys', Icon:Icons.Key },
            { label:'Operations Today', val:stats?.operations_today??'—', sub:'File operations', link:'/browser', Icon:Icons.Activity },
          ].map(({ label, val, sub, link, Icon }) => (
            <div key={label} className="bento-card">
              <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', marginBottom:10 }}>
                <span style={{ fontSize:12, color:'var(--muted)', fontWeight:500 }}>{label}</span>
                <Icon/>
              </div>
              <div style={{ fontSize:30, fontWeight:700, marginBottom:4 }}>{val}</div>
              <div style={{ fontSize:11, color:'var(--muted)' }}>{sub}</div>
              <div onClick={() => navigate(link)} style={{ marginTop:12, fontSize:12, color:'var(--primary)', cursor:'pointer', display:'flex', alignItems:'center', gap:4 }}>
                Manage <Icons.ArrowRight/>
              </div>
            </div>
          ))}
        </div>

        {/* Recent Activity */}
        <div className="bento-card">
          <div style={{ display:'flex', alignItems:'center', gap:8, marginBottom:16, fontSize:15, fontWeight:600 }}>
            <Icons.Activity/> Recent Activity
          </div>
          {stats?.recent_activities?.length > 0 ? (
            stats.recent_activities.map((a, i) => (
              <div key={a.id} style={{ display:'flex', alignItems:'center', gap:12, padding:'10px 8px', borderRadius:8, transition:'background 0.15s' }}
                   onMouseEnter={e=>e.currentTarget.style.background='rgba(255,255,255,0.03)'}
                   onMouseLeave={e=>e.currentTarget.style.background=''}>
                <div style={{ width:32, height:32, borderRadius:8, display:'flex', alignItems:'center', justifyContent:'center', background: a.status==='success'?'rgba(16,185,129,0.15)':'rgba(239,68,68,0.15)', color:a.status==='success'?'#34d399':'#f87171', flexShrink:0 }}>
                  <Icons.Activity/>
                </div>
                <div style={{ flex:1, minWidth:0 }}>
                  <div style={{ fontSize:13, fontWeight:500 }}>
                    {actionLabel(a.action)}{a.connection_name && <span style={{ color:'var(--muted)' }}> on {a.connection_name}</span>}
                  </div>
                  {a.path && <div style={{ fontSize:11, color:'var(--muted)', fontFamily:'monospace', overflow:'hidden', textOverflow:'ellipsis', whiteSpace:'nowrap' }}>{a.path}</div>}
                </div>
                <div style={{ display:'flex', alignItems:'center', gap:8, flexShrink:0 }}>
                  <span className={`badge ${a.status==='success'?'badge-green':'badge-red'}`}>
                    {a.status==='success'?'✓':'✕'} {a.status}
                  </span>
                  <span style={{ fontSize:11, color:'var(--muted)' }}>{relTime(a.timestamp)}</span>
                </div>
              </div>
            ))
          ) : (
            <div style={{ textAlign:'center', padding:'40px 0', color:'var(--muted)' }}>
              <div style={{ fontSize:36, marginBottom:8 }}>📋</div>
              <p style={{ margin:0 }}>No recent activity</p>
              <p style={{ fontSize:12, marginTop:4 }}>Start by adding a connection and browsing files</p>
            </div>
          )}
        </div>
      </div>
    </Layout>
  );
}

// ─── Page: Connections ────────────────────────────────────
function Connections() {
  const [conns, setConns] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState(null); // null | 'new' | connection object
  const [testing, setTesting] = useState(null);
  const [saving, setSaving] = useState(false);
  const [form, setForm] = useState({ name:'', protocol:'sftp', host:'', port:22, username:'', password:'', private_key:'' });

  const load = () => api.get('/connections').then(setConns).catch(()=>toast.error('Failed to load')).finally(()=>setLoading(false));
  useEffect(()=>{ load(); }, []);

  const openNew = () => { setForm({ name:'', protocol:'sftp', host:'', port:22, username:'', password:'', private_key:'' }); setModal('new'); };
  const openEdit = c => { setForm({ name:c.name, protocol:c.protocol, host:c.host, port:c.port, username:c.username, password:'', private_key:'' }); setModal(c); };

  const save = async e => {
    e.preventDefault(); setSaving(true);
    const data = { ...form }; if(!data.password) delete data.password; if(!data.private_key) delete data.private_key;
    try {
      if (modal === 'new') { await api.post('/connections', data); toast.success('Connection created'); }
      else { await api.put(`/connections/${modal.id}`, data); toast.success('Connection updated'); }
      setModal(null); load();
    } catch(err) { toast.error(err.message); }
    finally { setSaving(false); }
  };

  const del = async id => {
    if (!confirm('Delete this connection?')) return;
    try { await api.delete(`/connections/${id}`); toast.success('Deleted'); load(); }
    catch(err) { toast.error(err.message); }
  };

  const test = async id => {
    setTesting(id);
    try { await api.post(`/connections/${id}/test`); toast.success('Connection successful!'); }
    catch(err) { toast.error(err.message || 'Connection failed'); }
    finally { setTesting(null); }
  };

  const F = (k, v) => setForm(f => ({ ...f, [k]: v }));

  return (
    <Layout>
      <div style={{ display:'flex', flexDirection:'column', gap:24 }}>
        <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', flexWrap:'wrap', gap:12 }}>
          <div>
            <h1 style={{ fontSize:26, fontWeight:700, margin:0 }}>Connections</h1>
            <p style={{ color:'var(--muted)', fontSize:13, marginTop:4 }}>Manage your FTP and SFTP server connections</p>
          </div>
          <button className="btn btn-primary" onClick={openNew}><Icons.Plus/> New Connection</button>
        </div>

        {loading ? <div style={{ textAlign:'center', padding:40, color:'var(--muted)' }}><Spinner size={28}/></div>
        : conns.length === 0 ? (
          <div className="bento-card" style={{ textAlign:'center', padding:'48px 24px' }}>
            <div style={{ fontSize:48, marginBottom:12 }}>🖥️</div>
            <h3 style={{ fontWeight:600, margin:'0 0 8px' }}>No connections yet</h3>
            <p style={{ color:'var(--muted)', marginBottom:20 }}>Add your first FTP or SFTP server</p>
            <button className="btn btn-primary" onClick={openNew}><Icons.Plus/> Add Connection</button>
          </div>
        ) : (
          conns.map(c => (
            <div key={c.id} className="bento-card" style={{ padding:'20px 24px' }}>
              <div style={{ display:'flex', alignItems:'flex-start', justifyContent:'space-between', gap:12, flexWrap:'wrap' }}>
                <div style={{ display:'flex', alignItems:'flex-start', gap:14 }}>
                  <div style={{ width:44, height:44, borderRadius:12, background:'var(--secondary)', display:'flex', alignItems:'center', justifyContent:'center', flexShrink:0 }}>
                    <Icons.Server/>
                  </div>
                  <div>
                    <div style={{ display:'flex', alignItems:'center', gap:8, flexWrap:'wrap', marginBottom:4 }}>
                      <span style={{ fontSize:16, fontWeight:600 }}>{c.name}</span>
                      <span className={`proto-${c.protocol}`}>{c.protocol}</span>
                    </div>
                    <div style={{ fontSize:13, color:'var(--muted)', fontFamily:'monospace', marginBottom:8 }}>
                      {c.username}@{c.host}:{c.port}
                    </div>
                    <div style={{ display:'flex', alignItems:'center', gap:8, flexWrap:'wrap' }}>
                      <code style={{ fontSize:11, background:'var(--secondary)', padding:'2px 8px', borderRadius:4, color:'var(--muted)' }}>ID: {c.id}</code>
                      <button className="btn btn-ghost btn-icon" style={{ padding:'2px 4px' }} onClick={() => { navigator.clipboard.writeText(c.id); toast.success('ID copied!'); }}>
                        <Icons.Copy/>
                      </button>
                      {c.has_password && <span className="badge badge-blue">Password Auth</span>}
                      {c.has_private_key && <span className="badge badge-purple">Key Auth</span>}
                      {c.last_used && <span style={{ fontSize:11, color:'var(--muted)' }}>Last used {relTime(c.last_used)}</span>}
                    </div>
                  </div>
                </div>
                <div style={{ display:'flex', gap:8, flexShrink:0 }}>
                  <button className="btn btn-secondary btn-sm" onClick={() => test(c.id)} disabled={testing===c.id}>
                    {testing===c.id ? <Spinner/> : '⚡'} Test
                  </button>
                  <button className="btn btn-secondary btn-sm" onClick={() => openEdit(c)}><Icons.Edit/></button>
                  <button className="btn btn-danger btn-sm" onClick={() => del(c.id)}><Icons.Trash/></button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      {modal && (
        <div className="modal-bg" onClick={()=>setModal(null)}>
          <div className="modal-box" onClick={e=>e.stopPropagation()}>
            <div className="modal-title">{modal==='new' ? 'New Connection' : 'Edit Connection'}</div>
            <div className="modal-desc">{modal==='new' ? 'Enter FTP or SFTP server details' : 'Update the connection details'}</div>
            <form onSubmit={save}>
              <div style={{ marginBottom:12 }}>
                <label>Connection Name</label>
                <input placeholder="My Server" value={form.name} onChange={e=>F('name',e.target.value)} required/>
              </div>
              <div style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap:12, marginBottom:12 }}>
                <div>
                  <label>Protocol</label>
                  <select value={form.protocol} onChange={e=>{ F('protocol',e.target.value); F('port',e.target.value==='sftp'?22:21); }}>
                    <option value="sftp">SFTP</option>
                    <option value="ftp">FTP</option>
                  </select>
                </div>
                <div>
                  <label>Port</label>
                  <input type="number" value={form.port} onChange={e=>F('port',parseInt(e.target.value))} required/>
                </div>
              </div>
              <div style={{ marginBottom:12 }}>
                <label>Host</label>
                <input placeholder="ftp.example.com" value={form.host} onChange={e=>F('host',e.target.value)} required/>
              </div>
              <div style={{ marginBottom:12 }}>
                <label>Username</label>
                <input placeholder="user" value={form.username} onChange={e=>F('username',e.target.value)} required/>
              </div>
              <div style={{ marginBottom:12 }}>
                <label>Password {modal!=='new' && <span style={{ color:'var(--muted)', fontSize:11 }}>(leave empty to keep current)</span>}</label>
                <input type="password" placeholder="••••••••" value={form.password} onChange={e=>F('password',e.target.value)}/>
              </div>
              {form.protocol === 'sftp' && (
                <div style={{ marginBottom:12 }}>
                  <label>Private Key <span style={{ color:'var(--muted)', fontSize:11 }}>(optional, PEM format)</span></label>
                  <textarea rows="3" placeholder="-----BEGIN RSA PRIVATE KEY-----" value={form.private_key} onChange={e=>F('private_key',e.target.value)} style={{ fontFamily:'monospace', fontSize:11 }}/>
                </div>
              )}
              <div style={{ display:'flex', gap:8, justifyContent:'flex-end', marginTop:20 }}>
                <button type="button" className="btn btn-secondary" onClick={()=>setModal(null)}>Cancel</button>
                <button type="submit" className="btn btn-primary" disabled={saving}>{saving?<Spinner/>:null} {modal==='new'?'Create':'Update'}</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </Layout>
  );
}

// ─── Page: File Browser ───────────────────────────────────
function FileBrowser() {
  const [conns, setConns] = useState([]);
  const [selConn, setSelConn] = useState(null);
  const [path, setPath] = useState('/');
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [browsing, setBrowsing] = useState(false);
  const [renameModal, setRenameModal] = useState(null);
  const [mkdirModal, setMkdirModal] = useState(false);
  const [newName, setNewName] = useState('');
  const [newDir, setNewDir] = useState('');
  const [saving, setSaving] = useState(false);
  const fileRef = useRef();

  useEffect(() => {
    api.get('/connections').then(cs => { setConns(cs); if(cs.length>0){setSelConn(cs[0]);} }).finally(()=>setLoading(false));
  }, []);

  const browse = useCallback(async (connId, p) => {
    setBrowsing(true);
    try { const r = await api.get(`/files/${connId}/list?path=${encodeURIComponent(p)}`); setFiles(r.items); setPath(r.path); }
    catch(err) { toast.error(err.message || 'Failed to list'); }
    finally { setBrowsing(false); }
  }, []);

  useEffect(() => { if(selConn) browse(selConn.id, '/'); }, [selConn]);

  const nav = p => selConn && browse(selConn.id, p);

  const download = async item => {
    try {
      const blob = await apiFetch('GET', `/files/${selConn.id}/download?path=${encodeURIComponent(item.path)}`);
      const url = URL.createObjectURL(blob); const a = document.createElement('a');
      a.href=url; a.download=item.name; document.body.appendChild(a); a.click();
      URL.revokeObjectURL(url); a.remove(); toast.success('Download started');
    } catch(err) { toast.error('Failed to download'); }
  };

  const del = async item => {
    if(!confirm(`Delete "${item.name}"?`)) return;
    try {
      if(item.type==='directory') await api.delete(`/files/${selConn.id}/rmdir?path=${encodeURIComponent(item.path)}`);
      else await api.delete(`/files/${selConn.id}/delete?path=${encodeURIComponent(item.path)}`);
      toast.success('Deleted'); browse(selConn.id, path);
    } catch(err) { toast.error(err.message); }
  };

  const rename = async e => {
    e.preventDefault(); if(!renameModal||!newName) return; setSaving(true);
    const newPath = joinPath(parentPath(renameModal.path), newName);
    try {
      await api.post(`/files/${selConn.id}/rename?old_path=${encodeURIComponent(renameModal.path)}&new_path=${encodeURIComponent(newPath)}`);
      toast.success('Renamed'); setRenameModal(null); browse(selConn.id, path);
    } catch(err) { toast.error(err.message); }
    finally { setSaving(false); }
  };

  const mkdir = async e => {
    e.preventDefault(); if(!newDir) return; setSaving(true);
    try {
      await api.post(`/files/${selConn.id}/mkdir?path=${encodeURIComponent(joinPath(path,newDir))}`);
      toast.success('Directory created'); setMkdirModal(false); setNewDir(''); browse(selConn.id, path);
    } catch(err) { toast.error(err.message); }
    finally { setSaving(false); }
  };

  const upload = async e => {
    const file = e.target.files?.[0]; if(!file) return;
    const fd = new FormData(); fd.append('file', file);
    try {
      await api.postFile(`/files/${selConn.id}/upload?path=${encodeURIComponent(path)}`, fd);
      toast.success('Uploaded'); browse(selConn.id, path);
    } catch(err) { toast.error(err.message); }
    if(fileRef.current) fileRef.current.value = '';
  };

  const pathParts = path.split('/').filter(Boolean);

  return (
    <Layout>
      <div style={{ display:'flex', flexDirection:'column', gap:20 }}>
        <div>
          <h1 style={{ fontSize:26, fontWeight:700, margin:0 }}>File Browser</h1>
          <p style={{ color:'var(--muted)', fontSize:13, marginTop:4 }}>Browse and manage files on your remote servers</p>
        </div>

        {loading ? <div style={{ textAlign:'center', padding:40 }}><Spinner size={28}/></div>
        : conns.length===0 ? (
          <div className="bento-card" style={{ textAlign:'center', padding:'48px 24px' }}>
            <div style={{ fontSize:48, marginBottom:12 }}>🖥️</div>
            <h3 style={{ fontWeight:600, margin:'0 0 8px' }}>No connections available</h3>
            <p style={{ color:'var(--muted)', marginBottom:20 }}>Add a connection first</p>
            <Link to="/connections"><button className="btn btn-primary">Add Connection</button></Link>
          </div>
        ) : (
          <>
            {/* Toolbar */}
            <div className="bento-card" style={{ padding:14 }}>
              <div style={{ display:'flex', alignItems:'center', gap:10, flexWrap:'wrap' }}>
                <Icons.Server/>
                <select value={selConn?.id||''} onChange={e=>{const c=conns.find(x=>x.id===e.target.value);setSelConn(c);}} style={{ flex:1, minWidth:160 }}>
                  {conns.map(c=><option key={c.id} value={c.id}>{c.name} ({c.protocol})</option>)}
                </select>
                <button className="btn btn-secondary btn-sm" onClick={()=>browse(selConn.id,path)} disabled={browsing}>
                  {browsing?<Spinner/>:<Icons.RefreshCw/>}
                </button>
                <button className="btn btn-secondary btn-sm" onClick={()=>setMkdirModal(true)}><Icons.FolderPlus/> <span style={{display:'none'}} className="sm:inline">New Folder</span></button>
                <button className="btn btn-primary btn-sm" onClick={()=>fileRef.current?.click()}><Icons.Upload/> <span style={{display:'none'}} className="sm:inline">Upload</span></button>
                <input ref={fileRef} type="file" style={{display:'none'}} onChange={upload}/>
              </div>
            </div>

            {/* Breadcrumb */}
            <div style={{ display:'flex', alignItems:'center', gap:4, fontSize:13, overflowX:'auto', paddingBottom:4 }}>
              <button className="btn btn-ghost btn-sm btn-icon" onClick={()=>nav('/')}><Icons.Home/></button>
              <Icons.ChevronRight/>
              {pathParts.map((p,i)=>(
                <React.Fragment key={i}>
                  <button className="btn btn-ghost btn-sm" onClick={()=>nav('/'+pathParts.slice(0,i+1).join('/'))}>{p}</button>
                  {i<pathParts.length-1&&<Icons.ChevronRight/>}
                </React.Fragment>
              ))}
            </div>

            {/* File list */}
            <div className="bento-card" style={{ padding:0, overflow:'hidden' }}>
              {path!=='/' && (
                <div className="file-row" onClick={()=>nav(parentPath(path))}>
                  <Icons.ChevronUp/> <span style={{ color:'var(--muted)' }}>..</span>
                </div>
              )}
              {browsing ? (
                <div style={{ textAlign:'center', padding:40, color:'var(--muted)' }}><Spinner size={28}/></div>
              ) : files.length===0 ? (
                <div style={{ textAlign:'center', padding:40, color:'var(--muted)' }}>
                  <div style={{ fontSize:36 }}>📂</div><p>Directory is empty</p>
                </div>
              ) : (
                [...files].sort((a,b)=>{
                  if(a.type!==b.type) return a.type==='directory'?-1:1;
                  return a.name.localeCompare(b.name);
                }).map(item => (
                  <div key={item.path} className="file-row" onClick={()=>item.type==='directory'&&nav(item.path)}
                       style={{ cursor: item.type==='directory'?'pointer':'default' }}>
                    <div style={{ width:34, height:34, borderRadius:8, display:'flex', alignItems:'center', justifyContent:'center', fontSize:18, background:item.type==='directory'?'rgba(245,158,11,0.15)':'var(--secondary)', flexShrink:0 }}>
                      {fileIcon(item.type, item.name)}
                    </div>
                    <div style={{ flex:1, minWidth:0 }}>
                      <div style={{ fontSize:13, fontWeight:500 }}>{item.name}</div>
                      <div style={{ fontSize:11, color:'var(--muted)', display:'flex', gap:12, marginTop:2 }}>
                        {item.size!=null && <span>{formatBytes(item.size)}</span>}
                        {item.modified && <span>{relTime(item.modified)}</span>}
                        {item.permissions && <span style={{ fontFamily:'monospace' }}>{item.permissions}</span>}
                      </div>
                    </div>
                    <div style={{ display:'flex', gap:6, opacity:0 }} className="file-actions" onMouseEnter={e=>e.currentTarget.style.opacity=1} onMouseLeave={e=>e.currentTarget.style.opacity=0}>
                      {item.type==='file' && <button className="btn btn-secondary btn-sm btn-icon" onClick={e=>{e.stopPropagation();download(item);}}><Icons.Download/></button>}
                      <button className="btn btn-secondary btn-sm btn-icon" onClick={e=>{e.stopPropagation();setRenameModal(item);setNewName(item.name);}}><Icons.Edit/></button>
                      <button className="btn btn-danger btn-sm btn-icon" onClick={e=>{e.stopPropagation();del(item);}}><Icons.Trash/></button>
                    </div>
                  </div>
                ))
              )}
            </div>
          </>
        )}
      </div>

      {/* Rename modal */}
      {renameModal && (
        <div className="modal-bg" onClick={()=>setRenameModal(null)}>
          <div className="modal-box" onClick={e=>e.stopPropagation()}>
            <div className="modal-title">Rename</div>
            <div className="modal-desc">Enter a new name for "{renameModal.name}"</div>
            <form onSubmit={rename}>
              <div style={{ marginBottom:16 }}><label>New Name</label><input value={newName} onChange={e=>setNewName(e.target.value)} autoFocus/></div>
              <div style={{ display:'flex', gap:8, justifyContent:'flex-end' }}>
                <button type="button" className="btn btn-secondary" onClick={()=>setRenameModal(null)}>Cancel</button>
                <button type="submit" className="btn btn-primary" disabled={saving}>{saving?<Spinner/>:null} Rename</button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Mkdir modal */}
      {mkdirModal && (
        <div className="modal-bg" onClick={()=>setMkdirModal(false)}>
          <div className="modal-box" onClick={e=>e.stopPropagation()}>
            <div className="modal-title">Create Directory</div>
            <div className="modal-desc">Enter a name for the new directory</div>
            <form onSubmit={mkdir}>
              <div style={{ marginBottom:16 }}><label>Directory Name</label><input placeholder="new-folder" value={newDir} onChange={e=>setNewDir(e.target.value)} autoFocus/></div>
              <div style={{ display:'flex', gap:8, justifyContent:'flex-end' }}>
                <button type="button" className="btn btn-secondary" onClick={()=>setMkdirModal(false)}>Cancel</button>
                <button type="submit" className="btn btn-primary" disabled={saving}>{saving?<Spinner/>:null} Create</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </Layout>
  );
}

// ─── Page: API Keys ───────────────────────────────────────
function APIKeys() {
  const [keys, setKeys] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState(false);
  const [newKeyModal, setNewKeyModal] = useState(null);
  const [form, setForm] = useState({ name:'', expires_in_days:'30' });
  const [saving, setSaving] = useState(false);

  const load = () => api.get('/api-keys').then(setKeys).finally(()=>setLoading(false));
  useEffect(()=>{ load(); }, []);

  const create = async e => {
    e.preventDefault(); setSaving(true);
    try {
      const data = await api.post('/api-keys', { name:form.name, expires_in_days:form.expires_in_days==='never'?null:parseInt(form.expires_in_days) });
      setModal(false); setNewKeyModal(data); setForm({ name:'', expires_in_days:'30' }); load();
    } catch(err) { toast.error(err.message); }
    finally { setSaving(false); }
  };

  const revoke = async id => {
    if(!confirm('Revoke this API key? This cannot be undone.')) return;
    try { await api.delete(`/api-keys/${id}`); toast.success('API key revoked'); load(); }
    catch(err) { toast.error(err.message); }
  };

  const isExpired = d => d && new Date(d) < new Date();

  return (
    <Layout>
      <div style={{ display:'flex', flexDirection:'column', gap:24 }}>
        <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', flexWrap:'wrap', gap:12 }}>
          <div>
            <h1 style={{ fontSize:26, fontWeight:700, margin:0 }}>API Keys</h1>
            <p style={{ color:'var(--muted)', fontSize:13, marginTop:4 }}>Generate keys for programmatic access</p>
          </div>
          <button className="btn btn-primary" onClick={()=>setModal(true)}><Icons.Plus/> Generate Key</button>
        </div>

        <div className="bento-card" style={{ padding:14, background:'rgba(124,58,237,0.08)', borderColor:'rgba(124,58,237,0.25)' }}>
          <div style={{ display:'flex', gap:10, alignItems:'flex-start' }}>
            <div style={{ width:32, height:32, borderRadius:8, background:'rgba(124,58,237,0.2)', display:'flex', alignItems:'center', justifyContent:'center', flexShrink:0 }}><Icons.Key/></div>
            <div>
              <div style={{ fontSize:13, fontWeight:500 }}>Using API Keys</div>
              <div style={{ fontSize:12, color:'var(--muted)', marginTop:2 }}>
                Include your key in the <code style={{ background:'var(--secondary)', padding:'1px 5px', borderRadius:3 }}>X-API-Key</code> header when making requests.
              </div>
            </div>
          </div>
        </div>

        {loading ? <div style={{ textAlign:'center', padding:40 }}><Spinner size={28}/></div>
        : keys.length===0 ? (
          <div className="bento-card" style={{ textAlign:'center', padding:'48px 24px' }}>
            <div style={{ fontSize:48, marginBottom:12 }}>🔑</div>
            <h3 style={{ fontWeight:600, margin:'0 0 8px' }}>No API keys yet</h3>
            <p style={{ color:'var(--muted)', marginBottom:20 }}>Generate a key for programmatic access</p>
            <button className="btn btn-primary" onClick={()=>setModal(true)}><Icons.Plus/> Generate Key</button>
          </div>
        ) : (
          keys.map((k,i) => {
            const expired = isExpired(k.expires_at);
            return (
              <div key={k.id} className="bento-card" style={{ padding:'20px 24px' }}>
                <div style={{ display:'flex', alignItems:'flex-start', justifyContent:'space-between', gap:12, flexWrap:'wrap' }}>
                  <div style={{ display:'flex', gap:14 }}>
                    <div style={{ width:44, height:44, borderRadius:12, display:'flex', alignItems:'center', justifyContent:'center', flexShrink:0, background:k.is_active&&!expired?'rgba(16,185,129,0.15)':'var(--secondary)', color:k.is_active&&!expired?'#34d399':'var(--muted)' }}>
                      <Icons.Key/>
                    </div>
                    <div>
                      <div style={{ display:'flex', alignItems:'center', gap:8, flexWrap:'wrap', marginBottom:4 }}>
                        <span style={{ fontSize:16, fontWeight:600 }}>{k.name}</span>
                        {k.is_active ? (expired ? <span className="badge badge-amber">⚠ Expired</span> : <span className="badge badge-green">✓ Active</span>) : <span className="badge badge-red">Revoked</span>}
                      </div>
                      <div style={{ fontSize:13, fontFamily:'monospace', color:'var(--muted)', marginBottom:8 }}>{k.key_prefix}••••••••••••••••</div>
                      <div style={{ display:'flex', gap:12, fontSize:11, color:'var(--muted)', flexWrap:'wrap' }}>
                        <span>Created {formatDate(k.created_at)}</span>
                        {k.expires_at && <span>Expires {formatDate(k.expires_at)}</span>}
                        {k.last_used && <span>Last used {relTime(k.last_used)}</span>}
                      </div>
                    </div>
                  </div>
                  {k.is_active && (
                    <button className="btn btn-danger btn-sm" onClick={()=>revoke(k.id)}><Icons.Trash/> Revoke</button>
                  )}
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* Create modal */}
      {modal && (
        <div className="modal-bg" onClick={()=>setModal(false)}>
          <div className="modal-box" onClick={e=>e.stopPropagation()}>
            <div className="modal-title">Generate API Key</div>
            <div className="modal-desc">Create a new API key for programmatic access</div>
            <form onSubmit={create}>
              <div style={{ marginBottom:12 }}>
                <label>Key Name</label>
                <input placeholder="My Application" value={form.name} onChange={e=>setForm(f=>({...f,name:e.target.value}))} required/>
              </div>
              <div style={{ marginBottom:20 }}>
                <label>Expiration</label>
                <select value={form.expires_in_days} onChange={e=>setForm(f=>({...f,expires_in_days:e.target.value}))}>
                  <option value="7">7 days</option>
                  <option value="30">30 days</option>
                  <option value="90">90 days</option>
                  <option value="365">1 year</option>
                  <option value="never">Never expires</option>
                </select>
              </div>
              <div style={{ display:'flex', gap:8, justifyContent:'flex-end' }}>
                <button type="button" className="btn btn-secondary" onClick={()=>setModal(false)}>Cancel</button>
                <button type="submit" className="btn btn-primary" disabled={saving}>{saving?<Spinner/>:null} Generate</button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* New key display */}
      {newKeyModal && (
        <div className="modal-bg">
          <div className="modal-box">
            <div className="modal-title" style={{ display:'flex', alignItems:'center', gap:8 }}>
              <span style={{ color:'#34d399' }}>✓</span> API Key Generated
            </div>
            <div className="modal-desc">Copy your API key now — you won't be able to see it again!</div>
            <div style={{ background:'var(--secondary)', borderRadius:8, padding:14, fontFamily:'monospace', fontSize:12, wordBreak:'break-all', marginBottom:12 }}>
              {newKeyModal.api_key}
            </div>
            <button className="btn btn-primary" style={{ width:'100%', justifyContent:'center', marginBottom:12 }}
              onClick={()=>{ navigator.clipboard.writeText(newKeyModal.api_key); toast.success('Copied!'); }}>
              <Icons.Copy/> Copy to Clipboard
            </button>
            <button className="btn btn-secondary" style={{ width:'100%', justifyContent:'center' }} onClick={()=>setNewKeyModal(null)}>Done</button>
          </div>
        </div>
      )}
    </Layout>
  );
}

// ─── Page: API Docs ───────────────────────────────────────
function APIDocs() {
  const [tab, setTab] = useState('files');
  const base = window.location.origin + '/api';
  const CB = ({ c }) => <pre className="code-block">{c}</pre>;
  const EP = ({ method, path: p, desc, code }) => {
    const mc = { GET:'badge-green', POST:'badge-blue', PUT:'badge-amber', DELETE:'badge-red' };
    return (
      <div className="bento-card" style={{ marginBottom:12 }}>
        <div style={{ display:'flex', alignItems:'flex-start', gap:10, marginBottom:12 }}>
          <span className={`badge ${mc[method]}`}>{method}</span>
          <div>
            <code style={{ fontSize:13 }}>{p}</code>
            <div style={{ fontSize:12, color:'var(--muted)', marginTop:2 }}>{desc}</div>
          </div>
        </div>
        <CB c={code}/>
      </div>
    );
  };
  const tabs = ['files','connections','keys'];
  return (
    <Layout>
      <div style={{ display:'flex', flexDirection:'column', gap:24 }}>
        <div>
          <h1 style={{ fontSize:26, fontWeight:700, margin:0 }}>API Documentation</h1>
          <p style={{ color:'var(--muted)', fontSize:13, marginTop:4 }}>Interact with your files programmatically</p>
        </div>

        <div className="bento-card">
          <div style={{ display:'flex', alignItems:'center', gap:10, marginBottom:10 }}>
            <Icons.Key/><div>
              <div style={{ fontSize:13, fontWeight:600 }}>Authentication</div>
              <div style={{ fontSize:12, color:'var(--muted)' }}>Use API key in <code style={{ background:'var(--secondary)',padding:'1px 5px',borderRadius:3 }}>X-API-Key</code> header or JWT in <code style={{ background:'var(--secondary)',padding:'1px 5px',borderRadius:3 }}>Authorization: Bearer</code></div>
            </div>
          </div>
          <CB c={`curl "${base}/files/{id}/list?path=/" \\\n  -H "X-API-Key: your_key_here"`}/>
        </div>

        <div className="bento-card" style={{ padding:'10px 14px', background:'rgba(124,58,237,0.08)', borderColor:'rgba(124,58,237,0.25)' }}>
          <div style={{ display:'flex', alignItems:'center', gap:8 }}>
            <Icons.Code/>
            <span style={{ fontSize:12, fontWeight:500 }}>Base URL: </span>
            <code style={{ fontSize:12, color:'var(--muted)' }}>{base}</code>
          </div>
        </div>

        <div style={{ display:'flex', gap:4, background:'var(--secondary)', borderRadius:10, padding:4 }}>
          {tabs.map(t => (
            <button key={t} className={`btn btn-${tab===t?'primary':'ghost'}`} style={{ flex:1, justifyContent:'center', textTransform:'capitalize' }} onClick={()=>setTab(t)}>
              {t==='files'?'File Ops':t==='connections'?'Connections':'API Keys'}
            </button>
          ))}
        </div>

        {tab==='files' && <>
          <EP method="GET" path="/files/{id}/list" desc="List directory contents" code={`curl "${base}/files/{id}/list?path=/home/user" \\\n  -H "X-API-Key: your_key"`}/>
          <EP method="GET" path="/files/{id}/download" desc="Download a file" code={`curl "${base}/files/{id}/download?path=/file.txt" \\\n  -H "X-API-Key: your_key" -o file.txt`}/>
          <EP method="POST" path="/files/{id}/upload" desc="Upload a file (multipart)" code={`curl -X POST "${base}/files/{id}/upload?path=/home/user" \\\n  -H "X-API-Key: your_key" \\\n  -F "file=@local_file.txt"`}/>
          <EP method="POST" path="/files/{id}/mkdir" desc="Create a directory" code={`curl -X POST "${base}/files/{id}/mkdir?path=/home/user/newdir" \\\n  -H "X-API-Key: your_key"`}/>
          <EP method="DELETE" path="/files/{id}/delete" desc="Delete a file" code={`curl -X DELETE "${base}/files/{id}/delete?path=/file.txt" \\\n  -H "X-API-Key: your_key"`}/>
          <EP method="POST" path="/files/{id}/rename" desc="Rename file or directory" code={`curl -X POST "${base}/files/{id}/rename?old_path=/old.txt&new_path=/new.txt" \\\n  -H "X-API-Key: your_key"`}/>
        </>}
        {tab==='connections' && <>
          <EP method="GET" path="/connections" desc="List all connections" code={`curl "${base}/connections" \\\n  -H "Authorization: Bearer your_token"`}/>
          <EP method="POST" path="/connections" desc="Create a connection" code={`curl -X POST "${base}/connections" \\\n  -H "Authorization: Bearer your_token" \\\n  -H "Content-Type: application/json" \\\n  -d '{"name":"My Server","protocol":"sftp","host":"ftp.example.com","port":22,"username":"user","password":"secret"}'`}/>
          <EP method="POST" path="/connections/{id}/test" desc="Test a connection" code={`curl -X POST "${base}/connections/{id}/test" \\\n  -H "Authorization: Bearer your_token"`}/>
          <EP method="DELETE" path="/connections/{id}" desc="Delete a connection" code={`curl -X DELETE "${base}/connections/{id}" \\\n  -H "Authorization: Bearer your_token"`}/>
        </>}
        {tab==='keys' && <>
          <EP method="GET" path="/api-keys" desc="List API keys" code={`curl "${base}/api-keys" \\\n  -H "Authorization: Bearer your_token"`}/>
          <EP method="POST" path="/api-keys" desc="Create an API key" code={`curl -X POST "${base}/api-keys" \\\n  -H "Authorization: Bearer your_token" \\\n  -H "Content-Type: application/json" \\\n  -d '{"name":"My App Key","expires_in_days":30}'`}/>
          <EP method="DELETE" path="/api-keys/{id}" desc="Revoke an API key" code={`curl -X DELETE "${base}/api-keys/{id}" \\\n  -H "Authorization: Bearer your_token"`}/>
        </>}
      </div>
    </Layout>
  );
}

// ─── Page: Settings ───────────────────────────────────────
function Settings() {
  const { user } = useAuth();
  const [showToken, setShowToken] = useState(false);
  const token = localStorage.getItem('token');
  let tokenExpiry = null;
  try { const p = JSON.parse(atob(token.split('.')[1])); tokenExpiry = new Date(p.exp*1000); } catch{}

  return (
    <Layout>
      <div style={{ display:'flex', flexDirection:'column', gap:24 }}>
        <div>
          <h1 style={{ fontSize:26, fontWeight:700, margin:0 }}>Settings</h1>
          <p style={{ color:'var(--muted)', fontSize:13, marginTop:4 }}>Account info and access credentials</p>
        </div>

        {/* Profile */}
        <div className="bento-card">
          <div style={{ display:'flex', alignItems:'center', gap:8, marginBottom:16, fontSize:15, fontWeight:600 }}><Icons.User/> Profile</div>
          <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(180px,1fr))', gap:16 }}>
            {[['Name',user?.name],['Email',user?.email],['Member Since',formatDate(user?.created_at)]].map(([k,v])=>(
              <div key={k}><div style={{ fontSize:12, color:'var(--muted)', marginBottom:2 }}>{k}</div><div style={{ fontWeight:500 }}>{v||'—'}</div></div>
            ))}
            <div>
              <div style={{ fontSize:12, color:'var(--muted)', marginBottom:2 }}>User ID</div>
              <div style={{ display:'flex', alignItems:'center', gap:6 }}>
                <code style={{ fontSize:11, background:'var(--secondary)', padding:'2px 8px', borderRadius:4, overflow:'hidden', textOverflow:'ellipsis', whiteSpace:'nowrap', maxWidth:180 }}>{user?.id}</code>
                <button className="btn btn-ghost btn-icon" style={{ padding:'2px 4px' }} onClick={()=>{ navigator.clipboard.writeText(user?.id); toast.success('Copied!'); }}><Icons.Copy/></button>
              </div>
            </div>
          </div>
        </div>

        {/* JWT Token */}
        <div className="bento-card">
          <div style={{ display:'flex', alignItems:'center', gap:8, marginBottom:4, fontSize:15, fontWeight:600 }}><Icons.Shield/> JWT Token</div>
          <p style={{ fontSize:12, color:'var(--muted)', marginBottom:16 }}>Use this in the <code style={{ background:'var(--secondary)',padding:'1px 5px',borderRadius:3 }}>Authorization: Bearer</code> header</p>
          <div style={{ background:'rgba(255,255,255,0.04)', border:'1px solid var(--border)', borderRadius:8, padding:14, marginBottom:12 }}>
            <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between', marginBottom:10 }}>
              <span style={{ fontSize:13, fontWeight:500 }}>Bearer Token</span>
              <div style={{ display:'flex', gap:6 }}>
                <button className="btn btn-ghost btn-icon" onClick={()=>setShowToken(!showToken)}>{showToken?<Icons.EyeOff/>:<Icons.Eye/>}</button>
                <button className="btn btn-ghost btn-icon" onClick={()=>{ navigator.clipboard.writeText(token); toast.success('Token copied!'); }}><Icons.Copy/></button>
              </div>
            </div>
            <div style={{ fontFamily:'monospace', fontSize:11, wordBreak:'break-all', color:'var(--muted)', maxHeight:80, overflow:'auto' }}>
              {showToken ? token : '•'.repeat(60)}
            </div>
          </div>
          {tokenExpiry && <p style={{ fontSize:12, color:'var(--muted)', display:'flex', alignItems:'center', gap:6 }}><Icons.Clock/> Expires: {formatDate(tokenExpiry.toISOString())}</p>}
          <hr style={{ border:'none', borderTop:'1px solid var(--border)', margin:'16px 0' }}/>
          <div style={{ fontSize:13, fontWeight:500, marginBottom:8 }}>Usage Example</div>
          <pre className="code-block">{`curl "${window.location.origin}/api/connections" \\\n  -H "Authorization: Bearer YOUR_TOKEN"`}</pre>
        </div>

        {/* Auth methods */}
        <div className="bento-card" style={{ background:'rgba(124,58,237,0.05)', borderColor:'rgba(124,58,237,0.2)', padding:14 }}>
          <div style={{ fontSize:13, fontWeight:500, marginBottom:4 }}>Authentication Methods</div>
          <div style={{ fontSize:12, color:'var(--muted)', marginBottom:10 }}>JWT tokens for dashboard sessions · API keys for programmatic access</div>
          <div style={{ display:'flex', gap:8, flexWrap:'wrap' }}>
            <span className="badge badge-blue">JWT → Authorization header</span>
            <span className="badge badge-purple">API Key → X-API-Key header</span>
          </div>
        </div>
      </div>
    </Layout>
  );
}

// ─── App ──────────────────────────────────────────────────
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  const { navigate } = useRouter();
  useEffect(() => { if(!loading && !user) navigate('/login'); }, [user, loading]);
  if (loading) return (
    <div style={{ minHeight:'100vh', display:'flex', alignItems:'center', justifyContent:'center' }} className="grid-bg">
      <Spinner size={36}/>
    </div>
  );
  return user ? children : null;
}
function PublicRoute({ children }) {
  const { user, loading } = useAuth();
  const { navigate } = useRouter();
  useEffect(() => { if(!loading && user) navigate('/'); }, [user, loading]);
  if (loading) return null;
  return !user ? children : null;
}

function AppRoutes() {
  const { path } = useRouter();
  return (
    <AuthProvider>
      {(path === '/login') && <PublicRoute><Login/></PublicRoute>}
      {(path === '/register') && <PublicRoute><Register/></PublicRoute>}
      {(path === '/') && <ProtectedRoute><Dashboard/></ProtectedRoute>}
      {(path === '/connections') && <ProtectedRoute><Connections/></ProtectedRoute>}
      {(path === '/browser') && <ProtectedRoute><FileBrowser/></ProtectedRoute>}
      {(path === '/api-keys') && <ProtectedRoute><APIKeys/></ProtectedRoute>}
      {(path === '/docs') && <ProtectedRoute><APIDocs/></ProtectedRoute>}
      {(path === '/settings') && <ProtectedRoute><Settings/></ProtectedRoute>}
      {!['/login','/register','/','/connections','/browser','/api-keys','/docs','/settings'].includes(path) && (
        <ProtectedRoute><Dashboard/></ProtectedRoute>
      )}
    </AuthProvider>
  );
}

function App() {
  return (
    <Router>
      <AppRoutes/>
    </Router>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App/>);
</script>
<style>
/* Fix hover on file rows — can't do group-hover without JIT */
.file-row:hover .file-actions { opacity: 1 !important; }
</style>
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
SECRET_KEY    = os.environ.get("SECRET_KEY", secrets.token_hex(32))
ENCRYPTION_KEY= os.environ.get("ENCRYPTION_KEY", secrets.token_hex(32))
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
