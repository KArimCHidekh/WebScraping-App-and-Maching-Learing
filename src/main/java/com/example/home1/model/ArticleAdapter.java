package com.example.home1.model;


import android.content.Context;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.LayoutRes;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.example.home1.R;

import java.util.ArrayList;
import java.util.List;


public class ArticleAdapter extends ArrayAdapter<M_Article> {

    private Context mContext;
    private List<M_Article> moviesList = new ArrayList<>();

    public ArticleAdapter (@NonNull Context context,  ArrayList<M_Article> list) {
        super(context, 0 , list);
        mContext = context;
        moviesList = list;
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View listItem = convertView;
        if(listItem == null)
            listItem = LayoutInflater.from(mContext).inflate(R.layout.list_item,parent,false);

        M_Article currentMovie = moviesList.get(position);

        TextView name = (TextView) listItem.findViewById(R.id.textView_name);
        name.setText(currentMovie.getTitle());

        //TextView release = (TextView) listItem.findViewById(R.id.textView_release);
        //release.setText(currentMovie.getLink());

        return listItem;
    }
}