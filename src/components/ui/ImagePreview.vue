<script setup lang="ts">
import DocumentPreview from './DocumentPreview.vue'

interface Props {
    modelValue: boolean
    title: string
    url: string
}

defineProps<Props>()
const emit = defineEmits(['update:modelValue', 'download', 'share', 'print'])
</script>

<template>
    <DocumentPreview :modelValue="modelValue" @update:modelValue="emit('update:modelValue', $event)" :title="title"
        :url="url" type="image" @download="emit('download')" @share="emit('share')" @print="emit('print')" />
</template>
