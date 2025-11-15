import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    cors: true,
    proxy: {
      '/api': 'http://localhost:8000' // Backend-URL
    }
  }
})
