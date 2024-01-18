package com.example.dusi.web;

import lombok.Data;

@Data
public class Location {
    private double lat;
    private double lng;


    public Location(double lat, double lon) {
    }
}
