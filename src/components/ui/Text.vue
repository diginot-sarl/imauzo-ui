<script setup lang="ts">
import { computed } from 'vue'
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

const variants = {
    primary: 'text-[#050505]',
    secondary: 'text-[#65676B]',
    hint: 'text-[#65676B] italic',
    error: 'text-[#E02636]',
    success: 'text-[#2FA14A]'
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
    <p :class="cn(variants[variant], sizes[size], weights[weight], props.class)">
        <slot />
    </p>
</template>
