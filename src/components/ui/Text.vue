<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    variant?: 'primary' | 'secondary' | 'hint' | 'error' | 'success'
    size?: 'xs' | 'sm' | 'md' | 'lg'
    weight?: 'normal' | 'medium' | 'semibold' | 'bold'
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    variant: 'primary',
    size: 'md',
    weight: 'normal'
})

const variants: Record<string, string> = {
    primary: 'text-text-primary',
    secondary: 'text-text-secondary',
    hint: 'text-text-secondary italic',
    error: 'text-danger',
    success: 'text-success'
}

const sizes = {
    xs: 'text-xs',
    sm: 'text-[13px]', // Facebook often uses 13px for subtle texts
    md: 'text-[15px]', // FB default
    lg: 'text-base'
}

const weights = {
    normal: 'font-normal',
    medium: 'font-medium',
    semibold: 'font-semibold',
    bold: 'font-bold'
}
</script>

<template>
    <p :class="cn(
        variants[variant] || variants['primary'], 
        sizes[size] || sizes['md'], 
        weights[weight] || weights['normal'], 
        props.class
    )">
        <slot />
    </p>
</template>
