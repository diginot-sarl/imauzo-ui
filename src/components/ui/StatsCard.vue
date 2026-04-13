<script setup lang="ts">
import Card from './Card.vue'
import { TrendingUp, TrendingDown, Minus } from 'lucide-vue-next'

interface Props {
    label: string
    value: string | number
    trend?: number
    icon?: any // Lucide icon component
    trendLabel?: string
}

const props = defineProps<Props>()
</script>

<template>
    <Card class="rounded-xl border-[#CED0D4]">
        <div class="flex items-start justify-between">
            <div class="flex gap-2 items-center">
                <div v-if="icon" class="p-2 bg-transparent text-[#65676B] flex items-center justify-center mr-1">
                    <component :is="icon" class="w-5 h-5" />
                </div>
                <div>
                    <h3 class="text-[20px] font-bold text-[#050505] truncate">{{ value }}</h3>
                    <p class="fb-text-secondary text-[15px] font-normal mt-0.5">{{ label }}</p>
                </div>
            </div>
        </div>

        <div v-if="trend !== undefined" class="mt-4 flex items-center text-sm">
            <div :class="[
                'flex items-center gap-1 font-medium',
                trend > 0 ? 'text-success' : trend < 0 ? 'text-error' : 'text-[#65676B]'
            ]">
                <TrendingUp v-if="trend > 0" class="w-4 h-4" />
                <TrendingDown v-else-if="trend < 0" class="w-4 h-4" />
                <Minus v-else class="w-4 h-4" />

                <span>{{ Math.abs(trend) }}%</span>
            </div>
            <span v-if="trendLabel" class="fb-text-secondary ml-2 truncate">
                {{ trendLabel }}
            </span>
        </div>
    </Card>
</template>
