<script setup lang="ts">
import { computed } from 'vue'

interface Props {
    modelValue?: boolean
    label?: string
    hint?: string
    disabled?: boolean
    id?: string
}

const props = withDefaults(defineProps<Props>(), {
    modelValue: false,
    disabled: false,
})

const emit = defineEmits<{
    'update:modelValue': [value: boolean]
}>()

const localId = computed(() => props.id || `toggle-${Math.random().toString(36).substring(2, 9)}`)
</script>

<template>
    <div class="form-control" :class="{ 'opacity-50': disabled }">
        <label class="cursor-pointer label justify-start gap-3 py-1">
            <input :id="localId" type="checkbox" :checked="modelValue"
                @change="emit('update:modelValue', ($event.target as HTMLInputElement).checked)" :disabled="disabled"
                class="toggle toggle-primary bg-[#CED0D4] hover:bg-[#BCC0C4] border-transparent" />
            <div v-if="label || hint" class="flex flex-col">
                <span v-if="label" class="label-text text-[#050505] font-medium leading-tight select-none">{{ label
                    }}</span>
                <span v-if="hint" class="label-text-alt text-[#65676B] select-none mt-0.5">{{ hint }}</span>
            </div>
        </label>
    </div>
</template>

<style scoped>
/* Specific tweak for unselected toggle color closely matching FB gray */
.toggle:not(:checked) {
    --tglbg: white;
    background-color: #CED0D4;
}

.toggle:not(:checked):hover {
    background-color: #BCC0C4;
}
</style>
