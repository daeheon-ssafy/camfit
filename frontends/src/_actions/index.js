import axios from 'axios';
import * as types from './ActionTypes';
import {API_BASE_URL} from '../constants';
export function login(data) {
    const request = axios.post(`${API_BASE_URL}/accounts/api-token-auth/`, data)
        .then((res) =>
            res.data
        );
    return {
        type: types.LOGIN,
        payload: request
    };
}
export function signup(data) {
    const request = axios.post(`${API_BASE_URL}/accounts/signup/`, data)
        .then((res) => 
            res.data);

    return {
        type: types.SIGNUP,
        payload: request
    };
}
export function emailcheck(data) {
    const request = axios.post(`${API_BASE_URL}/accounts/emailCheck/`, data)
        .then((res) => 
            res.data);

    return {
        type: types.EMAILCHECK,
        payload: request
    };
}