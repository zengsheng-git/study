import { defineConfig } from 'dumi';

// 配置githup pages 上的路径
const fixpath=process.env.NODE_ENV === 'production' ? '/study/' : '/';

export default defineConfig({
  outputPath: 'dist', // 打包之后生成的文件夹
  themeConfig: {
    name: '编程文档',
    logo: fixpath +"logo.webp",  // logo路劲
    footer: "“无人问津也好，技不如人也罢，你都要试着安静下来，去做自己该做的事，而不是让内心的烦躁焦虑毁掉你本就不多的热情和定力” ——人民日报"
  },
  favicons: [fixpath +'logo.ico'], // icon路劲
  history: {
    type: "browser"
  },
  // analytics: {
  //   // 百度统计的 key
  //   baidu: 'XXXX',
  // },
  base: fixpath, // 文档起始路由
  // publicPath: "/" // 静态资源起始路径
  publicPath: fixpath , // 静态资源起始路径
});
