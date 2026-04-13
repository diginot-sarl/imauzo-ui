<script setup lang="ts">
import { ref } from 'vue'
import { Bold, Italic, Link2, List, AlignLeft, AlignCenter, AlignRight } from 'lucide-vue-next'
import { cn } from '../../lib/utils'

interface Props {
    modelValue: string
    placeholder?: string
    minHeight?: string
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    minHeight: 'min-h-[150px]',
    placeholder: 'Rédigez votre texte ici...'
})

const emit = defineEmits(['update:modelValue'])

const internalValue = ref(props.modelValue)

const onInput = (e: Event) => {
    const target = e.target as HTMLTextAreaElement
    internalValue.value = target.value
    emit('update:modelValue', target.value)
}

const tools = [
    { icon: Bold, label: 'Gras' },
    { icon: Italic, label: 'Italique' },
    { icon: Link2, label: 'Lien' },
    { icon: List, label: 'Liste' },
    { icon: AlignLeft, label: 'Aligner à gauche' },
    { icon: AlignCenter, label: 'Centrer' },
    { icon: AlignRight, label: 'Aligner à droite' },
]
</script>

<template>
    <div
        :class="cn('border border-[#CED0D4] rounded-lg bg-white overflow-hidden flex flex-col focus-within:border-[#0866FF] focus-within:ring-1 focus-within:ring-[#0866FF] transition-all', $props.class)">
        <!-- Toolbar -->
        <div class="flex items-center gap-1 p-1.5 border-b border-[#E4E6EB] bg-[#F0F2F5] shrink-0 overflow-x-auto">
            <button v-for="(tool, index) in tools" :key="tool.label" type="button" :title="tool.label"
                class="w-8 h-8 rounded-md flex items-center justify-center text-[#65676B] hover:bg-[#E4E6EB] hover:text-[#050505] transition-colors shrink-0">
                <component :is="tool.icon" class="w-[18px] h-[18px]" />
            </button>
        </div>

        <!-- Text Area -->
        <textarea :value="internalValue" @input="onInput" :placeholder="placeholder" :class="cn(
            'w-full p-3 resize-y outline-none text-[15px] text-[#050505] placeholder:text-[#8D949E] bg-white border-none',
            minHeight
        )"></textarea>
    </div>
</template>
