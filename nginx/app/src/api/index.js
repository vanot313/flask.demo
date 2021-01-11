import {get,post} from "./http";

export const upload = (files) => post(`/uploader/uploadmultiple`,files);

export const multipleClassify = () => get(`/data/multiple`);

export const singleClassify = () => get(`/data/single`);

export const analysis = (id) => get(`/data/getDataById?id=${id}`)
