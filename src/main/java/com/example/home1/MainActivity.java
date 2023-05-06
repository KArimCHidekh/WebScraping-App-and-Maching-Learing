package com.example.home1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.nfc.Tag;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


import com.example.home1.interfaces.ApiUtils;
import com.example.home1.interfaces.LoginService;
import com.example.home1.model.M_login;
import com.example.home1.model.M_login_result;


import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class MainActivity extends AppCompatActivity {

    private Button button ;
    private EditText tf_username ;
    private EditText   tf_password ;
    LoginService userService= ApiUtils.getUserService();


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //setContentView(R.layout.activity_login2);

        button = (Button) findViewById(R.id.button) ;
        tf_username = (EditText) findViewById(R.id.tf_username) ;
        tf_password = (EditText) findViewById(R.id.tf_password) ;
        //login("karim","karim");
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String username = tf_username.getText().toString();
                String password = tf_password .getText().toString();
                if(validateLogin(username, password)){
                    Log.i("Authentification", "User/passs ::    " + username+"/"+password);
                    doLogin(username, password);

                }

            }
        });

        tf_password.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String username = tf_username.getText().toString();
                String password = tf_password .getText().toString();
                if(validateLogin(username, password)){
                    Log.i("Authentification", "User/passs ::    " + username+"/"+password);
                    doLogin(username, password);

                }

            }
        });

        tf_username.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String username = tf_username.getText().toString();
                String password = tf_password .getText().toString();
                if(validateLogin(username, password)){
                    Log.i("Authentification", "User/passs ::    " + username+"/"+password);
                    doLogin(username, password);

                }

            }
        });



    }

    //----------------------------------------------------------------------------------------------
    public void openActivity2(){
        Intent intent = new Intent(this,MainUI.class) ;
        startActivity(intent);
    }
    //----------------------------------------------------------------------------------------------

    private boolean validateLogin(String username, String password){
        if(username == null || username.trim().length() == 0){
            Toast.makeText(this, "Username is required", Toast.LENGTH_SHORT).show();
            return false;
        }
        if(password == null || password.trim().length() == 0){
            Toast.makeText(this, "Password is required", Toast.LENGTH_SHORT).show();
            return false;
        }
        return true;
    }

    private void doLogin(final String username,final String password){
        M_login llll=new M_login();
        llll.setUsername(username);
        llll.setPassword(password);

        Call<M_login_result> call = userService.login(llll);
        call.enqueue(new Callback<M_login_result>() {
            @Override
            public void onResponse(Call<M_login_result> call, Response<M_login_result> response) {
                if(response.isSuccessful()){
                    M_login_result resObj = response.body();
                    if(resObj.getKey()!=null){
                        Log.i("Authentification", "ok  ::  KEY=" +resObj.getKey());
                        //login start main activity
                        Intent intent = new Intent(MainActivity.this, MainUI.class);
                        intent.putExtra("username", username);
                        startActivity(intent);


                    } else {
                        Log.i("Authentification", "error  ::  message=" +resObj.toString());
                        Toast.makeText(MainActivity.this, "The username or password is incorrect", Toast.LENGTH_SHORT).show();
                    }
                } else {
                    Toast.makeText(MainActivity.this, "Error! Please try again!", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<M_login_result> call, Throwable t) {
                Toast.makeText(MainActivity.this, t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
//--------------------------------------------------------------------------------------------------

}
