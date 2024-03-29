import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

// https://vitejs.dev/config/
export default defineConfig({


  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    host: "0.0.0.0",
    port: "3000",
    proxy: {
      '/skill': {
        target: 'http://localhost:5000/'
      },
      '/staff' : {
        target: 'http://localhost:5000/'
      },
      '/course' : {
        target: 'http://localhost:5000/'
      },
      '/courseSkill' : {
        target: 'http://localhost:5000/'
      },
      '/skill_to_course': {
        target: 'http://localhost:5000/'
      },
      '/job_role': {
        target: 'http://localhost:5000/'
      },
      '/registration': {
        target: 'http://localhost:5000/'
      },
    }
  },
});
