<script setup lang="ts">
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { ChevronDown, Check } from 'lucide-vue-next'

export interface MegaOption {
    value: string | number
    label: string
    description?: string
    icon?: any
}

interface Props {
    modelValue?: string | number | null
    options: MegaOption[]
    label?: string
    placeholder?: string
    error?: string
    hint?: string
    disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    placeholder: 'Sélectionner une option',
    disabled: false
})

const emit = defineEmits<{
    'update:modelValue': [value: string | number | null]
}>()

const isOpen = ref(false)
const selectRef = ref<HTMLElement | null>(null)

const selectedOption = computed(() => {
    return props.options.find(opt => opt.value === props.modelValue)
})

const toggleOpen = () => {
    if (props.disabled) return
    isOpen.value = !isOpen.value
}

const selectOption = (opt: MegaOption) => {
    emit('update:modelValue', opt.value)
    isOpen.value = false
}

// Click outside handler
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
            class="w-full flex items-center justify-between bg-[#F0F2F5] border border-transparent hover:bg-[#E4E6EB] transition-colors h-auto min-h-[44px] px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-[#0866FF]/20 focus:border-[#0866FF] text-left"
            :class="[
                error ? 'border-error focus:border-error bg-white' : '',
                disabled ? 'opacity-50 cursor-not-allowed' : '',
                isOpen ? 'bg-white border-[#0866FF]' : ''
            ]">
            <div v-if="selectedOption" class="flex flex-col">
                <span class="text-[#050505] font-medium leading-tight truncate">{{ selectedOption.label }}</span>
                <span v-if="selectedOption.description" class="text-xs text-[#65676B] truncate">{{
                    selectedOption.description }}</span>
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
                    <button type="button"
                        class="w-full flex items-center text-left px-3 py-2 hover:bg-[#F0F2F5] transition-colors"
                        @click="selectOption(opt)">
                        <div class="mr-3 text-[#65676B] flex-shrink-0" v-if="opt.icon">
                            <component :is="opt.icon" class="w-5 h-5" />
                        </div>

                        <div class="flex-1 min-w-0">
                            <div class="text-[#050505] font-medium truncate"
                                :class="{ 'text-[#0866FF]': modelValue === opt.value }">
                                {{ opt.label }}
                            </div>
                            <div v-if="opt.description" class="text-xs text-[#65676B] truncate">
                                {{ opt.description }}
                            </div>
                        </div>

                        <div class="w-5 flex justify-end flex-shrink-0">
                            <Check v-if="modelValue === opt.value" class="w-4 h-4 text-[#0866FF]" />
                        </div>
                    </button>
                </li>
            </ul>
        </div>

        <label v-if="error || hint" class="label pt-1 pb-0">
            <span v-if="error" class="label-text-alt text-error font-medium">{{ error }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>
