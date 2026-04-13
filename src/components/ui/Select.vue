<script setup lang="ts">
import { computed } from 'vue'

interface Option {
    label: string
    value: string | number
    disabled?: boolean
}

interface Props {
    modelValue?: string | number | null
    options: Option[]
    label?: string
    placeholder?: string
    error?: string
    hint?: string
    disabled?: boolean
    required?: boolean
    id?: string
}

const props = withDefaults(defineProps<Props>(), {
    placeholder: 'Sélectionner...',
    disabled: false,
    required: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: string | number | null]
}>()

const localId = computed(() => props.id || `select-${Math.random().toString(36).substring(2, 9)}`)
</script>

<template>
    <div class="form-control w-full">
        <label v-if="label" :for="localId" class="label pb-1 pt-0">
            <span class="label-text font-medium text-[#050505]">
                {{ label }}
                <span v-if="required" class="text-error ml-1">*</span>
            </span>
        </label>

        <select :id="localId" :value="modelValue"
            @change="emit('update:modelValue', ($event.target as HTMLSelectElement).value)" :disabled="disabled"
            class="select w-full bg-[#F0F2F5] border border-transparent focus:border-[#0866FF] focus:bg-white focus:outline-none transition-colors text-[#050505] h-[40px] px-3 rounded-md min-h-[40px]"
            :class="[
                error ? 'border-error focus:border-error bg-white' : '',
                disabled ? 'opacity-50 cursor-not-allowed' : '',
                !modelValue ? 'text-[#65676B]' : ''
            ]">
            <option disabled value="" v-if="placeholder">{{ placeholder }}</option>
            <option v-for="opt in options" :key="opt.value" :value="opt.value" :disabled="opt.disabled">
                {{ opt.label }}
            </option>
        </select>

        <label v-if="error || hint" class="label pt-1 pb-0">
            <span v-if="error" class="label-text-alt text-error font-medium">{{ error }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>
