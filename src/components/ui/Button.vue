<script setup lang="ts">
import { computed } from 'vue'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'
import { Loader2 } from 'lucide-vue-next'

const buttonVariants = cva(
    'inline-flex items-center justify-center gap-2 rounded-md font-semibold transition-colors duration-200 disabled:pointer-events-none disabled:opacity-50 select-none',
    {
        variants: {
            variant: {
                primary: 'bg-primary hover:bg-[#075ce5] text-white',
                secondary: 'bg-[#E4E6EB] hover:bg-[#D8DADF] text-[#050505]',
                ghost: 'hover:bg-[#F2F2F2] text-[#65676B]',
                danger: 'bg-[#E41E3F] hover:bg-[#C91A39] text-white',
            },
            size: {
                sm: 'h-[36px] px-3 text-[14px]',
                md: 'h-[44px] px-4 text-[15px]',
                lg: 'h-[48px] px-8 text-[17px]',
            },
        },
        defaultVariants: {
            variant: 'primary',
            size: 'md',
        },
    }
)

type ButtonProps = VariantProps<typeof buttonVariants>

interface Props {
    variant?: ButtonProps['variant']
    size?: ButtonProps['size']
    loading?: boolean
    disabled?: boolean
    type?: 'button' | 'submit' | 'reset'
    class?: string
}

const props = withDefaults(defineProps<Props>(), {
    variant: 'primary',
    size: 'md',
    loading: false,
    disabled: false,
    type: 'button',
})

const buttonClass = computed(() => cn(buttonVariants({ variant: props.variant, size: props.size }), props.class))
</script>

<template>
    <button :type="type" :class="buttonClass" :disabled="disabled || loading">
        <Loader2 v-if="loading" class="w-4 h-4 animate-spin" />
        <slot name="left-icon" v-if="!loading" />
        <slot />
        <slot name="right-icon" v-if="!loading" />
    </button>
</template>
