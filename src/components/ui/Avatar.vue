<script setup lang="ts">
import { ref, computed } from 'vue'
import { cn } from '../../lib/utils'

interface Props {
  src?: string
  initials?: string
  alt?: string
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  shape?: 'circle' | 'square' | 'squircle'
  status?: 'online' | 'offline' | 'busy' | 'none'
  ring?: boolean
  class?: any
}

const props = withDefaults(defineProps<Props>(), {
  size: 'md',
  shape: 'circle',
  status: 'none',
  ring: false
})

const hasError = ref(false)

const onImageError = () => {
  hasError.value = true
}

const sizeClass = computed(() => {
  const sizes = { 
    xs: 'w-8 h-8 text-xs', 
    sm: 'w-10 h-10 text-sm', 
    md: 'w-12 h-12 text-base', 
    lg: 'w-16 h-16 text-lg', 
    xl: 'w-24 h-24 text-2xl' 
  }
  return sizes[props.size]
})

const shapeClass = computed(() => {
  const shapes = { 
    circle: 'rounded-full', 
    square: 'rounded-xl', 
    squircle: 'mask mask-squircle' 
  }
  return shapes[props.shape]
})

const statusClass = computed(() => {
  if (props.status === 'none') return ''
  // DaisyUI avatar status classes
  return props.status === 'online' ? 'online' : props.status === 'offline' ? 'offline' : 'online ring-warning' // For busy we can tweak ring
})
</script>

<template>
  <div :class="cn('avatar', statusClass, props.class, { 'placeholder': !src || hasError })">
    <div :class="cn(
        sizeClass, 
        shapeClass, 
        ring ? 'ring ring-[#0866FF] ring-offset-base-100 ring-offset-2' : '', 
        'bg-[#E4E6EB] text-[#050505] font-semibold flex items-center justify-center shadow-sm transition-all'
      )">
      <!-- Real Image -->
      <img v-if="src && !hasError" :src="src" :alt="alt || initials || 'Avatar'" @error="onImageError" class="object-cover w-full h-full" />
      
      <!-- Fallback Initials -->
      <span v-else-if="initials">{{ initials }}</span>
      
      <!-- Fallback Slot (ex: Icon) -->
      <div v-else class="w-full h-full flex items-center justify-center">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
