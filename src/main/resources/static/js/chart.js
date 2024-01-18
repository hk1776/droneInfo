function altChart(id){
    const data = altMap.get(id);
    const data2 = altMap2.get(id);
    //var data = altMap.get(id);
    Highcharts.chart('myChart', {
        chart: {
            type: 'area'//차트타입
        },
        title: {
            text: '드론 고도차트',
            style: {
                fontSize: '15px' // 타이틀의 글꼴 크기를 설정합니다.
            },
            verticalAlign: 'top'
        },
        navigator: {
            margin:0,
            height: 15,
            enabled: true // 네비게이터를 활성화합니다.
        },
        yAxis: {
            title: {
                text: '고도(M)'
            }
        },

        tooltip: {
            pointFormat: '{series.name} {point.y:,.0f}M</b><br/>' //각 마커가 나타내는 정보를 표시
        },
        //마커 모양 옵션
        plotOptions: {
            area: {
                pointStart: 0,
                marker: {
                    enabled: true,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            },
            series: {
                animation: false // 애니메이션 비활성화
            }
        },
        //차트로 표기할 데이터 셋
        series: [{
            name: '지표면 기준',
            data:data
        }, {
            name: '해수면 기준',
            data: data2
        }]
    });
}

function speedChart(id){
    const speedData = speedMap.get(id);
    //var data = altMap.get(id);
    Highcharts.chart('myChart2', {

        title: {
            text: '드론 속도차트',
            style: {
                fontSize: '15px' // 타이틀의 글꼴 크기를 설정합니다.
            },
            verticalAlign: 'top'
        },
        navigator: {
            margin:0,
            height: 15,
            enabled: true // 네비게이터를 활성화합니다.
        },
        tooltip: {
            pointFormat: '{point.y:,.0f}km/h</b><br/>' //각 마커가 나타내는 정보를 표시
        },
        yAxis: {
            title: {
                text: '속도(Km/h)'
            }
        },
        //마커 모양 옵션
        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                animation: false
            }
        },
        //차트로 표기할 데이터 셋
        series: [{
            name: id,
            data: speedData
        }],

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }

    });

}
