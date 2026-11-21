# Crea index.html (página completa para GitHub Pages) y artifact.html a partir de app.html + data.js (de conv.py).
# La cabecera SEO sale de seo-cabecera.html y el texto sin JavaScript de seo-noscript.html.
import base64, os
here = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: open(os.path.join(here, n), encoding='utf-8').read()
s = rd('app.html')
data = open('data.js', encoding='utf-8').read()
logo = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(here, '..', 'icon.png'), 'rb').read()).decode()
s = s.replace('/*__DATA__*/', data).replace('/*__LOGO__*/', logo)
open('artifact.html', 'w', encoding='utf-8').write(s)
head = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#5856d6">
''' + rd('seo-cabecera.html') + '''<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
'''
i = s.index('<main')
full = head + s[:i] + '</head>\n<body>\n' + rd('seo-noscript.html') + s[i:] + '\n</body>\n</html>\n'
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(full)
print(len(s), len(full))
