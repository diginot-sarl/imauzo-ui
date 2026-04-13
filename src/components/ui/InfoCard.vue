<script setup lang="ts">
import { cn } from '../../lib/utils'
import Card from './Card.vue'
import Heading from './Heading.vue'
import Text from './Text.vue'
import Icon from './Icon.vue'

interface Props {
    title: string
    description?: string
    icon?: any
    variant?: 'info' | 'success' | 'warning' | 'error' | 'default'
    class?: any
}

const props = withDefaults(defineProps<Props>(), {
    variant: 'info'
})

const iconColors = {
    default: 'bg-gray-100 text-gray-600',
    info: 'bg-blue-100 text-blue-600',
    success: 'bg-green-100 text-green-600',
    warning: 'bg-yellow-100 text-yellow-600',
    error: 'bg-red-100 text-red-600'
}
</script>

<template>
    <Card :variant="variant" :class="cn('transition-colors', props.class)">
        <div class="flex items-center gap-3">
            <div v-if="icon"
                :class="cn('w-10 h-10 rounded-full flex items-center justify-center shrink-0', iconColors[variant])">
                <Icon :icon="icon" size="sm" />
            </div>
            <div>
                <Heading level="5">{{ title }}</Heading>
                <Text v-if="description" variant="secondary" size="xs">{{ description }}</Text>
            </div>
        </div>
    </Card>
</template>
