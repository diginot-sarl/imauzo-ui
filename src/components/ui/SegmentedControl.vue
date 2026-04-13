<script setup lang="ts">
interface Option {
  value: string | number
  label?: string
  icon?: any
}

const props = defineProps<{
    options: Option[],
    modelValue: string | number
}>()

const emit = defineEmits(['update:modelValue'])

const select = (val: string | number) => {
    emit('update:modelValue', val)
}
</script>

<template>
  <div class="inline-flex flex-wrap items-center bg-[#F0F2F5] p-1 rounded-xl gap-1">
     <button 
        v-for="opt in options" 
        :key="opt.value"
        type="button"
        @click="select(opt.value)"
        class="relative flex items-center justify-center px-4 py-2 min-h-9 text-[14px] font-semibold rounded-lg transition-all duration-200 outline-none select-none focus-visible:ring-2 focus-visible:ring-[#0866FF]"
        :class="modelValue === opt.value 
            ? 'text-[#050505] shadow-sm bg-white' 
            : 'text-[#65676B] hover:text-[#050505] hover:bg-[#E4E6EB]'"
     >
        <!-- Rendu dynamique du composant icône -->
        <component :is="opt.icon" v-if="opt.icon" class="w-[18px] h-[18px]" :class="opt.label ? 'mr-2' : ''" />
        <span v-if="opt.label">{{ opt.label }}</span>
     </button>
  </div>
</template>
