package com.example.home1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteStatement;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.example.home1.interfaces.ApiUtils;
import com.example.home1.interfaces.ArticleInterface;
import com.example.home1.interfaces.ArticleService;
import com.example.home1.interfaces.LoginService;
import com.example.home1.model.ArticleAdapter;
import com.example.home1.model.M_Article;
import com.example.home1.model.M_login;
import com.example.home1.model.M_login_result;
import com.google.gson.Gson;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ArticleListActivity extends AppCompatActivity {

    ArrayList<M_Article> titles = new ArrayList<>() ;
    ArrayList<String> content =  new ArrayList<>() ;
    ArrayAdapter arrayAdapter ;


    ArticleService articleService= ApiUtils.getArticleService();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_listarticle);

        ListView listview =(ListView) findViewById(R.id.listview) ;
        //arrayAdapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, titles) ;
        //listview.setAdapter(arrayAdapter) ;


        arrayAdapter  = new ArticleAdapter(this,titles);

         listview.setAdapter(arrayAdapter );


        listview.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
               Intent intent = new Intent(getApplicationContext() , ArticleActivity.class) ;
               M_Article selected= (M_Article)parent.getItemAtPosition(position);
               intent.putExtra("content", selected.getLink()) ;
               startActivity(intent);

            }
        });


        try {

            String tag=getIntent().getStringExtra("tag");
            api_request_article(tag);
        } catch (JSONException e) {
            e.printStackTrace();
        }

    }

    private void api_request_article(String tag) throws JSONException {
            System.out.println("<API get Article> :: started");
            M_Article llll=new M_Article();
            llll.setTag(tag);


            Call<List<M_Article>> call = articleService.getArticles(llll);
            call.enqueue(new Callback<List<M_Article>>() {
                @Override
                public void onResponse(Call<List<M_Article>> call, Response<List<M_Article>>response) {

                    if(response.isSuccessful()){

                        arrayAdapter.addAll(response.body());

                    } else {

                        Toast.makeText(ArticleListActivity.this, "Error! Please try again!", Toast.LENGTH_SHORT).show();

                    }
                }

                @Override
                public void onFailure(Call<List<M_Article>> call, Throwable t) {

                    Toast.makeText(ArticleListActivity.this, "Error! Please try again!", Toast.LENGTH_SHORT).show();
            }
            });
    }
    //----------------------------------------------------------------------------------------------



    public String bbbbb(){
        try {
        final String POST_PARAMS = "{ \"tag\": \"sport\"}" ;

        System.out.println(POST_PARAMS);
        URL obj = null;

            obj = new URL("http://192.168.1.226:8000/karim/articles/");

        HttpURLConnection postConnection = (HttpURLConnection) obj.openConnection();
        postConnection.setRequestMethod("POST");
        //postConnection.setRequestProperty("userId", "a1bcdefgh");
        postConnection.setRequestProperty("Content-Type", "application/json");
        postConnection.setDoOutput(true);
        OutputStream os = postConnection.getOutputStream();
        os.write(POST_PARAMS.getBytes());
        os.flush();
        os.close();
        int responseCode = postConnection.getResponseCode();
        System.out.println("POST Response Code :  " + responseCode);
        System.out.println("POST Response Message : " + postConnection.getResponseMessage());
        if (responseCode == HttpURLConnection.HTTP_OK) { //success
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    postConnection.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = in .readLine()) != null) {
                response.append(inputLine);
            } in .close();
            // print result
            System.out.println(response.toString());
            return response.toString();
        } else {
            System.out.println("POST NOT WORKED");
            return "";
        }
    } catch (ProtocolException ex) {
            ex.printStackTrace();
            return "";
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
            return "";
        } catch (IOException ex) {
            ex.printStackTrace();
            return "";
        }

    }
}
