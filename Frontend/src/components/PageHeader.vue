<script setup>
// import ThemeSwitch from "@/components/ThemeSwitch.vue";

const props = defineProps({
    title: {
        type: String,
        required: false,
        default: "Sky-Hackathon-9th"
    },
    teamName: {
        type: String,
        required: false,
        default: "无辑"
    }
})

</script>

<template>
    <div class="content">
        <img src="@/assets/svg/NVIDIA.svg" alt="NV icon" class="NVicon" />
        <div class="divider"/>
        <el-text class="interval_margin exam_title">{{ props.title }}</el-text>
        <el-text class="interval_margin team_name">Team: {{ props.teamName }}</el-text>
        <div style="flex-grow: 10"/>
<!--        <ThemeSwitch style="display: none"/>-->
    </div>
</template>

<style scoped>
.content {
    background: rgba(0, 0, 0, 0.8);
    width: 100%;
    height: 50px;
    position: absolute;
    display: flex;
    flex-direction: row;
    justify-content: start;
}

.interval_margin {
    margin: 0;
    padding: 0;
    border: 0;
    font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}

.divider {
    height: 40px;
    justify-self: center;
    background: white;
    width: 1px;
    margin: 5px 0
}

.NVicon {
    margin: 0 10px;
    flex-basis: 40px;
    flex-grow: 0;
}

.exam_title {
    font-size: 30px;
    margin-left: 20px;
    flex-basis: 270px;
    height: 100%;
    flex-grow: 0;

    display: flex;
    justify-content: center;
    flex-direction: column;
}

.team_name {
    font-size: 20px;
    height: 100%;
    margin-bottom: 10px;
    flex-basis: 120px;
    flex-grow: 0;
    display: flex;
    justify-content: end;
    flex-direction: column;
}
</style>