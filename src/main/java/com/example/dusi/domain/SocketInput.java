package com.example.dusi.domain;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Data

public class SocketInput {
    private String msg;
    private List<Mission> mission_info;
    private List<Flight> drone_state;

}

