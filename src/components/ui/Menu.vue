<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    class?: any
    compact?: boolean
}

const props = defineProps<Props>()
</script>

<template>
    <ul :class="cn('menu', compact ? 'menu-sm' : '', props.class)">
        <slot />
    </ul>
</template>
