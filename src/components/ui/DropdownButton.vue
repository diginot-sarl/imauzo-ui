<script setup lang="ts">
import { ref } from 'vue'
import { ChevronDown } from 'lucide-vue-next'
import { useFloating, autoUpdate, offset, flip, shift } from '@floating-ui/vue'
import { useClickOutside } from '../../lib/useClickOutside'

interface Props {
    label: string
    align?: 'end' | 'start'
    variant?: 'primary' | 'secondary' | 'ghost'
}

const props = withDefaults(defineProps<Props>(), {
    align: 'start',
    variant: 'secondary'
})

const isOpen = ref(false)
const reference = ref<HTMLElement | null>(null)
const floating = ref<HTMLElement | null>(null)

// Configure Floating UI
const { x, y, strategy } = useFloating(reference, floating, {
    placement: props.align === 'end' ? 'bottom-end' : 'bottom-start',
    whileElementsMounted: autoUpdate,
    middleware: [
        offset(6),
        flip(),
        shift({ padding: 8 })
    ],
})

import { computed } from 'vue'

const roughX = ref(0)
const roughY = ref(0)

const customFloatingStyles = computed(() => ({
    position: strategy.value,
    top: `${y.value ?? roughY.value}px`,
    left: `${x.value ?? roughX.value}px`,
}))

const toggleMenu = () => {
    if (!isOpen.value && reference.value) {
        const rect = reference.value.getBoundingClientRect()

        if (props.align === 'end') {
            roughX.value = rect.right + window.scrollX - 208 // 208px = w-52
        } else {
            roughX.value = rect.left + window.scrollX
        }
        // Offset 6px (Floating-UI setup)
        roughY.value = rect.bottom + window.scrollY + 6
    }
    isOpen.value = !isOpen.value
}

const closeMenu = () => {
    isOpen.value = false
}

// Ensure the menu closes when clicked outside
useClickOutside(floating, closeMenu, reference)
</script>

<template>
    <!-- Container w-fit essentiel pour que le menu hérite de la vraie largeur du trigger -->
    <div ref="reference" class="inline-block relative w-fit" @click="toggleMenu">
        
        <!-- Slot personnalisé permettant d'injecter un Avatar, IconButton, etc. -->
        <slot name="trigger" :isOpen="isOpen">
            <!-- Bouton par défaut si aucun trigger personnalisé n'est fourni -->
            <button type="button"
                class="btn btn-sm h-10 px-4 rounded-md tracking-wide text-[14px] font-semibold border-none shadow-none flex flex-nowrap items-center gap-1.5 transition-colors"
                :class="{
                    'bg-[#0866FF] text-white hover:bg-[#075ce5]': variant === 'primary',
                    'bg-[#E4E6EB] text-[#050505] hover:bg-[#D8DADF]': variant === 'secondary',
                    'bg-transparent text-[#050505] hover:bg-[#F0F2F5]': variant === 'ghost',
                    'ring-2 ring-[#0866FF] ring-opacity-50': isOpen && variant !== 'ghost'
                }">
                <slot name="label">{{ label }}</slot>
                <ChevronDown class="w-4 h-4 opacity-70 transition-transform" :class="isOpen ? 'rotate-180' : ''" />
            </button>
        </slot>

        <Teleport to="body">
            <Transition enter-active-class="transition duration-200 ease-out origin-top"
                enter-from-class="transform scale-95 opacity-0 -translate-y-2"
                enter-to-class="transform scale-100 opacity-100 translate-y-0"
                leave-active-class="transition duration-150 ease-in origin-top"
                leave-from-class="transform scale-100 opacity-100 translate-y-0"
                leave-to-class="transform scale-95 opacity-0 -translate-y-2">
                <ul v-if="isOpen" ref="floating" :style="customFloatingStyles"
                    class="menu z-[1000] p-1.5 shadow-[0_8px_24px_rgba(0,0,0,0.12)] bg-white rounded-xl w-52 border border-[#CED0D4]/80 flex flex-col gap-0.5"
                    @click="closeMenu">
                    <slot></slot>
                </ul>
            </Transition>
        </Teleport>
    </div>
</template>
