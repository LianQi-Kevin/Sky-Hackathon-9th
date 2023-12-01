<script setup>
import {Moon, Sunny} from "@element-plus/icons-vue";
import {useDark} from "@vueuse/core";

const props = defineProps({
    storageKey: {
        type: String,
        required: false,
        default: "vitepress-theme-appearance"
    },
})

const isDark = useDark({
    storageKey: props.storageKey,
    valueDark: 'dark',
    valueLight: 'light'
})
</script>

<template>
    <el-switch
        v-model="isDark"
        :active-action-icon="Moon"
        :inactive-action-icon="Sunny"
        :size="'large'"
        style="--el-switch-off-color: rgb(240, 240, 240); --el-switch-on-color: rgb(44, 44, 44)"
    />
</template>

<style lang="scss" scoped>
</style>