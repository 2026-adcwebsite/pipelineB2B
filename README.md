# B2B Pipeline – Sistemi i Shitjeve

Një faqe e vetme HTML (`pipeline_b2b.html`) që zëvendëson Excel-in e takimeve ditore.

## Rolet
- **Agjent**: regjistron dhe edito takimet e veta.
- **Menaxher**: dashboard në kohë reale, listë e plotë, eksport CSV.
- **Admin**: si menaxheri, plus miratimi dhe ndryshimi i roleve.

Kush e publikon faqen bëhet Admin automatikisht. Të tjerët dërgojnë kërkesë dhe Admini i miraton.

## Të dhënat (db)
- `staff/{userId}` → `{name, role}`
- `requests/{userId}` → `{name, at}`
- `meetings/{id}` → fushat e takimit (date, mode, agentId, agentName, type, company, nipt, industry, contact, pos, phone, email, prio, potential, bill, volton, status, comment, prods, laptop, printer, acc, ts)

## Kërkesat e runtime
Faqja përdor `window.claude` (capabilities `db`, `user`, `downloads`), prandaj funksionon vetëm e publikuar si Claude Artifact. Jashtë tij (p.sh. nga GitHub Pages) nuk lidhet me bazën e të dhënave.

Konfigurimi i publikimit:

```json
{
  "db": {"rules": [
    {"path": "staff",    "read": "view", "write": "admin"},
    {"path": "requests", "read": "view", "write": "interact"},
    {"path": "meetings", "read": "view", "write": "interact"}
  ]},
  "downloads": true,
  "user": {}
}
```

## Shënim sigurie
Ndarja e pamjeve sipas rolit është në nivel UI. Për imponim real: agjentët si “Contributor”, menaxherët/adminët si “Editor”.

## Struktura
```
src/index.html   skeleti i faqes
src/styles.css   dizajni (tema e çelët/errët)
src/app.js       logjika: roles, formulari, dashboard, përdoruesit
build.py         bashkon src/ në dist/pipeline_b2b.html
```
Ndërtimi: `python3 build.py`, pastaj publiko `dist/pipeline_b2b.html` si Claude Artifact me konfigurimin e mësipërm.
