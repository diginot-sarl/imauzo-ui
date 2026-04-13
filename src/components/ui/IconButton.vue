<script setup lang="ts">
import { computed } from 'vue'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '../../lib/utils'

const iconButtonVariants = cva(
    'inline-flex items-center justify-center shrink-0 rounded-full font-semibold transition-all duration-200 select-none focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#0866FF]/50',
    {
        variants: {
            variant: {
                primary: 'bg-[#0866FF] hover:bg-[#075ce5] active:bg-[#0650c9] text-white shadow-sm',
                secondary: 'bg-[#E4E6EB] hover:bg-[#D8DADF] active:bg-[#CCD0D5] text-[#050505]',
                ghost: 'bg-transparent hover:bg-[#F0F2F5] active:bg-[#E4E6EB] text-[#65676B]',
                danger: 'bg-[#E41E3F] hover:bg-[#C91A39] active:bg-[#B01732] text-white shadow-sm',
                success: 'bg-[#2FA14A] hover:bg-[#288C40] active:bg-[#207033] text-white shadow-sm',
                outline: 'bg-transparent border-2 border-[#CED0D4] hover:border-[#8D949E] text-[#050505] active:bg-[#F2F2F2]',
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

type IconButtonProps = VariantProps<typeof iconButtonVariants>

interface Props {
    variant?: IconButtonProps['variant']
    size?: IconButtonProps['size']
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

const buttonClass = computed(() => cn(
    iconButtonVariants({ variant: props.variant, size: props.size }), 
    (props.disabled || props.loading) ? 'opacity-50 cursor-not-allowed pointer-events-none' : '',
    props.class
))
</script>

<template>
    <button :type="type" :class="buttonClass" :disabled="disabled || loading">
        <span v-if="loading" class="loading loading-spinner text-current"></span>
        <slot v-else></slot>
    </button>
</template>
