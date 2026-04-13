<script setup lang="ts">
import { X } from 'lucide-vue-next'

interface Props {
    modelValue: boolean
    title?: string
    width?: 'sm' | 'md' | 'lg' | 'xl' | 'full'
}

const props = withDefaults(defineProps<Props>(), {
    modelValue: false,
    width: 'md',
})

const emit = defineEmits<{
    'update:modelValue': [value: boolean]
    close: []
}>()

const close = () => {
    emit('update:modelValue', false)
    emit('close')
}

// DaisyUI requires adding modal-open class to the modal dialog
</script>

<template>
    <dialog class="modal modal-bottom sm:modal-middle" :class="{ 'modal-open': modelValue }">
        <div class="modal-box p-0 shadow-xl overflow-hidden rounded-t-xl sm:rounded-xl" :class="{
            'max-w-sm': width === 'sm',
            'max-w-md': width === 'md',
            'max-w-lg': width === 'lg',
            'max-w-2xl': width === 'xl',
            'max-w-screen-xl': width === 'full',
        }">
            <!-- Header -->
            <div class="flex items-center justify-center p-4 border-b border-[#CED0D4] relative min-h-[60px]">
                <h3 class="text-[20px] font-bold text-[#050505] m-0">
                    {{ title }}
                    <slot name="title" v-if="!title" />
                </h3>
                <button @click="close"
                    class="absolute right-4 top-1/2 -translate-y-1/2 w-[36px] h-[36px] rounded-full bg-[#E4E6EB] hover:bg-[#D8DADF] flex items-center justify-center transition-colors text-[#65676B]">
                    <X class="w-5 h-5" stroke-width="2.5" />
                </button>
            </div>

            <!-- Content -->
            <div class="p-4 max-h-[70vh] overflow-y-auto">
                <slot />
            </div>

            <!-- Footer -->
            <div v-if="$slots.footer" class="p-4 border-t border-base-300 flex justify-end gap-2 bg-base-100">
                <slot name="footer" />
            </div>
        </div>

        <!-- Backdrop -->
        <form method="dialog" class="modal-backdrop" @click.prevent="close">
            <button>close</button>
        </form>
    </dialog>
</template>
