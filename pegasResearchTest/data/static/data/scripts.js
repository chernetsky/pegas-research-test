const CHART_MODES = {
    MODE_5: '5',
    MODE_30: '30'
}

let DISPLAY_MODE = CHART_MODES.MODE_5;

let chartData5;
let chartData30;

/**
 * Creates dataset for mode 30.
 * 
 * @param {Object} data 
 * @returns {Object} Converted data
 */
function preprocessData(data) {
    const data30 = {'min': [], 'avg': [], 'max': []};
    let counter = 0;
    let min = +Infinity;
    let max = -Infinity;
    let sum = 0;

    for(let i in data) {
        const row = data[i];
        const ts = row[0];
        const val = row[1];
    
        min = Math.min(min, val);
        max = Math.max(max, val);
        sum += val;

        if (++counter == 6) { // Every 30 minutes
            data30.min.push([ts, min]);
            data30.max.push([ts, max]);
            data30.avg.push([ts, +((sum / counter).toFixed(2))]);

            counter = 0;
            min = +Infinity;
            max = -Infinity;
            sum = 0;
        }
    }

    return data30;
}

function drawChart(data, mode) {
    const chartConfig = {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Статистика данных клиента'
        },
        xAxis: {
            type: 'datetime',
            labels: {
                format: '{value:%Y.%m.%d<br>%H:%M}'
            }
        },
        yAxis: {
            title: {
                text: 'Значение'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 2,
                states: {
                    hover: {
                        lineWidth: 2
                    }
                },
                threshold: null
            }
        }
    };

    if (mode == CHART_MODES.MODE_5) {
        chartConfig.series = [{
            type: 'area',
            name: '',
            data: data
        }];
    } else {
        chartConfig.series = [{
            type: 'line',
            name: 'Минимум',
            data: data.min,
            color: '#007bff'
        }, {
            type: 'line',
            name: 'Среднее',
            data: data.avg,
            color: '#38992b',
            stroke: 5
        }, {
            type: 'line',
            name: 'Максимум',
            data: data.max,
            color: '#c93d3d'
        }];
        chartConfig.legend.enabled = true;
    }

    Highcharts.setOptions({
        lang: {
            weekdays: [
                'Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг',
                'Пятница', 'Суббота'
            ],
            resetZoom : 'Сброс диапазона'
        }
    });

    Highcharts.chart('chart-container', chartConfig);
}

/*
 * Init toolbar 
 */
function switchMode() {
    DISPLAY_MODE = DISPLAY_MODE == CHART_MODES.MODE_5 ? CHART_MODES.MODE_30 : CHART_MODES.MODE_5;
    $('#chart-mode h4 span').text(DISPLAY_MODE);

    if (DISPLAY_MODE == CHART_MODES.MODE_5)
        drawChart(chartData5, DISPLAY_MODE);
    else
        drawChart(chartData30, DISPLAY_MODE);
}

$('#chart-mode .btn').mousedown(switchMode);

const data = fetch('/api/data/').then(response => {
    if (response.ok)
        return response.json();
}).then(data => {
    chartData5 = data['data'];
    chartData30 = preprocessData(chartData5);
    
    drawChart(chartData5, DISPLAY_MODE);
});
