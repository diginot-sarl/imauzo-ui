<script setup lang="ts">
import { cn } from '../../lib/utils'
</script>

<template>
  <div :class="cn('imauzo-button-group flex items-center shadow-sm rounded-lg', $attrs.class)">
    <slot></slot>
  </div>
</template>

<style scoped>
/* 
  Ciblez les divs internes (ex: Dropdown wrapper) ou les boutons directs. 
  Assure que seuls les bords extérieurs sont arrondis et qu'il n'y a pas de double-bordure.
*/
.imauzo-button-group :deep(> button:not(:first-child):not(:last-child)),
.imauzo-button-group :deep(> div:not(:first-child):not(:last-child) > button) {
  border-radius: 0;
  border-left-color: transparent;
  box-shadow: none;
}

.imauzo-button-group :deep(> button:first-child),
.imauzo-button-group :deep(> div:first-child > button) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
  box-shadow: none;
}

.imauzo-button-group :deep(> button:last-child),
.imauzo-button-group :deep(> div:last-child > button) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-left-color: transparent;
  box-shadow: none;
}

/* Fix hover pour les overlaps */
.imauzo-button-group :deep(> button:hover),
.imauzo-button-group :deep(> div:hover > button) {
  z-index: 10;
  position: relative;
}
</style>
