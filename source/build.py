"""Build relief.html (Claude preview) and the public pages (index, en/, es/) from src.html."""
import base64, os
D='/home/claude/relief'
s=open(f'{D}/src.html').read()
logo='data:image/webp;base64,'+base64.b64encode(open(f'{D}/logo-160.webp','rb').read()).decode()
mp='data:image/webp;base64,'+base64.b64encode(open(f'{D}/map-z14.webp','rb').read()).decode()
body=s.replace('__LOGO_DATA_URI__',logo).replace('__MAP_DATA_URI__',mp)
open(f'{D}/relief.html','w').write(body)
# PHOTO_FIX: absolute photo paths for the public pages (which live under /en/ and /es/)
pub=body.replace('src: "photos/','src: "/photos/')
rest=pub.replace('<title>Providence Church — Ayuda por el Sismo</title>\n','',1)
i=rest.index('<style>'); links=rest[:i]; r2=rest[i:]; j=r2.index('</style>')+8
style,content=r2[:j],r2[j:]
URL="https://providenceearthquakerelief.netlify.app/"
EN_DESC="Providence Church Coronado and local volunteers are collecting food, water, blankets, hygiene products and diapers for families affected by the earthquake in Azuero, Panama. Find a drop-off point or donate."
ES_DESC="Providence Church Coronado y voluntarios recolectan alimentos, agua, mantas, productos de higiene y pañales para las familias afectadas por el sismo en Azuero, Panamá. Encuentra un punto de recolección o dona."
def page(htmllang, pagelang, title, desc, locale, alt, suffix):
    attr=f' data-page-lang="{pagelang}"' if pagelang else ''
    return f'''<!doctype html>
<html lang="{htmllang}"{attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0E1830">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="https://providencechurchpa.org/img/favicon.png">
<link rel="apple-touch-icon" href="https://providencechurchpa.org/img/logo.png">
<link rel="canonical" href="{URL}{suffix}">
<link rel="alternate" hreflang="en" href="{URL}en/">
<link rel="alternate" hreflang="es" href="{URL}es/">
<meta property="og:url" content="{URL}{suffix}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Providence Church Coronado">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://providencechurchpa.org/img/logo.png">
<meta property="og:image:width" content="512">
<meta property="og:image:height" content="512">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{alt}">
<meta name="twitter:card" content="summary">
{links}{style}
</head>
<body>{content}
</body>
</html>
'''
for out in [f'{D}/deploy', '/home/claude/providence-earthquake-relief']:
    os.makedirs(f'{out}/en',exist_ok=True); os.makedirs(f'{out}/es',exist_ok=True)
    open(f'{out}/index.html','w').write(page("en",None,"Providence Church — Earthquake Relief",EN_DESC,"en_US","es_PA",""))
    open(f'{out}/en/index.html','w').write(page("en","en","Providence Church — Earthquake Relief",EN_DESC,"en_US","es_PA","en/"))
    open(f'{out}/es/index.html','w').write(page("es-PA","es","Providence Church — Ayuda por el Sismo",ES_DESC,"es_PA","en_US","es/"))
os.makedirs('/home/claude/providence-earthquake-relief/source',exist_ok=True)
open('/home/claude/providence-earthquake-relief/source/src.html','w').write(s)
print('built')
