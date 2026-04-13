<script setup lang="ts">
import { ref, computed } from 'vue'
import { X } from 'lucide-vue-next'

interface Props {
    modelValue?: string[]
    label?: string
    placeholder?: string
    error?: string
    hint?: string
    disabled?: boolean
    required?: boolean
    id?: string
}

const props = withDefaults(defineProps<Props>(), {
    modelValue: () => [],
    placeholder: 'Ajouter un tag...',
    disabled: false,
    required: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: string[]]
}>()

const localId = computed(() => props.id || `tag-input-${Math.random().toString(36).substring(2, 9)}`)
const inputValue = ref('')

const isFocused = ref(false)

const addTag = () => {
    const val = inputValue.value.trim()
    if (val && !props.modelValue.includes(val)) {
        emit('update:modelValue', [...props.modelValue, val])
    }
    inputValue.value = ''
}

const removeTag = (tag: string) => {
    if (props.disabled) return
    emit('update:modelValue', props.modelValue.filter(t => t !== tag))
}

const handleKeydown = (e: KeyboardEvent) => {
    if (e.key === 'Enter' || e.key === ',') {
        e.preventDefault()
        addTag()
    } else if (e.key === 'Backspace' && inputValue.value === '' && props.modelValue.length > 0) {
        // Remove the last tag when pressing backspace on empty input
        const newTags = [...props.modelValue]
        newTags.pop()
        emit('update:modelValue', newTags)
    }
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

        <div class="flex flex-wrap items-center gap-2 bg-[#F0F2F5] border transition-colors min-h-[40px] px-2 py-1.5 rounded-md cursor-text"
            :class="[
                error ? 'border-error bg-white' : 'border-transparent hover:bg-[#E4E6EB]',
                isFocused && !error ? 'bg-white border-[#0866FF] ring-2 ring-[#0866FF]/20' : '',
                disabled ? 'opacity-50 cursor-not-allowed pointer-events-none' : ''
            ]" @click="$refs.inputRef && ($refs.inputRef as HTMLInputElement).focus()">
            <!-- Tags -->
            <div v-for="tag in modelValue" :key="tag"
                class="inline-flex items-center bg-[#1877F2]/10 text-[#0866FF] text-[13px] font-medium px-2 py-1 rounded-sm">
                <span>{{ tag }}</span>
                <div @click.stop="removeTag(tag)"
                    class="ml-1 hover:bg-[#0866FF]/20 rounded-full p-0.5 transition-colors cursor-pointer">
                    <X class="w-3 h-3" />
                </div>
            </div>

            <!-- Input -->
            <input ref="inputRef" :id="localId" type="text" :placeholder="modelValue.length === 0 ? placeholder : ''"
                v-model="inputValue" @keydown="handleKeydown" @blur="isFocused = false; addTag()"
                @focus="isFocused = true" :disabled="disabled"
                class="flex-1 bg-transparent min-w-[60px] outline-none text-[#050505] placeholder:text-[#65676B] text-[15px] p-0 border-none m-0" />
        </div>

        <label v-if="error || hint" class="label pt-1 pb-0">
            <span v-if="error" class="label-text-alt text-error font-medium">{{ error }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>
