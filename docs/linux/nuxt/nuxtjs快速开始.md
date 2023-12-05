# NUXTJS 快速开始
---
## :book:参考
[🌐NUXT文档](https://nuxt.com/docs/getting-started/installation)

### :hammer: 安装

```bash
npx nuxi@latest init <project-name>
```
?> 如安装失败需配置一下系统的host,
`C:\Windows\System32\drivers\etc` 修改 `host`文件
添加 `185.199.108.133 raw.githubusercontent.com`

### :gear:启动
```
cd  <project-name>
npm install
npm run dev
```

******

## :pen:Nuxt Tailwindcss

[🌐:computer:Module地址](https://nuxt.com/modules/tailwindcss)
[🌐tailwindcss 中文官网](https://www.tailwindcss.cn/)
[🌐简单配色表](https://www.peisebiao.com/)
### :hammer:安装
```bash
# Using pnpm
pnpm add --save-dev @nuxtjs/tailwindcss

# Using yarn
yarn add --dev @nuxtjs/tailwindcss

# Using npm
npm install --save-dev @nuxtjs/tailwindcss
```

### :gear:配置
在`nuxt.config.ts` 添加 modules
```bash
{
  modules: [
    '@nuxtjs/tailwindcss'
  ]
}
```

---
## :rocket:Nuxt 路由
[🌐Nuxt Routing](https://nuxt.com/docs/getting-started/routing)

### 📁项目新建pages文件夹

```sh
🎹目录结构
| pages/
---| about.vue
---| index.vue
---| posts/
-----| [id].vue
```

未完...