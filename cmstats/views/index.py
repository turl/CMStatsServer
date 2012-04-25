from cmstats.database.schema.devices import Device
from cmstats.resources import Root
from cmstats.utils.countries import population
from pyramid.view import view_config
from pyramid.httpexceptions import exception_response


@view_config(context=Root, renderer='index.mako')
def index(request):
    kang = request.GET.get('unofficial', None)
    
    kwargs = {
            'device_count': Device.device_count(kang=kang),
            'version_count': Device.version_count(kang=kang),
            'total_nonkang': Device.count_nonkang(),
            'total_kang': Device.count_kang(),
            'total_last_day': Device.count_last_day(kang=kang),
    }

    return kwargs

@view_config(context=Root, name='map', renderer='map.mako')
def map_page(request):
    kang = request.GET.get('unofficial', None)
    country_data = []

    for country_code,country_installs in Device.country_count(kang=kang):
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
    kang = request.GET.get('unofficial', None)
    country_data = []

    kangs = Device.count_kang(device)
    nonkangs = Device.count_nonkang(device)

    #if there are no installs, this is not a valid device
    if (kangs + nonkangs) == 0:
        raise exception_response(400)

    for country_code, country_installs in Device.country_count(device, kang=kang):
        country = population.get(country_code, None)
        if country is not None:
            country_data.append((country[0], country_installs))

    kwargs = {
            'device': device,
            'country_data': country_data,
            'version_count': Device.version_count(device, kang=kang),
            'total_nonkang': nonkangs,
            'total_kang': kangs,
            'total_last_day': Device.count_last_day(device, kang=kang),
    }

    return kwargs

@view_config(context=Root, renderer='percountry.mako', route_name='percountry')
def percountry_page(request):
    country_code = request.matchdict['country'].lower()
    kang = request.GET.get('unofficial', None)
    country = population.get(country_code, None)
    if country is None:
        raise exception_response(400)
    
    kwargs = {
            'country': country[0],
            'population': country[1],
            'device_count': Device.device_count(country=country_code, kang=kang),
            'version_count': Device.version_count(country=country_code, kang=kang),
            'total_nonkang': Device.count_nonkang(country=country_code),
            'total_kang': Device.count_kang(country=country_code),
            'total_last_day': Device.count_last_day(country=country_code, kang=kang),
    }

    return kwargs
