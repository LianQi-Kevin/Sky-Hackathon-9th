<script setup>
import {getStyles} from "@/network/imgAPI.js";
import {ElMessage} from "element-plus";

const styles = reactive({
    "styleList": [2]
})

function getSDXLStyles(){
    const exportList = []
    for (const i of styles.styleList) {
        exportList.push(JSON.parse(JSON.stringify(styleDict.value[i])))
    }
    return exportList
}

defineExpose({
    // styles,
    getSDXLStyles

})

const styleDict = ref()

onMounted(() => {
    nextTick(() => {
        getStyles().then(response => {
            styleDict.value = response.data.data.style
        }).catch(err => {
            console.error(err)
            ElMessage.error( `${err.code}. Get SDXL Style Failed`)
        })
    })
})
</script>

<template>
    <el-select
        v-model="styles.styleList"
        multiple
        clearable
        collapse-tags
        collapse-tags-tooltip
        :max-collapse-tags="2"
        placeholder="请选择画面风格（可多选）"
    >
        <el-option
            v-for="item in styleDict"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        />
    </el-select>
</template>

<style scoped>

</style>