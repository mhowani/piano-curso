// Service worker de Piano Curso: permite instalar la app y usarla sin conexión.
// Al cambiar archivos de la web, sube VERSION para que los dispositivos descarguen lo nuevo.
const VERSION = 'piano-curso-v1';
const BASICOS = ['./', 'index.html', 'juegos.html', 'manual.html', 'privacidad.html',
  'site.webmanifest', 'icon.png', 'iconos/icon-192.png', 'iconos/icon-512.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) =>
    // Uno a uno: si falta alguna página, el resto se guarda igual.
    Promise.all(BASICOS.map((u) => c.add(u).catch(() => {})))
  ).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) =>
    Promise.all(ks.filter((k) => k !== VERSION).map((k) => caches.delete(k)))
  ).then(() => self.clients.claim()));
});

self.addEventListener('fetch', (e) => {
  const r = e.request;
  if (r.method !== 'GET') return; // el formulario de contacto (POST) va siempre a la red
  const url = new URL(r.url);
  const propio = url.origin === self.location.origin;
  const fuentes = /fonts\.(googleapis|gstatic)\.com$/.test(url.hostname);
  if (!propio && !fuentes) return;

  if (r.mode === 'navigate') {
    // Páginas: primero la red (para ver siempre la última versión), si no hay conexión, la copia.
    e.respondWith(fetch(r).then((res) => {
      const copia = res.clone();
      caches.open(VERSION).then((c) => c.put(r, copia));
      return res;
    }).catch(() => caches.match(r, { ignoreSearch: true }).then((m) => m || caches.match('index.html'))));
    return;
  }
  // Resto (iconos, fuentes): la copia al momento y se actualiza por detrás.
  e.respondWith(caches.match(r).then((m) => {
    const red = fetch(r).then((res) => {
      if (res.ok || res.type === 'opaque') { const copia = res.clone(); caches.open(VERSION).then((c) => c.put(r, copia)); }
      return res;
    }).catch(() => m);
    return m || red;
  }));
});
