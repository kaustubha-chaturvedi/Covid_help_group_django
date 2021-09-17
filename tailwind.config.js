module.exports = {
  purge: {
    preserveHtmlElements: true,
    content: [
      './CHP/templates/*.html',
      './CHP/templates/**/*.html'
    ]
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
