import jsontable as jsontable

#Create a list of paths you want to extract
paths = [{"$.timestampVGW":"timestampVGW"},	{"$.timestamp":"timestamp"}, {"$.type":"type"}, {"$.payload.application":"Application"},
         {"$.payload.key":"key"},
         {"$.payload.value":"value"},
         {"$.nsid":"NearSkyId"}]
#The JSON object you want to explore
sample = [{"timestampVGW":1577836800000,"timestamp":1577836800000,"type":"HAKVF","payload":{"application":"AxisCamera","key":"pedestrians","value":8},"nsid":"085b104d-37f8-4766-9b49-f29dd982bc79"},
{"timestampVGW":1577835000000,"timestamp":1577835000000,"type":"HAKVF","payload":{"application":"AxisCamera","key":"pedestrians","value":13},"nsid":"085b104d-37f8-4766-9b49-f29dd982bc79"}]
         

#Create an instance of a converter
converter = jsontable.converter()
#Set the paths you want to extract
converter.set_paths(paths)
#Input a JSON to be interpreted
rdsout = converter.convert_json(sample)
print(rdsout)
