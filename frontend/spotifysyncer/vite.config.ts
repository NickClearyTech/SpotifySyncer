import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'


export default defineConfig(({command, mode}) => {
  const envDir = resolve(__dirname, "./src/environment");
  const env = loadEnv(mode, envDir);
  return {
    plugins: [vue()],
    build:{
      minify: false,
      emptyOutDir: true,
      manifest: true
    },
    envDir: envDir,
    base: env.VITE_APP_BASE_URL ?? "/",
    server:{
      port: 4436,
      host: true,
      proxy: {
        "/api": {
          target: env.VITE_API_FULL_URL,
          changeOrigin: true,
          secure: false,
          xfwd: true
        }
      }
    },
  }
});