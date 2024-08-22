export default {
    props: {
        author: {
            type: String,
            required: true,
        },
        verifier: {
            type: String,
            required: true,
        },
        first_victor:{
            type: String,
            required: true,
        }
    },
    template: `
        <div class="level-authors">
            <div class="type-title-sm">Publisher</div>
            <p class="type-body">
                <span>{{ author }}</span>
            </p>
            <div class="type-title-sm">Verifier</div>
            <p class="type-body">
                <span>{{ verifier }}</span>
            </p>
            <div class="type-title-sm">First OBG Victor</div>
            <p class="type-body">
                <span>{{ first_victor }}</span>
            </p>
        </div>
    `,
};
