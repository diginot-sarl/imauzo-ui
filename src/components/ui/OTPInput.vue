<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

const props = defineProps<{
    length?: number
    modelValue?: string
}>()

const emit = defineEmits<{
    (e: 'update:modelValue', value: string): void
    (e: 'complete', value: string): void
}>()

const numInputs = props.length || 6
const digits = ref<string[]>(new Array(numInputs).fill(''))
const inputs = ref<HTMLInputElement[]>([])

// Automatically sync external modelValue if provided
watch(() => props.modelValue, (newVal) => {
    if (newVal && newVal.length <= numInputs) {
        for (let i = 0; i < numInputs; i++) {
            digits.value[i] = newVal[i] || ''
        }
    }
}, { immediate: true })

const handleInput = (e: Event, index: number) => {
    const target = e.target as HTMLInputElement
    const val = target.value
    
    // allow only numbers 
    target.value = val.replace(/[^0-9]/g, '').slice(-1)
    digits.value[index] = target.value

    emitUpdate()

    if (target.value && index < numInputs - 1) {
        inputs.value[index + 1]?.focus()
    }
}

const handleKeydown = (e: KeyboardEvent, index: number) => {
    // Move back on backspace if empty
    if (e.key === 'Backspace') {
        if (!digits.value[index] && index > 0) {
            inputs.value[index - 1]?.focus()
        }
    }
    // Arrow keys navigation
    if (e.key === 'ArrowLeft' && index > 0) {
        inputs.value[index - 1]?.focus()
    }
    if (e.key === 'ArrowRight' && index < numInputs - 1) {
        inputs.value[index + 1]?.focus()
    }
}

const handlePaste = (e: ClipboardEvent) => {
    e.preventDefault()
    const pastedData = e.clipboardData?.getData('text/plain').replace(/[^0-9]/g, '') || ''
    if (!pastedData) return

    for (let i = 0; i < numInputs; i++) {
        if (pastedData[i]) {
            digits.value[i] = pastedData[i]
        }
    }
    
    emitUpdate()
    
    // Focus the next empty input or the last one
    const nextIndex = Math.min(pastedData.length, numInputs - 1)
    nextTick(() => {
        inputs.value[nextIndex]?.focus()
    })
}

const emitUpdate = () => {
    const code = digits.value.join('')
    emit('update:modelValue', code)
    if (code.length === numInputs) {
        emit('complete', code)
    }
}
</script>

<template>
  <div class="flex gap-2 sm:gap-3" dir="ltr">
    <input 
      v-for="(_, index) in numInputs" 
      :key="index"
      :ref="el => { if (el) inputs[index] = el as HTMLInputElement }"
      type="text"
      inputmode="numeric"
      maxlength="1"
      :value="digits[index]"
      @input="handleInput($event, index)"
      @keydown="handleKeydown($event, index)"
      @paste="handlePaste"
      class="w-12 h-12 sm:w-16 sm:h-16 text-center text-2xl font-bold bg-[#F0F2F5] border-2 border-transparent text-[#050505] rounded-xl focus:bg-white focus:border-[#0866FF] focus:outline-none transition-all shadow-none focus:shadow-sm"
    />
  </div>
</template>
