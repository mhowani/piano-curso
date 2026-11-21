# Piano Curso (web)

Versión web de la app Piano Curso: plan diario de 15 a 60 minutos, curso por estilos (Fase 0 y niveles 1 a 3 de clásica, blues, jazz, pop y rock), solfeo, tabla de acordes, ejercicios exportables a MusicXML para MuseScore, metrónomo y progreso.

Todo está en un solo archivo, `index.html`, sin servidor ni dependencias. El progreso se guarda en el navegador de cada dispositivo (en Progreso › Copia de seguridad puedes pasarlo de uno a otro).

## Publicar con GitHub Pages

Settings › Pages › Source: *Deploy from a branch*, rama `main`, carpeta `/ (root)`. La web queda en `https://<usuario>.github.io/piano-curso/`.

## Regenerar desde la app de Xcode

`fuente/conv.py` lee `Curriculum.swift`, `ExerciseLibrary.swift` y `Chords.swift` y crea `data.js`; `fuente/build.py` lo junta con `fuente/app.html` y el logo para crear `index.html`. Ajusta las rutas al principio de cada script.

Las partituras enlazadas son búsquedas en IMSLP, MuseScore.com y Mutopia; lo recomendado es de dominio público en España salvo lo marcado con ⚠︎.
