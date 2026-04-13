<script setup lang="ts">
interface Props {
    icon?: any
    badge?: string | number
    pinned?: boolean
}

const props = defineProps<Props>()
</script>

<template>
    <button
        class="btn btn-ghost btn-circle relative flex items-center justify-center text-[#65676B] hover:bg-[#F0F2F5] transition-colors">
        <component v-if="icon" :is="icon" class="w-6 h-6" />
        <slot v-else></slot>
        <div v-if="badge"
            class="absolute top-1 right-1 badge badge-error badge-sm text-white px-1.5 min-w-[1.25rem] h-5">
            {{ badge }}
        </div>
    </button>
</template>
