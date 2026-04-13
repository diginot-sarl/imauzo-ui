<script setup lang="ts">
import Button from '../components/ui/Button.vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import IconButton from '../components/ui/IconButton.vue'
import ButtonGroup from '../components/ui/ButtonGroup.vue'
import DropdownButton from '../components/ui/DropdownButton.vue'
import { Plus, ArrowRight, Trash2, CheckCircle, Mail, MoreHorizontal, Settings, ChevronDown } from 'lucide-vue-next'
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">Button</Heading>
      <Text variant="secondary" size="lg">Composant d'action principal. Propose de multiples variantes visuelles (Facebook/Meta style), tailles, gestion des icônes latérales et indicateur de chargement DaisyUI natif.</Text>
    </div>

    <!-- Variants -->
    <Section title="Variantes (Variants)">
      <div class="flex flex-wrap items-center gap-4">
         <Button variant="primary">Primary</Button>
         <Button variant="secondary">Secondary</Button>
         <Button variant="ghost">Ghost</Button>
         <Button variant="outline">Outline</Button>
         <Button variant="danger">Danger</Button>
         <Button variant="success">Success</Button>
      </div>
    </Section>

    <!-- Tailles -->
    <Section title="Tailles (Sizes)">
      <div class="flex flex-wrap items-end gap-4">
         <Button size="xs">Extra Small</Button>
         <Button size="sm">Small</Button>
         <Button size="md">Medium</Button>
         <Button size="lg">Large</Button>
         <Button size="xl">Extra Large</Button>
      </div>
    </Section>

    <!-- États et Block -->
    <Section title="États (States)">
      <div class="flex flex-wrap items-center gap-4">
         <Button disabled>Désactivé (Disabled)</Button>
         <Button loading>En cours (Loading)</Button>
         <Button variant="secondary" loading>Sauvegarde...</Button>
         <Button variant="danger" loading>Suppression...</Button>
      </div>
      <div class="mt-4 w-full sm:w-1/2">
         <Button block>Bouton Block (Largeur complète)</Button>
      </div>
    </Section>

    <!-- Préfixes et Suffixes -->
    <Section title="Icônes Latérales (Prefix & Suffix Slots)">
      <div class="flex flex-wrap items-center gap-4">
         <Button>
            <template #prefix><Plus class="w-4 h-4" /></template>
            Nouveau projet
         </Button>

         <Button variant="secondary">
            Envoyer l'email
            <template #suffix><Mail class="w-4 h-4 text-[#65676B]" /></template>
         </Button>

         <Button variant="danger">
            <template #prefix><Trash2 class="w-4 h-4" /></template>
            Supprimer le compte
         </Button>

         <!-- Exemple interactif: chargement efface le prefix -->
         <Button variant="success" loading>
            <template #prefix><CheckCircle class="w-4 h-4" /></template>
            Succès Validé
         </Button>
      </div>
    </Section>

    <!-- IconButton -->
    <Section title="IconButton (Icônes seules)">
      <div class="flex flex-wrap items-center gap-4">
         <IconButton variant="primary" size="md"><Settings class="w-5 h-5" /></IconButton>
         <IconButton variant="secondary" size="lg"><MoreHorizontal class="w-6 h-6" /></IconButton>
         <IconButton variant="ghost" size="sm"><Trash2 class="w-4 h-4" /></IconButton>
         <IconButton variant="outline" size="md" loading></IconButton>
      </div>
    </Section>

    <!-- ButtonGroup -->
    <Section title="ButtonGroup (Groupement)">
      <div class="flex flex-wrap gap-8">
         <ButtonGroup>
            <Button variant="secondary">Jour</Button>
            <Button variant="secondary">Semaine</Button>
            <Button variant="secondary" class="bg-[#D8DADF] z-10">Mois</Button>
         </ButtonGroup>

         <ButtonGroup>
            <Button variant="primary">Créer un rapport</Button>
            <DropdownButton label="" align="end" variant="primary" class="w-10 px-0 justify-center">
                 <template #label><ChevronDown class="w-4 h-4" /></template>
                 <li><a>Sauvegarder brouillon</a></li>
                 <li><a class="text-error">Annuler</a></li>
            </DropdownButton>
         </ButtonGroup>
      </div>
    </Section>
  </div>
</template>
