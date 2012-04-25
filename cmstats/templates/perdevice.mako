<%inherit file="base.mako" />
<%def name="onload()">
drawChart();
</%def> 
<%def name="javascript()">
google.load('visualization', '1', {'packages':['corechart', 'table']});
function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Country');
    data.addColumn('number', 'Installs');
    data.addRows([
    % for value in country_data:
    ['${value[0]|h}', ${value[1]|h}],
    % endfor
    ]);
    
    var options = {
          chartArea: {left:20,top:0,width:"75%",height:"100%"},
          sliceVisibilityThreshold: 5/360,
          pieResidueSliceLabel: 'Others'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}
</%def>
        <h3>Total Installs for device ${device|h}</h3>
        <table>
            <tr>
                <th width="250">Type</th>
                <th>Total</th>
            </tr>
            <tr>
                <td>Official Installs</td>
                <td>${total_nonkang|number}</td>
            </tr>
            <tr>
                <td>Unofficial Installs</td>
                <td>${total_kang|number}</td>
            </tr>
            <tr>
                <td><b>TOTAL</b></td>
                <td><b>${(total_kang + total_nonkang)|number}</b></td>
            </tr>
            <tr>
                <td>Last 24 Hours</td>
                <td>${total_last_day|number}</td>
            </tr>
        </table>
        
        <h3>Installs by Version for device ${device|h}</h3>
        <table>
            <tr>
                <th width="250">Version</th>
                <th>Total</th>
            </tr>
            % for version in version_count:
            <tr><td>${version[1]|h}</td><td>${version[0]|number}</td></tr>
            % endfor
        </table>


        <h3>Installs per Country for device ${device|h}</h3>
        <div id="piechart"></div>
        <table>
            <tr>
                <th width="250">Country</th>
                <th>Total</th>
            </tr>
            % for value in country_data:
            <tr><td>${value[0]|h}</td><td>${value[1]|number}</td></tr>
            % endfor
        </table>
