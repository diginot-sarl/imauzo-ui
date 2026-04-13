<script setup lang="ts">
interface Props {
    value: number // Percentage 0-100
    size?: string // CSS size, e.g., '4rem'
    thickness?: string // CSS thickness, e.g., '4px'
    color?: string // Tailwind color class or hex
}

const props = withDefaults(defineProps<Props>(), {
    size: '3rem',
    thickness: '3px',
    color: '#0866FF'
})
</script>

<template>
    <div class="radial-progress font-semibold text-[13px]" :style="{
        '--value': value,
        '--size': size,
        '--thickness': thickness,
        'color': color
    }" role="progressbar" :aria-valuenow="value" aria-valuemin="0" aria-valuemax="100">
        <slot>{{ value }}%</slot>
    </div>
</template>

<style scoped>
/* Ensure the background ring is subtle Facebook-like gray */
.radial-progress {
    background-color: #E4E6EB;
}

.radial-progress::-moz-progress-bar {
    background-color: transparent;
}
</style>
