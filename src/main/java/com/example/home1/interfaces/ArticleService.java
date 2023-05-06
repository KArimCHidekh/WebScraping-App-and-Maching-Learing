package com.example.home1.interfaces;

import com.example.home1.model.M_Article;
import com.example.home1.model.M_login;
import com.example.home1.model.M_login_result;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.HTTP;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface ArticleService {

    //@GET("articles/")
    @Headers("Content-Type: application/json")
    @HTTP(method = "POST", path = "karim/articles/",hasBody = true)
    //@GET("articles/")
    Call<List<M_Article>>  getArticles(@Body M_Article article );


}