# Publicar Piano Curso en Google Play y Microsoft Store

La app de Android y la de Windows son **la misma web** (`https://mhowani.github.io/piano-curso/`) metida en un paquete de tienda:

- **Android**: una *Trusted Web Activity* (TWA). Se instala como cualquier app, ocupa la pantalla entera y funciona sin conexión.
- **Windows**: un paquete *MSIX* que abre la web en su propia ventana, con icono en el menú Inicio.

Ventaja: cuando cambias la web, las dos apps se actualizan solas; no hay que volver a subir nada a las tiendas salvo que cambies el nombre, el icono o los permisos.

Los dos paquetes se generan gratis en **[PWABuilder](https://www.pwabuilder.com)** (de Microsoft), sin instalar Android Studio ni Visual Studio.

## Lo que ya está hecho en este repositorio

| Archivo | Para qué |
|---|---|
| `site.webmanifest` | Nombre, colores, iconos 192/512 normales y *maskable* (Android los recorta en círculo), capturas y acceso directo a los juegos. |
| `sw.js` + `pwa.js` | *Service worker*: hace la app instalable y que funcione sin conexión. Si cambias la web, sube `VERSION` en `sw.js`. |
| `iconos/` | Iconos para el manifiesto y para la ficha de Google Play (`icon-512.png`). |
| `tienda/` | Capturas de móvil (1080×1920) y de escritorio (1920×1080), gráfico destacado de Google Play (1024×500) y la plantilla `assetlinks.json`. |

## 1. Android (Google Play)

### 1.1 Cuenta de desarrollador (solo tú)
1. Entra en <https://play.google.com/console/signup> con tu cuenta de Google y elige **Personal**.
2. Paga **25 USD** (una sola vez) y verifica tu identidad con el DNI. Tarda unos días.
3. Al ser cuenta personal nueva, Google exige una **prueba cerrada con al menos 12 personas durante 14 días seguidos** antes de dejarte publicar para todo el mundo. Ve buscando 12 amigos o familiares con Android (bastan sus correos de Gmail).

### 1.2 Generar el paquete
1. En <https://www.pwabuilder.com> pega `https://mhowani.github.io/piano-curso/` y pulsa **Start**.
2. **Package For Stores › Android › Generate Package**. En *Options* pon:
   - Package ID: `io.github.mhowani.pianocurso`
   - App name: `Piano Curso` · Launcher name: `Piano Curso`
   - Signing key: **Create new**. Rellena tu nombre y una contraseña que no olvides.
3. Descarga el ZIP. Dentro hay:
   - `app-release-signed.aab` → lo que se sube a Google Play.
   - `app-release-signed.apk` → para instalarlo tú directamente en tu móvil y probar.
   - `signing.keystore` y `signing-key-info.txt` → **guárdalos en un sitio seguro (y una copia)**. Sin ellos no podrás publicar actualizaciones nunca más.
   - `assetlinks.json` → ver el paso 1.4.

### 1.3 Crear la app en Play Console
1. **Crear aplicación**: nombre *Piano Curso*, idioma español (España), *Aplicación*, *Gratis*.
2. **Ficha de Play Store**:
   - Descripción breve (máx. 80): `Aprende piano desde cero, gratis: solfeo, técnica y repertorio por estilos.`
   - Descripción completa: puedes copiar la del manual o la de la web.
   - Icono: `iconos/icon-512.png` · Gráfico destacado: `tienda/grafico-play-1024x500.png` · Capturas de teléfono: `tienda/movil-1.png`, `movil-2.png`, `movil-3.png`.
   - Categoría: **Educación**. Correo de contacto: el tuyo.
3. **Contenido de la aplicación** (cuestionarios obligatorios):
   - Política de privacidad: `https://mhowani.github.io/piano-curso/privacidad.html`.
   - Anuncios: **No**. Acceso: **todo disponible sin restricciones**.
   - Clasificación de contenido: categoría *Referencia, noticias o educación*; responde **No** a todo → saldrá *PEGI 3*.
   - Público objetivo: **13 años o más** (si eliges menores entran las normas de apps para niños, más exigentes).
   - Seguridad de los datos: el progreso se guarda solo en el móvil, así que no se recoge nada… salvo el **formulario de contacto**, que envía nombre, correo y mensaje si el usuario lo rellena. Marca *Información personal › Nombre y Dirección de correo* y *Mensajes de la aplicación › Otros mensajes*, finalidad **Comunicaciones del desarrollador**, *opcional*, *cifrado en tránsito: sí*, *no se comparte*.
4. **Pruebas › Prueba cerrada**: crea una pista, sube el `.aab`, añade los correos de tus 12 testers y envía a revisión. Ellos aceptan la invitación desde el enlace y tienen que **tener la app instalada los 14 días**.
5. Pasados los 14 días: **Panel › Solicitar acceso a producción**, responde las preguntas y, cuando lo aprueben, **Producción › Crear versión** con el mismo `.aab`.

### 1.4 Quitar la barra del navegador (assetlinks)
Sin este paso la app funciona, pero muestra arriba una barra con la dirección web. Android comprueba que la app y la web son del mismo dueño leyendo `https://mhowani.github.io/.well-known/assetlinks.json` — en la **raíz del dominio**, no dentro de `/piano-curso/`. Por eso hace falta un repositorio aparte:

1. En GitHub crea un repositorio público llamado exactamente **`mhowani.github.io`**.
2. Súbele un archivo vacío `.nojekyll` y el archivo `.well-known/assetlinks.json`.
3. Contenido: la plantilla `tienda/assetlinks.json` con las dos huellas SHA-256:
   - la de tu clave (viene en el `assetlinks.json` del ZIP de PWABuilder);
   - la de Google: Play Console › tu app › **Configuración › Integridad de la aplicación › Firma de apps** › *Certificado de la clave de firma de apps* › SHA-256.
4. Activa Pages en ese repositorio (Settings › Pages › rama `main`, carpeta raíz) y comprueba que `https://mhowani.github.io/.well-known/assetlinks.json` se abre.

Si prefieres, dímelo cuando tengas las huellas y lo preparo yo.

## 2. Windows (Microsoft Store)

### 2.1 Cuenta de desarrollador (solo tú)
1. Entra en <https://storedeveloper.microsoft.com> con tu cuenta Microsoft y elige **Individual**. Para particulares es **gratis** desde 2025; solo piden verificar la identidad (DNI y un selfie).
2. En **Partner Center › Apps y juegos › Nueva aplicación › MSIX o PWA**, reserva el nombre **Piano Curso**.
3. Abre la app reservada › **Identidad del producto** y apunta tres datos: *Package/Identity/Name*, *Package/Identity/Publisher* (empieza por `CN=`) y *Package/Properties/PublisherDisplayName*.

### 2.2 Generar el paquete
1. En PWABuilder, con la misma dirección: **Package For Stores › Windows › Generate Package**.
2. Pega los tres datos del paso anterior (Package ID, Publisher ID y Publisher display name) y la versión `1.0.0`.
3. Descarga el ZIP. Contiene un `.msixbundle` (para la tienda) y un `.classic.appxbundle` (para Windows antiguos). Súbelos los dos.

### 2.3 Enviar a la tienda
En Partner Center, en tu app, **Iniciar envío**:
- Precios: **Gratis**, todos los mercados.
- Propiedades: categoría **Educación**, política de privacidad `https://mhowani.github.io/piano-curso/privacidad.html`.
- Clasificación por edades: el cuestionario de IARC, igual que en Google (todo **No**).
- Paquetes: los dos archivos del ZIP.
- Ficha (español): descripción, capturas `tienda/escritorio-1.png` y `escritorio-2.png`, logo `iconos/icon-512.png`.
Envía. La revisión suele tardar entre unas horas y 3 días.

## 3. Instalar sin tiendas (ya funciona hoy)
- **Android**: abre la web en Chrome › menú ⋮ › **Instalar aplicación**. O instala el `.apk` del ZIP de PWABuilder.
- **Windows**: abre la web en Edge o Chrome › icono de instalar en la barra de direcciones.
- **Mac/iPhone**: tienes la app de Xcode; en iPhone también vale Safari › Compartir › **Añadir a pantalla de inicio**.

## 4. Al actualizar la web
Cambia lo que quieras, sube `VERSION` en `sw.js` (por ejemplo `piano-curso-v2`) y publica en `main`. Las apps de las tiendas cogen los cambios solas la siguiente vez que se abren con conexión.
