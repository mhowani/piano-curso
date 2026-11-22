# Crea juegos.html (página completa para GitHub Pages) a partir de fuente/juegos-notas.html,
# añadiendo la cabecera HTML y un enlace para volver a Piano Curso.
import os
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'juegos-notas.html'), encoding='utf-8').read()
head = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#5856d6">
<meta name="description" content="Juegos gratis para memorizar las notas del piano: lectura en clave de Sol y de Fa, notas por colores, oído y ritmo. Parte de Piano Curso.">
<meta name="keywords" content="juegos de notas musicales, aprender notas del piano, lectura de notas, clave de sol, clave de fa, solfeo para principiantes, juegos de música gratis">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://mhowani.github.io/piano-curso/juegos.html">
<link rel="icon" type="image/png" href="icon.png">
<link rel="apple-touch-icon" href="icon.png">
<link rel="manifest" href="site.webmanifest">
<script src="pwa.js" defer></script>
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Piano Curso">
<meta property="og:title" content="Juegos de notas · Piano Curso">
<meta property="og:description" content="Juegos gratis para memorizar las notas del piano: lectura en clave de Sol y de Fa, notas por colores, oído y ritmo. Parte de Piano Curso.">
<meta property="og:url" content="https://mhowani.github.io/piano-curso/juegos.html">
<meta property="og:image" content="https://mhowani.github.io/piano-curso/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}
.volver{font-weight:700;text-decoration:none;color:var(--accent)}</style>
'''
i = s.index('<main')
body = s[i:].replace('<header>', '<header>\n    <a class="volver" href="index.html#solfeo">‹ Piano Curso</a>', 1)
out = head + s[:i] + '</head>\n<body>\n' + body + '\n</body>\n</html>\n'
open(os.path.join(here, '..', 'juegos.html'), 'w', encoding='utf-8').write(out)
print('juegos.html', len(out))
