import { onMounted, onUnmounted, type Ref } from 'vue'

export function useClickOutside(
    refToTrack: Ref<HTMLElement | null>,
    callback: () => void,
    excludeRef?: Ref<HTMLElement | null>
) {
    const listener = (event: MouseEvent | TouchEvent) => {
        const target = event.target as Node
        if (!refToTrack.value || refToTrack.value.contains(target)) {
            return
        }
        // If an exclude element is provided (like the trigger button), don't trigger callback if clicking inside it
        if (excludeRef?.value && excludeRef.value.contains(target)) {
            return
        }
        callback()
    }

    onMounted(() => {
        document.addEventListener('mousedown', listener)
        document.addEventListener('touchstart', listener)
    })

    onUnmounted(() => {
        document.removeEventListener('mousedown', listener)
        document.removeEventListener('touchstart', listener)
    })
}
