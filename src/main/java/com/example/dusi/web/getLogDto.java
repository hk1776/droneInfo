package com.example.dusi.web;

import lombok.Data;

@Data
public class getLogDto {
    private int index;

    public getLogDto() {
    }

    public getLogDto(int index) {
        this.index = index;
    }
}
