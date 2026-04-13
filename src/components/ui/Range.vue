<script setup lang="ts">
import { cn } from '../../lib/utils'

defineProps<{
    modelValue: number | string
    min?: number | string
    max?: number | string
    step?: number | string
    color?: 'primary' | 'secondary' | 'accent' | 'success' | 'warning' | 'error'
    size?: 'xs' | 'sm' | 'md' | 'lg'
}>()

const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <input 
      type="range" 
      :min="min || 0" 
      :max="max || 100" 
      :step="step || 1"
      :value="modelValue"
      @input="emit('update:modelValue', Number(($event.target as HTMLInputElement).value))"
      :class="cn(
          'range', 
          color ? `range-${color}` : 'range-primary',
          size ? `range-${size}` : 'range-md',
          $attrs.class
      )"
  />
</template>
