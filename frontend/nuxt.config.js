module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'Dollar Variation | Fernando Saavedra',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Dolar Currency' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: "stylesheet", href: "https://fonts.googleapis.com/css?family=Lato:300,300i,400,400i,700,700i,900,900i"},
      { rel: "stylesheet", href: "https://fonts.googleapis.com/css?family=Roboto:900"},
      { rel: "stylesheet", href: "/css/style.css"},
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },

  plugins: [
    { src: "~/plugins/chart", ssr: false }
  ],

  modules: [
    '@nuxtjs/axios',
  ],

  axios: {
    // proxyHeaders: false
  },



  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}

