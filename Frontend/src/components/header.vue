<script setup>
import ThemeSwitch from "@/components/ThemeSwitch.vue";
</script>

<template>
    <div class="content">
        <img src="@/assets/svg/NVIDIA.svg" alt="NV icon" class="NVicon" />
        <div class="divider"/>
        <p class="interval_margin exam_title">Sky-Hackathon-9th</p>
        <p class="interval_margin team_name">Team: 无辑</p>
        <div style="flex-grow: 10"/>
        <ThemeSwitch style="display: none"/>
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
    margin-top: 5px;
    flex-basis: 270px;
    flex-grow: 0;
}

.team_name {
    font-size: 20px;
    margin-top: 15px;
    flex-basis: 120px;
    flex-grow: 0;
}
</style>