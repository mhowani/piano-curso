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
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}
.volver{font-weight:700;text-decoration:none;color:var(--accent)}</style>
'''
i = s.index('<main')
body = s[i:].replace('<header>', '<header>\n    <a class="volver" href="index.html#solfeo">‹ Piano Curso</a>', 1)
out = head + s[:i] + '</head>\n<body>\n' + body + '\n</body>\n</html>\n'
open(os.path.join(here, '..', 'juegos.html'), 'w', encoding='utf-8').write(out)
print('juegos.html', len(out))
