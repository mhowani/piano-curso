import base64
s=open('app.html').read()
data=open('data.js').read()
logo='data:image/png;base64,'+base64.b64encode(open('/mnt/project-files/app/PianoCurso/Assets.xcassets/Logo.imageset/logo@1x.png','rb').read()).decode()
s=s.replace('/*__DATA__*/',data).replace('/*__LOGO__*/',logo)
open('artifact.html','w').write(s)
head='''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#5856d6">
<link rel="icon" href="%s">
<link rel="apple-touch-icon" href="%s">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style>
''' % (logo,logo)
i=s.index('<main')
full=head+s[:i]+'</head>\n<body>\n'+s[i:]+'\n</body>\n</html>\n'
open('index.html','w').write(full)
print(len(s),len(full))
