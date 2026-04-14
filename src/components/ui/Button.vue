<script setup lang="ts">
import { computed, useSlots } from 'vue'
import { cva } from 'class-variance-authority'
import { cn } from '../../lib/utils'

const buttonVariants = cva(
    'inline-flex items-center justify-center gap-2 font-semibold transition-all duration-200 select-none focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#0866FF]/50',
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
                xs: 'h-8 px-3 text-[13px] rounded-md',
                sm: 'h-9 px-4 text-[14px] rounded-md',
                md: 'h-10 px-5 text-[15px] rounded-lg',
                lg: 'h-12 px-6 text-[16px] rounded-xl',
                xl: 'h-14 px-8 text-[18px] rounded-2xl',
            },
        },
        defaultVariants: {
            variant: 'primary',
            size: 'md',
        },
    }
)

export type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger' | 'success' | 'outline'
export type ButtonSize = 'xs' | 'sm' | 'md' | 'lg' | 'xl'

interface Props {
    variant?: ButtonVariant
    size?: ButtonSize
    loading?: boolean
    disabled?: boolean
    type?: 'button' | 'submit' | 'reset'
    block?: boolean
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    variant: 'primary',
    size: 'md',
    loading: false,
    disabled: false,
    type: 'button',
    block: false
})

const slots = useSlots()

const VALID_VARIANTS: ButtonVariant[] = ['primary', 'secondary', 'ghost', 'danger', 'success', 'outline']
const VALID_SIZES: ButtonSize[] = ['xs', 'sm', 'md', 'lg', 'xl']

const buttonClass = computed(() => {
    const safeVariant = VALID_VARIANTS.includes(props.variant as ButtonVariant) ? props.variant : 'primary'
    const safeSize = VALID_SIZES.includes(props.size as ButtonSize) ? props.size : 'md'
    
    return cn(
        buttonVariants({ variant: safeVariant, size: safeSize }), 
        props.block ? 'w-full' : '',
        (props.disabled || props.loading) ? 'opacity-50 cursor-not-allowed pointer-events-none' : '',
        props.class
    )
})
</script>

<template>
    <button :type="type" :class="buttonClass" :disabled="disabled || loading">
        <!-- Spinner DaisyUI Natif -->
        <span v-if="loading" class="loading loading-spinner text-current"></span>
        
        <!-- Prefix Slot -->
        <slot name="prefix" v-if="!loading && slots.prefix" />
        
        <!-- Main Content -->
        <slot />
        
        <!-- Suffix Slot -->
        <slot name="suffix" v-if="slots.suffix" />
    </button>
</template>
