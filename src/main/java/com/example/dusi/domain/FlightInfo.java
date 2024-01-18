package com.example.dusi.domain;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class FlightInfo {

    private String msg;
    private String date;
    private List<Flight> drone_stat;
    private List<Mission> mission_info;

}
