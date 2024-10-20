import List from './pages/List.js';
import PlatList from './pages/PlatList.js';
import OBGList from './pages/OBGList.js'
import cllList from './pages/cllList.js'
import ilList from './pages/ilList.js'

export default [
    { path: '/list', component: List },
    { path: '/platformer_list', component: PlatList },
    { path: '/', component: OBGList },
    { path: '/clllist', component: cllList },
    { path: '/illist', component: ilList },
];
