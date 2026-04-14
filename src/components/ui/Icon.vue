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

const colors: Record<string, string> = {
    default: 'text-text-primary',
    primary: 'text-primary',
    secondary: 'text-text-secondary',
    danger: 'text-danger',
    success: 'text-success',
    warning: 'text-warning'
}
</script>

<template>
    <component :is="icon" :class="cn(
        'shrink-0', 
        sizes[size] || sizes['md'], 
        colors[color] || colors['default'], 
        props.class
    )" />
</template>
