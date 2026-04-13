<script setup lang="ts">
import { computed } from 'vue'

interface Props {
    modelValue?: string | number | boolean
    value: string | number | boolean
    label?: string
    hint?: string
    disabled?: boolean
    id?: string
    name: string
}

const props = withDefaults(defineProps<Props>(), {
    disabled: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: string | number | boolean]
}>()

const localId = computed(() => props.id || `radio-${Math.random().toString(36).substring(2, 9)}`)

const isChecked = computed(() => props.modelValue === props.value)
</script>

<template>
    <div class="form-control" :class="{ 'opacity-50': disabled }">
        <label class="cursor-pointer label justify-start gap-3 py-1">
            <input :id="localId" type="radio" :name="name" :value="value" :checked="isChecked"
                @change="emit('update:modelValue', value)" :disabled="disabled"
                class="radio radio-primary border-[#CED0D4] h-5 w-5" />
            <div v-if="label || hint" class="flex flex-col">
                <span v-if="label" class="label-text text-[#050505] font-medium leading-tight select-none">{{ label
                    }}</span>
                <span v-if="hint" class="label-text-alt text-[#65676B] select-none mt-0.5">{{ hint }}</span>
            </div>
        </label>
    </div>
</template>
