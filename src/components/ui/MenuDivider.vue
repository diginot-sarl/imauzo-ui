<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    class?: any
}

defineProps<Props>()
</script>

<template>
    <li class="menu-title" style="padding: 0; margin-top: 4px; margin-bottom: 4px;" v-if="$slots.default">
        <span :class="cn('text-xs uppercase font-bold text-[#65676B] tracking-wider', $props.class)">
            <slot />
        </span>
    </li>
    <div v-else :class="cn('h-px w-full bg-[#CED0D4]/60 my-1', $props.class)"></div>
</template>
