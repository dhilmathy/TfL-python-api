from tfl.client import Client
from tfl.api_token import ApiToken

application_id = r"c1636664"
application_key = r"deb7afb5b165d364c5a79ef0a792b97a"

token = ApiToken(application_id, application_key)

client = Client(token)

#print (client.get_line_meta_modes()[2])
#print (client.get_lines(mode="bus")[0])
#print (client.get_lines(line_id="victoria")[0])
#print(client.get_line_status("victoria")[0])
#print(client.get_line_status("victoria", include_details=True)[0])
#print(client.get_stop_points_by_line("victoria")[0])
#print(client.get_route_by_mode("bus")[0])
#print(client.get_line_disruptions_by_line_id("waterloo-city")[0])
#print(client.get_line_disruptions_by_mode("bus")[0])

print (client.get_stop_points_by_id("940GZZLUEAC"))
print (client.get_stop_points_by_mode("dlr"))