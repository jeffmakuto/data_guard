import { createStore } from 'vuex';

const store = createStore({
  state: {
    token: sessionStorage.getItem('token') || '',
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      sessionStorage.setItem('token', token);
    },
    clearToken(state) {
      state.token = '';
      sessionStorage.removeItem('token');
    },
  },
  actions: {
    login({ commit }, token) {
      commit('setToken', token);
    },
    logout({ commit }) {
      commit('clearToken');
    },
  },
  getters: {
    isAuthenticated: state => !!state.token,
  },
});

export default store;
