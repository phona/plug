import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/login',
        },

        {
            path: '/login',
            component: resolve => require(['../components/Login.vue'], resolve)
        },

        {
            path: '/register',
            component: resolve => require(['../components/Register.vue'], resolve)
        },

        {
            path: '/main',
            component: resolve => require(['../components/Main.vue'], resolve)
        }
    ]
});