<script setup lang="ts">
interface Props {
    label: string
    active?: boolean
    completed?: boolean
}

const props = defineProps<Props>()
</script>

<template>
    <li class="step" :data-content="completed ? '✓' : ''" :class="[
        active || completed ? 'step-primary text-[#050505]' : 'text-[#65676B]'
    ]">
        <div class="mt-2 text-[13px] font-semibold tracking-wide">
            {{ label }}
        </div>
    </li>
</template>

<style scoped>
/* Redéfinir la couleur du step actif pour coller au Meta Blue */
:deep(.step-primary:before),
:deep(.step-primary:after) {
    background-color: #0866FF !important;
    color: white !important;
}

:deep(.step-primary[data-content="✓"]:before) {
    background-color: #0866FF !important;
}
</style>
