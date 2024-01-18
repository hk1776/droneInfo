package com.example.dusi.domain;

import java.util.List;

public class Logs {
    private List<FlightInfo> logs;

    public Logs(List<FlightInfo> logs) {
        this.logs = logs;
    }

    public List<FlightInfo> getLogs() {
        return logs;
    }

    public void setLogs(List<FlightInfo> logs) {
        this.logs = logs;
    }
}
