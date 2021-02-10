# Vue项目的实践经历

##  2.8

1、vue项目的搭建：![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

2、vue项目在pycharm中进行前后端分离的操作，启动指令：在终端输入：npm run dev ；

此为热部署操作，可进行动态修改。

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

3、vue项目的结构主要如下图所示：

![IMG_263](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)

4、在vue项目中引入第三方组件：axios，vuex，element-ui。

vuex：Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。核心是store(仓库)

5、此处的data不可省略小括号，此为固定格式。尽量多的使用插值表达式，加入将下图中的msg引入，在table下加入{{msg}}即可，data下可传输相应的数据

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)

6、每添加一个路由，需要在routes中加入一个新的路径，路由目录router/index.js。

7、不同于jsp中的遍历，vue使用v-for进行操作

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

8、create函数：初始化函数，在页面一开始就会显示出来

9、解决跨越问题：![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)

或者在控制类之上加载@crossOrigin(origins={“http：//localhost:8080”,”null”})

10、vue项目架构

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg)

## 2.9

11、在编写样式的时候出现了错误，需要使用以下命令进行样式的安装。

- 如果是 **`常规`** 的，执行 **`npm install style-loader css-loader style-loader --save-dev`** 安装依赖就行。
- 如果是 **`less`** 的，执行 **`npm install less less-loader --save-dev`** 安装依赖就行。
- 如果是 **`sass`** 的，执行 **`npm install sass sass-loader --save-dev`** 安装依赖就行。或者（`$npm intall sass-loader --save ; $npm install node-sass --save`）

12、有关element的相关知识点

- <el-form>：代表这是一个表单
- <el-form> -> ref：表单被引用时的名称，标识
- <el-form> -> rules：表单验证规则
- <el-form> -> model：表单数据对象
- <el-form> -> label-width：表单域标签的宽度，作为 Form 直接子元素的 form-item 会继承该值
- <el-form> -> <el-form-item>：表单中的每一项子元素
- <el-form-item> -> label：标签文本
- <el-form-item> -> prop：表单域 model 字段，在使用 validate、resetFields 方法的情况下，该属性是必填的
- <el-input>：输入框
- <el-input> -> v-model：绑定的表单数据对象属性
- <el-input> -> style：行内样式
- <el-input> -> maxlength：最大字符长度限制

13、在表单中加入了校验器，但是因为js和vue项目的不熟练，碰了很多的钉子，总体进度而言比较慢，因为不熟悉，仅完成了登录。在idea测试时，css的嵌套也出了很多问题，比如元素嵌套直接报错？但是已经有思路了和时间方法了，所以接下去的进度会逐渐加快



