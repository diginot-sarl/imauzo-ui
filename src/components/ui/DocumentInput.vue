<script setup lang="ts">
import { ref, computed } from 'vue'
import { UploadCloud, File as FileIcon, X } from 'lucide-vue-next'

interface Props {
    modelValue?: File | null
    label?: string
    accept?: string
    error?: string
    hint?: string
    disabled?: boolean
    required?: boolean
    id?: string
    maxSizeMB?: number
}

const props = withDefaults(defineProps<Props>(), {
    disabled: false,
    required: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: File | null]
    'error': [msg: string]
}>()

const localId = computed(() => props.id || `doc-upload-${Math.random().toString(36).substring(2, 9)}`)
const isDragging = ref(false)
const fileInput = ref<HTMLInputElement | null>(null)

const sizeError = ref('')

const handleFile = (file: File) => {
    sizeError.value = ''
    if (props.maxSizeMB && file.size > props.maxSizeMB * 1024 * 1024) {
        const err = `La taille du fichier dépasse ${props.maxSizeMB} MB.`
        sizeError.value = err
        emit('error', err)
        return
    }
    emit('update:modelValue', file)
}

const onDrop = (e: DragEvent) => {
    isDragging.value = false
    if (props.disabled) return
    if (e.dataTransfer?.files && e.dataTransfer.files.length > 0) {
        handleFile(e.dataTransfer.files[0])
    }
}

const onFileChange = (e: Event) => {
    const target = e.target as HTMLInputElement
    if (target.files && target.files.length > 0) {
        handleFile(target.files[0])
    }
}

const removeFile = () => {
    emit('update:modelValue', null)
    if (fileInput.value) {
        fileInput.value.value = ''
    }
}

const byteToMB = (bytes: number) => {
    return (bytes / (1024 * 1024)).toFixed(2)
}
</script>

<template>
    <div class="form-control w-full">
        <label v-if="label" class="label pb-1 pt-0">
            <span class="label-text font-medium text-[#050505]">
                {{ label }}
                <span v-if="required" class="text-error ml-1">*</span>
            </span>
        </label>

        <div class="relative flex flex-col items-center justify-center w-full h-32 border-2 border-dashed rounded-lg transition-colors overflow-hidden"
            :class="[
                isDragging ? 'border-[#0866FF] bg-[#0866FF]/5' : 'border-[#CED0D4] bg-[#F0F2F5]',
                error || sizeError ? 'border-error bg-error/5' : '',
                disabled ? 'opacity-50 cursor-not-allowed border-[#CED0D4]' : 'hover:bg-[#E4E6EB] cursor-pointer'
            ]" @dragover.prevent="!disabled && (isDragging = true)" @dragleave.prevent="isDragging = false"
            @drop.prevent="onDrop" @click="!disabled && fileInput?.click()">
            <input ref="fileInput" :id="localId" type="file" :accept="accept" class="hidden" @change="onFileChange"
                :disabled="disabled" />

            <div v-if="!modelValue"
                class="flex flex-col items-center justify-center pt-5 pb-6 pointer-events-none text-center px-4">
                <UploadCloud class="w-8 h-8 mb-3 text-[#65676B]" :class="{ 'text-[#0866FF]': isDragging }" />
                <p class="mb-1 text-sm text-[#050505] font-medium">
                    Cliquez ou glissez un document ici
                </p>
                <p class="text-xs text-[#65676B]">
                    <span v-if="accept">Formats supportés: {{ accept }}</span>
                    <span v-if="maxSizeMB"> (Max. {{ maxSizeMB }} MB)</span>
                </p>
            </div>

            <div v-else class="w-full h-full flex items-center bg-white p-4 justify-between" @click.stop>
                <div class="flex items-center space-x-3 overflow-hidden">
                    <div class="w-10 h-10 bg-[#E4E6EB] rounded-md flex items-center justify-center flex-shrink-0">
                        <FileIcon class="w-5 h-5 text-[#65676B]" />
                    </div>
                    <div class="flex flex-col overflow-hidden">
                        <span class="text-sm font-medium text-[#050505] truncate max-w-[200px] sm:max-w-xs">{{
                            modelValue.name }}</span>
                        <span class="text-xs text-[#65676B]">{{ byteToMB(modelValue.size) }} MB</span>
                    </div>
                </div>

                <button @click="removeFile"
                    class="w-8 h-8 rounded-full flex items-center justify-center bg-[#F0F2F5] hover:bg-[#D8DADF] transition-colors"
                    title="Supprimer">
                    <X class="w-4 h-4 text-[#050505]" />
                </button>
            </div>
        </div>

        <label v-if="error || sizeError || hint" class="label pt-1 pb-0">
            <span v-if="error || sizeError" class="label-text-alt text-error font-medium">{{ error || sizeError
                }}</span>
            <span v-else-if="hint" class="label-text-alt fb-text-secondary">{{ hint }}</span>
        </label>
    </div>
</template>
