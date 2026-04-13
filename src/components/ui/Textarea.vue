<script setup lang="ts">
import { cn } from '../../lib/utils'

defineProps<{
    modelValue?: string | number
    placeholder?: string
    rows?: number | string
    error?: boolean
    success?: boolean
    disabled?: boolean
}>()

const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <div class="relative w-full">
      <textarea
        :value="modelValue"
        @input="emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)"
        :placeholder="placeholder"
        :rows="Number(rows) || 4"
        :disabled="disabled"
        :class="cn(
          'w-full px-4 py-3 bg-[#f0f2f5] border border-transparent rounded-lg text-[15px] font-normal transition-all placeholder-[#8D949E] resize-y',
          'focus:bg-white focus:border-[#0866FF] focus:outline-none focus:shadow-sm focus:ring-4 focus:ring-[#0866FF]/20',
          error ? 'border-[#E41E3F] focus:border-[#E41E3F] focus:ring-[#E41E3F]/20' : '',
          success ? 'border-[#2FA14A] focus:border-[#2FA14A] focus:ring-[#2FA14A]/20' : '',
          disabled ? 'opacity-50 cursor-not-allowed select-none' : '',
          $attrs.class
        )"
      ></textarea>
  </div>
</template>
