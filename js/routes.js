import List from './pages/List.js';
import Leaderboard from './pages/Leaderboard.js';
import Roulette from './pages/Roulette.js';
import PlatList from './pages/PlatList.js';
import OBGList from './pages/OBGList.js'
import cllList from './pages/cllList.js'

export default [
    { path: '/list', component: List },
    { path: '/leaderboard', component: Leaderboard },
    { path: '/roulette', component: Roulette },
    { path: '/platformer_list', component: PlatList },
    { path: '/', component: OBGList },
    { path: '/clllist', component: cllList },
];
