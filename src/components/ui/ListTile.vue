<script setup lang="ts">
import { ChevronRight } from 'lucide-vue-next'

interface Props {
    title: string
    subtitle?: string
    icon?: any
    avatar?: string
    trailingIcon?: any
    clickable?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    clickable: true
})

const emit = defineEmits<{
    'click': []
}>()
</script>

<template>
    <div class="flex items-center gap-3 p-3 rounded-lg transition-colors text-left w-full" :class="[
        clickable ? 'cursor-pointer hover:bg-[#F0F2F5]' : ''
    ]" @click="clickable && emit('click')" role="button" :tabindex="clickable ? 0 : -1">
        <!-- Left Icon / Avatar -->
        <div v-if="icon || avatar" class="shrink-0 flex items-center justify-center">
            <div v-if="avatar" class="avatar">
                <div class="w-12 h-12 rounded-full overflow-hidden border border-[#CED0D4]/30">
                    <img :src="avatar" alt="Avatar" class="object-cover w-full h-full" />
                </div>
            </div>
            <div v-else-if="icon" class="w-11 h-11 rounded-full bg-[#E4E6EB] flex items-center justify-center">
                <component :is="icon" class="w-6 h-6 text-[#050505]" />
            </div>
        </div>

        <slot name="leading"></slot>

        <!-- Content -->
        <div class="flex-1 min-w-0">
            <h4 class="text-[#050505] font-semibold text-[15px] truncate leading-tight">{{ title }}</h4>
            <p v-if="subtitle" class="text-[#65676B] text-[13px] truncate mt-0.5">{{ subtitle }}</p>
            <slot></slot>
        </div>

        <!-- Trailing -->
        <div class="shrink-0 flex items-center gap-2">
            <slot name="trailing"></slot>
            <component v-if="trailingIcon" :is="trailingIcon" class="w-5 h-5 text-[#65676B]" />
            <ChevronRight v-else-if="clickable && !trailingIcon && !$slots.trailing" class="w-5 h-5 text-[#B0B3B8]" />
        </div>
    </div>
</template>
