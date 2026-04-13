import codecs

app_content = """<script setup lang="ts">
import { ref } from 'vue'
import AvatarDoc from './docs/AvatarDoc.vue'
import ButtonDoc from './docs/ButtonDoc.vue'
import OTPInputDoc from './docs/OTPInputDoc.vue'
import DropdownDoc from './docs/DropdownDoc.vue'
import ControlsDoc from './docs/ControlsDoc.vue'
import InputsDoc from './docs/InputsDoc.vue'
import DataDoc from './docs/DataDoc.vue'
import NavDoc from './docs/NavDoc.vue'
import FeedbackDoc from './docs/FeedbackDoc.vue'
import AdvancedDoc from './docs/AdvancedDoc.vue'

import { 
  Users, DollarSign, Activity, FileText, 
  Home, Bell, Search, ArrowLeft, Eye, ThumbsUp, 
  Briefcase, PlusSquare, Lock, Menu, Settings, Shield
} from 'lucide-vue-next'

import Heading from './components/ui/Heading.vue'
import Layout from './components/ui/Layout.vue'
import Navbar from './components/ui/Navbar.vue'
import NavbarItem from './components/ui/NavbarItem.vue'
import Sidebar from './components/ui/Sidebar.vue'
import SidebarItem from './components/ui/SidebarItem.vue'
import DropdownButton from './components/ui/DropdownButton.vue'
import Avatar from './components/ui/Avatar.vue'

const activeDoc = ref('button')
const menuState = ref<'main' | 'stats'>('main')
const transitionName = ref('slide-left')

const goTo = (state: 'main' | 'stats') => {
  transitionName.value = state === 'stats' ? 'slide-left' : 'slide-right'
  menuState.value = state
}
</script>

<template>
  <Layout drawerId="imauzo-sidebar-drawer">
    <template #navbar>
      <Navbar title="iMauzo UI" drawerId="imauzo-sidebar-drawer">
        <template #right>
          <NavbarItem :icon="Search" />
          <NavbarItem :icon="Bell" badge="3" />
          <NavbarItem class="hidden sm:flex">
             <DropdownButton label="" align="end">
                 <template #trigger>
                     <div class="cursor-pointer hover:opacity-80 active:scale-95 transition-all">
                         <Avatar initials="JD" size="sm" />
                     </div>
                 </template>
                 <li class="menu-title px-3 py-2 flex flex-col gap-0.5">
                     <span class="font-bold text-[#050505]">John Doe</span>
                     <span class="text-xs font-normal text-[#65676B]">Administrateur système</span>
                 </li>
                 <div class="divider my-0.5"></div>
                 <li><a class="flex items-center gap-2 font-medium">Mon profil</a></li>
                 <li><a class="flex items-center gap-2 font-medium">Paramètres</a></li>
                 <li><a class="flex items-center gap-2 font-medium text-[#E41E3F] hover:bg-[#ffebee] hover:text-[#E41E3F]">Déconnexion</a></li>
             </DropdownButton>
          </NavbarItem>
        </template>
      </Navbar>
    </template>

    <template #sidebar>
      <transition :name="transitionName">
        <div v-if="menuState === 'main'" class="absolute inset-0 w-full h-full bg-[#FFFFFF] overflow-y-auto" key="main">
          <Sidebar class="w-full">
            <div class="px-3 pt-4 pb-4">
              <Heading level="3" class="leading-tight">Design System<br />iMauzo</Heading>
            </div>
            
            <SidebarItem title="Composants de base" :icon="Briefcase" disabled />
            <SidebarItem title="Avatar" :icon="Users" :active="activeDoc === 'avatar'" @click="activeDoc = 'avatar'" />
            <SidebarItem title="Button" :icon="PlusSquare" :active="activeDoc === 'button'" @click="activeDoc = 'button'" />
            <SidebarItem title="Dropdowns" :icon="Menu" :active="activeDoc === 'dropdown'" @click="activeDoc = 'dropdown'" />
            <SidebarItem title="Surfaces & Feedback" :icon="Shield" :active="activeDoc === 'feedback'" @click="activeDoc = 'feedback'" />
            
            <div class="divider my-1"></div>
            
            <SidebarItem title="Formulaires" :icon="FileText" :active="activeDoc === 'inputs'" @click="activeDoc = 'inputs'" />
            <SidebarItem title="OTP Input" :icon="Lock" :active="activeDoc === 'otp'" @click="activeDoc = 'otp'" />
            <SidebarItem title="Navigation" :icon="Home" :active="activeDoc === 'nav'" @click="activeDoc = 'nav'" />
            <SidebarItem title="Contrôles" :icon="Settings" :active="activeDoc === 'controls'" @click="activeDoc = 'controls'" />
            
            <div class="divider my-1"></div>
            
            <SidebarItem title="Données & Listes" :icon="Activity" :active="activeDoc === 'data'" @click="activeDoc = 'data'" />
            <SidebarItem title="Composants Métier" :icon="Briefcase" :active="activeDoc === 'advanced'" @click="activeDoc = 'advanced'" />

            <div class="divider my-1"></div>
            <!-- RESTAURATION DU MENU STATISTIQUES (ET AUTRES ANIMATIONS) -->
            <SidebarItem title="Statistiques" :icon="Activity" hasSubmenu @click="goTo('stats')" />
            <SidebarItem title="Contenu" :icon="FileText" hasSubmenu />
            <SidebarItem title="Monétisation" :icon="DollarSign" hasSubmenu />
            <SidebarItem title="Engagement" :icon="ThumbsUp" hasSubmenu />

          </Sidebar>
        </div>

        <div v-else class="absolute inset-0 w-full h-full bg-[#FFFFFF] overflow-y-auto" key="stats">
          <Sidebar class="w-full">
            <!-- Back button header -->
            <div class="px-2 pt-2">
              <button @click="goTo('main')"
                class="flex items-center gap-2 text-[#65676B] hover:bg-[#F0F2F5] px-2 py-1.5 mb-1 rounded-md w-full transition-colors text-[13px] font-semibold tracking-wide">
                <ArrowLeft class="w-4 h-4 text-[#050505]" />
                <span>Menu Principal</span>
              </button>
            </div>
            <div class="px-3 pb-4 pt-1">
              <Heading level="1">Statistiques</Heading>
            </div>

            <SidebarItem title="Vues" :icon="Eye" active />
            <SidebarItem title="Revenus" :icon="DollarSign" />
            <SidebarItem title="Interactions" :icon="ThumbsUp" />
            <SidebarItem title="Audience" :icon="Users" />
          </Sidebar>
        </div>
      </transition>
    </template>

    <div class="bg-[#F0F2F5] min-h-[100dvh] pb-12 w-full">
      <div class="max-w-6xl mx-auto mt-8 px-4">
        
        <KeepAlive>
           <AvatarDoc v-if="activeDoc === 'avatar'" />
           <ButtonDoc v-else-if="activeDoc === 'button'" />
           <OTPInputDoc v-else-if="activeDoc === 'otp'" />
           <DropdownDoc v-else-if="activeDoc === 'dropdown'" />
           <ControlsDoc v-else-if="activeDoc === 'controls'" />
           <InputsDoc v-else-if="activeDoc === 'inputs'" />
           <DataDoc v-else-if="activeDoc === 'data'" />
           <NavDoc v-else-if="activeDoc === 'nav'" />
           <FeedbackDoc v-else-if="activeDoc === 'feedback'" />
           <AdvancedDoc v-else-if="activeDoc === 'advanced'" />
        </KeepAlive>
        
      </div>
    </div>
  </Layout>
</template>
"""

with codecs.open(r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue', 'w', 'utf-8') as f:
    f.write(app_content)
