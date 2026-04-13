<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    href?: string
    to?: any // Support router-link
    external?: boolean
    disabled?: boolean
    class?: any
}

const props = defineProps<Props>()

const Element = props.to ? 'router-link' : (props.href ? 'a' : 'button')
</script>

<template>
    <component :is="Element" :href="href" :to="to" :target="external ? '_blank' : undefined"
        :rel="external ? 'noopener noreferrer' : undefined" :disabled="disabled" :class="cn(
            'inline-flex items-center gap-1.5 text-[14px] font-semibold transition-colors',
            disabled ? 'opacity-50 cursor-not-allowed text-[#65676B]' : 'text-[#0866FF] hover:underline cursor-pointer',
            props.class
        )">
        <slot name="icon" />
        <slot />
    </component>
</template>
