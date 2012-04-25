from cmstats.database.schema.devices import Device
from cmstats.resources import Root
from cmstats.utils.countries import population
from pyramid.view import view_config


@view_config(context=Root, renderer='index.mako')
def index(request):
    kwargs = {
            'device_count': Device.device_count(),
            'version_count': Device.version_count(),
            'total_nonkang': Device.count_nonkang(),
            'total_kang': Device.count_kang(),
            'total_last_day': Device.count_last_day(),
    }

    return kwargs

@view_config(context=Root, name='map', renderer='map.mako')
def map_page(request):
    country_data = []

    for country_code,country_installs in Device.country_count():
        country = population.get(country_code, None)
        if not country:
            continue

        count_norm = (float(country_installs)/float(country[1]))*100000
        country_data.append((country[0], count_norm))

    print country_data

    return {'country_data': country_data}

@view_config(context=Root, renderer='perdevice.mako', route_name='perdevice')
def perdevice_page(request):
    device = request.matchdict['device']
    country_data = []

    for country_code, country_installs in Device.country_count(device):
        country = population.get(country_code, None)
        if country is not None:
            country_data.append((country[0], country_installs))
    
    print country_data

    kwargs = {
            'device': device,
            'country_data': country_data,
            'version_count': Device.version_count(device),
            'total_nonkang': Device.count_nonkang(device),
            'total_kang': Device.count_kang(device),
            'total_last_day': Device.count_last_day(device),
    }

    return kwargs

@view_config(context=Root, renderer='percountry.mako', route_name='percountry')
def percountry_page(request):
    country_code = request.matchdict['country'].lower()
    country = population.get(country_code, None)
    if country is None:
        return 'Invalid country'
    
    print country
    
    kwargs = {
            'country': country[0],
            'population': country[1],
            'device_count': Device.device_count(country=country_code),
            'version_count': Device.version_count(country=country_code),
            'total_nonkang': Device.count_nonkang(country=country_code),
            'total_kang': Device.count_kang(country=country_code),
            'total_last_day': Device.count_last_day(country=country_code),
    }

    return kwargs
