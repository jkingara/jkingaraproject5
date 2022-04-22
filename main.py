import openpyxl
import numbers
import openpyxl.utils
import plotly.


def open_worksheet(files):
    population_worksheet = openpyxl.load_workbook(files)
    sheet_one = population_worksheet.active 
    return sheet_one 



#main function

def main(show_percent_change_map= countrypopchanges2020-2021.xlax):
    population_worksheet = open_worksheet("countrypopchanges2020-2021.xlax")
    display_population_changes = should_show_population_change()
    if display_population_changes == True
        population_worksheet() = show_population_change_map 
    else: show_percent_change_map

#population change func.
#user input

def should_display_population_change():
    input("Would you like to see the total population change from 2020-2021?")
    if True:
        return map
    else:
        return FALSE


map_to_show = plotly.graph_objects.Figure()
    data = plotly.graph_objects.Choropleth()
        locations= list_of_state_abrev,
        z= list_of_population_changes,
        locationmode="USA",
        colorscale='Red',
        colorbar_title="population change"

map_to_show.show()

main()