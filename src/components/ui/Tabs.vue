<script setup lang="ts">
interface Tab {
    label: string
    value: string | number
    icon?: any
}

interface Props {
    options: Tab[]
    modelValue: string | number
    fullWidth?: boolean
    variant?: 'bordered' | 'pills' | 'premium'
}

const props = withDefaults(defineProps<Props>(), {
    variant: 'pills'
})

const emit = defineEmits<{
    'update:modelValue': [value: string | number]
}>()
</script>

<template>
    <div role="tablist" class="w-full flex items-center" :class="[
        variant === 'bordered' ? 'border-b border-[#CED0D4]/30' : 'gap-2',
        fullWidth ? 'flex' : ''
    ]">
        <a v-for="tab in options" :key="tab.value" role="tab"
            class="flex items-center justify-center gap-2 transition-all duration-200 cursor-pointer" :class="[
                fullWidth ? 'flex-1' : '',
                variant === 'bordered' ? [
                    'h-12 px-4 border-b-[3px]',
                    modelValue === tab.value
                        ? 'font-semibold text-[#0866FF] border-[#0866FF]'
                        : 'text-[#65676B] hover:text-[#050505] hover:bg-[#F0F2F5]/50 border-transparent'
                ] : variant === 'premium' ? [
                    'h-11 px-5 rounded-xl font-bold text-[14px]',
                    modelValue === tab.value
                        ? 'bg-[#1C1E21] text-white shadow-sm'
                        : 'text-[#65676B] hover:bg-[#F0F2F5] hover:text-[#1C1E21]'
                ] : [
                    'h-8 px-4 rounded-full font-semibold text-[14px]',
                    modelValue === tab.value
                        ? 'bg-[#EBF5FF] text-[#0866FF] border border-[#0866FF]'
                        : 'text-[#65676B] hover:bg-[#F0F2F5] hover:text-[#050505] border border-transparent'
                ]
            ]" @click="emit('update:modelValue', tab.value)">
            <component v-if="tab.icon" :is="tab.icon" class="w-4 h-4" />
            {{ tab.label }}
        </a>
    </div>
</template>
