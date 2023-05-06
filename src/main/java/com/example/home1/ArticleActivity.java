package com.example.home1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class ArticleActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_article);
        WebView webview = (WebView) findViewById(R.id.webview) ;
        webview.getSettings().setJavaScriptEnabled(true);
        webview.setWebViewClient( new WebViewClient());

        Intent intent = getIntent() ;
        webview.loadUrl(intent.getStringExtra("content"));



    }
}
