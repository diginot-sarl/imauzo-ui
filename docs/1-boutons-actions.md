# 🖱️ 1. Boutons et Actions

Les composants d'actions ont été revus pour une typographie stricte et une résistance absolue aux erreurs (Graceful Fallback). **DaisyUI a été écrasé pour que tous ces boutons respectent strictement l'esthétique Meta.**

---

## `<Button>`
Le bouton universel de l'application. Ses props ont été limitées par TS pour une autocomplétion pure.

### 🎭 Propriétés (`Props`)
| Nom | Type | Valeurs Acceptées | Défaut | Description |
|:---|:---|:---|:---|:---|
| `variant` | `String` | `primary`, `secondary`, `danger`, `success`, `outline`, `ghost` | `'primary'` | La coloration sémantique. |
| `size` | `String` | `xs`, `sm`, `md`, `lg`, `xl` | `'md'` | Gabarit de hauteur et de marge. |
| `loading` | `Boolean`| `true`, `false` | `false` | Affiche le **vrai spinner natif** et neutralise les clics. |
| `disabled`| `Boolean`| `true`, `false` | `false` | Rend le bouton pale `#E2E5E9` et inactif. |
| `block` | `Boolean`| `true`, `false` | `false` | Passe l'affichage du bouton à 100% de la largeur parente (`w-full`). |

### 🧩 Les Slots (Emplacements)
| Nom du Slot | Utilisation |
|:---|:---|
| `default` | Le texte central. |
| `prefix` | Une icône (`lucide-vue-next`) à positionner **avant** le texte. Masqué automatiquement en cas de `loading`. |
| `suffix` | Une icône à positionner **après** le texte. |

### 🛠️ Exemple Complet
```vue
<script setup>
import { Button } from 'imauzo-ui'
import { PlusCircle, ChevronRight } from 'lucide-vue-next'
</script>

<template>
  <Button variant="primary" size="lg" :loading="isSaving" block>
    <template #prefix><PlusCircle /></template>
    Créer le Projet
    <template #suffix><ChevronRight /></template>
  </Button>
</template>
```

---

## `<IconButton>`
Variante du bouton contraint au ratio aspect 1:1 totalement encerclé (Radius `rounded-full` ou `rounded-md` selon contexte d'usage).

**Props Identiques au Button** : `variant`, `size`, `loading`, `disabled`. (La prop `block` n'existe pas).

### Exemple d'Usage
```vue
<IconButton variant="ghost" size="sm" loading>
  <Settings class="w-4 h-4 text-text-secondary" />
</IconButton>
```

---

## `<ButtonGroup>`
Permet d'associer deux `<Button>` (ou plus) en soudant leurs bordures de contact. L'arrondi FB (`6px`) ne s'applique qu'aux arêtes externes du groupe complet !

### Remarque
Placez impérativement des `<Button>` ou `<IconButton>` en tant qu'enfants directs.
```vue
<ButtonGroup>
  <Button variant="secondary">Mensuel</Button>
  <Button variant="primary">Annuel</Button>
</ButtonGroup>
```

---

## `<SegmentedControl>`
L'équivalent d'un interrupteur Mac OS ou iOS à état. Il s'agit d'un rail gris `<div bg-base-300>` dans lequel orbite un carré blanc qui encercle l'option active.

### Props
| Nom | Type | Description |
|:---|:---|:---|
| `options` | `Array<String>` | La liste des onglets (ex: `['Jour', 'Semaine', 'Mois']`). |
| `modelValue` | `String` | `v-model` liant le choix de l'utilisateur. |

### Exemple
```vue
<script setup>
const periode = ref('Mois')
</script>
<template>
  <SegmentedControl :options="['Jour', 'Semaine', 'Mois']" v-model="periode" />
</template>
```

---

## `<BackButton>`
Bouton pré-stylisé hyper discret (Gris `F0F2F5`, Hover ombragé) pour implémenter un retour facile avec flèche pointant vers la gauche. Intégrez-le dans un en-tête d'écran.
```vue
<BackButton @click="router.back()" />
```
