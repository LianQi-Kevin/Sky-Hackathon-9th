import HomeView from '@/views/HomeView.vue'

const routes = [
    {
        path: '/',
        alias: '/home',
        name: 'Home',
        component: HomeView,  // 首页不启用lazyLoad
        meta: {
            title: "Home"   // 页面标题 ( 非必要 )
        }
    },
    {
        path: '/about',
        name: 'About',
        // 使用import语句对页面启用lazyLoad
        component: () => import('@/views/AboutView.vue'),
        meta: {
            title: "About"
        }
    },
    {
        path: '/error/:id',
        component: () => import('@/views/notFound.vue'),
        props: (route) => ({id: route.params.id || 404}),
        meta: {
            title: 'ERROR'
        }
    },
    {
        // 配置全局匹配，跳转到 404 NOT FOUND
        path: '/:pathMatch(.*)*',
        redirect: '/error/404'
    }
]


export default routes
