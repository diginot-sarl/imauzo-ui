<script setup lang="ts">
import { ChevronRight } from 'lucide-vue-next'

interface Crumb {
    label: string
    to?: string
}

interface Props {
    items: Crumb[]
}

const props = defineProps<Props>()
</script>

<template>
    <div class="breadcrumbs text-[13px] font-medium text-[#65676B] py-2">
        <ul>
            <li v-for="(item, index) in items" :key="index">
                <!-- Render Link if it has a target -->
                <a v-if="item.to && index < items.length - 1" :href="item.to"
                    class="hover:underline hover:text-[#0866FF] transition-colors">
                    {{ item.label }}
                </a>

                <!-- Render normal text if it's the last element -->
                <span v-else :class="index === items.length - 1 ? 'text-[#050505] font-semibold' : ''">
                    {{ item.label }}
                </span>
            </li>
        </ul>
    </div>
</template>

<style scoped>
/* Customize DaisyUI breadcrumb separator with specific color */
:deep(.breadcrumbs > ul > li + *:before) {
    content: "";
    /* Using the default DaisyUI separator SVG */
    opacity: 0.5;
}
</style>
