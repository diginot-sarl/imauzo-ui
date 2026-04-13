<script setup lang="ts">
import { computed } from 'vue'

interface Props {
    size?: 'sm' | 'md' | 'lg' | 'xl'
    color?: 'primary' | 'neutral' | 'white' | 'base'
}

const props = withDefaults(defineProps<Props>(), {
    size: 'md',
    color: 'primary'
})

const sizeClass = computed(() => {
    switch (props.size) {
        case 'sm': return 'w-4'
        case 'md': return 'w-6'
        case 'lg': return 'w-8'
        case 'xl': return 'w-12'
        default: return 'w-6'
    }
})

const colorClass = computed(() => {
    switch (props.color) {
        case 'primary': return 'text-[#0866FF]'
        case 'neutral': return 'text-[#65676B]'
        case 'base': return 'text-[#050505]'
        case 'white': return 'text-[#FFFFFF]'
        default: return 'text-[#0866FF]'
    }
})
</script>

<template>
    <span class="loading loading-spinner" :class="[sizeClass, colorClass]"></span>
</template>
