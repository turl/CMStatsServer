<%inherit file="base.mako" />
        <h3>Total Installs</h3>
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
        
        <% isofficial = len(version_count) > 0 %>
        % if isofficial:
        <h3>Installs by Version</h3>
        <table>
            <tr>
                <th width="250">Version</th>
                <th>Total</th>
            </tr>
            % for version in version_count:
            <tr><td>${version[1]|h}</td><td>${version[0]|number}</td></tr>
            % endfor
        </table>
        % endif
        
        <h3>Installs by Device</h3>
        <table>
            <tr>
                <th width="250">Device</th>
                <th>Total</th>
            </tr>
            % for device in device_count:
            <tr><td><a href="/perdevice/${device[1]|h}">${device[1]|h}</a></td><td>${device[0]|number}</td></tr>
            % endfor
        </table>
