package com.example.dusi.domain;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Flight {
    private String organization;
    private String user_id;
    private String drone_id;
    private String status;
    private int data_uid;
    private int flight_mode;
    private double lat;
    private double lon;
    private int rel_alt;
    private int msl_alt;
    private int speed;
    private double roll;
    private double pitch;
    private double heading;
    private int battery;

    public Flight() {
    }

    public Flight(String organization, String user_id, String drone_id, String status, int data_uid, int flight_mode, double lat, double lon, int rel_alt, int msl_alt, int speed, double roll, double pitch, double heading, int battery) {
        this.organization = organization;
        this.user_id = user_id;
        this.drone_id = drone_id;
        this.status = status;
        this.data_uid = data_uid;
        this.flight_mode = flight_mode;
        this.lat = lat;
        this.lon = lon;
        this.rel_alt = rel_alt;
        this.msl_alt = msl_alt;
        this.speed = speed;
        this.roll = roll;
        this.pitch = pitch;
        this.heading = heading;
        this.battery = battery;
    }

    public Flight(boolean b, String organization, String userId, String droneId, String status, int dataUid, int flightMode, double lat, double lon, int relAlt, int mslAlt, int speed, double roll, double pitch, double heading, int battery) {
    }

}
