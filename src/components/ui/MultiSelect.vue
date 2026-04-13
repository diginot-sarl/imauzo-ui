<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { ChevronDown, Check, X } from 'lucide-vue-next'

export interface MultiOption {
    value: string | number
    label: string
}

interface Props {
    modelValue?: (string | number)[]
    options: MultiOption[]
    label?: string
    placeholder?: string
    error?: string
    hint?: string
    disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    modelValue: () => [],
    placeholder: 'Sélectionner des options',
    disabled: false
})

const emit = defineEmits<{
    'update:modelValue': [value: (string | number)[]]
}>()

const isOpen = ref(false)
const selectRef = ref<HTMLElement | null>(null)

const toggleOpen = () => {
    if (props.disabled) return
    isOpen.value = !isOpen.value
}

const toggleOption = (val: string | number) => {
    const current = [...props.modelValue]
    const idx = current.indexOf(val)
    if (idx === -1) {
        current.push(val)
    } else {
        current.splice(idx, 1)
    }
    emit('update:modelValue', current)
}

const removeOption = (val: string | number, e: Event) => {
    e.stopPropagation()
    const current = [...props.modelValue].filter(v => v !== val)
    emit('update:modelValue', current)
}

const selectedLabels = computed(() => {
    return props.modelValue.map(val => {
        const opt = props.options.find(o => o.value === val)
        return opt ? opt.label : val
    })
})

const handleClickOutside = (event: MouseEvent) => {
    if (selectRef.value && !selectRef.value.contains(event.target as Node)) {
        isOpen.value = false
    }
}

onMounted(() => {
    document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
    <div class="form-control w-full relative" ref="selectRef">
        <label v-if="label" class="label pb-1 pt-0">
            <span class="label-text font-medium text-[#050505]">{{ label }}</span>
        </label>

        <button type="button" @click="toggleOpen" :disabled="disabled"
            class="w-full flex items-center justify-between bg-[#F0F2F5] border border-transparent hover:bg-[#E4E6EB] transition-colors min-h-[44px] px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-[#0866FF]/20 focus:border-[#0866FF] text-left"
            :class="[
                error ? 'border-error focus:border-error bg-white' : '',
                disabled ? 'opacity-50 cursor-not-allowed' : '',
                isOpen ? 'bg-white border-[#0866FF]' : ''
            ]">
            <div v-if="modelValue.length > 0" class="flex flex-wrap gap-1">
                <div v-for="(val, index) in modelValue" :key="val"
                    class="inline-flex items-center bg-[#E4E6EB] text-[#050505] text-[13px] px-2 py-0.5 rounded-sm">
                    <span>{{ selectedLabels[index] }}</span>
                    <div @click="(e) => removeOption(val, e)"
                        class="ml-1 hover:bg-[#CED0D4] rounded-full p-0.5 transition-colors">
                        <X class="w-3 h-3" />
                    </div>
                </div>
            </div>
            <div v-else class="text-[#65676B] truncate">{{ placeholder }}</div>

            <ChevronDown class="w-4 h-4 text-[#65676B] flex-shrink-0 ml-2 transition-transform"
                :class="{ 'rotate-180': isOpen }" />
        </button>

        <div v-if="isOpen"
            class="absolute z-50 w-full mt-1 bg-white border border-[#CED0D4] rounded-lg shadow-md max-h-60 overflow-y-auto"
            :style="{ top: '100%' }">
            <ul class="py-1">
                <li v-for="opt in options" :key="opt.value">
                    <label
                        class="w-full flex items-center cursor-pointer px-3 py-2 hover:bg-[#F0F2F5] transition-colors">
                        <input type="checkbox" :checked="modelValue.includes(opt.value)"
                            @change="toggleOption(opt.value)"
                            class="checkbox checkbox-primary checkbox-sm border-[#CED0D4] rounded-sm" />
                        <span class="ml-3 text-[#050505] font-medium">{{ opt.label }}</span>
                    </label>
                </li>
                <li v-if="options.length === 0">
                    <div class="px-3 py-2 text-[#65676B] text-sm text-center">Aucune option</div>
                </li>
            </ul>
        </div>

        <label v-if="error || hint" class="label pt-1 pb-0">
            <span v-if="error" class="label-text-alt text-error font-medium">{{ error }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>
