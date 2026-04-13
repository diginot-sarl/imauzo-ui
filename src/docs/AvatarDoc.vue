<script setup lang="ts">
import Avatar from '../components/ui/Avatar.vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import { User } from 'lucide-vue-next'
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">Avatar</Heading>
      <Text variant="secondary" size="lg">Composant d'image de profil avec gestion complète des états : statuts de connexion, multiples tailles, formes, et un système robuste d'affichage des initiales en cas d'erreur de chargement d'image.</Text>
    </div>

    <Section title="Tailles (Sizes)">
      <div class="flex items-end gap-6 flex-wrap">
         <Avatar src="https://i.pravatar.cc/150?u=xs" size="xs" />
         <Avatar src="https://i.pravatar.cc/150?u=sm" size="sm" />
         <Avatar src="https://i.pravatar.cc/150?u=md" size="md" />
         <Avatar src="https://i.pravatar.cc/150?u=lg" size="lg" />
         <Avatar src="https://i.pravatar.cc/150?u=xl" size="xl" />
      </div>
    </Section>

    <Section title="Formes (Shapes)">
      <div class="flex items-center gap-6 flex-wrap">
         <Avatar src="https://i.pravatar.cc/150?u=circle" shape="circle" size="lg" />
         <Avatar src="https://i.pravatar.cc/150?u=square" shape="square" size="lg" />
         <Avatar src="https://i.pravatar.cc/150?u=squircle" shape="squircle" size="lg" />
      </div>
    </Section>

    <Section title="Indicateurs de statut (Status)">
      <div class="flex items-center gap-8 flex-wrap">
         <Avatar src="https://i.pravatar.cc/150?u=online" size="lg" status="online" />
         <Avatar src="https://i.pravatar.cc/150?u=offline" size="lg" status="offline" />
         <Avatar initials="JD" size="md" status="online" />
      </div>
    </Section>

    <Section title="États de Secours & 'Meta Ring' (Fallbacks & Ring)">
      <div class="flex items-center gap-8 flex-wrap">
         <!-- L'image existe -->
         <div class="flex flex-col items-center gap-2">
            <Avatar src="https://i.pravatar.cc/150?u=ring" size="lg" ring />
            <Text size="sm" variant="secondary">Ring Actif</Text>
         </div>
         
         <!-- Pas d'image, juste des initiales -->
         <div class="flex flex-col items-center gap-2">
            <Avatar initials="ER" size="lg" />
            <Text size="sm" variant="secondary">Initiales (Fallback)</Text>
         </div>
         
         <!-- Erreur de lien 404 simulée -->
         <div class="flex flex-col items-center gap-2">
            <Avatar src="https://lien-casse-fake.com/img.jpg" initials="404" size="lg" ring />
            <Text size="sm" variant="secondary">Erreur 404 (Auto-Fallback)</Text>
         </div>

         <!-- Icône par défaut si aucune info -->
         <div class="flex flex-col items-center gap-2">
            <Avatar size="lg">
               <User class="w-1/2 h-1/2 opacity-50" />
            </Avatar>
            <Text size="sm" variant="secondary">Icône (Slot par défaut)</Text>
         </div>
      </div>
    </Section>
  </div>
</template>
