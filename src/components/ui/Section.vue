<script setup lang="ts">
import { cn } from '../../lib/utils'

interface Props {
    class?: any
}

const props = defineProps<Props>()
</script>

<template>
    <section :class="cn('space-y-4', props.class)">
        <slot />
    </section>
</template>
