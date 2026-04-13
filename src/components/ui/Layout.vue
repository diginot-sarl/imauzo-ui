<script setup lang="ts">
import { computed } from 'vue'

interface Props {
    drawerId?: string
}

const props = withDefaults(defineProps<Props>(), {
    drawerId: 'imauzo-drawer'
})
</script>

<template>
    <div class="drawer lg:drawer-open h-screen bg-[#F0F2F5]">
        <input :id="drawerId" type="checkbox" class="drawer-toggle" />

        <!-- CONTENU PRINCIPAL -->
        <div class="drawer-content flex flex-col h-screen overflow-hidden">
            <!-- Navbar (Slot) -->
            <slot name="navbar" />

            <!-- Page Content (Scrollable) -->
            <main class="flex-1 overflow-y-auto w-full">
                <slot />
            </main>
        </div>

        <!-- SIDEBAR / DRAWER SIDE -->
        <div class="drawer-side z-50">
            <label :for="drawerId" aria-label="close sidebar" class="drawer-overlay"></label>
            <aside
                class="w-[280px] min-h-full bg-[#FFFFFF] shadow-[1px_0_4px_rgba(0,0,0,0.05)] border-r border-[#CED0D4]/40 flex flex-col">
                <!-- Logo / Header de Sidebar -->
                <div class="h-[56px] flex items-center px-4 border-b border-[#CED0D4] lg:border-transparent">
                    <slot name="sidebar-header">
                        <div class="font-bold text-[#0866FF] text-xl">App</div>
                    </slot>
                </div>

                <!-- Contenu de la sidebar (les liens) -->
                <div class="flex-1 relative overflow-hidden">
                    <slot name="sidebar" />
                </div>
            </aside>
        </div>
    </div>
</template>
