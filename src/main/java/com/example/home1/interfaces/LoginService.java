package com.example.home1.interfaces;

import com.example.home1.model.M_login;
import com.example.home1.model.M_login_result;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
public interface LoginService {

    @POST("auth/rest-auth/login/")
    Call<M_login_result>  login(@Body M_login body);

    @POST("auth/rest-auth/login/")
    Call<M_login_result> getStringScalar(@Body M_login body);
}