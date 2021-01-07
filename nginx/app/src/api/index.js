import {get,post} from "./http";

export const selectSingle = () => get(`/upload`);

export const test = () => get(`/data/temp`);

export const tests = () => get(`/data/uploader/upload`);
