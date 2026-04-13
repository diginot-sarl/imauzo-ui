<script setup lang="ts">
// Container for Sidebar items
</script>

<template>
    <ul class="menu p-2 w-full text-base-content bg-transparent font-sans">
        <slot />
    </ul>
</template>

<style scoped>
/* Reset some daisyui menu padding for custom sleek look */
.menu :where(li:not(.menu-title) > *:not(ul, details, .menu-title, .btn)),
.menu :where(li:not(.menu-title) > details > summary:not(.menu-title)) {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
}
</style>
