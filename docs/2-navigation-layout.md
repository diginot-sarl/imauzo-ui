# 🧭 2. Navigation et Layouts

Cette section détaille les composants de structure d'application. Ils permettent de monter un Dashboard d'entreprise complet en quelques lignes.

---

## `<Layout>`
Le Layout principal est le conteneur fondamental de votre application. Il scinde l'écran en deux colonnes fixes : une Sidebar latérale (ou Drawer sur mobile) et une vue principale Scrollable.

### 🧩 Les Slots
| Nom du Slot | Utilisation |
|:---|:---|
| `sidebar` | Doit contenir le composant `<Sidebar>` |
| `main` | Le contenu de votre page (Vue Router, Nuxt Page) |

```vue
<Layout>
  <template #sidebar><Sidebar ... /></template>
  <template #main><router-view /></template>
</Layout>
```

---

## `<Sidebar>` & `<SidebarItem>` (Avec Sous-Menus) 🌟
Le client a exigé une documentation stricte de la Sidebar. Voici comment configurer la navigation latérale avec **transitions et hiérarchie**.

### 1. La Sidebar Container
```vue
<Sidebar :isExpanded="isExpanded" @toggle="isExpanded = !isExpanded">
   <!-- Vos SidebarItems vont ici -->
</Sidebar>
```
La prop `isExpanded` gère le repliement de la barre en affichage "icônes seules".

### 2. Le `<SidebarItem>`
Chaque bouton du menu. Il gère l'état `active` et accueille une `<Icon>` injectée via props.
| Prop | Type | Description |
|:---|:---|:---|
| `label` | `String` | Titre du menu. Masqué si `isExpanded = false`. |
| `icon` | `Component` | Le SVG Lucide (ex: `:icon="Home"`). |
| `active` | `Boolean` | Met le lien en surbrillance d'état Meta Blue. |

### 3. Créer un Sous-Menu avec Transition Animée
Dans les Dashboard complexes, un `SidebarItem` agit comme un accordéon. S'il est cliqué, il s'ouvre avec une **Transition Slide-Down** (ou Fade) pour dévoiler ses sous-menus.

**Code d'implémentation (Template à copier-coller) :**
```vue
<script setup>
import { ref } from 'vue'
import { Sidebar, SidebarItem } from 'imauzo-ui'
import { Users, FileText, ChevronDown, ChevronUp } from 'lucide-vue-next'

// Contrôle de l'accordéon local
const openMenus = ref({ users: true })

function toggleMenu(menu) {
   openMenus.value[menu] = !openMenus.value[menu]
}
</script>

<template>
  <!-- Déclencheur Parent -->
  <SidebarItem 
      label="Utilisateurs" 
      :icon="Users"
      :active="openMenus.users"
      @click="toggleMenu('users')"
  >
     <!-- Indicateur de Chevron (Masqué si la sidebar est repliée) -->
     <template #suffix v-if="isExpanded">
         <ChevronUp v-if="openMenus.users" class="w-4 h-4 text-text-secondary" />
         <ChevronDown v-else class="w-4 h-4 text-text-secondary" />
     </template>
  </SidebarItem>

  <!-- LE SOUS MENU ET SA TRANSITION -->
  <!-- Utilisez l'accordéon DaisyUI ou la transition native Vue -->
  <Transition 
     enter-active-class="transition-all duration-300 ease-out"
     enter-from-class="opacity-0 -translate-y-2 max-h-0"
     enter-to-class="opacity-100 translate-y-0 max-h-[500px]"
     leave-active-class="transition-all duration-200 ease-in"
     leave-from-class="opacity-100 translate-y-0 max-h-[500px]"
     leave-to-class="opacity-0 -translate-y-2 max-h-0"
  >
     <div v-if="openMenus.users && isExpanded" class="flex flex-col gap-1 ml-6 pl-4 mt-1 mb-2 border-l border-base-border overflow-hidden">
        <!-- Enfants (Plus petits, sans icônes générales) -->
        <SidebarItem label="Gérer les rôles" size="sm" />
        <SidebarItem label="Invitations" size="sm" />
     </div>
  </Transition>
</template>
```

---

## `<Navbar>`
Barre de navigation supérieure rigide (`fixed top-0 w-full`), souvent imbriquée *avant* ou *dans* la vue principale du Layout.

```vue
<Navbar title="Aperçu des factures">
   <!-- Slot actions à droite -->
   <template #actions>
       <Button variant="primary">Nouvelle</Button>
       <Avatar src="/profile.jpg" />
   </template>
</Navbar>
```

---

## `<Drawer>`
Sur mobile, la `<Sidebar>` se transforme en `<Drawer>`.
- `isOpen` (V-model invisible de contrôle).
- Son assombrissement (`overlay`) occupe 100% de la fenêtre. Si on clique dessus, le tiroir se referme.
