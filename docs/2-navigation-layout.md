# 🧭 2. Navigation et Layouts

Cette section détaille les composants de structure et les contrôles directionnels de l'application. Ils permettent de monter n'importe quel point de repère visuel (Tabs, Sidebar, Chemins).

---

## `<Layout>`
Le conteneur fondamental. Scinde l'écran en deux colonnes fixes : une Sidebar latérale (ou Drawer sur mobile) et une vue principale Scrollable.
```vue
<Layout>
  <template #sidebar><Sidebar ... /></template>
  <template #main><router-view /></template>
</Layout>
```

---

## `<Sidebar>` & `<SidebarItem>` (Avec Sous-Menus) 🌟
Voici comment configurer la navigation latérale avec **transitions et hiérarchie**.

### Code d'implémentation (Template à copier-coller) :
```vue
<script setup>
import { ref } from 'vue'
import { Sidebar, SidebarItem } from 'imauzo-ui'
import { Users, ChevronDown, ChevronUp } from 'lucide-vue-next'
const openMenus = ref({ users: true })
function toggleMenu(menu) { openMenus.value[menu] = !openMenus.value[menu] }
</script>

<template>
  <SidebarItem label="Utilisateurs" :icon="Users" :active="openMenus.users" @click="toggleMenu('users')">
     <template #suffix v-if="isExpanded">
         <ChevronUp v-if="openMenus.users" class="w-4 h-4 text-text-secondary" />
         <ChevronDown v-else class="w-4 h-4 text-text-secondary" />
     </template>
  </SidebarItem>

  <Transition enter-active-class="transition-all duration-300 ease-out" enter-from-class="opacity-0 -translate-y-2 max-h-0" enter-to-class="opacity-100 translate-y-0 max-h-[500px]" leave-active-class="transition-all duration-200 ease-in" leave-from-class="opacity-100 translate-y-0 max-h-[500px]" leave-to-class="opacity-0 -translate-y-2 max-h-0">
     <div v-if="openMenus.users && isExpanded" class="flex flex-col gap-1 ml-6 pl-4 mt-1 mb-2 border-l border-base-border overflow-hidden">
        <SidebarItem label="Gérer les rôles" size="sm" />
        <SidebarItem label="Invitations" size="sm" />
     </div>
  </Transition>
</template>
```

---

## `<Navbar>` & `<NavbarItem>`
Barre de navigation supérieure (`fixed top-0 w-full`). Utilisez son sous-composant `<NavbarItem>` pour intégrer des éléments uniformément espacés, acceptant la prop `badge` pour signaler une alerte.
```vue
<Navbar title="Aperçu des factures">
   <template #actions>
       <NavbarItem badge="3"><Bell /></NavbarItem>
       <Avatar src="/profile.jpg" />
   </template>
</Navbar>
```

---

## `<Drawer>`
Sur mobile, la `<Sidebar>` se transforme en `<Drawer>`.
- `isOpen` (V-model invisible de contrôle). Son assombrissement (`overlay`) occupe 100% de la fenêtre. Si on clique dessus, le tiroir se referme.

---

## `<Breadcrumb>` (Fil d'Ariane)
Essentiel pour naviguer dans une arborescence complexe (ex: ERP). Il convertit un tableau d'objets en chemins cliquables et gère le chevauchement Meta SVG implicite.
```vue
<Breadcrumb 
  :items="[
    { label: 'Accueil', href: '/' },
    { label: 'Clients', href: '/clients' },
    { label: 'Fiche Dossier' } /* Non cliquable = Actif */
  ]" 
/>
```

---

## `<Tabs>`
Navigation horizontale encastrée par bloc.
```vue
<Tabs 
   v-model="currentTab" 
   :tabs="['Profil', 'Sécurité', 'Facturation']" 
/>
<!-- Le composant active le liséré bleu Facebook en-dessous de l'onglet actif. -->
```

---

## `<Pagination>`
Contrôle de série de pages pour les grands listings. Gère la truncation logique (ex: `1 ... 4 5 6 ... 12`).
```vue
<Pagination 
  :currentPage="page" 
  :totalPages="12" 
  @update:page="page = $event" 
/>
```

---

## `<Stepper>` & `<StepperItem>`
Gère le découpage visuel lors d'un entonnoir (Wizard/Processus d'achat).
```vue
<Stepper>
  <StepperItem title="Validation" :done="true" />
  <StepperItem title="Paiement" active />
  <StepperItem title="Livraison" />
</Stepper>
```

---

## `<HeaderWidget>`
Widget structurel premium qui encapsule un Titre `h2` et un module d'action en haut de page, avec séparation visuelle.
```vue
<HeaderWidget title="Liste des Employés" subtitle="Gérez vos collaborateurs">
  <template #action>
    <Button variant="primary">Ajouter</Button>
  </template>
</HeaderWidget>
```
