# Piano Curso (web)

Versión web de la app Piano Curso: plan diario de 15 a 60 minutos, curso por estilos (Fase 0 y niveles 1 a 3 de clásica, blues, jazz, pop y rock), solfeo, tabla de acordes, ejercicios exportables a MusicXML para MuseScore, metrónomo y progreso.

Todo está en un solo archivo, `index.html`, sin servidor ni dependencias. El progreso se guarda en el navegador de cada dispositivo (en Progreso › Copia de seguridad puedes pasarlo de uno a otro).

## Juegos de notas

`juegos.html` tiene diez juegos para memorizar las notas (Do2 a Do6) con los colores del pentagrama, que combinan vista, oído y ritmo: nombra la nota, contrarreloj, al teclado, coloca la nota, colores, oído (sube o baja y qué nota suena), ritmo, lee a compás, parejas y mapa con progreso. Se abre desde Solfeo › Juegos. Se genera con `python3 fuente/build_juegos.py` a partir de `fuente/juegos-notas.html`.

## App instalable (Android, Windows)

La web es una PWA (`site.webmanifest`, `sw.js`, `pwa.js`): se puede instalar desde el navegador y funciona sin conexión. Para Google Play y Microsoft Store se empaqueta con PWABuilder; los pasos están en [PUBLICAR-TIENDAS.md](PUBLICAR-TIENDAS.md). Al cambiar la web, sube `VERSION` en `sw.js`.

## Publicar con GitHub Pages

Settings › Pages › Source: *Deploy from a branch*, rama `main`, carpeta `/ (root)`. La web queda en `https://<usuario>.github.io/piano-curso/`.

## Regenerar desde la app de Xcode

`fuente/conv.py` lee `Curriculum.swift`, `ExerciseLibrary.swift` y `Chords.swift` y crea `data.js`; `fuente/build.py` lo junta con `fuente/app.html` y el logo para crear `index.html`. Ajusta las rutas al principio de cada script.

Las partituras enlazadas son búsquedas en IMSLP, MuseScore.com y Mutopia; lo recomendado es de dominio público en España salvo lo marcado con ⚠︎.

## Manual y privacidad

`manual.html` y `privacidad.html` se generan con `python3 fuente/paginas.py`. El mismo script crea `InfoContent.swift` para la app de Xcode si le pasas una carpeta (`python3 fuente/paginas.py ruta/a/Models`), así la web y la app muestran el mismo texto.
