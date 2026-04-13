<script setup lang="ts">
import { computed, useSlots } from 'vue'
import { cn } from '../../lib/utils'

interface Props {
    modelValue?: string | number
    label?: string
    placeholder?: string
    type?: 'text' | 'email' | 'password' | 'tel' | 'url' | 'search'
    error?: string | boolean
    success?: string | boolean
    hint?: string
    disabled?: boolean
    required?: boolean
    id?: string
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    type: 'text',
    placeholder: '',
    disabled: false,
    required: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: string | number]
}>()

const localId = computed(() => props.id || `text-input-${Math.random().toString(36).substring(2, 9)}`)
const slots = useSlots()
</script>

<template>
    <div class="form-control w-full relative">
        <label v-if="label" :for="localId" class="label pb-1.5 pt-0 px-0">
            <span class="label-text font-semibold text-[#050505] text-[13px] tracking-wide inline-flex items-center">
                {{ label }}
                <span v-if="required" class="text-[#E41E3F] ml-1 text-sm">*</span>
            </span>
        </label>
        
        <div class="relative flex items-center w-full">
            <!-- Prefix Icon Slot -->
            <div v-if="slots.prefix" class="absolute left-3 text-[#65676B] pointer-events-none z-10">
                <slot name="prefix"></slot>
            </div>
            
            <input :id="localId" :type="type" :placeholder="placeholder" :value="modelValue"
                @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)" :disabled="disabled"
                :class="cn(
                  'block appearance-none w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[15px] rounded-lg h-11 focus:outline-none shadow-none',
                  slots.prefix ? 'pl-10' : 'pl-4',
                  slots.suffix ? 'pr-10' : 'pr-4',
                  error ? 'border-[#E41E3F] focus:border-[#E41E3F] focus:ring-4 focus:ring-[#E41E3F]/20 bg-white' : '',
                  success ? 'border-[#2FA14A] focus:border-[#2FA14A] focus:ring-4 focus:ring-[#2FA14A]/20 bg-white' : '',
                  (!error && !success) ? 'focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20' : '',
                  disabled ? 'opacity-50 cursor-not-allowed select-none' : '',
                  props.class
                )" />
                
            <!-- Suffix Icon Slot -->
            <div v-if="slots.suffix" class="absolute right-3 text-[#65676B] pointer-events-none z-10">
                <slot name="suffix"></slot>
            </div>
        </div>
        
        <!-- Validation/Hint Text -->
        <label v-if="error || success || hint" class="label pt-1.5 pb-0 px-0">
            <span v-if="error && typeof error === 'string'" class="label-text-alt text-[#E41E3F] font-medium text-[13px] tracking-wide">{{ error }}</span>
            <span v-else-if="success && typeof success === 'string'" class="label-text-alt text-[#2FA14A] font-medium text-[13px] tracking-wide">{{ success }}</span>
            <span v-else-if="hint" class="label-text-alt text-[#65676B] text-[13px]">{{ hint }}</span>
        </label>
    </div>
</template>
