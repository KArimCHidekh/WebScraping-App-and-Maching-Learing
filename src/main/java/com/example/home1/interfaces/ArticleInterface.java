package com.example.home1.interfaces;

import com.example.home1.model.M_Article;

import java.util.List;

import retrofit2.Callback;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface ArticleInterface {

    public interface GitHubClient {
        @POST("articles")
        void reposForUser(
                @Path("/karim") String user,
                Callback<List<M_Article>> callback
        );
    }
}
