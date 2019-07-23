import Vue from 'vue';
import App from './App.vue';
import router from './router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';

Vue.config.productionTip = false
Vue.prototype.$axios = axios;

const token = localStorage.getItem('token');
if (token) {
    Vue.prototype.$axios.defaults.headers.common['Authorization'] = token;
}
Vue.use(ElementUI, { size: 'small' });

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
