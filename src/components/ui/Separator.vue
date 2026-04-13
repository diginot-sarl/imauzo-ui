<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    vertical?: boolean
    class?: any
}

const props = defineProps<Props>()
</script>

<template>
    <div role="separator" :class="cn(
        vertical ? 'w-px h-full' : 'h-px w-full',
        'bg-[#CED0D4]/60',
        props.class
    )"></div>
</template>
