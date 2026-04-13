<script setup lang="ts">
interface Props {
    align?: 'end' | 'start'
    width?: string
}

const props = withDefaults(defineProps<Props>(), {
    align: 'start',
    width: 'w-64'
})
</script>

<template>
    <div class="dropdown" :class="[align === 'end' ? 'dropdown-end' : 'dropdown-bottom']">
        <div tabindex="0" role="button" class="inline-block cursor-pointer">
            <slot name="trigger"></slot>
        </div>
        <div tabindex="0"
            class="dropdown-content z-[10] shadow-[0_4px_12px_rgba(0,0,0,0.1)] bg-white rounded-lg border border-[#CED0D4] mt-2 p-0"
            :class="width">
            <slot></slot>
        </div>
    </div>
</template>
