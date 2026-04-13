<script setup lang="ts">
import { cn } from '@/lib/utils'

interface CardProps {
    variant?: 'default' | 'muted' | 'info' | 'success' | 'warning' | 'error' | 'transparent'
    class?: string
    bodyClass?: string
    noPadding?: boolean
}

const props = withDefaults(defineProps<CardProps>(), {
    variant: 'default',
    noPadding: false
})

const variantClasses = {
    default: 'bg-white border-[#CED0D4]',
    muted: 'bg-[#F0F2F5] border-[#CED0D4] shadow-none',
    info: 'bg-[#EBF5FF] border-[#BDE0FE] shadow-none',
    success: 'bg-[#E7F3EB] border-[#A8E6CF] shadow-none',
    warning: 'bg-[#FFF5E5] border-[#FFE4B5] shadow-none',
    error: 'bg-[#FDF0F0] border-[#FFC1C1] shadow-none',
    transparent: 'bg-transparent border-transparent shadow-none'
}
</script>

<template>
    <div :class="cn(
        'rounded-xl border shadow-[0_1px_2px_rgba(0,0,0,0.05)] overflow-hidden',
        variantClasses[variant],
        props.class
    )">
        <div v-if="$slots.header" class="border-b border-inherit p-4 bg-white/40">
            <slot name="header" />
        </div>

        <div :class="cn(noPadding ? '' : 'p-4', props.bodyClass)">
            <slot />
        </div>

        <div v-if="$slots.footer" class="border-t border-[#CED0D4] bg-[#F0F2F5]/50 p-4 rounded-b-[7px]">
            <slot name="footer" />
        </div>
    </div>
</template>
