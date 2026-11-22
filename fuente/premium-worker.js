// Cloudflare Worker (gratis) que confirma las compras de Premium en Google Play.
// Google Play devuelve el dinero si una compra no se confirma («acknowledge») en 3 días,
// y la web (GitHub Pages) no puede hacerlo sola porque necesita una clave privada.
//
// Variables del Worker (Settings › Variables and Secrets):
//   GOOGLE_SA    (secreto)  el JSON completo de la cuenta de servicio de Google Cloud
//   PACKAGE_NAME (texto)    io.github.mhowani.pianocurso
// Los pasos están en PUBLICAR-TIENDAS.md › Premium.

const ORIGIN = "https://mhowani.github.io";
const cors = { "Access-Control-Allow-Origin": ORIGIN, "Access-Control-Allow-Methods": "POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type" };
const json = (o, status = 200) => new Response(JSON.stringify(o), { status, headers: { "Content-Type": "application/json", ...cors } });

export default {
  async fetch(req, env) {
    if (req.method === "OPTIONS") return new Response(null, { headers: cors });
    if (req.method !== "POST") return json({ error: "Solo POST" }, 405);
    let body; try { body = await req.json(); } catch (e) { return json({ error: "JSON no válido" }, 400); }
    const sku = String(body.sku || ""), tokens = (Array.isArray(body.tokens) ? body.tokens : []).slice(0, 5).map(String);
    if (!/^[a-z0-9._]{1,100}$/.test(sku) || !tokens.length) return json({ error: "Faltan datos" }, 400);

    const access = await googleToken(JSON.parse(env.GOOGLE_SA));
    const base = `https://androidpublisher.googleapis.com/androidpublisher/v3/applications/${env.PACKAGE_NAME}/purchases/products/${sku}/tokens/`;
    const results = [];
    for (const token of tokens) {
      const url = base + encodeURIComponent(token);
      const r = await fetch(url, { headers: { Authorization: `Bearer ${access}` } });
      if (!r.ok) { results.push({ valid: false }); continue; }
      const p = await r.json();
      const valid = p.purchaseState === 0; // 0 = comprada, 1 = cancelada, 2 = pendiente
      if (valid && p.acknowledgementState === 0) {
        await fetch(url + ":acknowledge", { method: "POST", headers: { Authorization: `Bearer ${access}`, "Content-Type": "application/json" }, body: "{}" });
      }
      results.push({ valid });
    }
    return json({ results });
  }
};

// Token de acceso de Google con la cuenta de servicio (JWT firmado con RS256).
async function googleToken(sa) {
  const b64url = (data) => btoa(typeof data === "string" ? data : String.fromCharCode(...new Uint8Array(data))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  const now = Math.floor(Date.now() / 1000);
  const head = b64url(JSON.stringify({ alg: "RS256", typ: "JWT" }));
  const claim = b64url(JSON.stringify({ iss: sa.client_email, scope: "https://www.googleapis.com/auth/androidpublisher", aud: "https://oauth2.googleapis.com/token", iat: now, exp: now + 3600 }));
  const pem = sa.private_key.replace(/-----[^-]+-----/g, "").replace(/\s/g, "");
  const key = await crypto.subtle.importKey("pkcs8", Uint8Array.from(atob(pem), c => c.charCodeAt(0)), { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", key, new TextEncoder().encode(`${head}.${claim}`));
  const r = await fetch("https://oauth2.googleapis.com/token", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=${head}.${claim}.${b64url(sig)}` });
  return (await r.json()).access_token;
}
