<script setup lang="ts">
import { AlertCircle, CheckCircle, Info, AlertTriangle } from 'lucide-vue-next'

interface Props {
    type?: 'info' | 'success' | 'warning' | 'error'
    title?: string
    message?: string
    dismissible?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    type: 'info',
    dismissible: false
})

const emit = defineEmits<{
    'close': []
}>()
</script>

<template>
    <div role="alert" class="alert flex items-start gap-4 p-4 rounded-lg shadow-sm border text-[14px] leading-tight"
        :class="{
            'bg-[#EAF3FF] border-[#EAF3FF]': type === 'info',
            'bg-[#E7F3EB] border-[#E7F3EB]': type === 'success',
            'bg-[#FFF5E5] border-[#FFF5E5]': type === 'warning',
            'bg-[#FDECEE] border-[#FDECEE]': type === 'error'
        }">
        <!-- Icon -->
        <div class="mt-0.5">
            <Info v-if="type === 'info'" class="w-5 h-5 text-[#0866FF]" />
            <CheckCircle v-else-if="type === 'success'" class="w-5 h-5 text-[#2FA14A]" />
            <AlertTriangle v-else-if="type === 'warning'" class="w-5 h-5 text-[#D88A00]" />
            <AlertCircle v-else-if="type === 'error'" class="w-5 h-5 text-[#E02636]" />
        </div>

        <!-- Content -->
        <div class="flex-1">
            <h3 v-if="title" class="font-bold text-[#050505] mb-1">{{ title }}</h3>
            <div class="text-[#050505]">
                <slot>{{ message }}</slot>
            </div>
        </div>

        <!-- Actions / Close -->
        <div class="flex items-center gap-3">
            <slot name="actions"></slot>

            <button v-if="dismissible" @click="emit('close')"
                class="text-[#65676B] hover:text-[#050505] transition-colors p-1" aria-label="Fermer">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
    </div>
</template>
