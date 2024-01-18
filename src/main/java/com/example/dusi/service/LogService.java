package com.example.dusi.service;

import com.example.dusi.domain.FlightInfo;
import com.google.gson.Gson;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
@Slf4j
public class LogService {
    String folderPath = "로그 경로";
    List<String> filePaths = listAllFilePaths(folderPath);
    public List<FlightInfo> findLog(int fIndex) throws FileNotFoundException {
        File file = new File(filePaths.get(fIndex));
        Reader reader = new FileReader(file);
        String[] parts = filePaths.get(fIndex).split("\\\\");
        String []time =parts[11].split("_");
        String date = parts[8]+"년"+parts[9]+"월"+parts[10]+"일 "+time[0]+":"+time[1]+":"+time[2].replace(".json","");
        Gson gson = new Gson();

        List<FlightInfo> flightInfos = Arrays.asList(gson.fromJson(reader,FlightInfo[].class));
        for(FlightInfo i : flightInfos){
            i.setDate(date);
        }

        return flightInfos;
    }
    public static List<String> listAllFilePaths(String folderPath) {
        List<String> filePaths = new ArrayList<>();
        File folder = new File(folderPath);

        if (folder.isDirectory()) {
            File[] files = folder.listFiles();

            if (files != null) {
                for (File file : files) {
                    if (file.isFile()) {
                        filePaths.add(file.getAbsolutePath());
                    } else if (file.isDirectory()) {
                        List<String> subfolderFilePaths = listAllFilePaths(file.getAbsolutePath());
                        filePaths.addAll(subfolderFilePaths);
                    }
                }
            }
        }

        return filePaths;
    }
}
