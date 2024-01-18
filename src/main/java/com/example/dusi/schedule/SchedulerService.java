package com.example.dusi.schedule;

import com.example.dusi.domain.Flight;
import com.example.dusi.domain.FlightInfo;
import com.example.dusi.domain.Mission;
import com.example.dusi.domain.WebSocketHandler;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

import java.io.*;
import java.text.SimpleDateFormat;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;

import static com.example.dusi.domain.WebSocketHandler.sessions;

@Service
@Slf4j
@RequiredArgsConstructor
public class  SchedulerService {
    private final ObjectMapper objectMapper;
    private int index = 0;
    private int fIndex = 0;
    private int delay = 0;

    public void setDelay(int delay) {
        this.delay = delay;
    }

    String folderPath = "로그 경로";
    List<String> filePaths = listAllFilePaths(folderPath);

    @Scheduled(initialDelay = 5000, fixedDelay = 1000)
    public void runAfterTenSecondsRepeatTenSeconds() throws FileNotFoundException, InterruptedException {
        if (filePaths != null) {
           log.info("filePath : {}",filePaths.get(index));
            File file = new File(filePaths.get(index));

            long lastModifiedTimestamp = file.lastModified();

            // Timestamp를 Date 객체로 변환
            Date lastModifiedDate = new Date(lastModifiedTimestamp);

            // Date를 원하는 형식으로 포맷팅 (예: "yyyy-MM-dd HH:mm:ss")
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            String formattedDate = dateFormat.format(lastModifiedDate);

            // 수정일자 출력
            System.out.println("파일의 수정일자: " + formattedDate);
            index++;
        }
    }
    public  <T>void sendMessage(T message) {
        sessions.parallelStream()
                .forEach(session -> sendMessage(session,message));
    }
    public <T> void sendMessage(WebSocketSession session,T message){
        try {
            log.info("서비스 메시지 = {}",message);
            session.sendMessage(new TextMessage(objectMapper.writeValueAsString(message)));

        }catch (IOException e){
            log.error(e.getMessage(),e);
        }
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
