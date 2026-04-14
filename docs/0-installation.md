# 🚀 0. Installation et Guide du Thème

iMauzo UI a été conçu en **"Option B"** : c'est un module NPM Headless qui délègue la compilation CSS au compiliateur Tailwind V4 de votre projet. Cela garantit une performance maximale (aucun doublon CSS) tout en forçant l'application du socle Meta Design System de Facebook.

---

## 💻 1. Installation du Package

Installons la librairie directement depuis le repository Git dans le dossier de votre projet final (ex: `imauzo-store-dashboard`) :

```bash
npm install git+ssh://git@github.com:diginot-sarl/imauzo-ui.git
```
*(iMauzo UI inscrira automatiquement `daisyui` et ses autres paquets frères dans votre `node_modules` de façon silencieuse.)*

---

## ⚡ 2. Paramétrage (Tailwind V4)

Dans le fichier d'entrée CSS de votre projet (souvent `main.css` ou `app.css`), déclarez notre configuration.

**L'ordre est absolument critique :**
```css
@import "tailwindcss";

/* 1. Assiette de variables Meta (Injectée en premier pour lier le :root Facebook) */
@import "imauzo-ui/style.css";

/* 2. Directive pour scanner le code brut Vue de la librairie */
@source "../node_modules/imauzo-ui/src/**/*.vue";

/* 3. Déclaration finale du plugin DaisyUI (si le dashboard ne l'a pas déjà déclaré) */
@plugin "daisyui";
```

Votre projet absorbe instantanément l'ADN Facebook. Vos configurations locales de Tailwind compileront toutes vos classes.

---

## 🎨 3. Charte Colorimétrique Officielle

Le framework met à votre disposition les variables natives Facebook que vous pouvez utiliser sans limites :

| Utilitaires Tailwind | Variable CSS Mappée | Utilité |
|:---|:---|:---|
| `bg-primary`, `text-primary` | `--color-primary` (#0866FF) | Actions dominantes (ex. *Ajouter au panier*) |
| `bg-secondary` | `--color-secondary` (#E4E6EB) | Actions courantes et annulatoires |
| `bg-danger` | `--color-danger` (#E41E3F) | Notifications rouges, Delete |
| `bg-success` | `--color-success` (#31A24C) | Validations, Enregistrements |
| `bg-base-200` | `--color-base-200` (#F0F2F5) | La teinte du fond de la page Web (Wash Grey) |
| `text-text-secondary` | `--color-text-secondary` (#65676B)| Textes passifs (Noms de statuts, dates) |

### 📐 Géométrie (Arrondis et Ombres)
* `rounded-md` (6px) : Destiné à tous vos `Button`
* `rounded-lg` (8px) : Destiné strictement aux `Card` et boites d'informations
* `shadow-md` : Elevation native du Dashboard.
