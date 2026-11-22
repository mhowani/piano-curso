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

## 5. Premium (pago único de 2,99 €)

La app es **gratis** en las tres tiendas y Premium es una **compra dentro de la app** (no consumible: se paga una vez y dura para siempre). Gratis: Fase 0 y Nivel 1. Premium: Niveles 2 y 3, notas con líneas adicionales y ritmo con corcheas en los juegos.

Cada tienda cobra, se queda un 15 % (apúntate a los programas para pequeños desarrolladores) e ingresa el IVA de cada venta en el país del comprador. Tú recibes el resto en tu cuenta bancaria.

El código ya está hecho. En `fuente/app.html` (constante `PREMIUM`) solo hay que rellenar los datos de cada tienda cuando los tengas, y regenerar con `fuente/build.py`. En la web normal (sin tienda) Premium no se puede comprar: es una demo gratuita que enseña dónde descargar la app.

### 5.1 Google Play
1. **Perfil de pagos**: Play Console › *Configuración › Perfil de pagos*. Rellena tu nombre, dirección, NIF y cuenta bancaria. Sin esto no deja crear productos.
2. **Crear el producto**: tu app › *Monetizar › Productos › Productos integrados en la aplicación › Crear producto*:
   - ID de producto: `premium` (no se puede cambiar después).
   - Nombre: `Piano Curso Premium`. Descripción: `Desbloquea los Niveles 2 y 3 y los juegos avanzados.`
   - Precio: **2,99 €** (Google calcula el resto de países). **Activar**.
3. **Paquete con pagos**: al generar el paquete en PWABuilder (paso 1.2), en *All settings* activa **Google Play Billing**. Si no aparece esa opción, dímelo y lo genero con Bubblewrap (`"playBilling": { "enabled": true }`).
4. **Confirmar las compras (obligatorio)**: Google devuelve el dinero si una compra no se confirma en 3 días, y eso necesita un pequeño servidor gratuito:
   1. En <https://console.cloud.google.com> crea un proyecto, activa la **Google Play Android Developer API** y crea una **cuenta de servicio** › *Claves › Añadir clave › JSON*. Se descarga un archivo: no lo compartas con nadie.
   2. En Play Console › *Usuarios y permisos › Invitar usuario*, pega el correo de esa cuenta de servicio y dale el permiso **Ver datos financieros, pedidos y respuestas a encuestas de cancelación** y **Gestionar pedidos y suscripciones** solo para Piano Curso.
   3. En <https://dash.cloudflare.com> (cuenta gratis) › *Workers & Pages › Create › Worker*, pega el contenido de `fuente/premium-worker.js` y despliega.
   4. En el Worker › *Settings › Variables and Secrets*: secreto `GOOGLE_SA` con todo el texto del JSON, y texto `PACKAGE_NAME` = `io.github.mhowani.pianocurso`.
   5. Copia la dirección del Worker (`https://….workers.dev`) en `PREMIUM.ackURL` de `fuente/app.html`.
5. **Probar**: Play Console › *Configuración › Pruebas de licencias* › añade tu Gmail. Con esa cuenta las compras de la prueba cerrada no se cobran.

### 5.2 Microsoft Store
1. Partner Center › *Configuración de la cuenta › Perfil de pago* y *Perfil fiscal* (formulario W-8BEN: residente en España, con tu NIF). Sin ellos no te pagan.
2. Tu app › *Complementos › Crear complemento* › tipo **Duradero**, ID `premium`. Duración: **para siempre**. Precio **2,99 €**. Nombre y descripción como en Google. Envíalo a certificación.
3. Copia el **Store ID** del complemento (empieza por `9…`) en `PREMIUM.microsoft.sku` de `fuente/app.html`.
4. Microsoft no exige servidor para confirmar la compra: la app la comprueba sola con la tienda.

### 5.3 App Store (iPhone, iPad y Mac)
Los pasos están en el `LEEME.md` de la app de Xcode: producto no consumible `com.ruben.pianocurso.premium` a 2,99 €, acuerdo de apps de pago y *App Store Small Business Program*.

### 5.4 Enlaces de la web
Cuando las apps estén publicadas, pon sus direcciones en `PREMIUM.links` de `fuente/app.html` y la web demo enseñará los botones para descargarlas. Dentro de la app de Android no se muestran: Google no permite enlazar a otras formas de pago.

### 5.5 Lo que te toca en España
- **Alta de autónomo** (Seguridad Social, sistema RETA, y Hacienda con el modelo 036/037) antes de empezar a cobrar de forma habitual. El primer año hay tarifa plana de unos 80 € al mes.
- **Declarar** los ingresos en el IRPF (pago fraccionado trimestral, modelo 130). Las tiendas actúan como intermediario y te mandan facturas mensuales de su comisión. Un gestor suele costar entre 40 y 60 € al mes y te lo lleva todo.
- **Política de privacidad y aviso legal** con tu nombre completo, NIF y un correo de contacto (lo exige la LSSI en cuanto la web o la app tienen actividad económica). Pásame esos datos y los añado a `privacidad.html` y a la app.
- La política de privacidad tiene que decir que las compras las gestiona cada tienda y que el servidor de Google Play recibe solo el código de la compra, sin datos personales.
