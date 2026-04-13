<script setup lang="ts">
interface Props {
    variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'error' | 'ghost' | 'neutral'
    outline?: boolean
}
const props = withDefaults(defineProps<Props>(), {
    variant: 'primary',
    outline: false
})
</script>

<template>
    <div class="badge font-semibold text-[12px] px-2.5 py-3" :class="[
        outline ? 'badge-outline' : 'border-transparent',
        !outline && variant === 'primary' ? 'bg-[#0866FF] text-white' : '',
        !outline && variant === 'secondary' ? 'bg-[#E4E6EB] text-[#050505]' : '',
        !outline && variant === 'success' ? 'bg-[#E7F3EB] text-[#2FA14A]' : '',
        !outline && variant === 'warning' ? 'bg-[#FFF5E5] text-[#D88A00]' : '',
        !outline && variant === 'error' ? 'bg-[#FDECEE] text-[#E02636]' : '',
        !outline && variant === 'neutral' ? 'bg-[#323436] text-white' : '',
        !outline && variant === 'ghost' ? 'bg-transparent text-[#65676B]' : '',

        outline && variant === 'primary' ? 'text-[#0866FF] border-[#0866FF]' : '',
        outline && variant === 'secondary' ? 'text-[#65676B] border-[#CED0D4]' : '',
        outline && variant === 'success' ? 'text-[#2FA14A] border-[#2FA14A]' : '',
        outline && variant === 'warning' ? 'text-[#D88A00] border-[#D88A00]' : '',
        outline && variant === 'error' ? 'text-[#E02636] border-[#E02636]' : ''
    ]">
        <slot></slot>
    </div>
</template>
