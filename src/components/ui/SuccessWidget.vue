<script setup lang="ts">
import { CheckCircle } from 'lucide-vue-next'
import { cn } from '../../lib/utils'
import Heading from './Heading.vue'
import Text from './Text.vue'

interface Props {
    title: string
    message?: string
    class?: any
}

defineProps<Props>()
</script>

<template>
    <div
        :class="cn('flex flex-col items-center justify-center text-center p-8 sm:p-10 bg-white rounded-xl shadow-sm border border-[#CED0D4]', $props.class)">
        <div
            class="w-16 h-16 sm:w-20 sm:h-20 bg-[#E7F3EB] text-[#2FA14A] rounded-full flex items-center justify-center mb-5 shrink-0">
            <CheckCircle class="w-8 h-8 sm:w-10 sm:h-10" />
        </div>
        <Heading level="2" class="mb-2 leading-tight text-[#050505]">{{ title }}</Heading>
        <Text variant="secondary" size="md" class="mb-8 max-w-md">{{ message }}</Text>

        <div class="w-full flex flex-col sm:flex-row gap-3 justify-center items-center">
            <slot />
        </div>
    </div>
</template>
