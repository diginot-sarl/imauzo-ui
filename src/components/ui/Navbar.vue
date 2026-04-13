<script setup lang="ts">
import { Menu } from 'lucide-vue-next'

interface Props {
    title?: string
    drawerId?: string // l'ID du checkbox pour le Drawer DaisyUI mobile
}

const props = defineProps<Props>()
</script>

<template>
    <div
        class="navbar bg-[#FFFFFF] shadow-[0_1px_4px_rgba(0,0,0,0.05)] border-b border-[#CED0D4]/30 px-4 min-h-[56px] sticky top-0 z-50">
        <!-- Mobile hamburger (visible que sur petits écrans si on a un Drawer) -->
        <div class="flex-none lg:hidden" v-if="drawerId">
            <label :for="drawerId" class="btn btn-square btn-ghost text-[#65676B] hover:bg-[#F0F2F5]">
                <Menu class="w-6 h-6" />
            </label>
        </div>

        <!-- Titre / Section gauche -->
        <div class="flex-1 flex items-center gap-2">
            <h1 v-if="title" class="text-xl font-bold text-[#050505] ml-2 lg:ml-0">{{ title }}</h1>
            <slot name="left"></slot>
        </div>

        <!-- Centre (Search bar par exemple) -->
        <div class="hidden md:flex flex-none items-center justify-center mx-4">
            <slot name="center"></slot>
        </div>

        <!-- Section Droite -->
        <div class="flex-none gap-2 flex items-center">
            <slot name="right"></slot>
        </div>
    </div>
</template>
