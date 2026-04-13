<script setup lang="ts">
import { cn } from '../../lib/utils'

interface TimeSlot {
    time: string
    available: boolean
}

interface Props {
    modelValue?: string | string[]
    slots: TimeSlot[]
    multiple?: boolean
    class?: any
}

const props = defineProps<Props>()
const emit = defineEmits(['update:modelValue'])

const isSelected = (time: string) => {
    if (props.multiple && Array.isArray(props.modelValue)) {
        return props.modelValue.includes(time)
    }
    return props.modelValue === time
}

const toggleSlot = (time: string) => {
    if (props.multiple) {
        const current = Array.isArray(props.modelValue) ? [...props.modelValue] : []
        if (current.includes(time)) {
            emit('update:modelValue', current.filter(t => t !== time))
        } else {
            emit('update:modelValue', [...current, time])
        }
    } else {
        emit('update:modelValue', time)
    }
}
</script>

<template>
    <div :class="cn('grid grid-cols-[repeat(auto-fill,minmax(85px,1fr))] gap-2.5 w-full', props.class)">
        <button v-for="slot in slots" :key="slot.time" type="button" :disabled="!slot.available"
            @click="slot.available && toggleSlot(slot.time)" :class="cn(
                'py-2 px-3 rounded-md text-[14px] font-semibold transition-all text-center border relative overflow-hidden',
                !slot.available
                    ? 'bg-[#F0F2F5] text-[#CED0D4] border-transparent cursor-not-allowed'
                    : isSelected(slot.time)
                        ? 'bg-[#0866FF] text-white border-[#0866FF] shadow-[0_2px_4px_rgba(8,102,255,0.2)]'
                        : 'bg-white text-[#050505] border-[#CED0D4] hover:bg-[#F0F2F5]'
            )">
            {{ slot.time }}
        </button>
    </div>
</template>
