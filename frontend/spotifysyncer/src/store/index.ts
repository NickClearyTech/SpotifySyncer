import {createStore} from "vuex";

export const store = createStore({
    state: {
        spotifyFlowCode: null
    },
    mutations: {
        setFlowCode (state, code) {
            state.spotifyFlowCode = code
        }
    }
})