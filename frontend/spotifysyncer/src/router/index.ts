import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from "../components/HelloWorld.vue";
import CallBack from "../components/CallBack.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HelloWorld,
    },
    {
        path: "/callback",
        name: "CallBack",
        component: CallBack
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router