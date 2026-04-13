<script setup lang="ts">
import { ChevronDown } from 'lucide-vue-next'

interface Props {
    label: string
    align?: 'end' | 'start'
    variant?: 'primary' | 'secondary' | 'ghost'
}

const props = withDefaults(defineProps<Props>(), {
    align: 'start',
    variant: 'secondary'
})
</script>

<template>
    <div class="dropdown" :class="[align === 'end' ? 'dropdown-end' : '']">
        <button tabindex="0" role="button"
            class="btn btn-sm h-10 px-4 rounded-md tracking-wide text-[14px] font-semibold border-none shadow-none flex flex-nowrap items-center gap-1.5 transition-colors"
            :class="{
                'bg-[#0866FF] text-white hover:bg-[#075ce5]': variant === 'primary',
                'bg-[#E4E6EB] text-[#050505] hover:bg-[#D8DADF]': variant === 'secondary',
                'bg-transparent text-[#050505] hover:bg-[#F0F2F5]': variant === 'ghost'
            }">
            <slot name="label">{{ label }}</slot>
            <ChevronDown class="w-4 h-4 opacity-70" />
        </button>

        <!-- Dropdown menu -->
        <ul tabindex="0"
            class="dropdown-content z-[5] menu p-1.5 shadow-[0_4px_12px_rgba(0,0,0,0.1)] bg-white rounded-lg w-52 border border-[#CED0D4] mt-1">
            <slot></slot>
        </ul>
    </div>
</template>

<style scoped>
/* Scoped for list items inside this dropdown to match Facebook style */
:deep(li > a) {
    border-radius: 6px;
    color: #050505;
    font-weight: 500;
    font-size: 14px;
    padding: 8px 12px;
}

:deep(li > a:hover) {
    background-color: #F0F2F5;
}
</style>
