function volt(vol){
    var remain;
    remain = (vol / 1000.0 - 14.2) / (16.5 - 14.2) * 100;
    //remain = (14300/1000.0- min)/(max-min)*100;
    if (remain < 0)
        remain = 0;
    else if (remain > 100)
        remain = 100;

    console.log("remain:"+remain);
    return remain / 100.0;
}
