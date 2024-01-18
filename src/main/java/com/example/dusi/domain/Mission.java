package com.example.dusi.domain;

import lombok.Data;

import java.util.List;

@Data
public class Mission {

    private String organization;
    private String drone_id;
    private String mi_name;
    private String mi_desc;
    private double home_lat;
    private double home_lon;
    private int mi_alt;
    private List<WayPoint> waypoint;

    public Mission(String organization, String drone_id, String mi_name, String mi_desc, double home_lat, double home_lon, int mi_alt, List<WayPoint> waypoint) {
        this.organization = organization;
        this.drone_id = drone_id;
        this.mi_name = mi_name;
        this.mi_desc = mi_desc;
        this.home_lat = home_lat;
        this.home_lon = home_lon;
        this.mi_alt = mi_alt;
        this.waypoint = waypoint;
    }
}
