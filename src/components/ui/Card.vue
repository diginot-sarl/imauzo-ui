<script setup lang="ts">
import { cn } from '@/lib/utils'

interface CardProps {
    class?: string
}

const props = defineProps<CardProps>()
</script>

<template>
    <div :class="cn('fb-card', props.class)">
        <div v-if="$slots.header" class="border-b border-[#CED0D4] p-4">
            <slot name="header" />
        </div>

        <div class="p-4">
            <slot />
        </div>

        <div v-if="$slots.footer" class="border-t border-[#CED0D4] bg-[#F0F2F5]/50 p-4 rounded-b-[7px]">
            <slot name="footer" />
        </div>
    </div>
</template>
