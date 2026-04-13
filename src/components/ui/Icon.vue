<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    icon: any
    size?: 'sm' | 'md' | 'lg' | 'xl'
    color?: 'primary' | 'secondary' | 'danger' | 'success' | 'warning' | 'default'
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    size: 'md',
    color: 'default'
})

const sizes = {
    sm: 'w-4 h-4',
    md: 'w-5 h-5',
    lg: 'w-6 h-6',
    xl: 'w-8 h-8'
}

const colors = {
    default: 'text-[#050505]',
    primary: 'text-[#0866FF]',
    secondary: 'text-[#65676B]',
    danger: 'text-[#E02636]',
    success: 'text-[#2FA14A]',
    warning: 'text-[#D88A00]'
}
</script>

<template>
    <component :is="icon" :class="cn('shrink-0', sizes[size], colors[color], props.class)" />
</template>
