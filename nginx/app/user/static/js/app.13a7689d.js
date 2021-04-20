(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["app"],{0:function(e,n,t){e.exports=t("56d7")},"0f9a":function(e,n,t){"use strict";t.r(n);t("b0c0"),t("d3b7"),t("498a"),t("a4d3"),t("e01a");var r=t("c24f"),u=t("5f87"),o=t("a18c"),c={token:Object(u["a"])(),introduction:"",name:"",avatar:"",roles:[],id:""},a={SET_TOKEN:function(e,n){e.token=n},SET_INTRODUCTION:function(e,n){e.introduction=n},SET_NAME:function(e,n){e.name=n},SET_AVATAR:function(e,n){e.avatar=n&&""!==n&&"default"!==n?n:"default.jpg"},SET_ROLES:function(e,n){e.roles=n},SET_ID:function(e,n){e.id=n}},i={login:function(e,n){var t=e.commit,o=n.username,c=n.password;return new Promise((function(e,n){Object(r["f"])({username:o.trim(),password:c}).then((function(n){var r=n.data;t("SET_TOKEN",r.rolename),Object(u["c"])(r.rolename),e()})).catch((function(e){n(e)}))}))},getInfo:function(e){var n=e.commit,t=e.state;return new Promise((function(e,u){Object(r["c"])().then((function(r){var o=r.data;o||u("验证失败，请重新登录！"),o.roles=[t.token];var c=o.roles,a=o.username,i=o.avatar,s=o.description,d=o.id;(!c||c.length<=0)&&u("getInfo: roles must be a non-null array!"),n("SET_ROLES",c),n("SET_NAME",a),n("SET_AVATAR",i),n("SET_INTRODUCTION",s),n("SET_ID",d),e(o)})).catch((function(e){u(e)}))}))},logout:function(e){var n=e.commit,t=e.state;e.dispatch;return new Promise((function(e,c){Object(r["g"])(t.token).then((function(){n("SET_ID",""),n("SET_TOKEN",""),n("SET_ROLES",[]),Object(u["b"])(),Object(o["d"])(),e()})).catch((function(e){c(e)}))}))},resetToken:function(e){var n=e.commit;return new Promise((function(e){n("SET_TOKEN",""),n("SET_ROLES",[]),Object(u["b"])(),e()}))}};n["default"]={namespaced:!0,state:c,mutations:a,actions:i}},"24ab":function(e,n,t){e.exports={theme:"#1890ff"}},"31c2":function(e,n,t){"use strict";t.r(n),t.d(n,"filterAsyncRoutes",(function(){return c}));var r=t("5530"),u=(t("caad"),t("2532"),t("159b"),t("99af"),t("d3b7"),t("a18c"));function o(e,n){return!n.meta||!n.meta.roles||e.some((function(e){return n.meta.roles.includes(e)}))}function c(e,n){var t=[];return e.forEach((function(e){var u=Object(r["a"])({},e);o(n,u)&&(u.children&&(u.children=c(u.children,n)),t.push(u))})),t}var a={routes:[],addRoutes:[]},i={SET_ROUTES:function(e,n){e.addRoutes=n,e.routes=u["b"].concat(n)}},s={generateRoutes:function(e,n){var t=e.commit;return new Promise((function(e){var r;r=n.includes("user")?u["a"]||[]:c(u["a"],n),t("SET_ROUTES",r),e(r)}))}};n["default"]={namespaced:!0,state:a,mutations:i,actions:s}},4360:function(e,n,t){"use strict";t("13d5"),t("d3b7"),t("ddb0"),t("5319"),t("ac1f");var r=t("2b0e"),u=t("2f62"),o=(t("b0c0"),{token:function(e){return e.user.token},avatar:function(e){return e.user.avatar},name:function(e){return e.user.name},introduction:function(e){return e.user.introduction},roles:function(e){return e.user.roles},id:function(e){return e.user.id},permission_routes:function(e){return e.permission.routes}}),c=o;r["default"].use(u["a"]);var a=t("c653"),i=a.keys().reduce((function(e,n){var t=n.replace(/^\.\/(.*)\.\w+$/,"$1"),r=a(n);return e[t]=r.default,e}),{}),s=new u["a"].Store({modules:i,getters:c});n["a"]=s},"56d7":function(e,n,t){"use strict";t.r(n);t("e260"),t("e6cf"),t("cca6"),t("a79d");var r=t("2b0e"),u=t("a78e"),o=t.n(u),c=(t("f5df1"),t("5c96")),a=t.n(c),i=(t("24ab"),t("33bc")),s=t("5f5b"),d=t("e0ec"),f=t.n(d),l=t("98c9"),h=(t("b20f"),t("b5c9"),function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{attrs:{id:"app"}},[t("router-view")],1)}),p=[],m={name:"App"},b=m,g=t("2877"),v=Object(g["a"])(b,h,p,!1,null,null,null),k=v.exports,T=t("a18c"),E=t("4360"),O=t("5530"),_=t("1da1"),w=(t("96cf"),t("5319"),t("ac1f"),t("5f87")),x=["/index","/login","/register"];T["c"].beforeEach(function(){var e=Object(_["a"])(regeneratorRuntime.mark((function e(n,t,r){var u,o,a,i,s;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(u=Object(w["a"])(),!u){e.next=31;break}if("/login"!==n.path){e.next=6;break}r({path:"/dashboard"}),e.next=29;break;case 6:if(o=E["a"].getters.roles&&E["a"].getters.roles.length>0,!o){e.next=11;break}r(),e.next=29;break;case 11:return e.prev=11,e.next=14,E["a"].dispatch("user/getInfo");case 14:return a=e.sent,i=a.roles,e.next=18,E["a"].dispatch("permission/generateRoutes",i);case 18:s=e.sent,T["c"].addRoutes(s),n.redirectedFrom?T["c"].replace(n.redirectedFrom):r(Object(O["a"])(Object(O["a"])({},n),{},{replace:!0})),e.next=29;break;case 23:return e.prev=23,e.t0=e["catch"](11),e.next=27,E["a"].dispatch("user/resetToken");case 27:c["Message"].error(e.t0||"Has Error"),r("/login?redirect=".concat(n.path));case 29:e.next=32;break;case 31:-1!==x.indexOf(n.path)?r():r("/login?redirect=".concat(n.path));case 32:case"end":return e.stop()}}),e,null,[[11,23]])})));return function(n,t,r){return e.apply(this,arguments)}}()),T["c"].afterEach((function(){}));var S=t("f13c");r["default"].use(a.a,{size:o.a.get("size")||"medium"}),r["default"].use(l["a"]),r["default"].use(f.a),r["default"].use(S),r["default"].use(s["a"]),r["default"].use(i["a"]),r["default"].config.productionTip=!1,new r["default"]({el:"#app",router:T["c"],store:E["a"],render:function(e){return e(k)}})},"5f87":function(e,n,t){"use strict";t.d(n,"a",(function(){return c})),t.d(n,"c",(function(){return a})),t.d(n,"b",(function(){return i}));var r=t("a78e"),u=t.n(r),o="TOKEN";function c(){return u.a.get(o)}function a(e){return u.a.set(o,e)}function i(){return u.a.remove(o)}},a18c:function(e,n,t){"use strict";t.d(n,"b",(function(){return o})),t.d(n,"a",(function(){return c})),t.d(n,"d",(function(){return s}));t("d3b7"),t("3ca3"),t("ddb0");var r=t("2b0e"),u=t("8c4f");r["default"].use(u["a"]);var o=[{path:"/index",component:function(){return Promise.all([t.e("chunk-bba68bf6"),t.e("chunk-595dce2c")]).then(t.bind(null,"37f9"))},hidden:!0},{path:"/register",component:function(){return Promise.all([t.e("chunk-bba68bf6"),t.e("chunk-24b82e04")]).then(t.bind(null,"d5c2"))},hidden:!0},{path:"/login",component:function(){return Promise.all([t.e("chunk-bba68bf6"),t.e("chunk-1269b13a")]).then(t.bind(null,"9ed6"))},hidden:!0},{path:"/401",component:function(){return t.e("chunk-db206ccc").then(t.bind(null,"24e2"))},hidden:!0},{path:"/404",component:function(){return t.e("chunk-ae0128be").then(t.bind(null,"1db4"))},hidden:!0},{path:"/",redirect:"/index",hidden:!0},{path:"/dashboard",component:function(){return Promise.all([t.e("chunk-ab6acc54"),t.e("chunk-4b887efd")]).then(t.bind(null,"9406"))},hidden:!0},{path:"*",redirect:"/404",hidden:!0}],c=[{path:"/profile",component:function(){return t.e("chunk-e19e3b86").then(t.bind(null,"ecac"))},hidden:!0},{path:"/order/list",component:function(){return t.e("chunk-7003498a").then(t.bind(null,"aed3"))},hidden:!0},{path:"/order/new",component:function(){return t.e("chunk-5c971e94").then(t.bind(null,"645e"))},hidden:!0},{path:"/order/detail",component:function(){return Promise.all([t.e("chunk-ab6acc54"),t.e("chunk-0f914814")]).then(t.bind(null,"8a11"))},hidden:!0},{path:"/expert/apply",component:function(){return t.e("chunk-493b33bc").then(t.bind(null,"8784"))},hidden:!0}],a=function(){return new u["a"]({scrollBehavior:function(){return{y:0}},routes:o})},i=a();function s(){var e=a();i.matcher=e.matcher}n["c"]=i},b20f:function(e,n,t){e.exports={menuText:"#bfcbd9",menuActiveText:"#409eff",subMenuActiveText:"#f4f4f5",menuBg:"#304156",menuHover:"#263445",subMenuBg:"#1f2d3d",subMenuHover:"#001528",sideBarWidth:"210px"}},b5c9:function(e,n,t){},c24f:function(e,n,t){"use strict";t.d(n,"l",(function(){return d})),t.d(n,"f",(function(){return f})),t.d(n,"c",(function(){return l})),t.d(n,"m",(function(){return h})),t.d(n,"g",(function(){return p})),t.d(n,"i",(function(){return m})),t.d(n,"j",(function(){return b})),t.d(n,"h",(function(){return g})),t.d(n,"k",(function(){return v})),t.d(n,"e",(function(){return k})),t.d(n,"b",(function(){return T})),t.d(n,"d",(function(){return E})),t.d(n,"a",(function(){return O}));t("d3b7");var r=t("bc3a"),u=t.n(r),o=t("5c96"),c=t("4360"),a=t("5f87"),i=u.a.create({baseURL:"http://49.235.73.129/",withCredentials:!0,timeout:5e3});i.interceptors.request.use((function(e){return c["a"].getters.token&&(e.headers["X-Token"]=Object(a["a"])()),e}),(function(e){return console.log(e),Promise.reject(e)})),i.interceptors.response.use((function(e){var n=e.data;return 200!==n.code?(Object(o["Message"])({message:n.msg||"Error",type:"error",duration:5e3}),50008!==n.code&&50012!==n.code&&50014!==n.code||o["MessageBox"].confirm("You have been logged out, you can cancel to stay on this page, or log in again","Confirm logout",{confirmButtonText:"Re-Login",cancelButtonText:"Cancel",type:"warning"}).then((function(){c["a"].dispatch("user/resetToken").then((function(){location.reload()}))})),Promise.reject(new Error(n.msg||"Error"))):n}),(function(e){return console.log("err"+e),Object(o["Message"])({message:e.msg||e,type:"error",duration:5e3}),Promise.reject(e)}));var s=i;function d(e){return s({url:"/user/register",method:"post",data:e})}function f(e){return s({url:"/user/login",method:"post",data:e})}function l(){return s({url:"/user/detail",method:"get"})}function h(e){return s({url:"/user/update",method:"post",data:e})}function p(){return s({url:"/user/logout",method:"get"})}function m(e){return s({url:"/user/new_cost",method:"post",data:e})}function b(e){return s({url:"/user/new_earning",method:"post",data:e})}function g(e){return s({url:"/user/new_comprehensive",method:"post",data:e,processData:!1,contentType:"multipart/form-data"})}function v(e){return s({url:"/user/new_market",method:"post",data:e,processData:!1,contentType:"multipart/form-data"})}function k(e){return s({url:"/user/get_work_order",method:"post",data:e})}function T(e){return s({url:"/user/detail_work_order",method:"post",data:{order_id:e}})}function E(e){return s({url:"/user/get_log",method:"get",data:e})}function O(e){return s({url:"/user/apply_for_expert",method:"post",data:e})}},c653:function(e,n,t){var r={"./permission.js":"31c2","./user.js":"0f9a"};function u(e){var n=o(e);return t(n)}function o(e){if(!t.o(r,e)){var n=new Error("Cannot find module '"+e+"'");throw n.code="MODULE_NOT_FOUND",n}return r[e]}u.keys=function(){return Object.keys(r)},u.resolve=o,e.exports=u,u.id="c653"}},[[0,"runtime","chunk-elementUI","chunk-libs"]]]);