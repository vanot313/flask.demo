webpackJsonp([1],{"+VVd":function(t,e){},"+nmv":function(t,e){},"4lOj":function(t,e){},"89IR":function(t,e){},"9VFh":function(t,e){},FJrj:function(t,e){},Hv02:function(t,e){},NHnr:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=s("7+uW"),n=s("Dd8w"),o=s.n(n),r=s("BO1k"),a=s.n(r),c={methods:{notify:function(t,e){this.$notify({title:t,type:e})},attachImageUrl:function(t){return t?this.$store.state.configure.HOST+t||"../assets/img/user.jpg":""},attachBirth:function(t){var e=String(t).match(/[0-9-]+(?=\s)/);return Array.isArray(e)?e[0]:e},replaceFName:function(t){return t.split("-")[1]},replaceLName:function(t){return t.split("-")[0]},toplay:function(t,e,s,i,n,o){this.$store.commit("setId",t),this.$store.commit("setListIndex",i),this.$store.commit("setUrl",this.$store.state.configure.HOST+e),this.$store.commit("setpicUrl",this.$store.state.configure.HOST+s),this.$store.commit("setTitle",this.replaceFName(n)),this.$store.commit("setArtist",this.replaceLName(n)),this.$store.commit("setLyric",this.parseLyric(o))},parseLyric:function(t){for(var e=t.split("\n"),s=/\[\d{2}:\d{2}.(\d{3}|\d{2})\]/g,i=[];!s.test(e[0]);)e=e.slice(1);0===e[e.length-1].length&&e.pop();var n=!0,o=!1,r=void 0;try{for(var c,l=a()(e);!(n=(c=l.next()).done);n=!0){var u=c.value,h=u.match(s),d=u.replace(s,""),m=!0,g=!1,f=void 0;try{for(var p,v=a()(h);!(m=(p=v.next()).done);m=!0){var y=p.value.slice(1,-1).split(":");""!==d&&i.push([60*parseInt(y[0],10)+parseFloat(y[1]),d])}}catch(t){g=!0,f=t}finally{try{!m&&v.return&&v.return()}finally{if(g)throw f}}}}catch(t){o=!0,r=t}finally{try{!n&&l.return&&l.return()}finally{if(o)throw r}}return i.sort(function(t,e){return t[0]-e[0]}),i},getSong:function(){var t=this;this.$route.query.keywords?this.$api.songAPI.getSongOfSingerName(this.$route.query.keywords).then(function(e){e.data.length?t.$store.commit("setListOfSongs",e.data):(t.$store.commit("setListOfSongs",[]),t.notify("系统暂无该歌曲","warning"))}).catch(function(t){console.log(t)}):(this.$store.commit("setListOfSongs",[]),this.notify("您输入内容为空","warning"))}}},l=s("NYxO"),u={name:"the-aside",mixins:[c],computed:o()({},Object(l.b)(["id","listOfSongs","showAside"])),mounted:function(){var t=this;document.addEventListener("click",function(){t.$store.commit("setShowAside",!1)},!0)}},h={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("transition",{attrs:{name:"slide-fade"}},[t.showAside?s("div",{staticClass:"the-aside"},[s("h2",{staticClass:"title"},[t._v("播放列表")]),t._v(" "),s("ul",{staticClass:"menus"},t._l(t.listOfSongs,function(e,i){return s("li",{key:i,class:{"is-play":t.id===e.id},on:{click:function(s){return t.toplay(e.id,e.url,e.pic,i,e.name,e.lyric)}}},[t._v("\n        "+t._s(t.replaceFName(e.name))+"\n      ")])}),0)]):t._e()])},staticRenderFns:[]};var d=s("VU/8")(u,h,!1,function(t){s("9VFh")},"data-v-27171de2",null).exports,m=[{name:"首页",path:"/home"},{name:"估值",path:"/song-list"},{name:"评定信息",path:"/singer"},{name:"我的信息",path:"/my-music"}],g=[{name:"登录",path:"/"},{name:"注册",path:"/login-up"}],f=[{name:"个人信息",path:"/info"},{name:"修改头像",path:"/upLoad"},{name:"退出",path:0}],p={name:"the-header",mixins:[c],data:function(){return{SystemName:"Data Analysis",navMsg:[],loginMsg:[],menuList:[],keywords:""}},computed:o()({},Object(l.b)(["userId","activeName","avator","username","loginIn"])),created:function(){this.navMsg=m,this.loginMsg=g,this.menuList=f},methods:{show:function(){document.querySelector("#user").addEventListener("click",function(t){document.querySelector(".menu").classList.add("show"),t.stopPropagation()},!1),document.querySelector(".menu").addEventListener("click",function(t){t.stopPropagation()},!1),document.addEventListener("click",function(){document.querySelector(".menu").classList.remove("show")},!1)},goHome:function(){this.$router.push({path:"/home"})},goPage:function(t,e){document.querySelector(".menu").classList.remove("show"),this.changeIndex(e),this.loginIn||"/my-music"!==t?this.$router.push({path:t}):this.notify("请先登录","warning")},changeIndex:function(t){this.$store.commit("setActiveName",t)},goMenuList:function(t){document.querySelector(".menu").classList.remove("show"),t?this.$router.push({path:t}):(this.$store.commit("setLoginIn",!1),this.$router.go(0))},goSearch:function(){this.$store.commit("setSearchword",this.keywords),this.$router.push({path:"/search",query:{keywords:this.keywords}})}}},v={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"the-header"},[s("div",{staticClass:"head-logo",on:{click:t.goHome}},[s("div",{staticClass:"logo-hd"},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-erji"}})])]),t._v(" "),s("span",[t._v(t._s(t.SystemName))])]),t._v(" "),s("ul",{ref:"change",staticClass:"navbar"},[t._l(t.navMsg,function(e){return s("li",{key:e.path,class:{active:e.name===t.activeName},on:{click:function(s){return t.goPage(e.path,e.name)}}},[t._v("\n      "+t._s(e.name)+"\n    ")])}),t._v(" "),s("li",[s("div",{staticClass:"head-search"},[s("input",{directives:[{name:"model",rawName:"v-model",value:t.keywords,expression:"keywords"}],attrs:{type:"text",placeholder:"搜索公司"},domProps:{value:t.keywords},on:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.goSearch()},input:function(e){e.target.composing||(t.keywords=e.target.value)}}}),t._v(" "),s("div",{staticClass:"search-btn",on:{click:function(e){return t.goSearch()}}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-sousuo"}})])])])]),t._v(" "),t._l(t.loginMsg,function(e){return t.loginIn?t._e():s("li",{key:e.type,class:{active:e.name===t.activeName},on:{click:function(s){return t.goPage(e.path,e.name)}}},[t._v(t._s(e.name))])})],2),t._v(" "),s("ul",{staticClass:"menu"},t._l(t.menuList,function(e,i){return s("li",{key:i,on:{click:function(s){return t.goMenuList(e.path)}}},[t._v(t._s(e.name))])}),0),t._v(" "),t.loginIn?s("div",{attrs:{id:"user"},on:{click:function(e){return t.show()}}},[s("img",{attrs:{src:t.attachImageUrl(t.avator),alt:""}})]):t._e()])},staticRenderFns:[]};var y=s("VU/8")(p,v,!1,function(t){s("4lOj")},"data-v-797dd023",null).exports,w={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"the-footer"},t._l(t.list,function(e,i){return s("p",{key:i},[t._v("\n    "+t._s(e)+"\n  ")])}),0)},staticRenderFns:[]};var I=s("VU/8")({name:"the-footer",data:function(){return{list:["关于 | 帮助 | 条款 | 反馈","Copyright ©XXX 2019"]}}},w,!1,function(t){s("m5vJ")},"data-v-30c4158a",null).exports,_={name:"scroll-top",methods:{returnTop:function(){var t=null;cancelAnimationFrame(t);var e=new Date,s=document.body.scrollTop||document.documentElement.scrollTop,i=500;t=requestAnimationFrame(function n(){var o=new Date-e,r=i-Math.max(0,i-o);document.documentElement.scrollTop=document.body.scrollTop=s-r*s/i,t=requestAnimationFrame(n),r===i&&cancelAnimationFrame(t)})}}},$={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"scroll-top",on:{click:this.returnTop}},[e("div",{staticClass:"box-in"})])},staticRenderFns:[]};var x=s("VU/8")(_,$,!1,function(t){s("+VVd")},"data-v-cfe6b7b2",null).exports,S={name:"song-audio",computed:o()({},Object(l.b)(["id","url","listOfSongs","isPlay","curTime","changeTime","autoNext"])),watch:{isPlay:function(){this.togglePlay()},changeTime:function(){this.$refs.player.currentTime=this.changeTime}},methods:{togglePlay:function(){var t=this.$refs.player;this.isPlay?t.play():t.pause()},startPlay:function(){var t=this.$refs.player;this.$store.commit("setDuration",t.duration),t.play(),this.$store.commit("setIsPlay",!0)},timeupdate:function(){var t=this.$refs.player;this.$store.commit("setCurTime",t.currentTime)},ended:function(){this.$store.commit("setIsPlay",!1),this.$store.commit("setCurTime",0),this.$store.commit("setAutoNext",!this.autoNext)}}},C={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"song-audio"},[e("audio",{ref:"player",attrs:{src:this.url,controls:"controls",preload:"true"},on:{canplay:this.startPlay,timeupdate:this.timeupdate,ended:this.ended}})])},staticRenderFns:[]};var k=s("VU/8")(S,C,!1,function(t){s("+nmv")},null,null).exports,L={name:"play-bar",mixins:[c],data:function(){return{tag:!1,nowTime:"00:00",songTime:"00:00",curLength:0,progressLength:0,mouseStartX:0,toggle:!0}},computed:o()({},Object(l.b)(["loginIn","userId","isPlay","playButtonUrl","id","url","title","artist","picUrl","curTime","duration","listOfSongs","listIndex","showAside","autoNext"])),watch:{isPlay:function(t){t?this.$store.commit("setPlayButtonUrl","#icon-zanting"):this.$store.commit("setPlayButtonUrl","#icon-bofang")},curTime:function(){this.nowTime=this.formatSeconds(this.curTime),this.songTime=this.formatSeconds(this.duration),this.curLength=this.curTime/this.duration*100},autoNext:function(){this.next()}},mounted:function(){this.progressLength=this.$refs.progress.getBoundingClientRect().width},methods:{download:function(){var t=this;this.$api.songAPI.download(this.url).then(function(e){var s=e.data,i=document.createElement("a");i.download=t.artist+"-"+t.title+".mp3",i.style.display="none";var n=new Blob([s]);i.href=URL.createObjectURL(n),document.body.appendChild(i),i.click(),document.body.removeChild(i)}).catch(function(t){console.log(t)})},changeAside:function(){var t=!this.showAside;this.$store.commit("setShowAside",t)},togglePlay:function(){this.isPlay?this.$store.commit("setIsPlay",!1):this.$store.commit("setIsPlay",!0)},formatSeconds:function(t){var e=parseInt(t),s=0,i=0;if(e>60&&(s=parseInt(e/60),e=parseInt(e%60),s>60&&(i=parseInt(s/60),s=60)),parseInt(e)<10)var n="0:0"+parseInt(e);else n="0:"+parseInt(e);return s>0&&(n=parseInt(e)<10?"0"+parseInt(e):parseInt(e),n=parseInt(s)+":"+n),i>0&&(n=parseInt(e)<10?"0"+parseInt(e):parseInt(e),n=parseInt(i)+":"+parseInt(s)+":"+n),n},mousedown:function(t){this.mouseStartX=t.clientX,this.tag=!0},mouseup:function(){this.tag=!1},mousemove:function(t){if(!this.duration)return!1;if(this.tag){var e=t.clientX-this.mouseStartX,s=this.$refs.curProgress.getBoundingClientRect().width;this.progressLength=this.$refs.progress.getBoundingClientRect().width;var i=(s+e)/this.progressLength*100;i>100&&(i=100),this.curLength=i,this.mouseStartX=t.clientX,this.changeTime(i)}},changeTime:function(t){var e=this.duration*(.01*t);this.$store.commit("setChangeTime",e)},updatemove:function(t){if(!this.tag){var e=this.$refs.bg.offsetLeft;this.progressLength=this.$refs.progress.getBoundingClientRect().width;var s=(t.clientX-e)/this.progressLength*100;s<0?s=0:s>100&&(s=100),this.curLength=s,this.changeTime(s)}},prev:function(){-1!==this.listIndex&&this.listOfSongs.length>1&&(this.listIndex>0?(this.$store.commit("setListIndex",this.listIndex-1),this.toPlay(this.listOfSongs[this.listIndex].url)):(this.$store.commit("setListIndex",this.listOfSongs.length-1),this.toPlay(this.listOfSongs[this.listIndex].url)))},next:function(){-1!==this.listIndex&&this.listOfSongs.length>1&&(this.listIndex<this.listOfSongs.length-1?(this.$store.commit("setListIndex",this.listIndex+1),this.toPlay(this.listOfSongs[this.listIndex].url)):(this.$store.commit("setListIndex",0),this.toPlay(this.listOfSongs[0].url)))},toPlay:function(t){t&&t!==this.url&&(this.$store.commit("setId",this.listOfSongs[this.listIndex].id),this.$store.commit("setUrl",this.$store.state.configure.HOST+t),this.$store.commit("setpicUrl",this.$store.state.configure.HOST+this.listOfSongs[this.listIndex].pic),this.$store.commit("setTitle",this.replaceFName(this.listOfSongs[this.listIndex].name)),this.$store.commit("setArtist",this.replaceLName(this.listOfSongs[this.listIndex].name)),this.$store.commit("setLyric",this.parseLyric(this.listOfSongs[this.listIndex].lyric)))},goPlayerPage:function(){this.$router.push({path:"/lyric/"+this.id})},collection:function(){var t=this;this.loginIn?this.$api.collectionAPI.setCollection(this.userId,0,this.id).then(function(e){1===e.data.code?t.notify("收藏成功","success"):2===e.data.code?t.notify("已收藏","warning"):t.$notify.error({title:"收藏失败",showClose:!1})}).catch(function(t){console.log(t)}):this.notify("请先登录","warning")}}},O={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"play-bar",class:{show:!t.toggle}},[s("div",{staticClass:"item-up",class:{turn:t.toggle},on:{click:function(e){t.toggle=!t.toggle}}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-jiantou-xia-cuxiantiao"}})])]),t._v(" "),s("div",{staticClass:"kongjian"},[s("div",{staticClass:"item",on:{click:t.prev}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-ziyuanldpi"}})])]),t._v(" "),s("div",{staticClass:"item",on:{click:t.togglePlay}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":t.playButtonUrl}})])]),t._v(" "),s("div",{staticClass:"item",on:{click:t.next}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-ziyuanldpi1"}})])]),t._v(" "),s("div",{staticClass:"item-img",on:{click:t.goPlayerPage}},[s("img",{attrs:{src:t.picUrl,alt:""}})]),t._v(" "),s("div",{staticClass:"playing-speed"},[s("div",{staticClass:"current-time"},[t._v(t._s(t.nowTime))]),t._v(" "),s("div",{staticClass:"progress-box"},[s("div",{staticClass:"item-song-title"},[s("div",[t._v(t._s(this.title))]),t._v(" "),s("div",[t._v(t._s(this.artist))])]),t._v(" "),s("div",{ref:"progress",staticClass:"progress",on:{mousemove:t.mousemove}},[s("div",{ref:"bg",staticClass:"bg",on:{click:t.updatemove}},[s("div",{ref:"curProgress",staticClass:"cur-progress",style:{width:t.curLength+"%"}})]),t._v(" "),s("div",{ref:"idot",staticClass:"idot",style:{left:t.curLength+"%"},on:{mousedown:t.mousedown,mouseup:t.mouseup}})])]),t._v(" "),s("div",{staticClass:"left-time"},[t._v(t._s(t.songTime))])]),t._v(" "),s("div",{staticClass:"item",on:{click:t.collection}},[s("el-button",{staticStyle:{border:"0"},attrs:{plain:""}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-xihuan-shi"}})])])],1),t._v(" "),s("div",{staticClass:"item",on:{click:t.download}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-xiazai"}})])]),t._v(" "),s("div",{staticClass:"item",on:{click:t.changeAside}},[s("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[s("use",{attrs:{"xlink:href":"#icon-liebiao"}})])])])])},staticRenderFns:[]};var T={name:"App",components:{PlayBar:s("VU/8")(L,O,!1,function(t){s("89IR")},"data-v-1a285014",null).exports,SongAudio:k,ScrollTop:x,TheAside:d,TheHeader:y,TheFooter:I}},P={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("the-header"),this._v(" "),e("the-aside"),this._v(" "),e("router-view",{staticClass:"content"}),this._v(" "),e("scroll-top"),this._v(" "),e("the-footer")],1)},staticRenderFns:[]};var b=s("VU/8")(T,P,!1,function(t){s("gbLa")},null,null).exports,A=s("/ocq"),N={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"login-logo"},[e("div",{staticClass:"item-logo"},[e("svg",{staticClass:"icon",attrs:{"aria-hidden":"true"}},[e("use",{attrs:{"xlink:href":"#icon-erji"}})])])])},staticRenderFns:[]};var F={name:"login-in",components:{LoginLogo:s("VU/8")({name:"login-logo"},N,!1,function(t){s("FJrj")},"data-v-733aa425",null).exports},mixins:[c],data:function(){return{loginForm:{username:"",password:""},rules:{username:[{validator:function(t,e,s){if(!e)return s(new Error("用户名不能为空"));s()},message:"请输入用户名",trigger:"blur"}],password:[{validator:function(t,e,s){""===e?s(new Error("请输入密码")):s()},message:"请输入密码",trigger:"blur"}]}}},mounted:function(){this.changeIndex("登录")},methods:{changeIndex:function(t){this.$store.commit("setActiveName",t)},loginIn:function(){var t=this;t.$api.userAPI.loginIn(this.loginForm.username,this.loginForm.password).then(function(e){1===e.data.code?(t.notify("登录成功","success"),t.setUserMsg(e.data.userMsg[0]),t.$store.commit("setLoginIn",!0),setTimeout(function(){t.changeIndex("首页"),t.$router.push({path:"/home"}),t.$router.go(0)},2e3)):t.notify("用户名或密码错误","error")}).catch(function(t){})},setUserMsg:function(t){this.$store.commit("setUserId",t.id),this.$store.commit("setUsername",t.username),this.$store.commit("setAvator",t.avator)},goLoginUp:function(){this.$router.push({path:"/login-up"})}}},U={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"login-in"},[s("login-logo"),t._v(" "),s("div",{staticClass:"login"},[t._m(0),t._v(" "),s("el-form",{ref:"loginForm",staticClass:"demo-ruleForm",attrs:{model:t.loginForm,"status-icon":"",rules:t.rules}},[s("el-form-item",{attrs:{prop:"username"}},[s("el-input",{attrs:{placeholder:"用户名"},model:{value:t.loginForm.username,callback:function(e){t.$set(t.loginForm,"username",e)},expression:"loginForm.username"}})],1),t._v(" "),s("el-form-item",{attrs:{prop:"password"}},[s("el-input",{attrs:{type:"password",placeholder:"密码"},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.loginIn(e)}},model:{value:t.loginForm.password,callback:function(e){t.$set(t.loginForm,"password",e)},expression:"loginForm.password"}})],1),t._v(" "),s("div",{staticClass:"login-btn"},[s("el-button",{on:{click:function(e){return t.goLoginUp()}}},[t._v("注册")]),t._v(" "),s("el-button",{attrs:{type:"primary"},on:{click:t.loginIn}},[t._v("登录")])],1)],1)],1)],1)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"login-head"},[e("span",[this._v("帐号登录")])])}]};var E=s("VU/8")(F,U,!1,function(t){s("Hv02")},"data-v-21a46218",null).exports;i.default.use(A.a);var R=new A.a({routes:[{path:"/",name:"login-in",component:E}]}),V=s("gyMJ"),j=s.n(V),q=s("zL8q"),M=s.n(q),B=s("mvHQ"),H=s.n(B),J={state:{HOST:"http://localhost:8888",loginIn:!1,searchword:"",showAside:!1,activeName:"",index:0},getters:{loginIn:function(t){var e=t.loginIn;return e||(e=JSON.parse(window.sessionStorage.getItem("loginIn")||null)),e},activeName:function(t){var e=t.activeName;return e||(e=JSON.parse(window.sessionStorage.getItem("activeName")||null)),e},showAside:function(t){var e=t.showAside;return e||(e=JSON.parse(window.sessionStorage.getItem("showAside")||null)),e},index:function(t){var e=t.index;return e||(e=JSON.parse(window.sessionStorage.getItem("index")||null)),e},searchword:function(t){return t.searchword}},mutations:{setLoginIn:function(t,e){t.loginIn=e,window.sessionStorage.setItem("loginIn",H()(e))},setActiveName:function(t,e){t.activeName=e,window.sessionStorage.setItem("activeName",H()(e))},setShowAside:function(t,e){t.showAside=e,window.sessionStorage.setItem("showAside",H()(e))},setIndex:function(t,e){t.index=e},setSearchword:function(t,e){t.searchword=e}},actions:{}},X={state:{userId:"",username:"",avator:""},getters:{userId:function(t){var e=t.userId;return e||(e=JSON.parse(window.localStorage.getItem("userId")||null)),e},username:function(t){var e=t.username;return e||(e=JSON.parse(window.localStorage.getItem("username")||null)),e},avator:function(t){var e=t.avator;return e||(e=JSON.parse(window.localStorage.getItem("avator")||null)),e}},mutations:{setUserId:function(t,e){t.userId=e,window.localStorage.setItem("userId",H()(e))},setUsername:function(t,e){t.username=e,window.localStorage.setItem("username",H()(e))},setAvator:function(t,e){t.avator=e,window.localStorage.setItem("avator",H()(e))}},actions:{}};i.default.use(l.a);var z=new l.a.Store({modules:{configure:J,user:X}});s("tvR6"),s("VaBq");i.default.use(M.a),i.default.config.productionTip=!1,i.default.prototype.$api=j.a,new i.default({el:"#app",router:R,store:z,components:{App:b},template:"<App/>"})},VaBq:function(t,e){},gbLa:function(t,e){},gyMJ:function(t,e){},m5vJ:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.779709469a00660e001a.js.map