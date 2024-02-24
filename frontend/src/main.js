import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:8000'; // Django development server

createApp(App).mount('#app');
