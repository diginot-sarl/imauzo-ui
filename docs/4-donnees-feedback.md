# 🛡️ 4. Données, Surfaces & Feedback

Cette ultime section traite de tous les éléments communicants : containers (`Cards`), affichage massif (`DataTables`), typographie pure (`Text`), et les fenêtres bloquantes (`Modals`).

---

## Textes et Typographie (`<Heading>`, `<Text>`, `<Section>`)
Composants génériques pour unifier l'enchainement de lecture sans polluer Tailwind de variables "font-size".
```vue
<Heading level="h2">Bienvenue sur le Dashboard</Heading>
<Text variant="secondary">Ceci est un texte de description standardisé.</Text>

<!-- Layout sémantique (Définit les paddings verticaux du document) -->
<Section>
  Contenu textuel a-typique.
</Section>
```

---

## Les Containers : `<Card>`, `<InfoCard>`, `<StatsCard>`
Le socle absolu du `base-100` Facebook (rayon `8px` et `<Section>` de slotage).
- `<Card>` : Carte neutre vierge avec Titre et Actions en haut à droite.
- `<InfoCard>` : Variante bleutée ou rouge appelant l'attention sur du texte descriptif.
- `<StatsCard>` : Affiche directement un Compteur chiffré, un label, et une flèche de tendance de croissance.

```vue
<StatsCard title="Revenus" value="12 400 €" trend="+5.2%" positive />
```

---

## L'Organisation : `<Accordion>` et `<ListTile>`
Gérez le dévoilement progressif.
- `<Accordion>` : Encapsulateur sémantique gérant le "Click-to-Reveal".
- `<ListTile>` : Permet de formaliser une ligne parfaite (`leading`, `title`, `subtitle`, `trailing`) extrêmement utilisée dans la modélisation de listes.

```vue
<ListTile title="Serveur Alpha" subtitle="192.168.1.1">
  <template #leading><Icon name="server" /></template>
  <template #trailing><Badge variant="success">En ligne</Badge></template>
</ListTile>
```

---

## Média et Icônes : `<Avatar>`, `<Icon>`, `<DocumentPreview>`, `<Editor>`
- `<Avatar>` : Gère le `shape` (circle, square) et le `ring` Facebook et les fallbacks initiales.
- `<Icon>` : Wrapper global propulsé par les icônes vectorielles.
- `<DocumentPreview>` / `<ImagePreview>` : Modal et visionneuse zoomée pour les documents lus.
- `<Editor>` : Outil de traitement de texte pur injecté.

---

## Interfaces Bloquantes & Dropdowns
- **`<DropdownButton>` / `<Popover>`** : Dropdowns via "Teleport". Ombres `shadow-lg` Meta.
- **`<Menu>`, `<MenuItem>`, `<MenuDivider>`** : La structure interne standard d'un Dropdown ou d'une Sidebar customisée pour isoler ses listes.
- **`<Modal>`** : Boite de dialogue vide native (avec backdrop gris oscuro), fermable par `Echap`.
- **`<ConfirmDialog>`** : Instance de `Modal` orientée texte/action précise (Oui/Non).

---

## Le Feedback Visuel Continu
Aidez l'utilisateur à comprendre l'état de son action.

- **Badges** `<Badge>` : Puce signalétique d'état (fond opalescent 20%).
- **Alertes** `<Alert>` / `<Notice>` : Bannière de message global sur la page (warning/danger).
- **Snackbar** `<Snackbar>` / `<Toast>` : Discrets notifications de temporisation en bas de page.
- **Loaders** `<Loader>` / `<CircleProgress>` : Spinners Meta authentiques isolés statiquement.
- **Success** `<SuccessWidget>` : Affichage final d'accomplissement avec énorme coche verte centrée.

---

## `<DataTable>`
Structure tabulaire massive permettant l'affichage de collections. Lignes alternées.
```vue
<DataTable :headers="enTetes" :data="lesClients">
   <!-- Surcharge d'une cellule -->
   <template #status="{ item }">
      <Badge variant="success">{{ item.status }}</Badge>
   </template>
</DataTable>
```

---
*Fin du document technique V1.0.0. iMauzo UI respecte le standard `Conventional Commits` et suit un versionnage sémantique rigoureux.*
