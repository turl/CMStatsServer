<%inherit file="base.mako" />
<%def name="onload()">
drawChart();
</%def>	
<%def name="javascript()">
google.load('visualization', '1', {'packages':['geochart', 'table']});
function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Country');
    data.addColumn('number', 'Installs');
    data.addRows([
    % for value in country_data:
    ['${value[0]|h}', ${value[1]|h}],
    % endfor
    ]);
    
    var config = {
        colorAxis: {minValue: 0, maxValue: 0, colors: ['#FF0000', '#00FF00']},
        displayMode: 'region'
    };
    
    var chart = new google.visualization.GeoChart(document.getElementById('map'), config);
    chart.draw(data, {width:681, height: 440});    
}
</%def>
        <div style="text-align: center">
            <h2>Installations by Country</h2>
            <h4>Normalized by country population.</h4>
            <div id="map"></div>
        </div>
