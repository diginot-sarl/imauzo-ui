# 📝 3. Formulaires et Entrées

iMauzo UI garantit une saisie textuelle premium avec la gestion standardisée des labels, astuces (*hints*), et statuts d'erreur stricts avec Feedback visuel immédiat (Ring rouge).

---

## `<TextInput>` & `<Textarea>`
Dédié aux saisies natives avec l'allure minimaliste Facebook. Le focus applique un trait bleu roi (`--color-primary`), et l'erreur bascule toutes les couleurs en `--color-danger`.

### Props
| Nom | Type | Description |
|:---|:---|:---|
| `modelValue` | `String` | Utilisable avec `v-model`. |
| `label` | `String` | Libellé au dessus du champ, en gras. |
| `hint` | `String` | Mention en gris italic sous le label. |
| `isValid`| `Boolean`| Vaut `true` par défaut. Si passé à `false`, force un rendu critique rouge. |
| `errorMessage` | `String` | Message rouge affiché sous l'Input si `isValid` est `false`. |
| `disabled` | `Boolean` | Rend la saisie opaque et réfractaire aux clics. |

### Exemple
```vue
<TextInput 
   v-model="email" 
   label="Adresse E-mail" 
   placeholder="ex: john@doe.com"
   :isValid="emailValide"
   errorMessage="Cet email est déjà pris." 
/>
```

*(Idem pour le `<Textarea>` avec la prop `rows` pour déterminer la taille de base).*

---

## `<OTPInput>`
Composant Premium Meta-style pour renseigner un code d'authentification à N cases textuelles.

### Fonctionnalités :
- 6 cases indépendantes, centrées avec typographie Large.
- Auto-focus séquentiel : passe de la case 1 à 2, etc. de manière invisible.
- Gestion du Retour-Arrière (`Backspace`) sur les cases.
- Émission d'un évenement `@complete="code"` à la complétion.

```vue
<OTPInput :length="6" @complete="(val) => alert('Code validé: ' + val)" />
```

---

## `<Range>`
Variante de `<input type="range">`. Stylisé avec la couleur Primaire Facebook, piste de repérage et poignée de modification.

```vue
<div class="w-64">
    <Text variant="secondary">Volume : {{ userVolume }}%</Text>
    <Range v-model="userVolume" :min="0" :max="100" />
</div>
```

---

## `<MegaSelect>` et Sélecteurs Avancés
L'UI dispose de sélecteurs massifs (`MegaSelect`) intégrant un filtre de recherche, et de sélecteurs Multiples (`MultiSelect`) ou par Tag textuel (`TextTagInput`). 
Gérez un modèle V-Model complexe :

```vue
<MegaSelect 
   v-model="selectedProject" 
   :options="projectList" 
   optionLabel="name" 
   optionValue="id" 
/>
```

---

## `<Checkbox>`, `<Radio>`, `<Switch>`
Ces trois composants sont tous supportés. Le visuel interne s'inspire du framework iOS / Meta :
- Le `Switch` (Toggle) affiche un ovale gris clair qui glisse et révèle une teinte `--color-primary` à l'activation.
- La `Checkbox` propose la coche animée et une bordure de `base-border`.

```vue
<Switch v-model="enableBeta" label="Activer la Beta" />
<Checkbox v-model="terms" label="J'accepte les règles FB" />
```
