### 2021年2月10日

vue-router笔记

1. 步骤一: 安装vue-router
   `npm install vue-router --save`

2. 步骤二: 在模块化工程中使用它(因为是一个插件, 所以可以通过Vue.use()来安装路由功能)

   使用vue-router的步骤:

   1. 第一步：导入路由对象，并且调用 Vue.use(VueRouter)
      `javascript import Vue from 'vue' import VueRouter from 'vue-router' Vue.use(VueRouter)`

   2. 第二步：创建路由实例，并且传入路由映射配置

   3. 步骤二：配置组件和路径的映射关系

   4. 步骤三：使用路由

   5. `<router-link>`: 该标签是一个vue-router中已经内置的组件, 它会被渲染成一个`<a>`标签.

   6. `<router-view>`: 该标签会根据当前的路径, 动态渲染出不同的组件.

   7. 网页的其他内容, 比如顶部的标题/导航, 或者底部的一些版权信息等会和`<router-view>`处于同一个等级.

   8. 在路由切换时, 切换的是`<router-view>`挂载的组件, 其他内容不会发生改变.

      - 在前面的`<router-link>`中, 我们只是使用了一个属性: to, 用于指定跳转的路径.
      - `<router-link>`还有一些其他属性:

      1. tag: tag可以指定`<router-link>`之后渲染成什么组件, 比如上面的代码会被渲染成一个`<li>`元素, 而不是`<a>`
      2. replace: replace不会留下history记录, 所以指定replace的情况下, 后退键返回不能返回到上一个页面中
      3. active-class: 当`<router-link>`对应的路由匹配成功时, 会自动给当前元素设置一个router-link-active的class, 设置active-class可以修改默认的名称.
         在进行高亮显示的导航菜单或者底部tabbar时, 会使用到该类.
         但是通常不会修改类的属性, 会直接使用默认的router-link-active即可.

#### 明天任务

给出各页面详细需求分析文档

数据库脚本

完成router和vuex的学习



### 2021年2月9日

#### webpack的基本功能和使用

npm init
	创建package.json

UnhandledPromiseRejectionWarning: TypeError: this.getResolve is not a function
	原因：css-loader版本过高

npm install vue-loader vue-template-compiler --save-dev

​	将转化vue文件

npm i -D postcss-loader
	解决scoped中的样式无法加载

npm install html-webpack-plugin --save-dev

#### vuecli的安装和使用

#### 明天任务

* 项目环境搭建

  



