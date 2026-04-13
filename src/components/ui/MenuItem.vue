<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    href?: string
    danger?: boolean
    active?: boolean
    disabled?: boolean
    class?: any
}

const props = defineProps<Props>()
defineEmits(['click'])
</script>

<template>
    <li :class="cn({ 'disabled': disabled }, props.class)">
        <a :href="href" :class="cn(
            'font-medium transition-colors',
            active ? 'active' : '',
            danger ? 'text-[#E02636] hover:bg-[#E02636]/10 hover:text-[#E02636]' : ''
        )" @click="!disabled && $emit('click', $event)">
            <slot name="icon"></slot>
            <slot></slot>
        </a>
    </li>
</template>
