<script setup lang="ts">
import IconButton from './IconButton.vue'
import { ArrowLeft } from 'lucide-vue-next'

const emit = defineEmits(['click'])
</script>

<template>
  <IconButton 
    variant="ghost" 
    size="md" 
    class="text-[#050505] bg-[#F0F2F5] hover:bg-[#E4E6EB] transition-colors"
    @click="emit('click')"
  >
     <ArrowLeft class="w-5 h-5" />
  </IconButton>
</template>
