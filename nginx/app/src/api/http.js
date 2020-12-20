import axios from 'axios';
import router from '../router'
axios.defaults.timeout = 10000; //10秒 超时时间
axios.defaults.withCredentials = true; //允许跨域
/*Content-type 响应头*/
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
/*基础url*/
axios.defaults.baseURL = "http://49.235.73.129:5000";

/*响应拦截器*/
axios.interceptors.response.use(
  response => {

    //访问到接口
    if(response.status == 200){
      return Promise.resolve(response);
    }else{
      //Promise是一个对象,从它可以获取异步操作的消息,一旦状态改变,就不会再变
      return Promise.reject(response);
    }
  },
  error => {
    if(error.response.status){
      switch(error.response.status){
        case 401:
          router.replace({
            path: '/',
            query: {
              redirect: router.currenRoute.fullPath //保存当前地址
            }
          });
          break;
        case 404:
          break;
      }
      return Promise.reject(error.response);
    }
  }
);

/**
 * 封装get方法
 * @param url
 * @param data
 * @returns {Promise}
 */
export function get(url,params={}) {
  return new Promise((resolve,reject) => {
    axios.get(url,{
      params:params
    })
      .then(response => {
        resolve(response.data);
      })
      .catch(err => {
        reject(err);
      })
  });
}

/*post 方法*/
export function post(url,data={}) {
  return new Promise((resolve,reject) => {
    axios.post(url,data)
      .then(response => {
        resolve(response.data);
      })
      .catch(err => {
        reject(err);
      })
  });
}
