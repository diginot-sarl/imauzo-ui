<script setup lang="ts">
import { computed } from 'vue'

interface Props {
    modelValue?: File | null
    label?: string
    accept?: string
    error?: string
    hint?: string
    disabled?: boolean
    required?: boolean
    id?: string
}

const props = withDefaults(defineProps<Props>(), {
    disabled: false,
    required: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: File | null]
}>()

const localId = computed(() => props.id || `upload-${Math.random().toString(36).substring(2, 9)}`)

const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement
    if (target.files && target.files.length > 0) {
        emit('update:modelValue', target.files[0])
    } else {
        emit('update:modelValue', null)
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

        <input :id="localId" type="file" :accept="accept" @change="handleFileChange" :disabled="disabled"
            class="file-input file-input-bordered bg-[#F0F2F5] border-transparent focus:border-[#0866FF] w-full text-[#65676B] h-[40px]"
            :class="[
                error ? 'border-error focus:border-error bg-white' : '',
                disabled ? 'opacity-50 cursor-not-allowed' : ''
            ]" />

        <label v-if="error || hint" class="label pt-1 pb-0">
            <span v-if="error" class="label-text-alt text-error font-medium">{{ error }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>

<style scoped>
/* Astuces : DaisyUI v5 utilise des variables, on customise le bouton fichier de base */
:deep(.file-input::file-selector-button) {
    background-color: #E4E6EB;
    border-right: 1px solid #CED0D4;
    color: #050505;
    font-weight: 600;
    text-transform: none;
}

:deep(.file-input:hover::file-selector-button) {
    background-color: #D8DADF;
}
</style>
