package com.example.dusi.web;

import com.example.dusi.domain.Drone;
import com.example.dusi.domain.FlightInfo;
import com.example.dusi.domain.Logs;
import com.example.dusi.service.LogService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

@Slf4j
@Controller
@RequiredArgsConstructor
@RequestMapping("/")
@CrossOrigin(origins = "*")
public class HomeController {
    private final LogService logService;

    @GetMapping
    public String home (){
        return "home2";
    }
    @GetMapping("/rtsp")
    public String rtsp(@RequestParam String droneId, Model model){
        model.addAttribute("droneId",droneId);
        return "wowza";
    }
    @ResponseBody
    @PostMapping("/log")
    public List<FlightInfo> log(@RequestBody getLogDto getLogDto) throws FileNotFoundException {
        try {
            List<FlightInfo> logs = logService.findLog(getLogDto.getIndex());
            return logs;
        }catch (IndexOutOfBoundsException e){
            List<FlightInfo> error = new ArrayList<>();
            FlightInfo flightInfo = new FlightInfo();
            flightInfo.setMsg("x");
            error.add(flightInfo);
            return error;
        }
    }

}


