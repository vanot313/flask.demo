import {get,post} from "./http";
import Axios from "axios";

export const upload = (files) => post(`/uploader/uploadmultiple`,files);

export const multipleClassify = () => get(`/data/multiple`);

export const singleClassify = () => get(`/data/single`);

export const analysis = (id) => get(`/data/getDataById?id=${id}`)

//下载
export const download = (url) => Axios({
  method: 'get',
  url: url,
  responseType: 'blob'
});
