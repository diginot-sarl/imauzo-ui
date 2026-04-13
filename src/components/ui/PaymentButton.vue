<script setup lang="ts">
import { Lock, ArrowRight } from 'lucide-vue-next'
import Button from './Button.vue'
import { cn } from '../../lib/utils'

interface Props {
    amount: string
    currency?: string
    loading?: boolean
    showArrow?: boolean
    class?: any
}

withDefaults(defineProps<Props>(), {
    currency: '$',
    showArrow: true
})
</script>

<template>
    <Button variant="primary" size="lg" :loading="loading" :class="cn(
        'w-full sm:w-auto min-w-full sm:min-w-[320px] shadow-[0_4px_12px_rgba(8,102,255,0.25)] hover:shadow-[0_6px_16px_rgba(8,102,255,0.3)] transition-all h-[52px]',
        $props.class
    )">
        <div class="flex items-center justify-between w-full relative">
            <Lock class="w-[18px] h-[18px] opacity-70 shrink-0" />

            <span class="font-bold flex-1 text-center tracking-wide text-[16px]">
                Payer {{ amount }} {{ currency }}
            </span>

            <ArrowRight v-if="showArrow"
                class="w-[18px] h-[18px] shrink-0 group-hover:translate-x-1 transition-transform duration-300" />
            <div v-else class="w-[18px] h-[18px] shrink-0"></div> <!-- Placeholder to keep text centered -->
        </div>
    </Button>
</template>
