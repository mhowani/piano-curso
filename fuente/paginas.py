# Contenido de la política de privacidad y del manual de usuario.
# Un solo origen para la web (privacidad.html, manual.html) y para la app de Xcode (InfoContent.swift).
# Uso:  python3 fuente/paginas.py [carpeta_de_la_app_swift]
# Formato del texto: **negrita** y [enlace](https://...). Bloques: ("p", texto) o ("ul", [textos]).
import os, re, sys, html

WEB = "https://mhowani.github.io/piano-curso/"
UPDATED = "22 de noviembre de 2026"
EMAIL = "cursopiano@outlook.es"
MAIL = f"[{EMAIL}](mailto:{EMAIL})"

PRIVACY = {
    "title": "Política de privacidad",
    "intro": f"Última actualización: {UPDATED}. Piano Curso es un proyecto personal y sin publicidad para aprender piano, gratuito en su parte básica y con una compra opcional (Premium). Esta política explica qué datos se tratan en la web y en la app, para qué y qué derechos tienes, según el Reglamento General de Protección de Datos (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD).",
    "sections": [
        ("responsable", "Quién es el responsable", [
            ("p", "El responsable del tratamiento es **Rubén**, titular de Piano Curso, con residencia en España. Para cualquier asunto de privacidad puedes escribirle a " + MAIL + " o desde el [formulario de contacto](" + WEB + "#contacto)."),
        ]),
        ("resumen", "En resumen", [
            ("ul", [
                "No hay cuentas, ni publicidad, ni cookies de seguimiento, ni herramientas de analítica.",
                "Tu progreso (minutos, lecciones y ajustes) se guarda **solo en tu dispositivo** y nunca se envía a ningún servidor.",
                "Solo se tratan datos personales si nos escribes (formulario de contacto o correo): tu nombre, tu correo y tu mensaje, para contestarte.",
                "Si compras Premium, el pago lo hace la tienda de tu dispositivo (App Store, Google Play o Microsoft Store). Piano Curso no ve tu nombre, tu correo ni tu tarjeta.",
            ]),
        ]),
        ("progreso", "Tu progreso en el dispositivo", [
            ("p", "En la web, el progreso se guarda en el almacenamiento local de tu navegador (localStorage). En la app, se guarda en el iPhone, iPad o Mac con el almacenamiento propio de Apple. Nadie más puede verlo. Lo puedes borrar cuando quieras borrando los datos del sitio en el navegador o desinstalando la app."),
            ("p", "Este almacenamiento local no es una cookie de seguimiento: solo sirve para que la aplicación funcione como pides, por lo que no necesita consentimiento (artículo 22.2 de la LSSI)."),
        ]),
        ("contacto", "Formulario de contacto", [
            ("ul", [
                "**Datos:** nombre, correo electrónico, tipo de mensaje y el texto que escribas.",
                "**Finalidad:** responder a tu mensaje.",
                "**Base legal:** tu consentimiento, que das al marcar la casilla antes de enviar (artículo 6.1.a del RGPD). Puedes retirarlo cuando quieras.",
                "**Plazo:** el mensaje se guarda en el correo del responsable el tiempo necesario para atenderte y como máximo 12 meses después de la última respuesta.",
                "**Encargado:** el envío lo hace [Web3Forms](https://web3forms.com), un servicio que recibe el mensaje y lo reenvía por correo. Sus servidores pueden estar fuera del Espacio Económico Europeo. Puedes leer su [política de privacidad](https://web3forms.com/privacy).",
                "Tus datos no se venden ni se ceden a nadie, y no se usan para enviarte publicidad.",
            ]),
            ("p", "Si prefieres no usar el formulario, también puedes abrir una incidencia en [GitHub](https://github.com/mhowani/piano-curso/issues). Ten en cuenta que esas incidencias son **públicas**."),
        ]),
        ("correo", "Correo electrónico", [
            ("p", "Si escribes a " + MAIL + ", tu dirección y tu mensaje se usan solo para contestarte, con la misma finalidad, base legal (tu consentimiento al escribir) y plazo que el formulario de contacto. El buzón está alojado en Outlook.com, de Microsoft, que actúa como encargado del tratamiento. Más información en la [declaración de privacidad de Microsoft](https://privacy.microsoft.com/es-es/privacystatement)."),
        ]),
        ("compras", "Compras (Premium)", [
            ("ul", [
                "Premium es un pago único que se hace dentro de la app con la tienda de tu dispositivo: **App Store** (Apple), **Google Play** (Google) o **Microsoft Store** (Microsoft). La tienda trata tus datos de pago según su propia política de privacidad y es quien emite el recibo.",
                "Piano Curso solo recibe de la tienda si la compra existe, para desbloquear el contenido. No recibe tu nombre, tu correo ni tus datos de pago.",
                "**Google Play:** para confirmar la compra, como exige Google, la app envía el código de la compra (un identificador sin datos personales) a un pequeño servidor en Cloudflare, que lo comprueba con Google. Ese servidor no guarda nada. Cloudflare, Inc. (EE. UU.) se acoge al Marco de Privacidad de Datos UE-EE. UU.",
                "**Base legal:** la ejecución del contrato de compra (artículo 6.1.b del RGPD).",
                "Para reembolsos o problemas con el cobro, escribe a la tienda donde compraste o a " + MAIL + ".",
            ]),
        ]),
        ("terceros", "Servicios de terceros", [
            ("ul", [
                "**Alojamiento:** la web está en GitHub Pages, de GitHub, Inc. (EE. UU.). Como cualquier servidor, registra tu dirección IP por seguridad. GitHub se acoge al Marco de Privacidad de Datos UE-EE. UU. Más información en la [declaración de privacidad de GitHub](https://docs.github.com/es/site-policy/privacy-policies/github-general-privacy-statement).",
                "**Tipografías:** la web carga sus letras desde Google Fonts, de Google LLC, que recibe tu dirección IP al descargarlas. Más información en la [política de privacidad de Google](https://policies.google.com/privacy?hl=es).",
                "**Enlaces externos:** las partituras y recursos enlazan a IMSLP, MuseScore.com, Mutopia y musictheory.net. Al abrirlos se aplican sus propias políticas de privacidad.",
            ]),
        ]),
        ("menores", "Menores de edad", [
            ("p", "Si tienes menos de 14 años, pide a tu madre, padre o tutor que escriba por ti en el formulario de contacto."),
        ]),
        ("derechos", "Tus derechos", [
            ("p", "Puedes pedir el acceso, la rectificación o la supresión de tus datos, la limitación u oposición a su tratamiento y su portabilidad, y retirar tu consentimiento. Escribe a " + MAIL + " o desde el [formulario de contacto](" + WEB + "#contacto) indicando qué derecho quieres ejercer."),
            ("p", "Si crees que no se han respetado tus derechos, puedes reclamar ante la [Agencia Española de Protección de Datos](https://www.aepd.es)."),
        ]),
        ("cambios", "Cambios en esta política", [
            ("p", "Si esta política cambia, se actualizará la fecha de arriba. Los cambios importantes se indicarán en la propia web."),
        ]),
    ],
}

MANUAL = {
    "title": "Manual de usuario",
    "intro": "Piano Curso te acompaña desde cero: cada día te propone una sesión a tu medida con solfeo, técnica y repertorio. La web y la app de iPhone, iPad y Mac funcionan igual. Aquí tienes cómo usar cada parte.",
    "sections": [
        ("empezar", "Primeros pasos", [
            ("ul", [
                "Abre la pestaña **Hoy** y elige con el deslizador cuántos minutos vas a practicar (de 15 a 60).",
                "Si nunca has tocado, deja tu nivel en **Fase 0**: unas 13 horas para conocer el teclado, leer las primeras notas y tocar tus primeras piezas.",
                "Pulsa el botón ▶ de cada bloque para practicar con cronómetro y metrónomo. Al pulsar **Guardar**, esos minutos cuentan para tu nivel.",
            ]),
        ]),
        ("hoy", "Hoy: tu sesión diaria", [
            ("p", "La sesión se reparte sola: **25 % solfeo, 25 % técnica, 38 % repertorio y 12 % juego libre**. Por debajo de 20 minutos no hay juego libre. Debajo del deslizador verás cuántas semanas te quedan para terminar el nivel practicando 5 días por semana."),
            ("p", "El repertorio cambia de estilo cada día: lunes y jueves clásica, martes blues, miércoles pop, viernes jazz o rock (alternos) y el fin de semana tu **estilo favorito**, que eliges al final de la pantalla. En la Fase 0 todo es de **Fundamentos**."),
            ("p", "Cuando completes las horas de un nivel, cambia tu nivel en **Tu nivel**. El contador de horas del nuevo nivel empieza de cero."),
        ]),
        ("curso", "Curso: el camino por estilos", [
            ("p", "En **Curso** están **Fundamentos** (solfeo y técnica, la base para todos los estilos) y las rutas de clásica, blues, jazz, pop y rock. Cada ruta es un camino con hitos numerados (0, 1, 2 y 3) y paradas que son las lecciones. La lección marcada como **SIGUIENTE** es la que te toca."),
            ("p", "Dentro de una lección:"),
            ("ul", [
                "Toca cada **paso** cuando lo hayas hecho; la barra muestra cuántos llevas.",
                "Los **acordes** de la lección se ven en un teclado y suenan al tocarlos.",
                "El **ejercicio de la app** suena con el botón Escuchar; puedes cambiar el tempo con − y +.",
                "Las **partituras gratuitas** abren la búsqueda en IMSLP (PDF), MuseScore.com y Mutopia. Lo recomendado es de dominio público en España, salvo lo marcado con ⚠︎.",
                "Al terminar, pulsa **Marcar como completada**.",
            ]),
        ]),
        ("musescore", "Ejercicios en MuseScore", [
            ("p", "Los 21 ejercicios propios se pueden descargar en formato **MusicXML**. Pulsa **Descargar .musicxml** y ábrelo en MuseScore con Archivo › Abrir. Si la descarga no empieza, pulsa **Copiar MusicXML**, pégalo en un archivo de texto y guárdalo con la extensión .musicxml. En la app de Mac, el botón **Abrir** lo abre directamente."),
        ]),
        ("acordes", "Tabla de acordes", [
            ("p", "Desde **Curso › Tabla de acordes** ves los 12 tipos de acorde (mayor, menor, 7ª, maj7…) en las 12 notas. Elige el tipo arriba y toca cualquier acorde para oírlo. La C roja marca cada Do."),
        ]),
        ("solfeo", "Solfeo y juegos de notas", [
            ("ul", [
                "**Teclado:** pulsa «Jugar» y encuentra la nota que se pide. Puedes ocultar los nombres de las teclas.",
                "**Lectura en clave de Sol y de Fa:** aparece una nota en el pentagrama y eliges su nombre. Empieza en el rango Fase 0 (Do a Sol) y sube a Nivel 1 y Completo.",
                "**Oído: intervalos:** escucha dos notas y elige la distancia entre ellas.",
                "**Juegos de notas:** nombra la nota, contrarreloj, al teclado, coloca la nota, colores, oído, ritmo, lectura a compás, parejas y mapa de progreso.",
            ]),
        ]),
        ("metronomo", "Cronómetro y metrónomo", [
            ("p", "Se abre con el botón ▶ de cada bloque, con **Practicar con cronómetro y metrónomo** en una lección o desde **Solfeo › Metrónomo**. Activa el metrónomo y elige las pulsaciones por minuto (de 40 a 200). El primer tiempo de cada compás suena más fuerte. A partir de 30 segundos puedes **Guardar** la sesión."),
        ]),
        ("progreso", "Progreso y copia de seguridad", [
            ("p", "En **Progreso** ves tu racha de días seguidos, las horas totales, las horas del nivel actual, el avance por ruta y tus últimas sesiones. Para borrar una sesión, pulsa × y después **Borrar**."),
            ("p", "El progreso se guarda solo en tu dispositivo. En la web puedes pasarlo a otro dispositivo con **Copia de seguridad**: pulsa **Copiar mi progreso**, pega el texto en el otro dispositivo con **Restaurar…** y pulsa **Restaurar este progreso**."),
        ]),
        ("instalar", "Tenerla como una app en el móvil", [
            ("ul", [
                "**iPhone o iPad (Safari):** abre la web, pulsa Compartir y luego **Añadir a pantalla de inicio**.",
                "**Android (Chrome):** abre el menú ⋮ y pulsa **Añadir a pantalla de inicio** o **Instalar aplicación**.",
            ]),
        ]),
        ("premium", "Premium", [
            ("p", "La Fase 0 y el Nivel 1 de todos los estilos son gratis. **Premium** es un pago único de 2,99 € que desbloquea los Niveles 2 y 3, los niveles difíciles de los juegos y las láminas para imprimir. Se compra dentro de la app de tu tienda (App Store, Google Play o Microsoft Store) desde la pantalla Premium."),
            ("p", "Si cambias de dispositivo, entra con la misma cuenta de la tienda y pulsa **Restaurar compra**. En la web normal Premium no se puede comprar: es una versión de prueba gratuita."),
        ]),
        ("preguntas", "Preguntas frecuentes", [
            ("ul", [
                "**No suena nada.** Toca primero cualquier botón de la página (los navegadores no dejan sonar nada hasta que interactúas) y comprueba que el iPhone no está en silencio.",
                "**He perdido mi progreso.** Ocurre si borras los datos del navegador o usas una ventana privada. Haz copias de vez en cuando desde Progreso.",
                "**¿Puedo usarla sin internet?** La app de Xcode sí. La web necesita conexión para abrirse; después, casi todo funciona aunque se corte.",
                "**¿Son legales las partituras?** Sí: se recomiendan obras de dominio público en España (autores fallecidos hace más de 80 años). En MuseScore.com, fíjate en la licencia, porque un arreglo moderno puede tener derechos.",
            ]),
        ]),
        ("ayuda", "¿Necesitas ayuda?", [
            ("p", "Escribe a " + MAIL + " o desde el [formulario de contacto](" + WEB + "#contacto) y te contestaremos por correo."),
        ]),
    ],
}

# ───────────────────────── HTML ─────────────────────────
def inline_html(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}"' + ('' if m.group(2).startswith(WEB) else ' target="_blank" rel="noopener"') + f'>{m.group(1)}</a>', t)
    return t

def page_html(doc, slug, description, other):
    toc = "".join(f'<li><a href="#{sid}">{html.escape(t)}</a></li>' for sid, t, _ in doc["sections"])
    body = ""
    for sid, t, blocks in doc["sections"]:
        body += f'<section id="{sid}"><h2>{html.escape(t)}</h2>'
        for kind, content in blocks:
            if kind == "p": body += f"<p>{inline_html(content)}</p>"
            else: body += "<ul>" + "".join(f"<li>{inline_html(x)}</li>" for x in content) + "</ul>"
        body += "</section>\n"
    title = doc["title"]
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#5856d6">
<title>{title} · Piano Curso</title>
<meta name="description" content="{html.escape(description)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{WEB}{slug}.html">
<link rel="icon" type="image/png" href="icon.png">
<link rel="apple-touch-icon" href="icon.png">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Piano Curso">
<meta property="og:title" content="{title} · Piano Curso">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{WEB}{slug}.html">
<meta property="og:image" content="{WEB}og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&family=Inter:wght@400;600;700&display=swap">
<style>
:root {{ --bg: #f4f3fb; --surface: #ffffff; --fg: #1d1b2e; --muted: #67647e; --line: #d9d7ea; --accent: #5856d6;
  --font-display: "Nunito", ui-rounded, system-ui, sans-serif; --font-body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg: #13121c; --surface: #1e1d2b; --fg: #f1f0fa; --muted: #a5a2bd; --line: #3a384e; --accent: #8e8cf5; color-scheme: dark; }} }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--fg); font: 16px/1.6 var(--font-body); }}
.wrap {{ max-width: 720px; margin: 0 auto; padding: 24px max(16px, env(safe-area-inset-right, 0px)) 64px max(16px, env(safe-area-inset-left, 0px)); }}
.back {{ display: inline-block; font-weight: 700; text-decoration: none; color: var(--accent); margin-bottom: 16px; }}
header.hero {{ color: #fff; border-radius: 24px; padding: 24px; background: linear-gradient(135deg, #5856d6, #af52de); margin-bottom: 20px; }}
header.hero h1 {{ font-family: var(--font-display); font-weight: 900; font-size: 2rem; line-height: 1.15; margin: 0 0 8px; text-wrap: balance; }}
header.hero p {{ margin: 0; opacity: .95; }}
nav.toc {{ background: var(--surface); border: 1px solid var(--line); border-radius: 18px; padding: 12px 20px; margin-bottom: 20px; }}
nav.toc ol {{ margin: 0; padding-left: 20px; }}
section {{ background: var(--surface); border: 1px solid var(--line); border-radius: 18px; padding: 4px 20px 8px; margin-bottom: 14px; scroll-margin-top: 16px; }}
h2 {{ font-family: var(--font-display); font-weight: 800; font-size: 1.3rem; margin: 16px 0 8px; }}
a {{ color: var(--accent); }}
li {{ margin-bottom: 6px; }}
footer {{ text-align: center; color: var(--muted); font-size: .9rem; margin-top: 24px; }}
:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
</style>
</head>
<body>
<div class="wrap">
<a class="back" href="index.html">‹ Volver a Piano Curso</a>
<header class="hero"><h1>{title}</h1><p>{inline_html(doc["intro"])}</p></header>
<nav class="toc" aria-label="Índice"><ol>{toc}</ol></nav>
<main>
{body}</main>
<footer><a href="index.html">Piano Curso</a> · <a href="{other[0]}">{other[1]}</a> · <a href="index.html#contacto">Contacto</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</div>
</body>
</html>
'''

# ───────────────────────── Swift ─────────────────────────
def swift_str(t):
    return '"' + t.replace("\\", "\\\\").replace('"', '\\"') + '"'

def swift_doc(name, doc):
    out = f"    static let {name} = InfoDocument(\n        title: {swift_str(doc['title'])},\n        intro: {swift_str(doc['intro'])},\n        sections: [\n"
    for sid, t, blocks in doc["sections"]:
        out += f"            InfoSection(id: {swift_str(sid)}, title: {swift_str(t)}, blocks: [\n"
        for kind, content in blocks:
            if kind == "p": out += f"                .paragraph({swift_str(content)}),\n"
            else: out += "                .bullets([\n" + "".join(f"                    {swift_str(x)},\n" for x in content) + "                ]),\n"
        out += "            ]),\n"
    return out + "        ])\n"

def swift_file():
    return ("import Foundation\n\n"
            "// Generado por fuente/paginas.py del repositorio piano-curso: edita allí el texto y vuelve a generarlo.\n"
            "// Texto con **negrita** y [enlaces](https://...) en Markdown.\n\n"
            "struct InfoDocument {\n    let title: String\n    let intro: String\n    let sections: [InfoSection]\n}\n\n"
            "struct InfoSection: Identifiable {\n    let id: String\n    let title: String\n    let blocks: [InfoBlock]\n}\n\n"
            "enum InfoBlock {\n    case paragraph(String)\n    case bullets([String])\n}\n\n"
            "enum InfoContent {\n"
            f"    static let webURL = URL(string: {swift_str(WEB)})!\n"
            f"    static let contactURL = URL(string: {swift_str(WEB + '#contacto')})!\n"
            f"    static let email = {swift_str(EMAIL)}\n"
            f"    static let emailURL = URL(string: {swift_str('mailto:' + EMAIL)})!\n"
            f"    static let privacyURL = URL(string: {swift_str(WEB + 'privacidad.html')})!\n"
            f"    static let manualURL = URL(string: {swift_str(WEB + 'manual.html')})!\n\n"
            + swift_doc("privacy", PRIVACY) + "\n" + swift_doc("manual", MANUAL) + "}\n")

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    open(os.path.join(root, "privacidad.html"), "w", encoding="utf-8").write(page_html(PRIVACY, "privacidad",
        "Política de privacidad de Piano Curso: qué datos se tratan (los mensajes que nos envías y la confirmación de las compras), para qué y cómo ejercer tus derechos según el RGPD.",
        ("manual.html", "Manual de usuario")))
    open(os.path.join(root, "manual.html"), "w", encoding="utf-8").write(page_html(MANUAL, "manual",
        "Manual de usuario de Piano Curso: cómo usar el plan diario, el curso por estilos, la tabla de acordes, los ejercicios para MuseScore, el solfeo, el metrónomo y el progreso.",
        ("privacidad.html", "Política de privacidad")))
    if len(sys.argv) > 1:
        open(os.path.join(sys.argv[1], "InfoContent.swift"), "w", encoding="utf-8").write(swift_file())
    print("ok")
