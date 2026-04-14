<script setup lang="ts">
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
      :class="[
          'range', 
          ['primary', 'secondary', 'accent', 'success', 'warning', 'error'].includes(color as string) ? `range-${color}` : 'range-primary',
          ['xs', 'sm', 'md', 'lg'].includes(size as string) ? `range-${size}` : 'range-md',
          $attrs.class
      ]"
  />
</template>
