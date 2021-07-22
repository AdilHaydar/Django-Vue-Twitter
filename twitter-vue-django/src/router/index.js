import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'


import Home from '../views/Home.vue'
import Profile from '../views/Profile'
import Explore from '../views/Explore'
import Settings from '../views/Settings'
import Notification from '../views/Notification'
import Root from '../views/Root'
import Login from '../views/Login'

const routes = [
  {
    path: '/',
    component: Root,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home
      },
      {
        path: '/explore',
        name: 'Explore',
        component: Explore
      },
      {
        path: '/settings',
        name: 'Settings',
        component: Settings,
        meta: {
          requireLogin: true
        }
      },
      {
        path: '/profile',
        name: 'Profile',
        component: Profile
      },
      {
        path: '/notification',
        name: 'Notification',
        component: Notification,
        meta: {
          requireLogin: true
        }
      },
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'Login', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
