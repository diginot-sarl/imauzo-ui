<script setup lang="ts">
import { cn } from '../../lib/utils'
import Heading from './Heading.vue'
import Text from './Text.vue'
import { ArrowLeft } from 'lucide-vue-next'

interface Props {
    title: string
    subtitle?: string
    showBack?: boolean
    class?: any
}

defineProps<Props>()
defineEmits(['back'])
</script>

<template>
    <div :class="cn('flex flex-col sm:flex-row sm:items-center justify-between gap-4 w-full', $props.class)">
        <div class="flex items-start sm:items-center gap-3">
            <button v-if="showBack" @click="$emit('back')"
                class="mt-1 sm:mt-0 p-1.5 rounded-full hover:bg-black/5 text-[#050505] transition-colors shrink-0"
                aria-label="Retour">
                <ArrowLeft class="w-5 h-5" />
            </button>
            <div>
                <Heading level="2" class="leading-tight">{{ title }}</Heading>
                <Text v-if="subtitle" variant="secondary" size="sm" class="mt-0.5">{{ subtitle }}</Text>
            </div>
        </div>

        <div v-if="$slots.actions" class="flex items-center gap-3 shrink-0">
            <slot name="actions" />
        </div>
    </div>
</template>
