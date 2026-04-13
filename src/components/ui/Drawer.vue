<script setup lang="ts">
import { watch } from 'vue'
import { X } from 'lucide-vue-next'
import IconButton from './IconButton.vue'

const props = withDefaults(defineProps<{
    modelValue: boolean
    title?: string
    position?: 'left' | 'right'
}>(), {
    position: 'right'
})

const emit = defineEmits(['update:modelValue'])

const close = () => emit('update:modelValue', false)

// Prevent body scroll when open
watch(() => props.modelValue, (val) => {
    if (val) document.body.style.overflow = 'hidden'
    else document.body.style.overflow = ''
})
</script>

<template>
  <Teleport to="body">
     <div v-if="modelValue" class="fixed inset-0 z-[9999] flex" :class="position === 'left' ? 'justify-start' : 'justify-end'">
        
        <!-- Overlay -->
        <Transition 
          enter-active-class="transition-opacity duration-300" enter-from-class="opacity-0" enter-to-class="opacity-100" 
          leave-active-class="transition-opacity duration-300" leave-from-class="opacity-100" leave-to-class="opacity-0"
          appear
        >
            <div v-show="modelValue" class="absolute inset-0 bg-[#050505]/40 backdrop-blur-[2px]" @click="close"></div>
        </Transition>
        
        <!-- Drawer Panel -->
        <Transition 
          :enter-active-class="`transition-transform duration-300 ease-out`" 
          :enter-from-class="position === 'left' ? '-translate-x-full' : 'translate-x-full'" 
          :enter-to-class="`translate-x-0`" 
          :leave-active-class="`transition-transform duration-200 ease-in`" 
          :leave-from-class="`translate-x-0`" 
          :leave-to-class="position === 'left' ? '-translate-x-full' : 'translate-x-full'"
          appear
        >
            <div v-show="modelValue" class="relative w-full max-w-md bg-white h-full shadow-2xl flex flex-col z-10 border-[#CED0D4]" :class="position === 'left' ? 'border-r rounded-r-2xl' : 'border-l rounded-l-2xl'">
                <div class="px-6 py-5 border-b border-[#CED0D4] flex items-center justify-between bg-white z-20" :class="position === 'left' ? 'rounded-tr-2xl' : 'rounded-tl-2xl'">
                    <h3 class="text-xl font-bold text-[#050505] tracking-tight">{{ title }}</h3>
                    <IconButton variant="ghost" size="sm" @click="close" class="bg-[#F0F2F5] hover:bg-[#E4E6EB]">
                        <X class="w-5 h-5 text-[#65676B]" />
                    </IconButton>
                </div>
                
                <div class="p-6 overflow-y-auto flex-1 bg-white">
                    <slot></slot>
                </div>
                
                <div class="border-t border-[#CED0D4] p-4 bg-white shadow-[0_-4px_16px_rgba(0,0,0,0.05)] z-20" v-if="$slots.footer">
                    <slot name="footer"></slot>
                </div>
            </div>
        </Transition>
     </div>
  </Teleport>
</template>
