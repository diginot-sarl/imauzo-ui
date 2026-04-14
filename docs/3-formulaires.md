# 📝 3. Formulaires et Entrées

L'univers des Inputs iMauzo inclut tout le panel allant de la saisie numérique simple au document hybride uploader.

---

## Inputs Standards : `<TextInput>`, `<NumberInput>`, `<Textarea>`
Dédiés aux saisies natives avec l'allure minimaliste Facebook. Le focus applique un trait bleu roi (`--color-primary`), et l'erreur bascule toutes les couleurs en `--color-danger`.

```vue
<TextInput v-model="email" label="Adresse E-mail" />
<NumberInput v-model="age" label="Âge" :min="18" />
<Textarea v-model="bio" label="Description" :rows="4" />
```

---

## Sélecteurs Classiques et Avancés
La librairie prend nativement en charge des sélecteurs robustes, incluant le support de la recherche.

- **`<Select>`** : Liste déroulante native.
- **`<MegaSelect>`** : Choix unique avec Champ de Recherche et rendu UI Dropdown personnalisé.
- **`<MultiSelect>`** : Choix multiples générant automatiquement des `<Badge>` dans la barre de saisie.
- **`<TextTagInput>`** : Permet de taper "Entrée" pour former des mots-clés interactifs dans l'input (comme les tags Github).

```vue
<MegaSelect v-model="user" :options="usersList" optionLabel="nom" optionValue="id" />
<TextTagInput v-model="motsCles" label="Tags associés" />
```

---

## Uploadeurs & Documents
Composants spécialisés dans l'ingestion de fichiers avec aperçu généré localement (Miniature d'image ou signalétique PDF).

- **`<UploadInput>`** : Permet d'importer un fichier d'image ou de document (Visuel Drag&Drop).
- **`<MultiUploadInput>`** : Import massif de fichiers multiples.
- **`<DocumentInput>`** : Optimisé spécifiquement pour le scan de pièces d'identités ou de KYC, embarquant un format visuel en "Slot Card".

```vue
<UploadInput v-model="file" label="Envoyer la facture (.pdf)" accept=".pdf" />
```

---

## `<OTPInput>`
Composant Premium Meta-style pour renseigner un code d'authentification à N cases textuelles.
```vue
<OTPInput :length="6" @complete="(val) => verify(val)" />
```

---

## `<SearchInput>`
Input natif possédant une loupe intégrée et programmé pour les filtres rapides de l'application. Ne requiert pas de manipulation des slots, la loupe fait partie du design interne.
```vue
<SearchInput v-model="query" placeholder="Chercher un projet..." />
```

---

## Composants Booleans : `<Checkbox>`, `<Radio>`, `<Switch>`
Le visuel interne s'inspire du framework iOS / Meta :
- Le `Switch` affiche un ovale glissant qui révèle la teinte `--color-primary`.
- La `Checkbox` propose la coche animée et une bordure de `base-border`.
- Le `Radio` un cercle sélectionné classique pour les choix uniques.

```vue
<Switch v-model="enableBeta" label="Activer la Beta" />
<Checkbox v-model="terms" label="J'accepte les règles FB" />
```

---

## `<Range>`
Variante de `<input type="range">`. Stylisé avec la couleur Primaire Facebook, piste de repérage et poignée de modification.
```vue
<Range v-model="userVolume" :min="0" :max="100" />
```
