<script setup lang="ts">
import { AlertCircle } from 'lucide-vue-next'

interface Props {
    message: string
    actionLabel?: string
    show?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    show: false
})

const emit = defineEmits<{
    'action': []
    'close': []
}>()
</script>

<template>
    <transition name="toast-slide">
        <div v-if="show" class="fixed bottom-4 left-1/2 -translate-x-1/2 w-[90%] max-w-[400px] z-[9999]">
            <div
                class="bg-[#323436] text-white rounded-lg shadow-lg px-4 py-3 flex items-center justify-between gap-4 w-full">
                <!-- Message text container (flex-1 lets it grow and text-left aligns appropriately) -->
                <span class="text-[14px] leading-snug font-medium flex-1 text-left">{{ message }}</span>

                <!-- Actions container (shrink-0 prevents it from squashing) -->
                <div class="flex items-center gap-3 shrink-0">
                    <button v-if="actionLabel" class="text-[#4596F6] font-semibold text-[14px] hover:underline"
                        @click="emit('action')">
                        {{ actionLabel }}
                    </button>
                    <button @click="emit('close')" class="hover:bg-white/10 rounded-full p-1 transition-colors"
                        aria-label="Fermer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-[#B0B3B8]" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </transition>
</template>

<style scoped>
.toast-slide-enter-active,
.toast-slide-leave-active {
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.toast-slide-enter-from,
.toast-slide-leave-to {
    opacity: 0;
    transform: translate(-50%, 20px);
}
</style>
