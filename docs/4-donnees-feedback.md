# 🛡️ 4. Données, Surfaces & Feedback

Cette ultime section traite de tous les éléments qui permettent de communiquer visuellement avec l'utilisateur ou d'afficher des données complexes (Surfaces). Dans l'empreinte Meta, le feedback est souvent géré par des overlays sombres ou des encarts aux bordures arrondies doucement (`8px` pour le radius général).

---

## `<Avatar>`
Un micro-composant affichant l'image de profil de l'utilisateur. Si l'image fait défaut, un Fallback utilisant le texte `initial` remplit l'espace avec un aspect gris perle.

### Props principales
| Nom | Typage | Description |
|:---|:---|:---|
| `src` | `String` | URL de l'image de l'utilisateur |
| `initial`| `String` | Composé des initales (ex: `JD`). Limité à 2 caractères. |
| `size` | `String` | Tailles `xs` à `xl`. Influe sur le font-size des initiales. |
| `shape` | `String` | `circle` (255px, par defaut), `square` (6px) |
| `ring` | `Boolean` | Encercle l'avatar d'une aura primaire en hover. |

**Exemple :** `<Avatar initial="AB" size="md" />`

---

## `<Badge>`
Puce signalétique. Conforme à la colorimétrie absolue Meta.

```vue
<!-- Affiche un conteneur vert pâle text-écrit émeraude -->
<Badge variant="success">Publié</Badge>

<Badge variant="danger" outline>Attention requise</Badge>
<Badge variant="secondary">Brouillon</Badge>
```

---

## `<DropdownButton>` & Menus
Les Dropdowns d'iMauzo utilisent une technologie de positionnement par "Teleport" afin de ne pas être coupés ou z-indexés par les ascendants (pratique dans un DataTable). L'ouverture dévoile un menu à rayon `6px` et l'ombre `shadow-lg` officielle Facebook.

```vue
<DropdownButton variant="outline" size="sm" class="ml-auto">
   <template #icon>Filtres <ChevronDown /></template>
   
   <!-- Contenu du menu téléporté -->
   <ul class="p-2 space-y-1">
      <li class="fb-card hover:bg-base-200 cursor-pointer p-2 text-sm rounded">Filtres Récents</li>
   </ul>
</DropdownButton>
```

---

## `<DataTable>`
Structure tabulaire massive permettant l'affichage de collections. Les en-têtes sont fixes. Les trames alternent légèrement de couleur.

### Déclaration Type
Passez la liste de vos clés avec `headers`, et le set de données dans `data`.
```vue
<script setup>
const lesClients = [{ id: 1, nom: 'Meta', status: 'Actif' }]
const enTetes = [
   { key: 'nom', label: 'Nom' },
   { key: 'status', label: 'État' }
]
</script>

<template>
  <DataTable :headers="enTetes" :data="lesClients">
     <!-- Surcharge d'une cellule manuelle (si on veut ajouter un composant Badge) -->
     <template #status="{ item }">
        <Badge variant="success">{{ item.status }}</Badge>
     </template>
  </DataTable>
</template>
```

---

## `<Toast>` et Notifications
L'affichage `Toast` se greffe généralement dans une couche mère (`Layout`). Elle apparaît brièvement dans le coin. Chez Meta, ces Toasts sont de couleur d'inverse (Noir ou F0F2F5 contrasté). 
(Fourni actuellement comme API visuelle de base en attendant le script de Toast Global).

---

## `<ConfirmDialog>` (Modale Méta)
Affiche une Surface bloquante avec Overlay foncé à 40%. Ce composant s'ouvre depuis le centre avec une légère transition d'agrandissement (`scale-95` to `scale-100`).

```vue
<ConfirmDialog 
   :isOpen="isOpen" 
   title="Déconnexion" 
   content="Êtes-vous sûr de vouloir de vous déconnecter ?"
   confirmText="Se déconnecter"
   confirmVariant="danger"
   @confirm="processLogout"
   @cancel="isOpen = false"
/>
```

---
*Vous voilà formellement maitre de la librairie **iMauzo UI**. Chaque atome de ces composants a été conçu pour se marier en une synergie parfaite. Intégrez, et appréciez.*
