package com.example.home1.interfaces;

public class ApiUtils {

    public static final String BASE_URL = "http://192.168.1.226:8000/";
    public static final String BASE_URL_article = "http://192.168.1.226:8000/karim/";

    public static LoginService getUserService(){
        return RetrofitClient.getClient(BASE_URL).create(LoginService.class);
    }
    public static ArticleService getArticleService(){
        return RetrofitClient.getClient(BASE_URL_article).create(ArticleService.class);
    }


}
