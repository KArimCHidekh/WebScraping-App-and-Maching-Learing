package com.example.home1;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;


public class MainUI extends AppCompatActivity {

    private LinearLayout btn_sport ;
    private LinearLayout btn_culture ;
    private LinearLayout btn_science ;
    private LinearLayout btn_economy ;
    private LinearLayout btn_health ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ui);

        btn_sport  = (LinearLayout) findViewById(R.id.btn_sport) ;
        btn_culture  = (LinearLayout) findViewById(R.id.btn_culture) ;
        btn_science = (LinearLayout) findViewById(R.id.btn_science) ;
        btn_economy = (LinearLayout) findViewById(R.id.btn_economy) ;
        btn_health = (LinearLayout) findViewById(R.id.btn_health) ;


        btn_sport .setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { openActivity("sport"); }
        });
        btn_culture  .setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { openActivity("culture"); }
        });
        btn_science .setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { openActivity("science"); }
        });
        btn_economy .setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { openActivity("economie"); }
        });
        btn_health .setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { openActivity("sante"); }
        });


    }

    public void openActivity(String tag){
        Intent intent = new Intent(this, ArticleListActivity.class) ;
        intent.putExtra("tag", tag);
        startActivity(intent);
    }
}
