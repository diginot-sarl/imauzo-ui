<script setup lang="ts">
import { Info } from 'lucide-vue-next'

interface Props {
    title?: string
    message?: string
    actionLabel?: string
    icon?: any
}

const props = defineProps<Props>()
const emit = defineEmits<{
    'action': []
}>()
</script>

<template>
    <div
        class="bg-[#FFFFFF] border border-[#CED0D4] rounded-lg p-4 shadow-[0_1px_2px_rgba(0,0,0,0.05)] flex items-start sm:items-center gap-4 flex-col sm:flex-row">
        <!-- Icon Container -->
        <div class="bg-[#F0F2F5] p-2.5 rounded-full shrink-0">
            <component :is="icon || Info" class="w-6 h-6 text-[#050505]" />
        </div>

        <!-- Content -->
        <div class="flex-1">
            <h4 v-if="title" class="font-bold text-[#050505] text-[15px] leading-tight mb-1">{{ title }}</h4>
            <p class="text-[#65676B] text-[13px] sm:text-[14px] leading-snug">
                <slot>{{ message }}</slot>
            </p>
        </div>

        <!-- Call to action -->
        <div v-if="actionLabel" class="shrink-0 w-full sm:w-auto mt-2 sm:mt-0">
            <button @click="emit('action')"
                class="w-full sm:w-auto bg-[#EAF3FF] text-[#0866FF] hover:bg-[#dcebfe] transition-colors border-none px-4 py-2 rounded-md font-semibold text-[14px]">
                {{ actionLabel }}
            </button>
        </div>
    </div>
</template>
