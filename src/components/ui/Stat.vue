<script setup lang="ts">
import { cn } from '../../lib/utils'

defineProps<{
   title: string
   value: string | number
   description?: string
   icon?: any
}>()
</script>

<template>
  <div :class="cn('stat px-6 py-5 rounded-xl bg-white border border-[#CED0D4] shadow-sm', $attrs.class)">
    <div v-if="icon" class="stat-figure text-[#0866FF] opacity-80">
      <component :is="icon" class="w-8 h-8" />
    </div>
    <div class="stat-title text-[#65676B] text-[13px] font-semibold tracking-wide">{{ title }}</div>
    <div class="stat-value text-[#050505] text-3xl font-bold mt-1 tracking-tight">{{ value }}</div>
    <div v-if="description" class="stat-desc text-[#8D949E] font-medium mt-2">{{ description }}</div>
  </div>
</template>
