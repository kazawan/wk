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

---
## ✈️Prisma 使用SQLite
[参考:使用 Prisma 将 API 和数据库添加到您的 Nuxt 应用程序](https://devpress.csdn.net/vue/62f14b6e7e668234661840b4.html)


### :hammer:Prisma 安装

```shell
npm install --save-dev prisma
npm install @prisma/client

```

### :gear: Prisma init 初始化
```sh
npx prisma init
```

### 修改`prisma\schema.prisma`文件
```js
// schema.prisma
datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

generator client {
  provider = "prisma-client-js"
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  published Boolean  @default(false)
  author    User?    @relation(fields: [authorId], references: [id])
  authorId  Int?
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}
```


### 同步数据库架构 
```sh
npx prisma migrate dev --name init
```

### 生成客户端
```sh
npx prisma generate
```

### 打开prisma客户端

```sh
npx prisma studio
```
此时可以在客户端界面操作数据库

### nuxt api 控制CRUD
在`./server/api/` 下生成`getAll.js`
```js
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

const getCount = async () => {
    return await prisma.counts.findMany()
}

export default defineEventHandler(async(event)=>{
    try{
        const counts = await getCount()
        return {
            statusCode: 200,
            body: JSON.stringify(counts)
        }
    }catch(err){
        return {
            statusCode: 500,
            body: JSON.stringify(err)
        }
    }
    
})
```

打开浏览器输入`http://localhost:$port/api/getAll`
返回
```sh
{
  "statusCode": 200,
  "body": "[{\"id\":1,\"count\":100}]"
}
```




