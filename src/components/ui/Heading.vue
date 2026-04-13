<script setup lang="ts">
import { computed } from 'vue'
import { cn } from '../../lib/utils'

interface Props {
    level?: '1' | '2' | '3' | '4' | '5' | '6'
    variant?: 'primary' | 'secondary' | 'section'
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    level: '2',
    variant: 'primary'
})

const Tag = computed(() => `h${props.level}` as any)

const variants = {
    primary: 'text-[#050505]',
    secondary: 'text-[#65676B]',
    section: 'text-[#65676B] uppercase tracking-wider'
}

const sizes = {
    '1': 'text-2xl lg:text-3xl font-bold',
    '2': 'text-xl lg:text-2xl font-bold',
    '3': 'text-lg font-bold',
    '4': 'text-base font-semibold',
    '5': 'text-sm font-semibold',
    '6': 'text-xs font-semibold'
}
</script>

<template>
    <component :is="Tag" :class="cn(variants[variant], sizes[level], props.class)">
        <slot />
    </component>
</template>
