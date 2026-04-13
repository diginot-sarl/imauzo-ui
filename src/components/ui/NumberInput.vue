<script setup lang="ts">
import { computed } from 'vue'

interface Props {
    modelValue?: number | null
    label?: string
    placeholder?: string
    min?: number
    max?: number
    step?: number
    error?: string
    hint?: string
    disabled?: boolean
    required?: boolean
    id?: string
}

const props = withDefaults(defineProps<Props>(), {
    placeholder: '',
    disabled: false,
    required: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: number | null]
}>()

const localId = computed(() => props.id || `number-input-${Math.random().toString(36).substring(2, 9)}`)

const onInput = (e: Event) => {
    const target = e.target as HTMLInputElement
    const value = target.value
    emit('update:modelValue', value === '' ? null : Number(value))
}
</script>

<template>
    <div class="form-control w-full">
        <label v-if="label" :for="localId" class="label pb-1 pt-0">
            <span class="label-text font-medium text-[#050505]">
                {{ label }}
                <span v-if="required" class="text-error ml-1">*</span>
            </span>
        </label>
        <input :id="localId" type="number" :placeholder="placeholder" :value="modelValue" :min="min" :max="max"
            :step="step" @input="onInput" :disabled="disabled"
            class="block w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[#050505] placeholder:text-[#8D949E] px-3 rounded-lg h-11 focus:outline-none shadow-none [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-inner-spin-button]:m-0"
            :class="[
                error ? 'border-[#E41E3F] focus:border-[#E41E3F] focus:ring-4 focus:ring-[#E41E3F]/20 bg-white' : 'focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20',
                disabled ? 'opacity-50 cursor-not-allowed' : ''
            ]" />
        <label v-if="error || hint" class="label pt-1 pb-0">
            <span v-if="error" class="label-text-alt text-error font-medium">{{ error }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>

<style scoped>
/* Hide the arrows for number inputs to look cleaner */
.input-number-clean::-webkit-outer-spin-button,
.input-number-clean::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

.input-number-clean {
    -moz-appearance: textfield;
}
</style>
