<script setup lang="ts">
interface Props {
    variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'error' | 'ghost' | 'neutral'
    outline?: boolean
}
const props = withDefaults(defineProps<Props>(), {
    variant: 'primary',
    outline: false
})
</script>

<template>
    <div class="badge font-semibold text-[12px] px-2.5 py-3" :class="[
        outline ? 'badge-outline' : 'border-transparent',
        (function() {
            const v = ['primary', 'secondary', 'success', 'warning', 'error', 'ghost', 'neutral'].includes(variant as string) ? variant : 'primary';
            
            if (!outline) {
                if (v === 'primary') return 'bg-primary text-white';
                if (v === 'secondary') return 'bg-secondary text-text-primary';
                if (v === 'success') return 'bg-success/20 text-success';
                if (v === 'warning') return 'bg-warning/20 text-warning';
                if (v === 'error') return 'bg-danger/20 text-danger';
                if (v === 'neutral') return 'bg-[#323436] text-white';
                if (v === 'ghost') return 'bg-transparent text-text-secondary';
            } else {
                if (v === 'primary') return 'text-primary border-primary';
                if (v === 'secondary') return 'text-text-secondary border-base-border';
                if (v === 'success') return 'text-success border-success';
                if (v === 'warning') return 'text-warning border-warning';
                if (v === 'error') return 'text-danger border-danger';
                if (v === 'neutral') return 'text-[#323436] border-[#323436]';
                if (v === 'ghost') return 'text-text-secondary border-transparent';
            }
            return '';
        })()
    ]">
        <slot></slot>
    </div>
</template>
