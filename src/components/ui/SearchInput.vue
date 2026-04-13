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
    <div class="relative w-full">
        <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-[#65676B]">
            <Search class="w-4 h-4" />
        </div>
        <input type="text" :placeholder="placeholder" :value="modelValue" @input="onInput" :disabled="disabled"
            class="input w-full bg-[#F0F2F5] border border-transparent focus:border-[#0866FF] focus:bg-white focus:outline-none transition-colors text-[#050505] placeholder:text-[#65676B] h-[40px] pl-10 pr-10 rounded-full"
            :class="{ 'opacity-50 cursor-not-allowed': disabled }" />
        <button v-show="modelValue" type="button" @click="clearSearch"
            class="absolute inset-y-0 right-0 flex items-center pr-3 group">
            <div
                class="w-4 h-4 rounded-full bg-[#CED0D4] group-hover:bg-[#65676B] flex items-center justify-center transition-colors">
                <X class="w-3 h-3 text-white" />
            </div>
        </button>
    </div>
</template>
