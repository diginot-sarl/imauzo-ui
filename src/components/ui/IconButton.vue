<script setup lang="ts">
import { computed } from 'vue'
import { cva } from 'class-variance-authority'
import { cn } from '../../lib/utils'

const iconButtonVariants = cva(
    'inline-flex items-center justify-center shrink-0 rounded-full font-semibold transition-all duration-200 select-none focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#0866FF]/50',
    {
        variants: {
            variant: {
                primary: 'bg-primary hover:bg-primary-hover active:bg-primary-active text-white shadow-sm',
                secondary: 'bg-secondary hover:bg-secondary-hover active:bg-secondary-active text-text-primary',
                ghost: 'bg-transparent hover:bg-ghost-hover active:bg-ghost-active text-text-secondary',
                danger: 'bg-danger hover:bg-danger-hover active:bg-danger-active text-white shadow-sm',
                success: 'bg-success hover:bg-success-hover active:bg-success-active text-white shadow-sm',
                outline: 'bg-transparent border-2 border-base-border hover:border-base-border-hover text-text-primary active:bg-ghost-hover',
            },
            size: {
                xs: 'w-8 h-8',       // Icons should ideally be w-4
                sm: 'w-9 h-9',       // Icons w-4
                md: 'w-10 h-10',     // Icons w-5
                lg: 'w-12 h-12',     // Icons w-5
                xl: 'w-14 h-14',     // Icons w-6
            },
        },
        defaultVariants: {
            variant: 'ghost',
            size: 'md',
        },
    }
)

export type IconButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger' | 'success' | 'outline'
export type IconButtonSize = 'xs' | 'sm' | 'md' | 'lg' | 'xl'

interface Props {
    variant?: IconButtonVariant
    size?: IconButtonSize
    loading?: boolean
    disabled?: boolean
    type?: 'button' | 'submit' | 'reset'
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    variant: 'ghost',
    size: 'md',
    loading: false,
    disabled: false,
    type: 'button',
})

const VALID_VARIANTS: IconButtonVariant[] = ['primary', 'secondary', 'ghost', 'danger', 'success', 'outline']
const VALID_SIZES: IconButtonSize[] = ['xs', 'sm', 'md', 'lg', 'xl']

const buttonClass = computed(() => {
    const safeVariant = VALID_VARIANTS.includes(props.variant as IconButtonVariant) ? props.variant : 'ghost'
    const safeSize = VALID_SIZES.includes(props.size as IconButtonSize) ? props.size : 'md'

    return cn(
        iconButtonVariants({ variant: safeVariant, size: safeSize }), 
        (props.disabled || props.loading) ? 'opacity-50 cursor-not-allowed pointer-events-none' : '',
        props.class
    )
})
</script>

<template>
    <button :type="type" :class="buttonClass" :disabled="disabled || loading">
        <span v-if="loading" class="loading loading-spinner text-current"></span>
        <slot v-else></slot>
    </button>
</template>
