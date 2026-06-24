/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#92B1A5',
          dark: '#7A9C90',
        },
        secondary: {
          DEFAULT: '#DA8C91',
        },
        accent: {
          DEFAULT: '#DEB4C4',
        },
        neutral: {
          light: '#DDD2D2',
        },
        background: {
          DEFAULT: '#F8F6F4',
        },
        foreground: {
          DEFAULT: '#2E2E2E',
        },
      },
      fontFamily: {
        serif: ['Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif'],
        sans: ['-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', '"Helvetica Neue"', 'Arial', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
