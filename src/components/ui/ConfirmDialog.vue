<script setup lang="ts">
import { cn } from '../../lib/utils'
import Modal from './Modal.vue'
import Button from './Button.vue'
import Text from './Text.vue'
import { AlertTriangle, Info, CheckCircle, XCircle } from 'lucide-vue-next'
import { computed } from 'vue'

interface Props {
    modelValue: boolean
    title: string
    message?: string
    confirmText?: string
    cancelText?: string
    variant?: 'danger' | 'warning' | 'info' | 'success'
    loading?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    confirmText: 'Confirmer',
    cancelText: 'Annuler',
    variant: 'danger',
    loading: false
})

const emit = defineEmits(['update:modelValue', 'confirm', 'cancel'])

const close = () => {
    emit('update:modelValue', false)
    emit('cancel')
}

const confirm = () => {
    emit('confirm')
    // Le parent se chargera de fermer la modale si nécessaire
}

const icons = {
    danger: AlertTriangle,
    warning: AlertTriangle,
    info: Info,
    success: CheckCircle
}

const iconColors = {
    danger: 'text-[#E02636] bg-[#E02636]/10',
    warning: 'text-[#D88A00] bg-[#D88A00]/10',
    info: 'text-[#0866FF] bg-[#0866FF]/10',
    success: 'text-[#2FA14A] bg-[#2FA14A]/10'
}

const buttonVariants = {
    danger: 'danger',
    warning: 'primary', // Peut être jaune/orange selon design
    info: 'primary',
    success: 'primary'
}
</script>

<template>
    <Modal :modelValue="modelValue" @update:modelValue="emit('update:modelValue', $event)" :title="title" maxWidth="sm">
        <div class="flex sm:items-start gap-4 flex-col sm:flex-row">
            <div
                :class="cn('w-12 h-12 shrink-0 rounded-full flex items-center justify-center shrink-0', iconColors[variant])">
                <component :is="icons[variant]" class="w-6 h-6" />
            </div>

            <div class="pt-1">
                <Text class="text-[14px] leading-relaxed">
                    <slot>{{ message }}</slot>
                </Text>
            </div>
        </div>

        <template #footer>
            <div class="flex gap-3 justify-end w-full">
                <Button variant="secondary" @click="close" class="flex-1 sm:flex-none">
                    {{ cancelText }}
                </Button>
                <Button :variant="buttonVariants[variant] as any" :loading="loading" @click="confirm"
                    class="flex-1 sm:flex-none">
                    {{ confirmText }}
                </Button>
            </div>
        </template>
    </Modal>
</template>
