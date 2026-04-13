<script setup lang="ts">
import { ChevronRight } from 'lucide-vue-next'

interface Props {
    icon?: any
    title: string
    to?: string
    active?: boolean
    badge?: string | number
    hasSubmenu?: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{ click: [] }>()

const onClick = () => emit('click')
</script>

<template>
    <li>
        <a @click="onClick" :class="[
            'flex items-center gap-3 px-3 py-2.5 rounded-lg transition-colors font-medium mb-1',
            active ? 'bg-[#EAF3FF] text-[#0866FF]' : 'text-[#050505] hover:bg-[#F0F2F5]'
        ]">
            <div v-if="icon" class="flex items-center justify-center w-8 h-8 rounded-full"
                :class="active ? 'bg-[#0866FF] text-white' : 'bg-[#E4E6EB] text-[#050505]'">
                <component :is="icon" class="w-5 h-5" />
            </div>

            <span class="flex-1 text-[15px]">{{ title }}</span>

            <span v-if="badge" class="badge badge-sm" :class="active ? 'badge-primary' : ''">
                {{ badge }}
            </span>
            <ChevronRight v-if="hasSubmenu" class="w-4 h-4 text-[#65676B]" />
        </a>
    </li>
</template>
