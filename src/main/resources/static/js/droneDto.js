//드론정보 DTO
class Drone {
    constructor(organization, user_id, drone_id,status,data_uid,flight_mode,lat,lon,rel_alt,msl_alt,speed,roll,pitch,heading,battery,lastUpdate) { // 인자를 받아 할당한다.
        // fields
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
        this.lastUpdate = lastUpdate;
    }
}
