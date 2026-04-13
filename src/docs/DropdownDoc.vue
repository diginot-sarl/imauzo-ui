<script setup lang="ts">
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import DropdownButton from '../components/ui/DropdownButton.vue'
import IconButton from '../components/ui/IconButton.vue'
import Avatar from '../components/ui/Avatar.vue'
import { MoreHorizontal, Settings, LogOut, User } from 'lucide-vue-next'
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">Dropdown</Heading>
      <Text variant="secondary" size="lg">Menus déroulants intelligents avec portail externe (Teleport) pour éviter toute coupure, propulsés par Floating UI. Supporte entièrement les déclencheurs (triggers) personnalisés comme les icônes ou avatars.</Text>
    </div>

    <!-- Classique -->
    <Section title="Classique">
      <div class="flex gap-4">
         <DropdownButton label="Options (Primaire)" variant="primary">
            <li><a>Modifier</a></li>
            <li><a>Dupliquer</a></li>
            <li><a class="text-error">Archiver</a></li>
         </DropdownButton>

         <DropdownButton label="Filtres" variant="secondary" align="end">
            <li><a>Nom (A-Z)</a></li>
            <li><a>Le plus récent</a></li>
         </DropdownButton>
      </div>
    </Section>

    <!-- Icon-Only Triggers -->
    <Section title="Icon-Only (Sans texte)">
      <div class="flex items-center gap-8">
         <DropdownButton label="">
            <template #trigger>
                <!-- On injecte notre IconButton pour l'esthétique parfaite 1:1 -->
                <IconButton variant="ghost" size="md">
                    <MoreHorizontal class="w-5 h-5" />
                </IconButton>
            </template>
            <li><a>Voir les détails</a></li>
            <li><a class="text-error">Supprimer définitivement</a></li>
         </DropdownButton>

         <DropdownButton label="" align="end">
            <template #trigger="{ isOpen }">
                <!-- Variante Primary encadrée -->
                <IconButton variant="secondary" size="lg" :class="isOpen ? 'ring-2 ring-[#0866FF] ring-opacity-50' : ''">
                    <Settings class="w-6 h-6" />
                </IconButton>
            </template>
            <li><a>Configuration</a></li>
            <li><a>Licence</a></li>
         </DropdownButton>
      </div>
    </Section>

    <!-- Avatar Trigger -->
    <Section title="Déclencheur Avatar (Meta Navbar Style)">
      <div class="p-4 bg-[#FFFFFF] shadow-sm rounded-lg border border-[#CED0D4] flex items-center justify-between">
         <div class="font-bold text-[#0866FF]">Top Bar Mockup</div>
         
         <!-- Dropdown encapsulant l'avatar -->
         <DropdownButton label="" align="end">
             <template #trigger>
                 <div class="cursor-pointer hover:opacity-80 active:scale-95 transition-all">
                     <Avatar initials="JD" size="sm" />
                 </div>
             </template>
             <li class="menu-title px-4 py-2">
                 <span class="font-bold text-[#050505]">John Doe</span>
                 <span class="text-xs font-normal text-[#65676B]">Admin</span>
             </li>
             <div class="divider my-0"></div>
             <li><a class="flex items-center gap-2"><User class="w-4 h-4"/> Mon profil</a></li>
             <li><a class="flex items-center gap-2"><Settings class="w-4 h-4"/> Paramètres</a></li>
             <li><a class="flex items-center gap-2 text-error"><LogOut class="w-4 h-4"/> Déconnexion</a></li>
         </DropdownButton>
      </div>
    </Section>
  </div>
</template>
