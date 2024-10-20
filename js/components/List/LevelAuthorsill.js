export default {
    props: {
        author: {
            type: String,
            required: true,
        },
    },
    template: `
        <div class="level-authors">
            <div class="type-title-sm">Publisher</div>
            <p class="type-body">
                <span>{{ author }}</span>
            </p>
        </div>
    `,
};
