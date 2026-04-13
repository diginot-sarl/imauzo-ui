<script setup lang="ts">
interface Props {
    title: string
    name?: string
    defaultOpen?: boolean
}
const props = defineProps<Props>()
</script>

<template>
    <div class="collapse collapse-arrow bg-white border border-[#CED0D4] rounded-lg shadow-sm">
        <input type="radio" :name="name" :checked="defaultOpen" v-if="name" />
        <input type="checkbox" :checked="defaultOpen" v-else />

        <!-- Title -->
        <div class="collapse-title text-[15px] font-semibold text-[#050505] min-h-0 py-3 pr-12 flex items-center">
            {{ title }}
        </div>

        <!-- Content -->
        <div class="collapse-content text-[#65676B] text-[14px]">
            <div class="pt-0 pb-1">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<style scoped>
.collapse-arrow>.collapse-title:after {
    top: 1.2rem;
    color: #65676B;
}

.collapse:focus-within {
    box-shadow: none;
}
</style>
