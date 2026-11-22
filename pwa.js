// Registra el service worker (app instalable y sin conexión en Android, Windows, Mac e iPhone).
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
}
