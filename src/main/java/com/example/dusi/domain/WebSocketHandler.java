package com.example.dusi.domain;

import com.example.dusi.web.HomeController;
import com.example.dusi.web.Location;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

@Slf4j
@RequiredArgsConstructor
@Component
public class WebSocketHandler extends TextWebSocketHandler {
    private final ObjectMapper objectMapper;
    public static Set<WebSocketSession> sessions = new HashSet<>();
    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        String payload = message.getPayload();
        log.info("입력{}",payload);
        FlightInfo input = objectMapper.readValue(payload,FlightInfo.class);
        if(input.getMsg().equals("flight_info")){
            Flight flight = input.getDrone_stat().get(0);
            sessions.add(session);
            sendMessage(flight);
        } else if (input.getMsg().equals("mission_file")){
            Mission mission = input.getMission_info().get(0);
            sessions.add(session);
            sendMessage(mission);
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
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        super.afterConnectionClosed(session, status);
        sessions.remove(session);
    }

}


