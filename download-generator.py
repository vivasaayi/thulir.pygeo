horizontal_grid="25"
vertical_grid="08"

commands = ""

day_range = range(1,100)
year = "2020"

for item in day_range:
    day_str = str(item) + ""
    
    if(len(day_str) == 1):
        day_str = day_str.rjust(3, "0")   
    elif(len(day_str) == 2):
        day_str = day_str.rjust(3, "0")   


    day_str = year + day_str 

    command = "aws s3 cp --request-payer --recursive s3://modis-pds/MCD43A4.006/{}/{}/{}/ ./data/{} --no-sign-request\n".format(
        horizontal_grid,
        vertical_grid,
        day_str,
        day_str
    )
    commands = commands + command
    commands = commands + "echo 'Downloaded data for Day: {}'\n".format(item)

print(commands)

