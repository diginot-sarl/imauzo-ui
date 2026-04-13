<script setup lang="ts">
import { computed } from 'vue'
import { Search, X } from 'lucide-vue-next'

interface Props {
    modelValue?: string
    placeholder?: string
    disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    modelValue: '',
    placeholder: 'Rechercher...',
    disabled: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: string]
    search: [value: string]
    clear: []
}>()

const onInput = (event: Event) => {
    const value = (event.target as HTMLInputElement).value
    emit('update:modelValue', value)
    emit('search', value)
}

const clearSearch = () => {
    emit('update:modelValue', '')
    emit('search', '')
    emit('clear')
}
</script>

<template>
    <div class="relative flex items-center w-full">
        <div class="absolute left-3 text-[#65676B] pointer-events-none z-10 flex items-center justify-center">
            <Search class="w-[18px] h-[18px]" />
        </div>
        
        <input type="text" :placeholder="placeholder" :value="modelValue" @input="onInput" :disabled="disabled"
            class="block appearance-none w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[15px] pl-10 pr-10 rounded-full h-10 focus:outline-none focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20 shadow-none"
            :class="{ 'opacity-50 cursor-not-allowed select-none': disabled }" />
            
        <button v-show="modelValue" type="button" @click="clearSearch"
            class="absolute right-3 flex items-center justify-center group z-10">
            <div class="w-[18px] h-[18px] rounded-full bg-[#CED0D4] group-hover:bg-[#8D949E] flex items-center justify-center transition-colors">
                <X class="w-3 h-3 text-white" />
            </div>
        </button>
    </div>
</template>
