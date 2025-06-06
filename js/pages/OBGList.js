import { store } from "../main.js";
import { embed } from "../util.js";
import { fetchEditors, fetchList } from "../content3.js";

import Spinner from "../components/Spinner.js";
import LevelAuthors from "../components/List/LevelAuthors.js";

const roleIconMap = {
    owner: "crown",
    admin: "user-gear",
    helper: "user-shield",
    dev: "code",
    trial: "user-lock",
};

export default {
    components: { Spinner, LevelAuthors },
    template: `
        <main v-if="loading">
            <Spinner></Spinner>
        </main>
        <main v-else class="page-list">
            <div class="list-container">
                <table class="list" v-if="list">
                    <tr v-for="([level, err], i) in list">
                        <td class="rank" v-if="level.rank + 1 <= 100">
                            <p class="type-label-lg" v-if="level.rank == 0">-</p>
                            <p class="type-label-lg" v-if="level.rank != 0">#{{level.rank}}</p>
                        </td>
                        <td class="level" :class="{ 'active': selected == i, 'error': !level }" v-if="i + 1 <= 100">
                            <button @click="selected = i">
                                <span class="type-label-lg">{{ level?.name || \`Error (\${err}.json)\` }}</span>
                            </button>
                        </td>
                    </tr>
                </table>
                <div style="display: table; height: 75px; overflow: hidden;">
                    <div style="display: table-cell; vertical-align: middle;">
                        <p class="list"> LEGACY LIST </p>
                    </div>
                </div>
                <table class="legacy" v-if="list">
                    <tr v-for="([level, err], i) in list">
                        <td class="rank" v-if="i + 1 > 100">
                            <p class="type-label-lg">Legacy</p>
                        </td>
                        <td class="level" :class="{ 'active': selected == i, 'error': !level }" v-if="i + 1 > 100">
                            <button @click="selected = i">
                                <span class="type-label-lg">{{ level?.name || \`Error (\${err}.json)\` }}</span>
                            </button>
                        </td>
                    </tr>
                </table>
            </div>
            <div class="level-container">
                <div class="level" v-if="level">
                    <h3 v-if="level.rank == 0">Benchmark Level</h3>
                    <h1>{{ level.name }}</h1>
                    <LevelAuthors :author="level.author" :verifier="level.verifier" :first_victor="level.first_victor" v-if="level.rank != 0"></LevelAuthors>
                    <iframe class="video" id="videoframe" :src="video" frameborder="0"></iframe>
                    <ul class="stats" v-if="level.rank != 0">
                        <li>
                            <div class="type-title-sm">In-game difficulty</div>
                            <p>{{ level.difficulty }}</p>
                        </li>
                        <li>
                            <div class="type-title-sm">ID</div>
                            <p>{{ level.id }}</p>
                        </li>
                    </ul>
                    <p style="white-space: pre-line">
                        {{level.funny}}
                    <\p>
                </div>
                <div v-else class="level" style="height: 100%; justify-content: center; align-items: center;">
                    <p>(ノಠ益ಠ)ノ彡┻━┻</p>
                </div>
            </div>
            <div class="meta-container">
                <div class="meta">
                    <div class="errors" v-show="errors.length > 0">
                        <p class="error" v-for="error of errors">{{ error }}</p>
                    </div>
                    <div class="og">
                        <p class="type-label-md">Website layout made by <a href="https://tsl.pages.dev/" target="_blank">TheShittyList</a></p>
                    </div>
                    <template v-if="editors">
                        <h3>List Editors</h3>
                        <ol class="editors">
                            <li v-for="editor in editors">
                                <img :src="\`/assets/\${roleIconMap[editor.role]}-dark.svg\`" :alt="editor.role">
                                <a v-if="editor.link" class="type-label-lg link" target="_blank" :href="editor.link">{{ editor.name }}</a>
                                <p v-else>{{ editor.name }}</p>
                            </li>
                        </ol>
                    </template>
                    <h3>Description</h3>
                    <p>
                        This is the list for classic levels made by server members.
                    </p>
                    <p>
                        For the full list, check out <a href="https://docs.google.com/spreadsheets/d/1rUbKDpv_LYnAlNvJs7ObY4_x8OflzSpu5H34n1S55Gs/edit?gid=0#gid=0" target="_blank" rel="noopener noreferrer"> <u> our spreadsheet </u> </a>
                    </p>
                </div>
            </div>
        </main>
    `,
    data: () => ({
        list: [],
        editors: [],
        loading: true,
        selected: 0,
        errors: [],
        roleIconMap,
        store
    }),
    computed: {
        level() {
            return this.list[this.selected][0];
        },
        video() {
            if (!this.level.showcase) {
                return embed(this.level.verification);
            }

            return embed(
                this.toggledShowcase
                    ? this.level.showcase
                    : this.level.verification
            );
        },
    },
    async mounted() {
        // Hide loading spinner
        this.list = await fetchList();
        this.editors = await fetchEditors();

        // Error handling
        if (!this.list) {
            this.errors = [
                "Failed to load list. Retry in a few minutes or notify list staff.",
            ];
        } else {
            this.errors.push(
                ...this.list
                    .filter(([_, err]) => err)
                    .map(([_, err]) => {
                        return `Failed to load level. (${err}.json)`;
                    })
            );
            if (!this.editors) {
                this.errors.push("Failed to load list editors.");
            }
        }

        this.loading = false;
    },
    methods: {
        embed
    },
};
