import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index"
import {store} from "./store/index";

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import VueCookies from 'vue-cookies';

const vuetify = createVuetify({
    components,
    directives,
    theme: {
        defaultTheme: 'dark'
    }
})


createApp(App).use(store).use(router).use(vuetify).use(VueCookies).mount('#app')
