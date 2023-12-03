<script setup>

import {ChatRound, House, Location, Tools} from "@element-plus/icons-vue";
</script>

<template>
<!--    <el-menu default-active="1" class="Menu" @open="handleOpen" @close="handleClose">-->
    <el-menu default-active="/home" class="Menu" mode="vertical" :collapse="false" :router="true">
        <el-menu-item index="/home">
            <template #title>
                <el-icon><House /></el-icon>
                <span>Home</span>
            </template>
        </el-menu-item>
        <el-sub-menu index="">
            <template #title>
                <el-icon><Tools /></el-icon>
                <span>Tools</span>
            </template>
            <el-menu-item index="imgDetect">
                <template #title>
                    <el-icon><location /></el-icon>
                    <span>Img Detect</span>
                </template>
            </el-menu-item>
            <el-menu-item index="Chat">
                <template #title>
                    <el-icon><ChatRound /></el-icon>
                    <span>ChatGPT</span>
                </template>
            </el-menu-item>
            <el-menu-item index="SDXL">
                <template #title>
                    <el-icon><location /></el-icon>
                    <span>SDXL</span>
                </template>
            </el-menu-item>
        </el-sub-menu>
        <el-divider />
        <el-menu-item index="/About">
            <template #title>
                <span>About</span>
            </template>
        </el-menu-item>
    </el-menu>
</template>

<style scoped>


</style>